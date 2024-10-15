# SNMP MIB module (CHIPAGENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CHIPAGENT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:54:43 2024
# On host MacBook-Pro.local platform Darwin version 24.0.0 by user lextm
# Using Python version 3.12.0 (main, Nov 14 2023, 23:52:11) [Clang 15.0.0 (clang-1500.0.40.1)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint,
 ConstraintsUnion) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint",
    "ConstraintsUnion")

# Import SMI symbols from the MIBs this MIB depends on

(DisplayString,) = mibBuilder.importSymbols(
    "RFC1155-SMI",
    "DisplayString")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 enterprises,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Chipcom_ObjectIdentity = ObjectIdentity
chipcom = _Chipcom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49)
)
_Chipmib02_ObjectIdentity = ObjectIdentity
chipmib02 = _Chipmib02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2)
)
_ChipGen_ObjectIdentity = ObjectIdentity
chipGen = _ChipGen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 1)
)


class _ChipGenProduct_Type(Integer32):
    """Custom type chipGenProduct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              7)
        )
    )
    namedValues = NamedValues(
        *(("product-5100M-MGT", 1),
          ("product-5102B-EE", 2),
          ("product-5112H-UTP", 4),
          ("product-5200M-MGT", 7),
          ("product-5300M-MGT", 5),
          ("product-8383B", 3))
    )


_ChipGenProduct_Type.__name__ = "Integer32"
_ChipGenProduct_Object = MibScalar
chipGenProduct = _ChipGenProduct_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 1, 1),
    _ChipGenProduct_Type()
)
chipGenProduct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chipGenProduct.setStatus("mandatory")


class _ChipGenServiceDate_Type(DisplayString):
    """Custom type chipGenServiceDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_ChipGenServiceDate_Type.__name__ = "DisplayString"
_ChipGenServiceDate_Object = MibScalar
chipGenServiceDate = _ChipGenServiceDate_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 1, 2),
    _ChipGenServiceDate_Type()
)
chipGenServiceDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chipGenServiceDate.setStatus("mandatory")
_ChipGenNetman_Type = IpAddress
_ChipGenNetman_Object = MibScalar
chipGenNetman = _ChipGenNetman_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 1, 3),
    _ChipGenNetman_Type()
)
chipGenNetman.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chipGenNetman.setStatus("mandatory")


class _ChipGenDiagnostics_Type(Integer32):
    """Custom type chipGenDiagnostics based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failed", 2),
          ("passed", 1))
    )


_ChipGenDiagnostics_Type.__name__ = "Integer32"
_ChipGenDiagnostics_Object = MibScalar
chipGenDiagnostics = _ChipGenDiagnostics_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 1, 4),
    _ChipGenDiagnostics_Type()
)
chipGenDiagnostics.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chipGenDiagnostics.setStatus("mandatory")


class _ChipGenSerial_Type(DisplayString):
    """Custom type chipGenSerial based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_ChipGenSerial_Type.__name__ = "DisplayString"
_ChipGenSerial_Object = MibScalar
chipGenSerial = _ChipGenSerial_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 1, 5),
    _ChipGenSerial_Type()
)
chipGenSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chipGenSerial.setStatus("mandatory")
_ChipGenID_Type = Integer32
_ChipGenID_Object = MibScalar
chipGenID = _ChipGenID_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 1, 6),
    _ChipGenID_Type()
)
chipGenID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chipGenID.setStatus("mandatory")


