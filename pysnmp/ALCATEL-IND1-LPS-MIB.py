# SNMP MIB module (ALCATEL-IND1-LPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALCATEL-IND1-LPS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:36:30 2024
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

(softentIND1MacAddress,) = mibBuilder.importSymbols(
    "ALCATEL-IND1-BASE",
    "softentIND1MacAddress")

(systemServicesDate,
 systemServicesTime) = mibBuilder.importSymbols(
    "ALCATEL-IND1-SYSTEM-MIB",
    "systemServicesDate",
    "systemServicesTime")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 MacAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

alcatelIND1LearnedPortSecurityMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 8, 2)
)
alcatelIND1LearnedPortSecurityMIB.setRevisions(
        ("2010-05-13 00:00",
         "2007-04-03 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AlcatelIND1LearnedPortSecurityMIBNotifications_ObjectIdentity = ObjectIdentity
alcatelIND1LearnedPortSecurityMIBNotifications = _AlcatelIND1LearnedPortSecurityMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 8, 2, 0)
)
if mibBuilder.loadTexts:
    alcatelIND1LearnedPortSecurityMIBNotifications.setStatus("current")
_AlcatelIND1LearnedPortSecurityMIBObjects_ObjectIdentity = ObjectIdentity
alcatelIND1LearnedPortSecurityMIBObjects = _AlcatelIND1LearnedPortSecurityMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 8, 2, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1LearnedPortSecurityMIBObjects.setStatus("current")
_LearnedPortSecurityTable_Object = MibTable
learnedPortSecurityTable = _LearnedPortSecurityTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 8, 2, 1, 1)
)
if mibBuilder.loadTexts:
    learnedPortSecurityTable.setStatus("current")
_LearnedPortSecurityEntry_Object = MibTableRow
learnedPortSecurityEntry = _LearnedPortSecurityEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 8, 2, 1, 1, 1)
)
learnedPortSecurityEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    learnedPortSecurityEntry.setStatus("current")


class _LpsViolationOption_Type(Integer32):
    """Custom type lpsViolationOption based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("discard", 3),
          ("restrict", 1),
          ("shutdown", 2))
    )


_LpsViolationOption_Type.__name__ = "Integer32"
_LpsViolationOption_Object = MibTableColumn
lpsViolationOption = _LpsViolationOption_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 8, 2, 1, 1, 1, 1),
    _LpsViolationOption_Type()
)
lpsViolationOption.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lpsViolationOption.setStatus("current")


class _LpsMaxMacNum_Type(Integer32):
    """Custom type lpsMaxMacNum based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_LpsMaxMacNum_Type.__name__ = "Integer32"
_LpsMaxMacNum_Object = MibTableColumn
lpsMaxMacNum = _LpsMaxMacNum_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 8, 2, 1, 1, 1, 2),
    _LpsMaxMacNum_Type()
)
lpsMaxMacNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lpsMaxMacNum.setStatus("current")


class _LpsLoMacRange_Type(MacAddress):
    """Custom type lpsLoMacRange based on MacAddress"""
    defaultHexValue = "000000000000"


_LpsLoMacRange_Object = MibTableColumn
lpsLoMacRange = _LpsLoMacRange_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 8, 2, 1, 1, 1, 3),
    _LpsLoMacRange_Type()
)
lpsLoMacRange.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lpsLoMacRange.setStatus("current")


class _LpsHiMacRange_Type(MacAddress):
    """Custom type lpsHiMacRange based on MacAddress"""
    defaultHexValue = "ffffffffffff"


_LpsHiMacRange_Object = MibTableColumn
lpsHiMacRange = _LpsHiMacRange_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 8, 2, 1, 1, 1, 4),
    _LpsHiMacRange_Type()
)
lpsHiMacRange.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lpsHiMacRange.setStatus("current")


class _LpsAdminStatus_Type(Integer32):
    """Custom type lpsAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("locked", 3))
    )


_LpsAdminStatus_Type.__name__ = "Integer32"
_LpsAdminStatus_Object = MibTableColumn
lpsAdminStatus = _LpsAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 8, 2, 1, 1, 1, 5),
    _LpsAdminStatus_Type()
)
lpsAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lpsAdminStatus.setStatus("current")


class _LpsOperStatus_Type(Integer32):
    """Custom type lpsOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("securityViolated", 3),
          ("up", 1))
    )


