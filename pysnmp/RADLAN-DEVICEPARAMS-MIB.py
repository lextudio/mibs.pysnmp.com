# SNMP MIB module (RADLAN-DEVICEPARAMS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RADLAN-DEVICEPARAMS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:36:57 2024
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

(rnd,) = mibBuilder.importSymbols(
    "RADLAN-MIB",
    "rnd")

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
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

rndDeviceParams = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 89, 2)
)
rndDeviceParams.setRevisions(
        ("2007-01-02 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class RlImageIdType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("image1", 1),
          ("image2", 2))
    )



# MIB Managed Objects in the order of their OIDs



class _RndBridgeType_Type(Integer32):
    """Custom type rndBridgeType based on Integer32"""
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
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48)
        )
    )
    namedValues = NamedValues(
        *(("ceb", 2),
          ("ceblb", 3),
          ("ete", 12),
          ("gatelinx", 36),
          ("ielb", 30),
          ("itlb", 35),
          ("leb", 31),
          ("lre", 46),
          ("ltb", 8),
          ("mrt", 47),
          ("ogRanTR", 38),
          ("ogRubE", 42),
          ("ogRubT", 43),
          ("ogVan", 40),
          ("openGate12", 32),
          ("openGate2", 37),
          ("openGate4", 33),
          ("ran", 34),
          ("rdapter", 39),
          ("reb", 1),
          ("rebsx", 6),
          ("rete", 13),
          ("rtb", 7),
          ("rtre", 10),
          ("tre", 9),
          ("vGate2", 48),
          ("vGate4", 45),
          ("wanGate", 41),
          ("wanGateI", 44),
          ("xeb", 4),
          ("xeb1", 5),
          ("xtb", 11))
    )


_RndBridgeType_Type.__name__ = "Integer32"
_RndBridgeType_Object = MibScalar
rndBridgeType = _RndBridgeType_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 1),
    _RndBridgeType_Type()
)
rndBridgeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rndBridgeType.setStatus("current")
_RndInactiveArpTimeOut_Type = Integer32
_RndInactiveArpTimeOut_Object = MibScalar
rndInactiveArpTimeOut = _RndInactiveArpTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 2),
    _RndInactiveArpTimeOut_Type()
)
rndInactiveArpTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndInactiveArpTimeOut.setStatus("current")
_RndBridgeAlarm_ObjectIdentity = ObjectIdentity
rndBridgeAlarm = _RndBridgeAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 2, 3)
)
_RndErrorDesc_Type = DisplayString
_RndErrorDesc_Object = MibScalar
rndErrorDesc = _RndErrorDesc_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 3, 1),
    _RndErrorDesc_Type()
)
rndErrorDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rndErrorDesc.setStatus("current")


class _RndErrorSeverity_Type(Integer32):
    """Custom type rndErrorSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("error", 2),
          ("fatal-error", 3),
          ("info", 0),
          ("warning", 1))
    )


_RndErrorSeverity_Type.__name__ = "Integer32"
_RndErrorSeverity_Object = MibScalar
rndErrorSeverity = _RndErrorSeverity_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 3, 2),
    _RndErrorSeverity_Type()
)
rndErrorSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rndErrorSeverity.setStatus("current")
_RndBrgVersion_Type = DisplayString
_RndBrgVersion_Object = MibScalar
rndBrgVersion = _RndBrgVersion_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 4),
    _RndBrgVersion_Type()
)
rndBrgVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rndBrgVersion.setStatus("current")
_RndBrgFeatures_Type = OctetString
_RndBrgFeatures_Object = MibScalar
rndBrgFeatures = _RndBrgFeatures_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 5),
    _RndBrgFeatures_Type()
)
rndBrgFeatures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rndBrgFeatures.setStatus("current")
_RndBrgLicense_Type = OctetString
_RndBrgLicense_Object = MibScalar
rndBrgLicense = _RndBrgLicense_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 6),
    _RndBrgLicense_Type()
)
rndBrgLicense.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndBrgLicense.setStatus("current")
_RndIpHost_ObjectIdentity = ObjectIdentity
rndIpHost = _RndIpHost_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 2, 7)
)
_RndCommunityTable_Object = MibTable
rndCommunityTable = _RndCommunityTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 7, 2)
)
if mibBuilder.loadTexts:
    rndCommunityTable.setStatus("current")
_RndCommunityEntry_Object = MibTableRow
rndCommunityEntry = _RndCommunityEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 7, 2, 1)
)
rndCommunityEntry.setIndexNames(
    (0, "RADLAN-DEVICEPARAMS-MIB", "rndCommunityMngStationAddr"),
    (1, "RADLAN-DEVICEPARAMS-MIB", "rndCommunityString"),
)
if mibBuilder.loadTexts:
    rndCommunityEntry.setStatus("current")
_RndCommunityMngStationAddr_Type = IpAddress
_RndCommunityMngStationAddr_Object = MibTableColumn
rndCommunityMngStationAddr = _RndCommunityMngStationAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 7, 2, 1, 1),
    _RndCommunityMngStationAddr_Type()
)
rndCommunityMngStationAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rndCommunityMngStationAddr.setStatus("current")


class _RndCommunityString_Type(DisplayString):
    """Custom type rndCommunityString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_RndCommunityString_Type.__name__ = "DisplayString"