class _ChipGenVers_Type(DisplayString):
    """Custom type chipGenVers based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_ChipGenVers_Type.__name__ = "DisplayString"
_ChipGenVers_Object = MibScalar
chipGenVers = _ChipGenVers_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 1, 7),
    _ChipGenVers_Type()
)
chipGenVers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chipGenVers.setStatus("mandatory")
_ChipGenAuthFailureAddr_Type = IpAddress
_ChipGenAuthFailureAddr_Object = MibScalar
chipGenAuthFailureAddr = _ChipGenAuthFailureAddr_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 1, 8),
    _ChipGenAuthFailureAddr_Type()
)
chipGenAuthFailureAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chipGenAuthFailureAddr.setStatus("mandatory")
_ChipGenTimeLastChanged_Type = TimeTicks
_ChipGenTimeLastChanged_Object = MibScalar
chipGenTimeLastChanged = _ChipGenTimeLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 1, 9),
    _ChipGenTimeLastChanged_Type()
)
chipGenTimeLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chipGenTimeLastChanged.setStatus("mandatory")
_ChipEcho_ObjectIdentity = ObjectIdentity
chipEcho = _ChipEcho_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 2)
)


class _ChipEchoStart_Type(Integer32):
    """Custom type chipEchoStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noEcho", 1),
          ("startEcho", 2))
    )


_ChipEchoStart_Type.__name__ = "Integer32"
_ChipEchoStart_Object = MibScalar
chipEchoStart = _ChipEchoStart_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 2, 1),
    _ChipEchoStart_Type()
)
chipEchoStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chipEchoStart.setStatus("mandatory")
_ChipEchoAddr_Type = IpAddress
_ChipEchoAddr_Object = MibScalar
chipEchoAddr = _ChipEchoAddr_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 2, 2),
    _ChipEchoAddr_Type()
)
chipEchoAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chipEchoAddr.setStatus("mandatory")


class _ChipEchoPattern_Type(Integer32):
    """Custom type chipEchoPattern based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mixed", 3),
          ("ones", 2),
          ("zeroes", 1))
    )


_ChipEchoPattern_Type.__name__ = "Integer32"
_ChipEchoPattern_Object = MibScalar
chipEchoPattern = _ChipEchoPattern_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 2, 3),
    _ChipEchoPattern_Type()
)
chipEchoPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chipEchoPattern.setStatus("mandatory")


class _ChipEchoNumber_Type(Integer32):
    """Custom type chipEchoNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ChipEchoNumber_Type.__name__ = "Integer32"
_ChipEchoNumber_Object = MibScalar
chipEchoNumber = _ChipEchoNumber_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 2, 4),
    _ChipEchoNumber_Type()
)
chipEchoNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chipEchoNumber.setStatus("mandatory")