_LpsOperStatus_Type.__name__ = "Integer32"
_LpsOperStatus_Object = MibTableColumn
lpsOperStatus = _LpsOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 8, 2, 1, 1, 1, 6),
    _LpsOperStatus_Type()
)
lpsOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsOperStatus.setStatus("current")
_LpsRowStatus_Type = RowStatus
_LpsRowStatus_Object = MibTableColumn
lpsRowStatus = _LpsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 8, 2, 1, 1, 1, 7),
    _LpsRowStatus_Type()
)
lpsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lpsRowStatus.setStatus("current")


class _LpsRelease_Type(Integer32):
    """Custom type lpsRelease based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("release", 1)
    )


_LpsRelease_Type.__name__ = "Integer32"
_LpsRelease_Object = MibTableColumn
lpsRelease = _LpsRelease_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 8, 2, 1, 1, 1, 8),
    _LpsRelease_Type()
)
lpsRelease.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lpsRelease.setStatus("current")


class _LpsMaxFilteredMacNum_Type(Integer32):
    """Custom type lpsMaxFilteredMacNum based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_LpsMaxFilteredMacNum_Type.__name__ = "Integer32"
_LpsMaxFilteredMacNum_Object = MibTableColumn
lpsMaxFilteredMacNum = _LpsMaxFilteredMacNum_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 8, 2, 1, 1, 1, 9),
    _LpsMaxFilteredMacNum_Type()
)
lpsMaxFilteredMacNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lpsMaxFilteredMacNum.setStatus("current")


class _LpsLearnTrapThreshold_Type(Integer32):
    """Custom type lpsLearnTrapThreshold based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_LpsLearnTrapThreshold_Type.__name__ = "Integer32"
_LpsLearnTrapThreshold_Object = MibTableColumn
lpsLearnTrapThreshold = _LpsLearnTrapThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 8, 2, 1, 1, 1, 10),
    _LpsLearnTrapThreshold_Type()
)
lpsLearnTrapThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lpsLearnTrapThreshold.setStatus("current")


class _LpsViolatingMac_Type(MacAddress):
    """Custom type lpsViolatingMac based on MacAddress"""
    defaultHexValue = "000000000000"


_LpsViolatingMac_Object = MibTableColumn
lpsViolatingMac = _LpsViolatingMac_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 8, 2, 1, 1, 1, 11),
    _LpsViolatingMac_Type()
)
lpsViolatingMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsViolatingMac.setStatus("current")
_LearnedPortSecurityGlobalGroup_ObjectIdentity = ObjectIdentity
learnedPortSecurityGlobalGroup = _LearnedPortSecurityGlobalGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 8, 2, 1, 3)
)


class _LpsLearningWindowTime_Type(Integer32):
    """Custom type lpsLearningWindowTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2880),
    )


_LpsLearningWindowTime_Type.__name__ = "Integer32"
_LpsLearningWindowTime_Object = MibScalar
lpsLearningWindowTime = _LpsLearningWindowTime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 8, 2, 1, 3, 1),
    _LpsLearningWindowTime_Type()
)
lpsLearningWindowTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpsLearningWindowTime.setStatus("current")


class _LpsLearningWindowTimeWithStaticConversion_Type(Integer32):
    """Custom type lpsLearningWindowTimeWithStaticConversion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_LpsLearningWindowTimeWithStaticConversion_Type.__name__ = "Integer32"
_LpsLearningWindowTimeWithStaticConversion_Object = MibScalar
lpsLearningWindowTimeWithStaticConversion = _LpsLearningWindowTimeWithStaticConversion_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 8, 2, 1, 3, 2),
    _LpsLearningWindowTimeWithStaticConversion_Type()
)
lpsLearningWindowTimeWithStaticConversion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpsLearningWindowTimeWithStaticConversion.setStatus("current")


class _LpsConvertToStatic_Type(Integer32):
    """Custom type lpsConvertToStatic based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2147483647, 2147483647),
        ValueRangeConstraint(1001, 17000),
    )


