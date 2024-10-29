from importFED import FEDexclude,FEDinclude
import FWCore.ParameterSet.Config as cms
from Configuration.Eras.Era_Run3_cff import Run3

detector = "Pixel"
process = cms.Process("PRAW", Run3)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32( 100 )
)

process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool( True ),
    numberOfThreads = cms.untracked.uint32( 4 ),
    numberOfStreams = cms.untracked.uint32( 0 )
)

process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
from Configuration.AlCa.GlobalTag import GlobalTag as customiseGlobalTag
process.GlobalTag = customiseGlobalTag(process.GlobalTag, globaltag = '140X_dataRun3_HLT_for2024TSGStudies_v1')

import HLTrigger.HLTfilters.hltHighLevel_cfi as hlt
process.hltFilter = hlt.hltHighLevel.clone(
    TriggerResultsTag = cms.InputTag('TriggerResults', '', 'MYHLT'),
    HLTPaths = ['Dataset_HLTMonitor']
)

# source module (EDM inputs)
process.source = cms.Source( "PoolSource",
    fileNames = cms.untracked.vstring(
        '/store/data/Run2024F/Muon0/RAW-RECO/ZMu-PromptReco-v1/000/382/216/00000/aadd1ab9-4eb8-4fb2-ac62-bdd1bebe882e.root'
        #'/store/data/Run2024F/EphemeralHLTPhysics1/RAW/v1/000/382/250/00000/005365a4-1194-48b8-a3c3-8da53a6a5dd5.root',
    ),
    inputCommands = cms.untracked.vstring(
        'drop *_*_*_RECO', 
        'keep FEDRawDataCollection_*_*_*'
    )
)

# Pixel, ECAL, ES, HCAL, Strips, Muons, Other
pixel_fed_list = (cms.vuint32(tuple(FEDinclude("Pixel"))))
ecal_fed_list = (cms.vuint32(tuple(FEDinclude("ECAL"))))
es_fed_list = (cms.vuint32(tuple(FEDinclude("ES"))))
hcal_fed_list = (cms.vuint32(tuple(FEDinclude("HCAL"))))
strips_fed_list = (cms.vuint32(tuple(FEDinclude("Strips"))))
muons_fed_list = (cms.vuint32(tuple(FEDinclude("Muons"))))
other_fed_list = (cms.vuint32(tuple(FEDinclude("Other"))))

process.partialRawDataRepackerPixel = cms.EDProducer( "EvFFEDSelector",
    inputTag = cms.InputTag( "rawDataCollector" ),
    fedList = pixel_fed_list
)
process.partialRawDataRepackerECAL = cms.EDProducer( "EvFFEDSelector",
    inputTag = cms.InputTag( "rawDataCollector" ),
    fedList = ecal_fed_list
)
process.partialRawDataRepackerES = cms.EDProducer( "EvFFEDSelector",
    inputTag = cms.InputTag( "rawDataCollector" ),
    fedList = es_fed_list
)
process.partialRawDataRepackerHCAL = cms.EDProducer( "EvFFEDSelector",
    inputTag = cms.InputTag( "rawDataCollector" ),
    fedList = hcal_fed_list
)
process.partialRawDataRepackerStrips = cms.EDProducer( "EvFFEDSelector",
    inputTag = cms.InputTag( "rawDataCollector" ),
    fedList = strips_fed_list
)
process.partialRawDataRepackerMuons = cms.EDProducer( "EvFFEDSelector",
    inputTag = cms.InputTag( "rawDataCollector" ),
    fedList = muons_fed_list
)
process.partialRawDataRepackerOther = cms.EDProducer( "EvFFEDSelector",
    inputTag = cms.InputTag( "rawDataCollector" ),
    fedList = other_fed_list
)

process.output = cms.OutputModule( "PoolOutputModule", fileName = cms.untracked.string( f'PartialRaw.root' ),
    compressionAlgorithm = cms.untracked.string( "ZSTD" ),
    compressionLevel = cms.untracked.int32( 3 ),
    fastCloning = cms.untracked.bool( False ),
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string( "" ),
        dataTier = cms.untracked.string( "RAW" )
    ),
    SelectEvents = cms.untracked.PSet(  SelectEvents = cms.vstring( 'PartialRawRepackers' ) ),
    outputCommands = cms.untracked.vstring( 'drop *',
      'keep FEDRawDataCollection_*_*_*',
      'keep *_siPixelDigis_*_*')
)

process.load('Configuration.StandardSequences.RawToDigi_Data_cff')
process.raw2digi_step = cms.Path(process.RawToDigi)

process.PartialRawRepackers = cms.Path(process.partialRawDataRepackerPixel 
                                       + process.partialRawDataRepackerECAL
                                       + process.partialRawDataRepackerES 
                                    #    + process.partialRawDataRepackerHCAL # Crashing 
                                       + process.partialRawDataRepackerStrips 
                                       + process.partialRawDataRepackerMuons 
                                       + process.partialRawDataRepackerOther)
process.PartialRawOutput = cms.FinalPath(process.output)

process.schedule = cms.Schedule( *(  process.raw2digi_step,process.PartialRawRepackers,process.PartialRawOutput, ))