class _ChipEchoSize_Type(Integer32):
    """Custom type chipEchoSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 1500),
    )


_ChipEchoSize_Type.__name__ = "Integer32"
_ChipEchoSize_Object = MibScalar
chipEchoSize = _ChipEchoSize_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 2, 5),
    _ChipEchoSize_Type()
)
chipEchoSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chipEchoSize.setStatus("mandatory")
_ChipEchoResponseCounts_Type = Counter32
_ChipEchoResponseCounts_Object = MibScalar
chipEchoResponseCounts = _ChipEchoResponseCounts_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 2, 6),
    _ChipEchoResponseCounts_Type()
)
chipEchoResponseCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chipEchoResponseCounts.setStatus("mandatory")
_ChipProducts_ObjectIdentity = ObjectIdentity
chipProducts = _ChipProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3)
)
_Online_ObjectIdentity = ObjectIdentity
online = _Online_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1)
)
_OlAgents_ObjectIdentity = ObjectIdentity
olAgents = _OlAgents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 1)
)
_OlConc_ObjectIdentity = ObjectIdentity
olConc = _OlConc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 2)
)
_OlEnv_ObjectIdentity = ObjectIdentity
olEnv = _OlEnv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 3)
)
_OlModules_ObjectIdentity = ObjectIdentity
olModules = _OlModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4)
)
_OlSpecMods_ObjectIdentity = ObjectIdentity
olSpecMods = _OlSpecMods_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4)
)
_Ol50nnMCTL_ObjectIdentity = ObjectIdentity
ol50nnMCTL = _Ol50nnMCTL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 3)
)
_Ol51nnMMGT_ObjectIdentity = ObjectIdentity
ol51nnMMGT = _Ol51nnMMGT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 4)
)
_Ol51nnMFIB_ObjectIdentity = ObjectIdentity
ol51nnMFIB = _Ol51nnMFIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 5)
)
_Ol51nnMUTP_ObjectIdentity = ObjectIdentity
ol51nnMUTP = _Ol51nnMUTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 6)
)
_Ol51nnMTP_ObjectIdentity = ObjectIdentity
ol51nnMTP = _Ol51nnMTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 7)
)
_Ol51nnMBNC_ObjectIdentity = ObjectIdentity
ol51nnMBNC = _Ol51nnMBNC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 8)
)
_Ol51nnBEE_ObjectIdentity = ObjectIdentity
ol51nnBEE = _Ol51nnBEE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 9)
)
_Ol51nnRES_ObjectIdentity = ObjectIdentity
ol51nnRES = _Ol51nnRES_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 10)
)
_Ol51nnREE_ObjectIdentity = ObjectIdentity
ol51nnREE = _Ol51nnREE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 11)
)
_Ol51nnMAUIF_ObjectIdentity = ObjectIdentity
ol51nnMAUIF = _Ol51nnMAUIF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 12)
)
_Ol51nnMAUIM_ObjectIdentity = ObjectIdentity
ol51nnMAUIM = _Ol51nnMAUIM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 13)
)
_Ol5208MTP_ObjectIdentity = ObjectIdentity
ol5208MTP = _Ol5208MTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 14)
)
_Ol51nnMFP_ObjectIdentity = ObjectIdentity
ol51nnMFP = _Ol51nnMFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 15)
)
_Ol51nnMFBP_ObjectIdentity = ObjectIdentity
ol51nnMFBP = _Ol51nnMFBP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 16)
)
_Ol51nnMTPL_ObjectIdentity = ObjectIdentity
ol51nnMTPL = _Ol51nnMTPL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 17)
)
_Ol51nnMTPPL_ObjectIdentity = ObjectIdentity
ol51nnMTPPL = _Ol51nnMTPPL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 18)
)
_Ol52nnMTP_ObjectIdentity = ObjectIdentity
ol52nnMTP = _Ol52nnMTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 19)
)
_Ol52nnMFR_ObjectIdentity = ObjectIdentity
ol52nnMFR = _Ol52nnMFR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 20)
)
_Ol51nnMTS_ObjectIdentity = ObjectIdentity
ol51nnMTS = _Ol51nnMTS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 21)
)
_Ol51nnMFL_ObjectIdentity = ObjectIdentity
ol51nnMFL = _Ol51nnMFL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 22)
)
_Ol50nnMRCTL_ObjectIdentity = ObjectIdentity
ol50nnMRCTL = _Ol50nnMRCTL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 23)
)
_Ol51nnMFB_ObjectIdentity = ObjectIdentity
ol51nnMFB = _Ol51nnMFB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 24)
)
_Ol53nnMMGT_ObjectIdentity = ObjectIdentity
ol53nnMMGT = _Ol53nnMMGT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 25)
)
_Ol53nnMFBMIC_ObjectIdentity = ObjectIdentity
ol53nnMFBMIC = _Ol53nnMFBMIC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 26)
)
_Ol53nnMFIBST_ObjectIdentity = ObjectIdentity
ol53nnMFIBST = _Ol53nnMFIBST_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 27)
)
_Ol53nnMSTP_ObjectIdentity = ObjectIdentity
ol53nnMSTP = _Ol53nnMSTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 28)
)
_Ol51nnMTPCL_ObjectIdentity = ObjectIdentity
ol51nnMTPCL = _Ol51nnMTPCL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 29)
)
_Ol52nnBTT_ObjectIdentity = ObjectIdentity
ol52nnBTT = _Ol52nnBTT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 30)
)
_Ol51nnIx_ObjectIdentity = ObjectIdentity
ol51nnIx = _Ol51nnIx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 31)
)
_Ol52nnMMGT_ObjectIdentity = ObjectIdentity
ol52nnMMGT = _Ol52nnMMGT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 32)
)
_Ol50nnMHCTL_ObjectIdentity = ObjectIdentity
ol50nnMHCTL = _Ol50nnMHCTL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 4, 4, 33)
)
_OlNets_ObjectIdentity = ObjectIdentity
olNets = _OlNets_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5)
)
_OlNet_ObjectIdentity = ObjectIdentity
olNet = _OlNet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 1)
)
_OlEnet_ObjectIdentity = ObjectIdentity
olEnet = _OlEnet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 2)
)
_OlTRnet_ObjectIdentity = ObjectIdentity
olTRnet = _OlTRnet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 3)
)
_OlFDDInet_ObjectIdentity = ObjectIdentity
olFDDInet = _OlFDDInet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 5, 4)
)
_OlGroups_ObjectIdentity = ObjectIdentity
olGroups = _OlGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 6)
)
_OlAlarm_ObjectIdentity = ObjectIdentity
olAlarm = _OlAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 7)
)
_OlThresh_ObjectIdentity = ObjectIdentity
olThresh = _OlThresh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 7, 1)
)
_OlThreshControl_ObjectIdentity = ObjectIdentity
olThreshControl = _OlThreshControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 1, 7, 1, 1)
)
_Oebm_ObjectIdentity = ObjectIdentity
oebm = _Oebm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 2)
)
_Midnight_ObjectIdentity = ObjectIdentity
midnight = _Midnight_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 3)
)
_WorkGroupHub_ObjectIdentity = ObjectIdentity
workGroupHub = _WorkGroupHub_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 4)
)
_HubSysGroup_ObjectIdentity = ObjectIdentity
hubSysGroup = _HubSysGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 4, 1)
)
_HardwareGroup_ObjectIdentity = ObjectIdentity
hardwareGroup = _HardwareGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 4, 2)
)
_SoftwareGroup_ObjectIdentity = ObjectIdentity
softwareGroup = _SoftwareGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 4, 3)
)
_HubGroup_ObjectIdentity = ObjectIdentity
hubGroup = _HubGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 4, 4)
)
_BoardGroup_ObjectIdentity = ObjectIdentity
boardGroup = _BoardGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 4, 5)
)
_PortGroup_ObjectIdentity = ObjectIdentity
portGroup = _PortGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 4, 6)
)
_AlarmGroup_ObjectIdentity = ObjectIdentity
alarmGroup = _AlarmGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 4, 7)
)
_Emm_ObjectIdentity = ObjectIdentity
emm = _Emm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 5)
)
_ChipBridge_ObjectIdentity = ObjectIdentity
chipBridge = _ChipBridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 6)
)
_Trmm_ObjectIdentity = ObjectIdentity
trmm = _Trmm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 7)
)
_Fmm_ObjectIdentity = ObjectIdentity
fmm = _Fmm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 8)
)
_Focus1_ObjectIdentity = ObjectIdentity
focus1 = _Focus1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 9)
)
_Oeim_ObjectIdentity = ObjectIdentity
oeim = _Oeim_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 3, 10)
)
_ChipExperiment_ObjectIdentity = ObjectIdentity
chipExperiment = _ChipExperiment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 4)
)
_ChipExpTokenRing_ObjectIdentity = ObjectIdentity
chipExpTokenRing = _ChipExpTokenRing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 1)
)
_Dot5_ObjectIdentity = ObjectIdentity
dot5 = _Dot5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 1, 1)
)
_Dot1dBridge_ObjectIdentity = ObjectIdentity
dot1dBridge = _Dot1dBridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 4, 14)
)
_ChipTTY_ObjectIdentity = ObjectIdentity
chipTTY = _ChipTTY_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 5)
)
_ChipTTYNumber_Type = Integer32
_ChipTTYNumber_Object = MibScalar
chipTTYNumber = _ChipTTYNumber_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 5, 1),
    _ChipTTYNumber_Type()
)
chipTTYNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chipTTYNumber.setStatus("mandatory")
_ChipTTYTable_Object = MibTable
chipTTYTable = _ChipTTYTable_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 5, 2)
)
if mibBuilder.loadTexts:
    chipTTYTable.setStatus("mandatory")
_ChipTTYEntry_Object = MibTableRow
chipTTYEntry = _ChipTTYEntry_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 5, 2, 1)
)
chipTTYEntry.setIndexNames(
    (0, "CHIPAGENT-MIB", "chipTTYIndex"),
)
if mibBuilder.loadTexts:
    chipTTYEntry.setStatus("mandatory")
_ChipTTYIndex_Type = Integer32
_ChipTTYIndex_Object = MibTableColumn
chipTTYIndex = _ChipTTYIndex_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 5, 2, 1, 1),
    _ChipTTYIndex_Type()
)
chipTTYIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chipTTYIndex.setStatus("mandatory")


class _ChipTTYBaud_Type(Integer32):
    """Custom type chipTTYBaud based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(110,
              300,
              1200,
              2400,
              4800,
              9600,
              19200,
              38400)
        )
    )
    namedValues = NamedValues(
        *(("forty-eight-hundred", 4800),
          ("nineteen-two-hundred", 19200),
          ("ninety-six-hundred", 9600),
          ("one-hundred-ten", 110),
          ("thirty-eight-thousand-four-hundred", 38400),
          ("three-hundred", 300),
          ("twelve-hundred", 1200),
          ("twenty-four-hundred", 2400))
    )