_LpsConvertToStatic_Type.__name__ = "Integer32"
_LpsConvertToStatic_Object = MibScalar
lpsConvertToStatic = _LpsConvertToStatic_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 8, 2, 1, 3, 3),
    _LpsConvertToStatic_Type()
)
lpsConvertToStatic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpsConvertToStatic.setStatus("current")


class _LpsLearningWindowNoAging_Type(Integer32):
    """Custom type lpsLearningWindowNoAging based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_LpsLearningWindowNoAging_Type.__name__ = "Integer32"
_LpsLearningWindowNoAging_Object = MibScalar
lpsLearningWindowNoAging = _LpsLearningWindowNoAging_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 8, 2, 1, 3, 4),
    _LpsLearningWindowNoAging_Type()
)
lpsLearningWindowNoAging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpsLearningWindowNoAging.setStatus("current")


class _LpsLearningWindowBootupStatus_Type(Integer32):
    """Custom type lpsLearningWindowBootupStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_LpsLearningWindowBootupStatus_Type.__name__ = "Integer32"
_LpsLearningWindowBootupStatus_Object = MibScalar
lpsLearningWindowBootupStatus = _LpsLearningWindowBootupStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 8, 2, 1, 3, 5),
    _LpsLearningWindowBootupStatus_Type()
)
lpsLearningWindowBootupStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpsLearningWindowBootupStatus.setStatus("current")


class _LpsLearningWindowTimeRemaining_Type(Integer32):
    """Custom type lpsLearningWindowTimeRemaining based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 172800),
    )


_LpsLearningWindowTimeRemaining_Type.__name__ = "Integer32"
_LpsLearningWindowTimeRemaining_Object = MibScalar
lpsLearningWindowTimeRemaining = _LpsLearningWindowTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 8, 2, 1, 3, 6),
    _LpsLearningWindowTimeRemaining_Type()
)
lpsLearningWindowTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsLearningWindowTimeRemaining.setStatus("current")
_LearnedPortSecurityL2MacAddressTable_Object = MibTable
learnedPortSecurityL2MacAddressTable = _LearnedPortSecurityL2MacAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 8, 2, 1, 4)
)
if mibBuilder.loadTexts:
    learnedPortSecurityL2MacAddressTable.setStatus("current")
_LearnedPortSecurityL2MacAddressEntry_Object = MibTableRow
learnedPortSecurityL2MacAddressEntry = _LearnedPortSecurityL2MacAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 8, 2, 1, 4, 1)
)
learnedPortSecurityL2MacAddressEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ALCATEL-IND1-LPS-MIB", "lpsL2VlanId"),
    (0, "ALCATEL-IND1-LPS-MIB", "lpsL2MacAddress"),
)
if mibBuilder.loadTexts:
    learnedPortSecurityL2MacAddressEntry.setStatus("current")


class _LpsL2VlanId_Type(Integer32):
    """Custom type lpsL2VlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_LpsL2VlanId_Type.__name__ = "Integer32"
_LpsL2VlanId_Object = MibTableColumn
lpsL2VlanId = _LpsL2VlanId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 8, 2, 1, 4, 1, 1),
    _LpsL2VlanId_Type()
)
lpsL2VlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpsL2VlanId.setStatus("current")
_LpsL2MacAddress_Type = MacAddress
_LpsL2MacAddress_Object = MibTableColumn
lpsL2MacAddress = _LpsL2MacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 8, 2, 1, 4, 1, 2),
    _LpsL2MacAddress_Type()
)
lpsL2MacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpsL2MacAddress.setStatus("current")


class _LpsL2MacAddressLearnType_Type(Integer32):
    """Custom type lpsL2MacAddressLearnType based on Integer32"""
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
        *(("configured", 1),
          ("dynamic", 2),
          ("filtered", 3),
          ("quarantined", 4))
    )