_RndCommunityString_Object = MibTableColumn
rndCommunityString = _RndCommunityString_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 7, 2, 1, 2),
    _RndCommunityString_Type()
)
rndCommunityString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rndCommunityString.setStatus("current")


class _RndCommunityAccess_Type(Integer32):
    """Custom type rndCommunityAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("readOnly", 1),
          ("readWrite", 2),
          ("super", 3))
    )


_RndCommunityAccess_Type.__name__ = "Integer32"
_RndCommunityAccess_Object = MibTableColumn
rndCommunityAccess = _RndCommunityAccess_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 7, 2, 1, 3),
    _RndCommunityAccess_Type()
)
rndCommunityAccess.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rndCommunityAccess.setStatus("current")


class _RndCommunityTrapsEnable_Type(Integer32):
    """Custom type rndCommunityTrapsEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("snmpV1", 1),
          ("snmpV2", 2),
          ("snmpV3", 3),
          ("trapsDisable", 4))
    )


_RndCommunityTrapsEnable_Type.__name__ = "Integer32"
_RndCommunityTrapsEnable_Object = MibTableColumn
rndCommunityTrapsEnable = _RndCommunityTrapsEnable_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 7, 2, 1, 4),
    _RndCommunityTrapsEnable_Type()
)
rndCommunityTrapsEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rndCommunityTrapsEnable.setStatus("current")


class _RndCommunityStatus_Type(Integer32):
    """Custom type rndCommunityStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("invalid", 2))
    )


_RndCommunityStatus_Type.__name__ = "Integer32"
_RndCommunityStatus_Object = MibTableColumn
rndCommunityStatus = _RndCommunityStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 7, 2, 1, 5),
    _RndCommunityStatus_Type()
)
rndCommunityStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rndCommunityStatus.setStatus("current")


class _RndCommunityPortSecurity_Type(Integer32):
    """Custom type rndCommunityPortSecurity based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_RndCommunityPortSecurity_Type.__name__ = "Integer32"
_RndCommunityPortSecurity_Object = MibTableColumn
rndCommunityPortSecurity = _RndCommunityPortSecurity_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 7, 2, 1, 6),
    _RndCommunityPortSecurity_Type()
)
rndCommunityPortSecurity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rndCommunityPortSecurity.setStatus("current")