_ChipTTYBaud_Type.__name__ = "Integer32"
_ChipTTYBaud_Object = MibTableColumn
chipTTYBaud = _ChipTTYBaud_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 5, 2, 1, 2),
    _ChipTTYBaud_Type()
)
chipTTYBaud.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chipTTYBaud.setStatus("mandatory")


class _ChipTTYParity_Type(Integer32):
    """Custom type chipTTYParity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("even", 2),
          ("none", 3),
          ("odd", 1))
    )


_ChipTTYParity_Type.__name__ = "Integer32"
_ChipTTYParity_Object = MibTableColumn
chipTTYParity = _ChipTTYParity_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 5, 2, 1, 3),
    _ChipTTYParity_Type()
)
chipTTYParity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chipTTYParity.setStatus("mandatory")


class _ChipTTYStop_Type(Integer32):
    """Custom type chipTTYStop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("one", 1),
          ("two", 2))
    )


_ChipTTYStop_Type.__name__ = "Integer32"
_ChipTTYStop_Object = MibTableColumn
chipTTYStop = _ChipTTYStop_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 5, 2, 1, 4),
    _ChipTTYStop_Type()
)
chipTTYStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chipTTYStop.setStatus("mandatory")


class _ChipTTYData_Type(Integer32):
    """Custom type chipTTYData based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("eight", 8),
          ("seven", 7))
    )


_ChipTTYData_Type.__name__ = "Integer32"
_ChipTTYData_Object = MibTableColumn
chipTTYData = _ChipTTYData_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 5, 2, 1, 5),
    _ChipTTYData_Type()
)
chipTTYData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chipTTYData.setStatus("mandatory")
_ChipTTYTimeout_Type = Integer32
_ChipTTYTimeout_Object = MibTableColumn
chipTTYTimeout = _ChipTTYTimeout_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 5, 2, 1, 6),
    _ChipTTYTimeout_Type()
)
chipTTYTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chipTTYTimeout.setStatus("mandatory")


class _ChipTTYPrompt_Type(DisplayString):
    """Custom type chipTTYPrompt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_ChipTTYPrompt_Type.__name__ = "DisplayString"