_LpsL2MacAddressLearnType_Type.__name__ = "Integer32"
_LpsL2MacAddressLearnType_Object = MibTableColumn
lpsL2MacAddressLearnType = _LpsL2MacAddressLearnType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 8, 2, 1, 4, 1, 3),
    _LpsL2MacAddressLearnType_Type()
)
lpsL2MacAddressLearnType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsL2MacAddressLearnType.setStatus("current")
_LpsL2MacAddressRowStatus_Type = RowStatus
_LpsL2MacAddressRowStatus_Object = MibTableColumn
lpsL2MacAddressRowStatus = _LpsL2MacAddressRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 8, 2, 1, 4, 1, 4),
    _LpsL2MacAddressRowStatus_Type()
)
lpsL2MacAddressRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lpsL2MacAddressRowStatus.setStatus("current")
_LpsTrapsObj_ObjectIdentity = ObjectIdentity
lpsTrapsObj = _LpsTrapsObj_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 8, 2, 1, 5)
)


class _LpsTrapSwitchName_Type(SnmpAdminString):
    """Custom type lpsTrapSwitchName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_LpsTrapSwitchName_Type.__name__ = "SnmpAdminString"
_LpsTrapSwitchName_Object = MibScalar
lpsTrapSwitchName = _LpsTrapSwitchName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 8, 2, 1, 5, 1),
    _LpsTrapSwitchName_Type()
)
lpsTrapSwitchName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsTrapSwitchName.setStatus("current")
_LpsTrapSwitchIpAddr_Type = IpAddress
_LpsTrapSwitchIpAddr_Object = MibScalar
lpsTrapSwitchIpAddr = _LpsTrapSwitchIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 8, 2, 1, 5, 2),
    _LpsTrapSwitchIpAddr_Type()
)
lpsTrapSwitchIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsTrapSwitchIpAddr.setStatus("current")
_LpsTrapSwitchSlice_Type = Integer32
_LpsTrapSwitchSlice_Object = MibScalar
lpsTrapSwitchSlice = _LpsTrapSwitchSlice_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 8, 2, 1, 5, 3),
    _LpsTrapSwitchSlice_Type()
)
lpsTrapSwitchSlice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsTrapSwitchSlice.setStatus("current")
_LpsTrapSwitchPort_Type = Integer32
_LpsTrapSwitchPort_Object = MibScalar
lpsTrapSwitchPort = _LpsTrapSwitchPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 8, 2, 1, 5, 4),
    _LpsTrapSwitchPort_Type()
)
lpsTrapSwitchPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsTrapSwitchPort.setStatus("current")
_LpsTrapViolatingMac_Type = MacAddress
_LpsTrapViolatingMac_Object = MibScalar
lpsTrapViolatingMac = _LpsTrapViolatingMac_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 8, 2, 1, 5, 5),
    _LpsTrapViolatingMac_Type()
)
lpsTrapViolatingMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsTrapViolatingMac.setStatus("current")


class _LpsTrapViolationType_Type(Integer32):
    """Custom type lpsTrapViolationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("discard", 3),
          ("restrict", 1),
          ("shutdown", 2))
    )


_LpsTrapViolationType_Type.__name__ = "Integer32"
_LpsTrapViolationType_Object = MibScalar
lpsTrapViolationType = _LpsTrapViolationType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 8, 2, 1, 5, 6),
    _LpsTrapViolationType_Type()
)
lpsTrapViolationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsTrapViolationType.setStatus("current")
_LpsTrapSwitchVlan_Type = Integer32
_LpsTrapSwitchVlan_Object = MibScalar
lpsTrapSwitchVlan = _LpsTrapSwitchVlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 8, 2, 1, 5, 7),
    _LpsTrapSwitchVlan_Type()
)
lpsTrapSwitchVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsTrapSwitchVlan.setStatus("current")
_LpsTrapBridgeMac_Type = MacAddress
_LpsTrapBridgeMac_Object = MibScalar
lpsTrapBridgeMac = _LpsTrapBridgeMac_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 8, 2, 1, 5, 8),
    _LpsTrapBridgeMac_Type()
)
lpsTrapBridgeMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpsTrapBridgeMac.setStatus("current")
_AlcatelIND1LearnedPortSecurityMIBConformance_ObjectIdentity = ObjectIdentity
alcatelIND1LearnedPortSecurityMIBConformance = _AlcatelIND1LearnedPortSecurityMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 8, 2, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1LearnedPortSecurityMIBConformance.setStatus("current")
_AlcatelIND1LearnedPortSecurityMIBGroups_ObjectIdentity = ObjectIdentity
alcatelIND1LearnedPortSecurityMIBGroups = _AlcatelIND1LearnedPortSecurityMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 8, 2, 2, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1LearnedPortSecurityMIBGroups.setStatus("current")
_AlcatelIND1LearnedPortSecurityMIBCompliances_ObjectIdentity = ObjectIdentity
alcatelIND1LearnedPortSecurityMIBCompliances = _AlcatelIND1LearnedPortSecurityMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 8, 2, 2, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1LearnedPortSecurityMIBCompliances.setStatus("current")

