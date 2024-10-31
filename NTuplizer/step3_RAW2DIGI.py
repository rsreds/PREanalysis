# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: step3 --conditions auto:run3_data_prompt_relval -s RAW2DIGI --datatier DIGI --eventcontent RECO --data --process reRECO --scenario pp --era Run3 --customise Configuration/DataProcessing/RecoTLR.customisePostEra_Run3 -n 100 --filein /store/data/Run2024F/Muon0/RAW-RECO/ZMu-PromptReco-v1/000/382/216/00000/aadd1ab9-4eb8-4fb2-ac62-bdd1bebe882e.root
from importFED import FEDexclude,FEDinclude 
import FWCore.ParameterSet.Config as cms
from Configuration.Eras.Era_Run3_cff import Run3

process = cms.Process('reRECO',Run3)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.RawToDigi_Data_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(100),
    output = cms.optional.untracked.allowed(cms.int32,cms.PSet)
)

# Input source
process.source = cms.Source("PoolSource",
    secondaryFileNames = cms.untracked.vstring('/store/relval/CMSSW_14_2_0_pre2/RelValQCD_Pt_80_120_5362_HI_2024/GEN-SIM-DIGI-RAW-HLTDEBUG/141X_mcRun3_2024_realistic_HI_v5_STD_RegeneratedGS_2024HIN_noPU-v1/2580000/6886a037-5bea-4b34-9365-9162552694b7.root',
                                      '/store/relval/CMSSW_14_2_0_pre2/RelValQCD_Pt_80_120_5362_HI_2024/GEN-SIM-DIGI-RAW-HLTDEBUG/141X_mcRun3_2024_realistic_HI_v5_STD_RegeneratedGS_2024HIN_noPU-v1/2580000/6e6a801b-3be3-4cf4-9964-ef8fe3b25506.root',
                                      '/store/relval/CMSSW_14_2_0_pre2/RelValQCD_Pt_80_120_5362_HI_2024/GEN-SIM-DIGI-RAW-HLTDEBUG/141X_mcRun3_2024_realistic_HI_v5_STD_RegeneratedGS_2024HIN_noPU-v1/2580000/c088c4b4-1ac0-4e6d-a8ff-43187dfe26d0.root'),
    fileNames = cms.untracked.vstring('/store/relval/CMSSW_14_2_0_pre2/RelValQCD_Pt_80_120_5362_HI_2024/GEN-SIM-RECO/141X_mcRun3_2024_realistic_HI_v5_STD_RegeneratedGS_2024HIN_noPU-v1/2580000/59f0803f-b748-4bd7-ac3e-df2087512590.root',
                                               '/store/relval/CMSSW_14_2_0_pre2/RelValQCD_Pt_80_120_5362_HI_2024/GEN-SIM-RECO/141X_mcRun3_2024_realistic_HI_v5_STD_RegeneratedGS_2024HIN_noPU-v1/2580000/d5761040-3e83-4987-8f59-01b1af2f0399.root')
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
    numberOfThreads = cms.untracked.uint32(1),
    printDependencies = cms.untracked.bool(False),
    sizeOfStackForThreadsInKB = cms.optional.untracked.uint32,
    throwIfIllegalParameter = cms.untracked.bool(True),
    wantSummary = cms.untracked.bool(False)
)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('step3 nevts:100'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
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

# Output definition
process.RECOoutput = cms.OutputModule("PoolOutputModule",
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('DIGI'),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string('step3_Raw2Digi_PartialRaw.root'),
    SelectEvents = cms.untracked.PSet(  SelectEvents = cms.vstring( 'partialrawrepackers_step' ) ),
    outputCommands = cms.untracked.vstring(
            'drop *',
            'keep FEDRawDataCollection_*_*_*',
            'keep *_siStripDigis_*_*',
            'keep *_siPixelDigis_*_*',
            'keep *_ecalDigis_*_*',
            'keep *_hcalDigis_*_*',
            'keep *_simHcalDigis_*_*',
            'keep *_simEcalDigis_*_*',
            'keep *_simSiStripDigis_*_*',
            'keep *_simSiPixelDigis_*_*',
            'drop *_*_*_RECO'
      )
    # splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, globaltag = '141X_mcRun3_2024_realistic_HI_v5')

# Path and EndPath definitions
process.raw2digi_step = cms.Path(process.RawToDigi)
process.partialrawrepackers_step = cms.Path(process.partialRawDataRepackerPixel 
                                       + process.partialRawDataRepackerECAL
                                       + process.partialRawDataRepackerES 
                                    #    + process.partialRawDataRepackerHCAL # Crashing 
                                       + process.partialRawDataRepackerStrips 
                                       + process.partialRawDataRepackerMuons 
                                       + process.partialRawDataRepackerOther)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.output_step = cms.EndPath(process.RECOoutput)

# Schedule definition
process.schedule = cms.Schedule(process.raw2digi_step,process.partialrawrepackers_step,process.endjob_step,process.output_step)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)

# customisation of the process.

# Automatic addition of the customisation function from Configuration.DataProcessing.RecoTLR
from Configuration.DataProcessing.RecoTLR import customisePostEra_Run3 

#call to customisation function customisePostEra_Run3 imported from Configuration.DataProcessing.RecoTLR
process = customisePostEra_Run3(process)

# End of customisation functions


# Customisation from command line

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