_ChipTTYPrompt_Object = MibTableColumn
chipTTYPrompt = _ChipTTYPrompt_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 5, 2, 1, 7),
    _ChipTTYPrompt_Type()
)
chipTTYPrompt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chipTTYPrompt.setStatus("mandatory")


class _ChipTTYDTR_Type(Integer32):
    """Custom type chipTTYDTR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("asserted", 1),
          ("deasserted", 2))
    )


_ChipTTYDTR_Type.__name__ = "Integer32"
_ChipTTYDTR_Object = MibTableColumn
chipTTYDTR = _ChipTTYDTR_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 5, 2, 1, 8),
    _ChipTTYDTR_Type()
)
chipTTYDTR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chipTTYDTR.setStatus("mandatory")


class _ChipTTYTerminalType_Type(DisplayString):
    """Custom type chipTTYTerminalType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_ChipTTYTerminalType_Type.__name__ = "DisplayString"
_ChipTTYTerminalType_Object = MibTableColumn
chipTTYTerminalType = _ChipTTYTerminalType_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 5, 2, 1, 9),
    _ChipTTYTerminalType_Type()
)
chipTTYTerminalType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chipTTYTerminalType.setStatus("mandatory")
_ChipTFTP_ObjectIdentity = ObjectIdentity
chipTFTP = _ChipTFTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 6)
)