# Managed Objects groups

learnedPortSecurityGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 8, 2, 2, 1, 1)
)
learnedPortSecurityGroup.setObjects(
      *(("ALCATEL-IND1-LPS-MIB", "lpsViolationOption"),
        ("ALCATEL-IND1-LPS-MIB", "lpsMaxMacNum"),
        ("ALCATEL-IND1-LPS-MIB", "lpsLoMacRange"),
        ("ALCATEL-IND1-LPS-MIB", "lpsHiMacRange"),
        ("ALCATEL-IND1-LPS-MIB", "lpsAdminStatus"),
        ("ALCATEL-IND1-LPS-MIB", "lpsOperStatus"),
        ("ALCATEL-IND1-LPS-MIB", "lpsRowStatus"),
        ("ALCATEL-IND1-LPS-MIB", "lpsRelease"),
        ("ALCATEL-IND1-LPS-MIB", "lpsMaxFilteredMacNum"),
        ("ALCATEL-IND1-LPS-MIB", "lpsLearnTrapThreshold"),
        ("ALCATEL-IND1-LPS-MIB", "lpsViolatingMac"))
)
if mibBuilder.loadTexts:
    learnedPortSecurityGroup.setStatus("current")

learnedPortSecurityGlobGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 8, 2, 2, 1, 2)
)
learnedPortSecurityGlobGroup.setObjects(
      *(("ALCATEL-IND1-LPS-MIB", "lpsLearningWindowTime"),
        ("ALCATEL-IND1-LPS-MIB", "lpsLearningWindowTimeWithStaticConversion"),
        ("ALCATEL-IND1-LPS-MIB", "lpsConvertToStatic"),
        ("ALCATEL-IND1-LPS-MIB", "lpsLearningWindowNoAging"),
        ("ALCATEL-IND1-LPS-MIB", "lpsLearningWindowBootupStatus"),
        ("ALCATEL-IND1-LPS-MIB", "lpsLearningWindowTimeRemaining"))
)
if mibBuilder.loadTexts:
    learnedPortSecurityGlobGroup.setStatus("current")

learnedPortSecurityL2MacAddressGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 8, 2, 2, 1, 4)
)
learnedPortSecurityL2MacAddressGroup.setObjects(
      *(("ALCATEL-IND1-LPS-MIB", "lpsL2MacAddressLearnType"),
        ("ALCATEL-IND1-LPS-MIB", "lpsL2MacAddressRowStatus"))
)
if mibBuilder.loadTexts:
    learnedPortSecurityL2MacAddressGroup.setStatus("current")

learnedPortSecurityTrapsObjGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 8, 2, 2, 1, 6)
)
learnedPortSecurityTrapsObjGroup.setObjects(
      *(("ALCATEL-IND1-LPS-MIB", "lpsTrapSwitchName"),
        ("ALCATEL-IND1-LPS-MIB", "lpsTrapSwitchIpAddr"),
        ("ALCATEL-IND1-LPS-MIB", "lpsTrapSwitchSlice"),
        ("ALCATEL-IND1-LPS-MIB", "lpsTrapSwitchPort"),
        ("ALCATEL-IND1-LPS-MIB", "lpsTrapViolatingMac"),
        ("ALCATEL-IND1-LPS-MIB", "lpsTrapViolationType"),
        ("ALCATEL-IND1-LPS-MIB", "lpsTrapSwitchVlan"),
        ("ALCATEL-IND1-LPS-MIB", "lpsTrapBridgeMac"))
)
if mibBuilder.loadTexts:
    learnedPortSecurityTrapsObjGroup.setStatus("current")


