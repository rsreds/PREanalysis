from importFED import FEDexclude,FEDinclude
import FWCore.ParameterSet.Config as cms
from Configuration.Eras.Era_Run3_cff import Run3

detector = "Pixel"
process = cms.Process("PRAW", Run3)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32( 100 )
)

process.options = cms.untracked.PSet(
    IgnoreCompletely = cms.untracked.vstring(),
    Rethrow = cms.untracked.vstring(),
    TryToContinue = cms.untracked.vstring(),
    accelerators = cms.untracked.vstring('*'),
    allowUnscheduled = cms.obsolete.untracked.bool,
    canDeleteEarly = cms.untracked.vstring(),
    deleteNonConsumedUnscheduledModules = cms.untracked.bool(True),
    dumpOptions = cms.untracked.bool(False),
    emptyRunLumiMode = cms.obsolete.untracked.string,
    eventSetup = cms.untracked.PSet(
        forceNumberOfConcurrentIOVs = cms.untracked.PSet(
            allowAnyLabel_=cms.required.untracked.uint32
        ),
        numberOfConcurrentIOVs = cms.untracked.uint32(0)
    ),
    fileMode = cms.untracked.string('FULLMERGE'),
    forceEventSetupCacheClearOnNewRun = cms.untracked.bool(False),
    holdsReferencesToDeleteEarly = cms.untracked.VPSet(),
    makeTriggerResults = cms.obsolete.untracked.bool,
    modulesToCallForTryToContinue = cms.untracked.vstring(),
    modulesToIgnoreForDeleteEarly = cms.untracked.vstring(),
    numberOfConcurrentLuminosityBlocks = cms.untracked.uint32(0),
    numberOfConcurrentRuns = cms.untracked.uint32(1),
    numberOfStreams = cms.untracked.uint32(0),
    numberOfThreads = cms.untracked.uint32(4),
    printDependencies = cms.untracked.bool(False),
    sizeOfStackForThreadsInKB = cms.optional.untracked.uint32,
    throwIfIllegalParameter = cms.untracked.bool(True),
    wantSummary = cms.untracked.bool(True)
)

process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
from Configuration.AlCa.GlobalTag import GlobalTag as customiseGlobalTag
process.GlobalTag = customiseGlobalTag(process.GlobalTag, globaltag = '141X_mcRun3_2024_realistic_HI_v5')

import HLTrigger.HLTfilters.hltHighLevel_cfi as hlt
process.hltFilter = hlt.hltHighLevel.clone(
    TriggerResultsTag = cms.InputTag('TriggerResults', '', 'MYHLT'),
    HLTPaths = ['Dataset_HLTMonitor']
)

# source module (EDM inputs)
process.source = cms.Source("PoolSource",
    secondaryFileNames = cms.untracked.vstring('/store/relval/CMSSW_14_2_0_pre2/RelValQCD_Pt_80_120_5362_HI_2024/GEN-SIM-DIGI-RAW-HLTDEBUG/141X_mcRun3_2024_realistic_HI_v5_STD_RegeneratedGS_2024HIN_noPU-v1/2580000/6886a037-5bea-4b34-9365-9162552694b7.root',
                                      '/store/relval/CMSSW_14_2_0_pre2/RelValQCD_Pt_80_120_5362_HI_2024/GEN-SIM-DIGI-RAW-HLTDEBUG/141X_mcRun3_2024_realistic_HI_v5_STD_RegeneratedGS_2024HIN_noPU-v1/2580000/6e6a801b-3be3-4cf4-9964-ef8fe3b25506.root',
                                      '/store/relval/CMSSW_14_2_0_pre2/RelValQCD_Pt_80_120_5362_HI_2024/GEN-SIM-DIGI-RAW-HLTDEBUG/141X_mcRun3_2024_realistic_HI_v5_STD_RegeneratedGS_2024HIN_noPU-v1/2580000/c088c4b4-1ac0-4e6d-a8ff-43187dfe26d0.root'),
    fileNames = cms.untracked.vstring('/store/relval/CMSSW_14_2_0_pre2/RelValQCD_Pt_80_120_5362_HI_2024/GEN-SIM-RECO/141X_mcRun3_2024_realistic_HI_v5_STD_RegeneratedGS_2024HIN_noPU-v1/2580000/59f0803f-b748-4bd7-ac3e-df2087512590.root',
                                               '/store/relval/CMSSW_14_2_0_pre2/RelValQCD_Pt_80_120_5362_HI_2024/GEN-SIM-RECO/141X_mcRun3_2024_realistic_HI_v5_STD_RegeneratedGS_2024HIN_noPU-v1/2580000/d5761040-3e83-4987-8f59-01b1af2f0399.root')
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
        dataTier = cms.untracked.string( "DIGI" )
    ),
    SelectEvents = cms.untracked.PSet(  SelectEvents = cms.vstring( 'PartialRawRepackers' ) ),
    outputCommands = cms.untracked.vstring( 'drop *',
      'keep FEDRawDataCollection_*_*_*',
      'keep *DigiSim*_*_*_*',
      'keep *_*Digis_*_*')
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