class _ChipTFTPStart_Type(Integer32):
    """Custom type chipTFTPStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("tftpGet", 2),
          ("tftpNoTransfer", 1),
          ("tftpPut", 3))
    )


_ChipTFTPStart_Type.__name__ = "Integer32"
_ChipTFTPStart_Object = MibScalar
chipTFTPStart = _ChipTFTPStart_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 6, 1),
    _ChipTFTPStart_Type()
)
chipTFTPStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chipTFTPStart.setStatus("mandatory")


class _ChipTFTPSlot_Type(Integer32):
    """Custom type chipTFTPSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              255)
        )
    )
    namedValues = NamedValues(
        *(("agent-slot", 255),
          ("slot-1", 1),
          ("slot-10", 10),
          ("slot-11", 11),
          ("slot-12", 12),
          ("slot-13", 13),
          ("slot-14", 14),
          ("slot-15", 15),
          ("slot-16", 16),
          ("slot-17", 17),
          ("slot-2", 2),
          ("slot-3", 3),
          ("slot-4", 4),
          ("slot-5", 5),
          ("slot-6", 6),
          ("slot-7", 7),
          ("slot-8", 8),
          ("slot-9", 9))
    )


_ChipTFTPSlot_Type.__name__ = "Integer32"
_ChipTFTPSlot_Object = MibScalar
chipTFTPSlot = _ChipTFTPSlot_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 6, 2),
    _ChipTFTPSlot_Type()
)
chipTFTPSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chipTFTPSlot.setStatus("mandatory")
_ChipTFTPIpAddress_Type = IpAddress
_ChipTFTPIpAddress_Object = MibScalar
chipTFTPIpAddress = _ChipTFTPIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 6, 3),
    _ChipTFTPIpAddress_Type()
)
chipTFTPIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chipTFTPIpAddress.setStatus("mandatory")


class _ChipTFTPFileName_Type(DisplayString):
    """Custom type chipTFTPFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_ChipTFTPFileName_Type.__name__ = "DisplayString"
_ChipTFTPFileName_Object = MibScalar
chipTFTPFileName = _ChipTFTPFileName_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 6, 4),
    _ChipTFTPFileName_Type()
)
chipTFTPFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chipTFTPFileName.setStatus("mandatory")


class _ChipTFTPFileType_Type(Integer32):
    """Custom type chipTFTPFileType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bootCode", 2),
          ("flashCode", 1))
    )


_ChipTFTPFileType_Type.__name__ = "Integer32"
_ChipTFTPFileType_Object = MibScalar
chipTFTPFileType = _ChipTFTPFileType_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 6, 5),
    _ChipTFTPFileType_Type()
)
chipTFTPFileType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chipTFTPFileType.setStatus("mandatory")