# Notification objects

lpsViolationTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 8, 2, 0, 1)
)
lpsViolationTrap.setObjects(
      *(("ALCATEL-IND1-LPS-MIB", "lpsTrapSwitchName"),
        ("ALCATEL-IND1-LPS-MIB", "lpsTrapSwitchIpAddr"),
        ("ALCATEL-IND1-LPS-MIB", "lpsTrapSwitchSlice"),
        ("ALCATEL-IND1-LPS-MIB", "lpsTrapSwitchPort"),
        ("ALCATEL-IND1-LPS-MIB", "lpsTrapViolatingMac"),
        ("ALCATEL-IND1-LPS-MIB", "lpsTrapViolationType"),
        ("ALCATEL-IND1-LPS-MIB", "lpsTrapSwitchVlan"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemServicesDate"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemServicesTime"))
)
if mibBuilder.loadTexts:
    lpsViolationTrap.setStatus(
        "current"
    )

lpsPortUpAfterLearningWindowExpiredTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 8, 2, 0, 2)
)
lpsPortUpAfterLearningWindowExpiredTrap.setObjects(
      *(("ALCATEL-IND1-LPS-MIB", "lpsTrapSwitchName"),
        ("ALCATEL-IND1-LPS-MIB", "lpsTrapSwitchSlice"),
        ("ALCATEL-IND1-LPS-MIB", "lpsTrapSwitchPort"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemServicesDate"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemServicesTime"))
)
if mibBuilder.loadTexts:
    lpsPortUpAfterLearningWindowExpiredTrap.setStatus(
        "current"
    )

lpsLearnMac = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 8, 2, 0, 3)
)
lpsLearnMac.setObjects(
      *(("ALCATEL-IND1-LPS-MIB", "lpsTrapSwitchName"),
        ("ALCATEL-IND1-LPS-MIB", "lpsTrapSwitchSlice"),
        ("ALCATEL-IND1-LPS-MIB", "lpsTrapSwitchPort"),
        ("ALCATEL-IND1-LPS-MIB", "lpsTrapSwitchVlan"),
        ("ALCATEL-IND1-LPS-MIB", "lpsTrapBridgeMac"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemServicesDate"),
        ("ALCATEL-IND1-SYSTEM-MIB", "systemServicesTime"))
)
if mibBuilder.loadTexts:
    lpsLearnMac.setStatus(
        "current"
    )


# Notifications groups

learnedPortSecurityTrapsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 8, 2, 2, 1, 3)
)
learnedPortSecurityTrapsGroup.setObjects(
      *(("ALCATEL-IND1-LPS-MIB", "lpsViolationTrap"),
        ("ALCATEL-IND1-LPS-MIB", "lpsPortUpAfterLearningWindowExpiredTrap"),
        ("ALCATEL-IND1-LPS-MIB", "lpsLearnMac"))
)
if mibBuilder.loadTexts:
    learnedPortSecurityTrapsGroup.setStatus(
        "current"
    )

learnedPortSecurityNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 8, 2, 2, 1, 7)
)
learnedPortSecurityNotificationGroup.setObjects(
    ("ALCATEL-IND1-LPS-MIB", "lpsLearnMac")
)
if mibBuilder.loadTexts:
    learnedPortSecurityNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