class _RndCommunityOwner_Type(DisplayString):
    """Custom type rndCommunityOwner based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RndCommunityOwner_Type.__name__ = "DisplayString"
_RndCommunityOwner_Object = MibTableColumn
rndCommunityOwner = _RndCommunityOwner_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 7, 2, 1, 7),
    _RndCommunityOwner_Type()
)
rndCommunityOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rndCommunityOwner.setStatus("current")


class _RndCommunityTrapDestPort_Type(Integer32):
    """Custom type rndCommunityTrapDestPort based on Integer32"""
    defaultValue = 162

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RndCommunityTrapDestPort_Type.__name__ = "Integer32"
_RndCommunityTrapDestPort_Object = MibTableColumn
rndCommunityTrapDestPort = _RndCommunityTrapDestPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 7, 2, 1, 8),
    _RndCommunityTrapDestPort_Type()
)
rndCommunityTrapDestPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rndCommunityTrapDestPort.setStatus("current")
_RlMridTable_Object = MibTable
rlMridTable = _RlMridTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 7, 3)
)
if mibBuilder.loadTexts:
    rlMridTable.setStatus("current")
_RlMridEntry_Object = MibTableRow
rlMridEntry = _RlMridEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 7, 3, 1)
)
rlMridEntry.setIndexNames(
    (0, "RADLAN-DEVICEPARAMS-MIB", "rndCommunityMngStationAddr"),
    (1, "RADLAN-DEVICEPARAMS-MIB", "rndCommunityString"),
)
if mibBuilder.loadTexts:
    rlMridEntry.setStatus("current")
_RlMridConnection_Type = Integer32
_RlMridConnection_Object = MibTableColumn
rlMridConnection = _RlMridConnection_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 7, 3, 1, 1),
    _RlMridConnection_Type()
)
rlMridConnection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlMridConnection.setStatus("current")
_RlManagedMrid_Type = Integer32
_RlManagedMrid_Object = MibTableColumn
rlManagedMrid = _RlManagedMrid_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 7, 3, 1, 2),
    _RlManagedMrid_Type()
)
rlManagedMrid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlManagedMrid.setStatus("current")
_RndIpHostManagement_ObjectIdentity = ObjectIdentity
rndIpHostManagement = _RndIpHostManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 2, 7, 4)
)
_RndIpHostManagementSupported_Type = TruthValue
_RndIpHostManagementSupported_Object = MibScalar
rndIpHostManagementSupported = _RndIpHostManagementSupported_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 7, 4, 1),
    _RndIpHostManagementSupported_Type()
)
rndIpHostManagementSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rndIpHostManagementSupported.setStatus("current")
_RndIpHostManagementIfIndex_Type = Integer32
_RndIpHostManagementIfIndex_Object = MibScalar
rndIpHostManagementIfIndex = _RndIpHostManagementIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 7, 4, 2),
    _RndIpHostManagementIfIndex_Type()
)
rndIpHostManagementIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndIpHostManagementIfIndex.setStatus("current")


class _RndManagedTime_Type(DisplayString):
    """Custom type rndManagedTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_RndManagedTime_Type.__name__ = "DisplayString"
_RndManagedTime_Object = MibScalar
rndManagedTime = _RndManagedTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 8),
    _RndManagedTime_Type()
)
rndManagedTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndManagedTime.setStatus("current")


class _RndManagedDate_Type(DisplayString):
    """Custom type rndManagedDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_RndManagedDate_Type.__name__ = "DisplayString"
_RndManagedDate_Object = MibScalar
rndManagedDate = _RndManagedDate_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 9),
    _RndManagedDate_Type()
)
rndManagedDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndManagedDate.setStatus("current")
_RndBaseBootVersion_Type = DisplayString
_RndBaseBootVersion_Object = MibScalar
rndBaseBootVersion = _RndBaseBootVersion_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 10),
    _RndBaseBootVersion_Type()
)
rndBaseBootVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rndBaseBootVersion.setStatus("current")
_GenGroup_ObjectIdentity = ObjectIdentity
genGroup = _GenGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 2, 11)
)
_GenGroupHWVersion_Type = DisplayString
_GenGroupHWVersion_Object = MibScalar
genGroupHWVersion = _GenGroupHWVersion_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 11, 1),
    _GenGroupHWVersion_Type()
)
genGroupHWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genGroupHWVersion.setStatus("current")


class _GenGroupConfigurationSymbol_Type(DisplayString):
    """Custom type genGroupConfigurationSymbol based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_GenGroupConfigurationSymbol_Type.__name__ = "DisplayString"
_GenGroupConfigurationSymbol_Object = MibScalar
genGroupConfigurationSymbol = _GenGroupConfigurationSymbol_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 11, 2),
    _GenGroupConfigurationSymbol_Type()
)
genGroupConfigurationSymbol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genGroupConfigurationSymbol.setStatus("current")