class _ChipTFTPResult_Type(Integer32):
    """Custom type chipTFTPResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17)
        )
    )
    namedValues = NamedValues(
        *(("accessError", 6),
          ("clear", 1),
          ("decodeError", 17),
          ("diskFull", 7),
          ("fepromErase", 14),
          ("fepromProg", 15),
          ("fileNotFound", 5),
          ("illegalTFTPOperation", 8),
          ("invalidDownloadKey", 11),
          ("invalidNetwork", 13),
          ("invalidSlot", 12),
          ("invalidTFTPTransactionID", 9),
          ("noResponse", 10),
          ("okay", 3),
          ("otherTFTPError", 4),
          ("xferError", 16),
          ("xferInProgress", 2))
    )


_ChipTFTPResult_Type.__name__ = "Integer32"
_ChipTFTPResult_Object = MibScalar
chipTFTPResult = _ChipTFTPResult_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 6, 6),
    _ChipTFTPResult_Type()
)
chipTFTPResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chipTFTPResult.setStatus("mandatory")
_ChipDownload_ObjectIdentity = ObjectIdentity
chipDownload = _ChipDownload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 49, 2, 7)
)


class _ChipDownloadUDKSerial_Type(DisplayString):
    """Custom type chipDownloadUDKSerial based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_ChipDownloadUDKSerial_Type.__name__ = "DisplayString"
_ChipDownloadUDKSerial_Object = MibScalar
chipDownloadUDKSerial = _ChipDownloadUDKSerial_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 7, 1),
    _ChipDownloadUDKSerial_Type()
)
chipDownloadUDKSerial.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chipDownloadUDKSerial.setStatus("mandatory")


class _ChipDownloadKey_Type(DisplayString):
    """Custom type chipDownloadKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_ChipDownloadKey_Type.__name__ = "DisplayString"
_ChipDownloadKey_Object = MibScalar
chipDownloadKey = _ChipDownloadKey_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 7, 2),
    _ChipDownloadKey_Type()
)
chipDownloadKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chipDownloadKey.setStatus("mandatory")


class _ChipDownloadDateTime_Type(DisplayString):
    """Custom type chipDownloadDateTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_ChipDownloadDateTime_Type.__name__ = "DisplayString"