alcatelIND1LearnedPortSecurityMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 8, 2, 2, 2, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1LearnedPortSecurityMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-IND1-LPS-MIB",
    **{"alcatelIND1LearnedPortSecurityMIB": alcatelIND1LearnedPortSecurityMIB,
       "alcatelIND1LearnedPortSecurityMIBNotifications": alcatelIND1LearnedPortSecurityMIBNotifications,
       "lpsViolationTrap": lpsViolationTrap,
       "lpsPortUpAfterLearningWindowExpiredTrap": lpsPortUpAfterLearningWindowExpiredTrap,
       "lpsLearnMac": lpsLearnMac,
       "alcatelIND1LearnedPortSecurityMIBObjects": alcatelIND1LearnedPortSecurityMIBObjects,
       "learnedPortSecurityTable": learnedPortSecurityTable,
       "learnedPortSecurityEntry": learnedPortSecurityEntry,
       "lpsViolationOption": lpsViolationOption,
       "lpsMaxMacNum": lpsMaxMacNum,
       "lpsLoMacRange": lpsLoMacRange,
       "lpsHiMacRange": lpsHiMacRange,
       "lpsAdminStatus": lpsAdminStatus,
       "lpsOperStatus": lpsOperStatus,
       "lpsRowStatus": lpsRowStatus,
       "lpsRelease": lpsRelease,
       "lpsMaxFilteredMacNum": lpsMaxFilteredMacNum,
       "lpsLearnTrapThreshold": lpsLearnTrapThreshold,
       "lpsViolatingMac": lpsViolatingMac,
       "learnedPortSecurityGlobalGroup": learnedPortSecurityGlobalGroup,
       "lpsLearningWindowTime": lpsLearningWindowTime,
       "lpsLearningWindowTimeWithStaticConversion": lpsLearningWindowTimeWithStaticConversion,
       "lpsConvertToStatic": lpsConvertToStatic,
       "lpsLearningWindowNoAging": lpsLearningWindowNoAging,
       "lpsLearningWindowBootupStatus": lpsLearningWindowBootupStatus,
       "lpsLearningWindowTimeRemaining": lpsLearningWindowTimeRemaining,
       "learnedPortSecurityL2MacAddressTable": learnedPortSecurityL2MacAddressTable,
       "learnedPortSecurityL2MacAddressEntry": learnedPortSecurityL2MacAddressEntry,
       "lpsL2VlanId": lpsL2VlanId,
       "lpsL2MacAddress": lpsL2MacAddress,
       "lpsL2MacAddressLearnType": lpsL2MacAddressLearnType,
       "lpsL2MacAddressRowStatus": lpsL2MacAddressRowStatus,
       "lpsTrapsObj": lpsTrapsObj,
       "lpsTrapSwitchName": lpsTrapSwitchName,
       "lpsTrapSwitchIpAddr": lpsTrapSwitchIpAddr,
       "lpsTrapSwitchSlice": lpsTrapSwitchSlice,
       "lpsTrapSwitchPort": lpsTrapSwitchPort,
       "lpsTrapViolatingMac": lpsTrapViolatingMac,
       "lpsTrapViolationType": lpsTrapViolationType,
       "lpsTrapSwitchVlan": lpsTrapSwitchVlan,
       "lpsTrapBridgeMac": lpsTrapBridgeMac,
       "alcatelIND1LearnedPortSecurityMIBConformance": alcatelIND1LearnedPortSecurityMIBConformance,
       "alcatelIND1LearnedPortSecurityMIBGroups": alcatelIND1LearnedPortSecurityMIBGroups,
       "learnedPortSecurityGroup": learnedPortSecurityGroup,
       "learnedPortSecurityGlobGroup": learnedPortSecurityGlobGroup,
       "learnedPortSecurityTrapsGroup": learnedPortSecurityTrapsGroup,
       "learnedPortSecurityL2MacAddressGroup": learnedPortSecurityL2MacAddressGroup,
       "learnedPortSecurityTrapsObjGroup": learnedPortSecurityTrapsObjGroup,
       "learnedPortSecurityNotificationGroup": learnedPortSecurityNotificationGroup,
       "alcatelIND1LearnedPortSecurityMIBCompliances": alcatelIND1LearnedPortSecurityMIBCompliances,
       "alcatelIND1LearnedPortSecurityMIBCompliance": alcatelIND1LearnedPortSecurityMIBCompliance}
)