class _GenGroupHWStatus_Type(Integer32):
    """Custom type genGroupHWStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("hardwareProblems", 2),
          ("notSupported", 255),
          ("ok", 1))
    )


_GenGroupHWStatus_Type.__name__ = "Integer32"
_GenGroupHWStatus_Object = MibScalar
genGroupHWStatus = _GenGroupHWStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 11, 3),
    _GenGroupHWStatus_Type()
)
genGroupHWStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genGroupHWStatus.setStatus("current")
_RndBasePhysicalAddress_Type = PhysAddress
_RndBasePhysicalAddress_Object = MibScalar
rndBasePhysicalAddress = _RndBasePhysicalAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 12),
    _RndBasePhysicalAddress_Type()
)
rndBasePhysicalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rndBasePhysicalAddress.setStatus("current")
_RndSoftwareFile_ObjectIdentity = ObjectIdentity
rndSoftwareFile = _RndSoftwareFile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 2, 13)
)
_RndActiveSoftwareFileTable_Object = MibTable
rndActiveSoftwareFileTable = _RndActiveSoftwareFileTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 13, 1)
)
if mibBuilder.loadTexts:
    rndActiveSoftwareFileTable.setStatus("current")
_RndActiveSoftwareFileEntry_Object = MibTableRow
rndActiveSoftwareFileEntry = _RndActiveSoftwareFileEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 13, 1, 1)
)
rndActiveSoftwareFileEntry.setIndexNames(
    (0, "RADLAN-DEVICEPARAMS-MIB", "rndUnitNumber"),
)
if mibBuilder.loadTexts:
    rndActiveSoftwareFileEntry.setStatus("current")
_RndUnitNumber_Type = Integer32
_RndUnitNumber_Object = MibTableColumn
rndUnitNumber = _RndUnitNumber_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 13, 1, 1, 1),
    _RndUnitNumber_Type()
)
rndUnitNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndUnitNumber.setStatus("current")
_RndActiveSoftwareFile_Type = RlImageIdType
_RndActiveSoftwareFile_Object = MibTableColumn
rndActiveSoftwareFile = _RndActiveSoftwareFile_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 13, 1, 1, 2),
    _RndActiveSoftwareFile_Type()
)
rndActiveSoftwareFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rndActiveSoftwareFile.setStatus("current")


class _RndActiveSoftwareFileAfterReset_Type(Integer32):
    """Custom type rndActiveSoftwareFileAfterReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("image1", 1),
          ("image2", 2),
          ("invalidImage", 3))
    )


_RndActiveSoftwareFileAfterReset_Type.__name__ = "Integer32"
_RndActiveSoftwareFileAfterReset_Object = MibTableColumn
rndActiveSoftwareFileAfterReset = _RndActiveSoftwareFileAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 13, 1, 1, 3),
    _RndActiveSoftwareFileAfterReset_Type()
)
rndActiveSoftwareFileAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndActiveSoftwareFileAfterReset.setStatus("current")


class _RlResetStatus_Type(Bits):
    """Custom type rlResetStatus based on Bits"""
    namedValues = NamedValues(
        *(("downgrade", 2),
          ("no-stack-integrity", 1),
          ("ok", 0))
    )

_RlResetStatus_Type.__name__ = "Bits"
_RlResetStatus_Object = MibScalar
rlResetStatus = _RlResetStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 13, 2),
    _RlResetStatus_Type()
)
rlResetStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlResetStatus.setStatus("current")
_RndImageSize_Type = Integer32
_RndImageSize_Object = MibScalar
rndImageSize = _RndImageSize_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 14),
    _RndImageSize_Type()
)
rndImageSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rndImageSize.setStatus("current")
_RndBackupConfigurationEnabled_Type = TruthValue
_RndBackupConfigurationEnabled_Object = MibScalar
rndBackupConfigurationEnabled = _RndBackupConfigurationEnabled_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 15),
    _RndBackupConfigurationEnabled_Type()
)
rndBackupConfigurationEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rndBackupConfigurationEnabled.setStatus("current")
_RndImageInfo_ObjectIdentity = ObjectIdentity
rndImageInfo = _RndImageInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 2, 16)
)
_RndImageInfoTable_Object = MibTable
rndImageInfoTable = _RndImageInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 16, 1)
)
if mibBuilder.loadTexts:
    rndImageInfoTable.setStatus("current")
_RndImageInfoEntry_Object = MibTableRow
rndImageInfoEntry = _RndImageInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 16, 1, 1)
)
rndImageInfoEntry.setIndexNames(
    (0, "RADLAN-DEVICEPARAMS-MIB", "rndStackUnitNumber"),
)
if mibBuilder.loadTexts:
    rndImageInfoEntry.setStatus("current")