_ChipDownloadDateTime_Object = MibScalar
chipDownloadDateTime = _ChipDownloadDateTime_Object(
    (1, 3, 6, 1, 4, 1, 49, 2, 7, 3),
    _ChipDownloadDateTime_Type()
)
chipDownloadDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chipDownloadDateTime.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CHIPAGENT-MIB",
    **{"chipcom": chipcom,
       "chipmib02": chipmib02,
       "chipGen": chipGen,
       "chipGenProduct": chipGenProduct,
       "chipGenServiceDate": chipGenServiceDate,
       "chipGenNetman": chipGenNetman,
       "chipGenDiagnostics": chipGenDiagnostics,
       "chipGenSerial": chipGenSerial,
       "chipGenID": chipGenID,
       "chipGenVers": chipGenVers,
       "chipGenAuthFailureAddr": chipGenAuthFailureAddr,
       "chipGenTimeLastChanged": chipGenTimeLastChanged,
       "chipEcho": chipEcho,
       "chipEchoStart": chipEchoStart,
       "chipEchoAddr": chipEchoAddr,
       "chipEchoPattern": chipEchoPattern,
       "chipEchoNumber": chipEchoNumber,
       "chipEchoSize": chipEchoSize,
       "chipEchoResponseCounts": chipEchoResponseCounts,
       "chipProducts": chipProducts,
       "online": online,
       "olAgents": olAgents,
       "olConc": olConc,
       "olEnv": olEnv,
       "olModules": olModules,
       "olSpecMods": olSpecMods,
       "ol50nnMCTL": ol50nnMCTL,
       "ol51nnMMGT": ol51nnMMGT,
       "ol51nnMFIB": ol51nnMFIB,
       "ol51nnMUTP": ol51nnMUTP,
       "ol51nnMTP": ol51nnMTP,
       "ol51nnMBNC": ol51nnMBNC,
       "ol51nnBEE": ol51nnBEE,
       "ol51nnRES": ol51nnRES,
       "ol51nnREE": ol51nnREE,
       "ol51nnMAUIF": ol51nnMAUIF,
       "ol51nnMAUIM": ol51nnMAUIM,
       "ol5208MTP": ol5208MTP,
       "ol51nnMFP": ol51nnMFP,
       "ol51nnMFBP": ol51nnMFBP,
       "ol51nnMTPL": ol51nnMTPL,
       "ol51nnMTPPL": ol51nnMTPPL,
       "ol52nnMTP": ol52nnMTP,
       "ol52nnMFR": ol52nnMFR,
       "ol51nnMTS": ol51nnMTS,
       "ol51nnMFL": ol51nnMFL,
       "ol50nnMRCTL": ol50nnMRCTL,
       "ol51nnMFB": ol51nnMFB,
       "ol53nnMMGT": ol53nnMMGT,
       "ol53nnMFBMIC": ol53nnMFBMIC,
       "ol53nnMFIBST": ol53nnMFIBST,
       "ol53nnMSTP": ol53nnMSTP,
       "ol51nnMTPCL": ol51nnMTPCL,
       "ol52nnBTT": ol52nnBTT,
       "ol51nnIx": ol51nnIx,
       "ol52nnMMGT": ol52nnMMGT,
       "ol50nnMHCTL": ol50nnMHCTL,
       "olNets": olNets,
       "olNet": olNet,
       "olEnet": olEnet,
       "olTRnet": olTRnet,
       "olFDDInet": olFDDInet,
       "olGroups": olGroups,
       "olAlarm": olAlarm,
       "olThresh": olThresh,
       "olThreshControl": olThreshControl,
       "oebm": oebm,
       "midnight": midnight,
       "workGroupHub": workGroupHub,
       "hubSysGroup": hubSysGroup,
       "hardwareGroup": hardwareGroup,
       "softwareGroup": softwareGroup,
       "hubGroup": hubGroup,
       "boardGroup": boardGroup,
       "portGroup": portGroup,
       "alarmGroup": alarmGroup,
       "emm": emm,
       "chipBridge": chipBridge,
       "trmm": trmm,
       "fmm": fmm,
       "focus1": focus1,
       "oeim": oeim,
       "chipExperiment": chipExperiment,
       "chipExpTokenRing": chipExpTokenRing,
       "dot5": dot5,
       "dot1dBridge": dot1dBridge,
       "chipTTY": chipTTY,
       "chipTTYNumber": chipTTYNumber,
       "chipTTYTable": chipTTYTable,
       "chipTTYEntry": chipTTYEntry,
       "chipTTYIndex": chipTTYIndex,
       "chipTTYBaud": chipTTYBaud,
       "chipTTYParity": chipTTYParity,
       "chipTTYStop": chipTTYStop,
       "chipTTYData": chipTTYData,
       "chipTTYTimeout": chipTTYTimeout,
       "chipTTYPrompt": chipTTYPrompt,
       "chipTTYDTR": chipTTYDTR,
       "chipTTYTerminalType": chipTTYTerminalType,
       "chipTFTP": chipTFTP,
       "chipTFTPStart": chipTFTPStart,
       "chipTFTPSlot": chipTFTPSlot,
       "chipTFTPIpAddress": chipTFTPIpAddress,
       "chipTFTPFileName": chipTFTPFileName,
       "chipTFTPFileType": chipTFTPFileType,
       "chipTFTPResult": chipTFTPResult,
       "chipDownload": chipDownload,
       "chipDownloadUDKSerial": chipDownloadUDKSerial,
       "chipDownloadKey": chipDownloadKey,
       "chipDownloadDateTime": chipDownloadDateTime}
)
