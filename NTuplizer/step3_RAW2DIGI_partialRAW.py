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
    secondaryFileNames = cms.untracked.vstring(
# '/store/relval/CMSSW_14_2_0_pre1/RelValTTbar_14TeV/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v21_STD_2024_PU-v3/2590000/12159f21-4931-4490-a9b7-6c9b9f0cbb70.root',
# '/store/relval/CMSSW_14_2_0_pre1/RelValTTbar_14TeV/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v21_STD_2024_PU-v3/2590000/7b721acf-91d2-479c-94a2-ada037435e6d.root',
# '/store/relval/CMSSW_14_2_0_pre1/RelValTTbar_14TeV/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v21_STD_2024_PU-v3/2590000/95f9925a-d7f9-4d35-8b27-6e435f46512f.root',
# '/store/relval/CMSSW_14_2_0_pre1/RelValTTbar_14TeV/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v21_STD_2024_PU-v3/2590000/e9c05c18-6f04-4da8-8831-6cc727eecad5.root',
# '/store/relval/CMSSW_14_2_0_pre1/RelValTTbar_14TeV/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v21_STD_2024_PU-v3/2590000/40272785-46dd-4863-b7c3-0583bcf438c1.root',
# '/store/relval/CMSSW_14_2_0_pre1/RelValTTbar_14TeV/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v21_STD_2024_PU-v3/2590000/8a92c9c0-21ff-4141-ad53-454dfe88b008.root',
# '/store/relval/CMSSW_14_2_0_pre1/RelValTTbar_14TeV/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v21_STD_2024_PU-v3/2590000/97822ade-c230-4023-84f3-1581d20a565c.root',
# '/store/relval/CMSSW_14_2_0_pre1/RelValTTbar_14TeV/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v21_STD_2024_PU-v3/2590000/efd7b1e9-30aa-432e-bda0-d3a5e7d9cac9.root',
# '/store/relval/CMSSW_14_2_0_pre1/RelValTTbar_14TeV/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v21_STD_2024_PU-v3/2590000/44bbf957-4bd7-4491-8b4c-c5e849f0b1bb.root',
# '/store/relval/CMSSW_14_2_0_pre1/RelValTTbar_14TeV/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v21_STD_2024_PU-v3/2590000/956a3184-ee77-4fb8-b941-55ac1efcc077.root',
'/store/relval/CMSSW_14_2_0_pre1/RelValTTbar_14TeV/GEN-SIM-DIGI-RAW/PU_140X_mcRun3_2024_realistic_v21_STD_2024_PU-v3/2590000/b20570d9-b5e4-4e16-a6a5-c5a7eb7f426d.root'
),
    fileNames = cms.untracked.vstring('/store/relval/CMSSW_14_2_0_pre1/RelValTTbar_14TeV/GEN-SIM-RECO/PU_140X_mcRun3_2024_realistic_v21_STD_2024_PU-v3/2590000/1e4e0463-6540-4868-8941-bba8e9f53129.root',
# '/store/relval/CMSSW_14_2_0_pre1/RelValTTbar_14TeV/GEN-SIM-RECO/PU_140X_mcRun3_2024_realistic_v21_STD_2024_PU-v3/2590000/8192a4a5-5703-4300-87c8-b4777478b6bc.root',
# '/store/relval/CMSSW_14_2_0_pre1/RelValTTbar_14TeV/GEN-SIM-RECO/PU_140X_mcRun3_2024_realistic_v21_STD_2024_PU-v3/2590000/a9ec961c-5bff-4023-a80a-728454d96abc.root',
# '/store/relval/CMSSW_14_2_0_pre1/RelValTTbar_14TeV/GEN-SIM-RECO/PU_140X_mcRun3_2024_realistic_v21_STD_2024_PU-v3/2590000/3c1e9bba-59d3-44b6-ad73-320ca3aaf0d0.root',
# '/store/relval/CMSSW_14_2_0_pre1/RelValTTbar_14TeV/GEN-SIM-RECO/PU_140X_mcRun3_2024_realistic_v21_STD_2024_PU-v3/2590000/84691d05-8baf-49d2-a875-f4c78d0f2431.root',
# '/store/relval/CMSSW_14_2_0_pre1/RelValTTbar_14TeV/GEN-SIM-RECO/PU_140X_mcRun3_2024_realistic_v21_STD_2024_PU-v3/2590000/aec76d64-8baa-42db-8a09-aa75d304c1e6.root',
# '/store/relval/CMSSW_14_2_0_pre1/RelValTTbar_14TeV/GEN-SIM-RECO/PU_140X_mcRun3_2024_realistic_v21_STD_2024_PU-v3/2590000/5d9c5dfc-490c-4875-a2a3-b043081d82ed.root',
# '/store/relval/CMSSW_14_2_0_pre1/RelValTTbar_14TeV/GEN-SIM-RECO/PU_140X_mcRun3_2024_realistic_v21_STD_2024_PU-v3/2590000/9069d3ba-a48b-4c59-ad69-4e1dbf10fd86.root',
# '/store/relval/CMSSW_14_2_0_pre1/RelValTTbar_14TeV/GEN-SIM-RECO/PU_140X_mcRun3_2024_realistic_v21_STD_2024_PU-v3/2590000/f1b8683c-123e-4f36-9dc8-f55e9f94ad62.root'
)
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
    numberOfThreads = cms.untracked.uint32(16),
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
    fileName = cms.untracked.string('step3_RAW2DIGI_partialRAW.root'),
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
            'keep *_simEcalPreshowerDigis_*_*',
            'keep *_ecalPreshowerDigis_*_*',
            'drop *_*_*_RECO'
            # 'keep *_siPixelClusters_*_RECO',
            # 'keep *_siStripClusters_*_RECO',
      )
    # splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, globaltag = '140X_mcRun3_2024_realistic_v21')

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

# Load reconstruction
process.load('Configuration.StandardSequences.Reconstruction_Data_cff')


# Add paths for reconstruction
process.reconstruction_step = cms.Path(process.reconstruction)


# Extend the schedule to include the new steps
process.schedule.extend([process.reconstruction_step])

# Update the output commands to keep clusters, rechits, and generalTracks
process.RECOoutput.outputCommands.extend([
    'keep *_siPixelClusters_*_*',
    'keep *_siStripClusters_*_*',
    'keep *_siPixelRecHits_*_*',
    'keep *_siStripMatchedRecHits_*_*',
    'keep *_generalTracks_*_*'
])