_RndStackUnitNumber_Type = Integer32
_RndStackUnitNumber_Object = MibTableColumn
rndStackUnitNumber = _RndStackUnitNumber_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 16, 1, 1, 1),
    _RndStackUnitNumber_Type()
)
rndStackUnitNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndStackUnitNumber.setStatus("current")
_RndImage1Name_Type = DisplayString
_RndImage1Name_Object = MibTableColumn
rndImage1Name = _RndImage1Name_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 16, 1, 1, 2),
    _RndImage1Name_Type()
)
rndImage1Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rndImage1Name.setStatus("current")
_RndImage2Name_Type = DisplayString
_RndImage2Name_Object = MibTableColumn
rndImage2Name = _RndImage2Name_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 16, 1, 1, 3),
    _RndImage2Name_Type()
)
rndImage2Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rndImage2Name.setStatus("current")
_RndImage1Version_Type = DisplayString
_RndImage1Version_Object = MibTableColumn
rndImage1Version = _RndImage1Version_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 16, 1, 1, 4),
    _RndImage1Version_Type()
)
rndImage1Version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rndImage1Version.setStatus("current")
_RndImage2Version_Type = DisplayString
_RndImage2Version_Object = MibTableColumn
rndImage2Version = _RndImage2Version_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 16, 1, 1, 5),
    _RndImage2Version_Type()
)
rndImage2Version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rndImage2Version.setStatus("current")
_RndImage1Date_Type = DisplayString
_RndImage1Date_Object = MibTableColumn
rndImage1Date = _RndImage1Date_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 16, 1, 1, 6),
    _RndImage1Date_Type()
)
rndImage1Date.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rndImage1Date.setStatus("current")
_RndImage2Date_Type = DisplayString
_RndImage2Date_Object = MibTableColumn
rndImage2Date = _RndImage2Date_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 16, 1, 1, 7),
    _RndImage2Date_Type()
)
rndImage2Date.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rndImage2Date.setStatus("current")
_RndImage1Time_Type = DisplayString
_RndImage1Time_Object = MibTableColumn
rndImage1Time = _RndImage1Time_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 16, 1, 1, 8),
    _RndImage1Time_Type()
)
rndImage1Time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rndImage1Time.setStatus("current")
_RndImage2Time_Type = DisplayString
_RndImage2Time_Object = MibTableColumn
rndImage2Time = _RndImage2Time_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 16, 1, 1, 9),
    _RndImage2Time_Type()
)
rndImage2Time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rndImage2Time.setStatus("current")
_RndImage1Description_Type = DisplayString
_RndImage1Description_Object = MibTableColumn
rndImage1Description = _RndImage1Description_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 16, 1, 1, 10),
    _RndImage1Description_Type()
)
rndImage1Description.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndImage1Description.setStatus("current")
_RndImage2Description_Type = DisplayString
_RndImage2Description_Object = MibTableColumn
rndImage2Description = _RndImage2Description_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 16, 1, 1, 11),
    _RndImage2Description_Type()
)
rndImage2Description.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rndImage2Description.setStatus("current")
_RlComponentsInfoTable_Object = MibTable
rlComponentsInfoTable = _RlComponentsInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 16, 2)
)
if mibBuilder.loadTexts:
    rlComponentsInfoTable.setStatus("current")
_RlComponentsInfoEntry_Object = MibTableRow
rlComponentsInfoEntry = _RlComponentsInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 16, 2, 1)
)
rlComponentsInfoEntry.setIndexNames(
    (0, "RADLAN-DEVICEPARAMS-MIB", "rlComponentsInfoStackUnitNumber"),
    (0, "RADLAN-DEVICEPARAMS-MIB", "rlComponentsInfoImageId"),
    (1, "RADLAN-DEVICEPARAMS-MIB", "rlComponentsInfoComponent"),
)
if mibBuilder.loadTexts:
    rlComponentsInfoEntry.setStatus("current")
_RlComponentsInfoStackUnitNumber_Type = Integer32
_RlComponentsInfoStackUnitNumber_Object = MibTableColumn
rlComponentsInfoStackUnitNumber = _RlComponentsInfoStackUnitNumber_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 16, 2, 1, 1),
    _RlComponentsInfoStackUnitNumber_Type()
)
rlComponentsInfoStackUnitNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlComponentsInfoStackUnitNumber.setStatus("current")
_RlComponentsInfoImageId_Type = RlImageIdType
_RlComponentsInfoImageId_Object = MibTableColumn
rlComponentsInfoImageId = _RlComponentsInfoImageId_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 16, 2, 1, 2),
    _RlComponentsInfoImageId_Type()
)
rlComponentsInfoImageId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlComponentsInfoImageId.setStatus("current")


class _RlComponentsInfoComponent_Type(DisplayString):
    """Custom type rlComponentsInfoComponent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_RlComponentsInfoComponent_Type.__name__ = "DisplayString"
_RlComponentsInfoComponent_Object = MibTableColumn
rlComponentsInfoComponent = _RlComponentsInfoComponent_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 16, 2, 1, 3),
    _RlComponentsInfoComponent_Type()
)
rlComponentsInfoComponent.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlComponentsInfoComponent.setStatus("current")
_RlComponentsInfoBaseline_Type = DisplayString
_RlComponentsInfoBaseline_Object = MibTableColumn
rlComponentsInfoBaseline = _RlComponentsInfoBaseline_Object(
    (1, 3, 6, 1, 4, 1, 89, 2, 16, 2, 1, 5),
    _RlComponentsInfoBaseline_Type()
)
rlComponentsInfoBaseline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlComponentsInfoBaseline.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RADLAN-DEVICEPARAMS-MIB",
    **{"RlImageIdType": RlImageIdType,
       "rndDeviceParams": rndDeviceParams,
       "rndBridgeType": rndBridgeType,
       "rndInactiveArpTimeOut": rndInactiveArpTimeOut,
       "rndBridgeAlarm": rndBridgeAlarm,
       "rndErrorDesc": rndErrorDesc,
       "rndErrorSeverity": rndErrorSeverity,
       "rndBrgVersion": rndBrgVersion,
       "rndBrgFeatures": rndBrgFeatures,
       "rndBrgLicense": rndBrgLicense,
       "rndIpHost": rndIpHost,
       "rndCommunityTable": rndCommunityTable,
       "rndCommunityEntry": rndCommunityEntry,
       "rndCommunityMngStationAddr": rndCommunityMngStationAddr,
       "rndCommunityString": rndCommunityString,
       "rndCommunityAccess": rndCommunityAccess,
       "rndCommunityTrapsEnable": rndCommunityTrapsEnable,
       "rndCommunityStatus": rndCommunityStatus,
       "rndCommunityPortSecurity": rndCommunityPortSecurity,
       "rndCommunityOwner": rndCommunityOwner,
       "rndCommunityTrapDestPort": rndCommunityTrapDestPort,
       "rlMridTable": rlMridTable,
       "rlMridEntry": rlMridEntry,
       "rlMridConnection": rlMridConnection,
       "rlManagedMrid": rlManagedMrid,
       "rndIpHostManagement": rndIpHostManagement,
       "rndIpHostManagementSupported": rndIpHostManagementSupported,
       "rndIpHostManagementIfIndex": rndIpHostManagementIfIndex,
       "rndManagedTime": rndManagedTime,
       "rndManagedDate": rndManagedDate,
       "rndBaseBootVersion": rndBaseBootVersion,
       "genGroup": genGroup,
       "genGroupHWVersion": genGroupHWVersion,
       "genGroupConfigurationSymbol": genGroupConfigurationSymbol,
       "genGroupHWStatus": genGroupHWStatus,
       "rndBasePhysicalAddress": rndBasePhysicalAddress,
       "rndSoftwareFile": rndSoftwareFile,
       "rndActiveSoftwareFileTable": rndActiveSoftwareFileTable,
       "rndActiveSoftwareFileEntry": rndActiveSoftwareFileEntry,
       "rndUnitNumber": rndUnitNumber,
       "rndActiveSoftwareFile": rndActiveSoftwareFile,
       "rndActiveSoftwareFileAfterReset": rndActiveSoftwareFileAfterReset,
       "rlResetStatus": rlResetStatus,
       "rndImageSize": rndImageSize,
       "rndBackupConfigurationEnabled": rndBackupConfigurationEnabled,
       "rndImageInfo": rndImageInfo,
       "rndImageInfoTable": rndImageInfoTable,
       "rndImageInfoEntry": rndImageInfoEntry,
       "rndStackUnitNumber": rndStackUnitNumber,
       "rndImage1Name": rndImage1Name,
       "rndImage2Name": rndImage2Name,
       "rndImage1Version": rndImage1Version,
       "rndImage2Version": rndImage2Version,
       "rndImage1Date": rndImage1Date,
       "rndImage2Date": rndImage2Date,
       "rndImage1Time": rndImage1Time,
       "rndImage2Time": rndImage2Time,
       "rndImage1Description": rndImage1Description,
       "rndImage2Description": rndImage2Description,
       "rlComponentsInfoTable": rlComponentsInfoTable,
       "rlComponentsInfoEntry": rlComponentsInfoEntry,
       "rlComponentsInfoStackUnitNumber": rlComponentsInfoStackUnitNumber,
       "rlComponentsInfoImageId": rlComponentsInfoImageId,
       "rlComponentsInfoComponent": rlComponentsInfoComponent,
       "rlComponentsInfoBaseline": rlComponentsInfoBaseline}
)
