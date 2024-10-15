# SNMP MIB module (Juniper-UNI-ATM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Juniper-UNI-ATM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:16:32 2024
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

(atmfM4VcTestCode,
 atmfM4VcTestId,
 atmfM4VcTestObject,
 atmfM4VcTestResult,
 atmfM4VcTestType,
 atmfM4VpTestCode,
 atmfM4VpTestId,
 atmfM4VpTestObject,
 atmfM4VpTestResult,
 atmfM4VpTestType) = mibBuilder.importSymbols(
    "ATM-FORUM-SNMP-M4-MIB",
    "atmfM4VcTestCode",
    "atmfM4VcTestId",
    "atmfM4VcTestObject",
    "atmfM4VcTestResult",
    "atmfM4VcTestType",
    "atmfM4VpTestCode",
    "atmfM4VpTestId",
    "atmfM4VpTestObject",
    "atmfM4VpTestResult",
    "atmfM4VpTestType")

(atmVclVci,
 atmVclVpi,
 atmVplVpi) = mibBuilder.importSymbols(
    "ATM-MIB",
    "atmVclVci",
    "atmVclVpi",
    "atmVplVpi")

(AtmAddr,
 AtmVcIdentifier,
 AtmVorXAdminStatus,
 AtmVpIdentifier) = mibBuilder.importSymbols(
    "ATM-TC-MIB",
    "AtmAddr",
    "AtmVcIdentifier",
    "AtmVorXAdminStatus",
    "AtmVpIdentifier")

(InterfaceIndex,
 InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero",
    "ifIndex")

(juniMibs,) = mibBuilder.importSymbols(
    "Juniper-MIBs",
    "juniMibs")

(JuniEnable,
 JuniInterfaceLocationType,
 JuniInterfaceLocationValue,
 JuniNextIfIndex) = mibBuilder.importSymbols(
    "Juniper-TC",
    "JuniEnable",
    "JuniInterfaceLocationType",
    "JuniInterfaceLocationValue",
    "JuniNextIfIndex")

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
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

juniAtmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8)
)
juniAtmMIB.setRevisions(
        ("2005-11-15 11:33",
         "2005-08-17 17:26",
         "2005-02-17 23:15",
         "2004-12-08 15:22",
         "2003-12-30 15:07",
         "2004-02-25 20:23",
         "2003-09-19 22:01",
         "2003-07-14 15:37",
         "2003-01-15 19:32",
         "2002-08-09 14:03",
         "2002-08-09 13:40",
         "2002-01-24 14:00",
         "2001-12-14 18:04",
         "2001-11-26 16:39",
         "2000-11-27 19:51",
         "2000-08-02 00:00",
         "2000-05-12 00:00",
         "2000-01-13 00:00",
         "1999-08-04 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class JuniAtmNbmaMapName(OctetString, TextualConvention):
    status = "current"
    displayHint = "32a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )



class JuniAtmNbmaMapNameOrNull(OctetString, TextualConvention):
    status = "current"
    displayHint = "32a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )



class JuniAtmLocationType(Integer32, TextualConvention):
    status = "obsolete"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("slotPort", 1),
          ("unknown", 0))
    )



class JuniAtmLocationValue(OctetString, TextualConvention):
    status = "obsolete"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )



# MIB Managed Objects in the order of their OIDs

_JuniAtmObjects_ObjectIdentity = ObjectIdentity
juniAtmObjects = _JuniAtmObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1)
)
_JuniAtmIfLayer_ObjectIdentity = ObjectIdentity
juniAtmIfLayer = _JuniAtmIfLayer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1)
)
_JuniAtmNextIfIndex_Type = JuniNextIfIndex
_JuniAtmNextIfIndex_Object = MibScalar
juniAtmNextIfIndex = _JuniAtmNextIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 1),
    _JuniAtmNextIfIndex_Type()
)
juniAtmNextIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAtmNextIfIndex.setStatus("current")
_JuniAtmIfTable_Object = MibTable
juniAtmIfTable = _JuniAtmIfTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 2)
)
if mibBuilder.loadTexts:
    juniAtmIfTable.setStatus("current")
_JuniAtmIfEntry_Object = MibTableRow
juniAtmIfEntry = _JuniAtmIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 2, 1)
)
juniAtmIfEntry.setIndexNames(
    (0, "Juniper-UNI-ATM-MIB", "juniAtmIfIndex"),
)
if mibBuilder.loadTexts:
    juniAtmIfEntry.setStatus("current")
_JuniAtmIfIndex_Type = InterfaceIndex
_JuniAtmIfIndex_Object = MibTableColumn
juniAtmIfIndex = _JuniAtmIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 2, 1, 1),
    _JuniAtmIfIndex_Type()
)
juniAtmIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniAtmIfIndex.setStatus("current")
_JuniAtmIfRowStatus_Type = RowStatus
_JuniAtmIfRowStatus_Object = MibTableColumn
juniAtmIfRowStatus = _JuniAtmIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 2, 1, 2),
    _JuniAtmIfRowStatus_Type()
)
juniAtmIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAtmIfRowStatus.setStatus("current")
_JuniAtmIfLowerIfIndex_Type = InterfaceIndexOrZero
_JuniAtmIfLowerIfIndex_Object = MibTableColumn
juniAtmIfLowerIfIndex = _JuniAtmIfLowerIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 2, 1, 3),
    _JuniAtmIfLowerIfIndex_Type()
)
juniAtmIfLowerIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAtmIfLowerIfIndex.setStatus("current")


class _JuniAtmIfIlmiVpi_Type(AtmVpIdentifier):
    """Custom type juniAtmIfIlmiVpi based on AtmVpIdentifier"""
    defaultValue = 0


_JuniAtmIfIlmiVpi_Object = MibTableColumn
juniAtmIfIlmiVpi = _JuniAtmIfIlmiVpi_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 2, 1, 4),
    _JuniAtmIfIlmiVpi_Type()
)
juniAtmIfIlmiVpi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAtmIfIlmiVpi.setStatus("current")


class _JuniAtmIfIlmiVci_Type(AtmVcIdentifier):
    """Custom type juniAtmIfIlmiVci based on AtmVcIdentifier"""
    defaultValue = 16


_JuniAtmIfIlmiVci_Object = MibTableColumn
juniAtmIfIlmiVci = _JuniAtmIfIlmiVci_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 2, 1, 5),
    _JuniAtmIfIlmiVci_Type()
)
juniAtmIfIlmiVci.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAtmIfIlmiVci.setStatus("current")


class _JuniAtmIfIlmiVcd_Type(Integer32):
    """Custom type juniAtmIfIlmiVcd based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JuniAtmIfIlmiVcd_Type.__name__ = "Integer32"
_JuniAtmIfIlmiVcd_Object = MibTableColumn
juniAtmIfIlmiVcd = _JuniAtmIfIlmiVcd_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 2, 1, 6),
    _JuniAtmIfIlmiVcd_Type()
)
juniAtmIfIlmiVcd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAtmIfIlmiVcd.setStatus("current")


class _JuniAtmIfIlmiPollFrequency_Type(Integer32):
    """Custom type juniAtmIfIlmiPollFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_JuniAtmIfIlmiPollFrequency_Type.__name__ = "Integer32"
_JuniAtmIfIlmiPollFrequency_Object = MibTableColumn
juniAtmIfIlmiPollFrequency = _JuniAtmIfIlmiPollFrequency_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 2, 1, 7),
    _JuniAtmIfIlmiPollFrequency_Type()
)
juniAtmIfIlmiPollFrequency.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAtmIfIlmiPollFrequency.setStatus("current")
if mibBuilder.loadTexts:
    juniAtmIfIlmiPollFrequency.setUnits("seconds")


class _JuniAtmIfIlmiAdminState_Type(Integer32):
    """Custom type juniAtmIfIlmiAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_JuniAtmIfIlmiAdminState_Type.__name__ = "Integer32"
_JuniAtmIfIlmiAdminState_Object = MibTableColumn
juniAtmIfIlmiAdminState = _JuniAtmIfIlmiAdminState_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 2, 1, 8),
    _JuniAtmIfIlmiAdminState_Type()
)
juniAtmIfIlmiAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAtmIfIlmiAdminState.setStatus("current")


class _JuniAtmIfUniVersion_Type(Integer32):
    """Custom type juniAtmIfUniVersion based on Integer32"""
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
        *(("uniVersionAutoConfig", 0),
          ("version3Dot0", 1),
          ("version3Dot1", 2),
          ("version4Dot0", 3))
    )


_JuniAtmIfUniVersion_Type.__name__ = "Integer32"
_JuniAtmIfUniVersion_Object = MibTableColumn
juniAtmIfUniVersion = _JuniAtmIfUniVersion_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 2, 1, 9),
    _JuniAtmIfUniVersion_Type()
)
juniAtmIfUniVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAtmIfUniVersion.setStatus("current")


class _JuniAtmIfOamCellRxAdminState_Type(Integer32):
    """Custom type juniAtmIfOamCellRxAdminState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("oamCellAdminStateDisabled", 0),
          ("oamCellAdminStateEnabled", 1))
    )


_JuniAtmIfOamCellRxAdminState_Type.__name__ = "Integer32"
_JuniAtmIfOamCellRxAdminState_Object = MibTableColumn
juniAtmIfOamCellRxAdminState = _JuniAtmIfOamCellRxAdminState_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 2, 1, 10),
    _JuniAtmIfOamCellRxAdminState_Type()
)
juniAtmIfOamCellRxAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAtmIfOamCellRxAdminState.setStatus("current")
_JuniAtmIfInCells_Type = Counter64
_JuniAtmIfInCells_Object = MibTableColumn
juniAtmIfInCells = _JuniAtmIfInCells_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 2, 1, 11),
    _JuniAtmIfInCells_Type()
)
juniAtmIfInCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAtmIfInCells.setStatus("current")
_JuniAtmIfOutCells_Type = Counter64
_JuniAtmIfOutCells_Object = MibTableColumn
juniAtmIfOutCells = _JuniAtmIfOutCells_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 2, 1, 12),
    _JuniAtmIfOutCells_Type()
)
juniAtmIfOutCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAtmIfOutCells.setStatus("current")


class _JuniAtmIfVcCount_Type(Integer32):
    """Custom type juniAtmIfVcCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 268431360),
    )


_JuniAtmIfVcCount_Type.__name__ = "Integer32"
_JuniAtmIfVcCount_Object = MibTableColumn
juniAtmIfVcCount = _JuniAtmIfVcCount_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 2, 1, 13),
    _JuniAtmIfVcCount_Type()
)
juniAtmIfVcCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAtmIfVcCount.setStatus("current")
_JuniAtmIfMapGroup_Type = JuniAtmNbmaMapNameOrNull
_JuniAtmIfMapGroup_Object = MibTableColumn
juniAtmIfMapGroup = _JuniAtmIfMapGroup_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 2, 1, 14),
    _JuniAtmIfMapGroup_Type()
)
juniAtmIfMapGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAtmIfMapGroup.setStatus("current")


class _JuniAtmIfCacAdminState_Type(JuniEnable):
    """Custom type juniAtmIfCacAdminState based on JuniEnable"""


_JuniAtmIfCacAdminState_Object = MibTableColumn
juniAtmIfCacAdminState = _JuniAtmIfCacAdminState_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 2, 1, 15),
    _JuniAtmIfCacAdminState_Type()
)
juniAtmIfCacAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAtmIfCacAdminState.setStatus("current")


class _JuniAtmIfCacUbrWeight_Type(Integer32):
    """Custom type juniAtmIfCacUbrWeight based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JuniAtmIfCacUbrWeight_Type.__name__ = "Integer32"
_JuniAtmIfCacUbrWeight_Object = MibTableColumn
juniAtmIfCacUbrWeight = _JuniAtmIfCacUbrWeight_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 2, 1, 16),
    _JuniAtmIfCacUbrWeight_Type()
)
juniAtmIfCacUbrWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAtmIfCacUbrWeight.setStatus("current")
if mibBuilder.loadTexts:
    juniAtmIfCacUbrWeight.setUnits("kbps")


class _JuniAtmIfCacSubscriptionBandwidth_Type(Integer32):
    """Custom type juniAtmIfCacSubscriptionBandwidth based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JuniAtmIfCacSubscriptionBandwidth_Type.__name__ = "Integer32"
_JuniAtmIfCacSubscriptionBandwidth_Object = MibTableColumn
juniAtmIfCacSubscriptionBandwidth = _JuniAtmIfCacSubscriptionBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 2, 1, 17),
    _JuniAtmIfCacSubscriptionBandwidth_Type()
)
juniAtmIfCacSubscriptionBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAtmIfCacSubscriptionBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    juniAtmIfCacSubscriptionBandwidth.setUnits("kbps")


class _JuniAtmIfCacAvailableBandwidth_Type(Integer32):
    """Custom type juniAtmIfCacAvailableBandwidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JuniAtmIfCacAvailableBandwidth_Type.__name__ = "Integer32"
_JuniAtmIfCacAvailableBandwidth_Object = MibTableColumn
juniAtmIfCacAvailableBandwidth = _JuniAtmIfCacAvailableBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 2, 1, 18),
    _JuniAtmIfCacAvailableBandwidth_Type()
)
juniAtmIfCacAvailableBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAtmIfCacAvailableBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    juniAtmIfCacAvailableBandwidth.setUnits("kbps")


class _JuniAtmIfCacAvailableBandwidthRx_Type(Integer32):
    """Custom type juniAtmIfCacAvailableBandwidthRx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JuniAtmIfCacAvailableBandwidthRx_Type.__name__ = "Integer32"
_JuniAtmIfCacAvailableBandwidthRx_Object = MibTableColumn
juniAtmIfCacAvailableBandwidthRx = _JuniAtmIfCacAvailableBandwidthRx_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 2, 1, 19),
    _JuniAtmIfCacAvailableBandwidthRx_Type()
)
juniAtmIfCacAvailableBandwidthRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAtmIfCacAvailableBandwidthRx.setStatus("deprecated")
if mibBuilder.loadTexts:
    juniAtmIfCacAvailableBandwidthRx.setUnits("kbps")


class _JuniAtmIfE164Autoconversion_Type(Integer32):
    """Custom type juniAtmIfE164Autoconversion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_JuniAtmIfE164Autoconversion_Type.__name__ = "Integer32"
_JuniAtmIfE164Autoconversion_Object = MibTableColumn
juniAtmIfE164Autoconversion = _JuniAtmIfE164Autoconversion_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 2, 1, 20),
    _JuniAtmIfE164Autoconversion_Type()
)
juniAtmIfE164Autoconversion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAtmIfE164Autoconversion.setStatus("obsolete")


class _JuniAtmIfE164Gateway_Type(Integer32):
    """Custom type juniAtmIfE164Gateway based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_JuniAtmIfE164Gateway_Type.__name__ = "Integer32"
_JuniAtmIfE164Gateway_Object = MibTableColumn
juniAtmIfE164Gateway = _JuniAtmIfE164Gateway_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 2, 1, 21),
    _JuniAtmIfE164Gateway_Type()
)
juniAtmIfE164Gateway.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAtmIfE164Gateway.setStatus("obsolete")


class _JuniAtmIfE164OneToOneAddrTrans_Type(Integer32):
    """Custom type juniAtmIfE164OneToOneAddrTrans based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_JuniAtmIfE164OneToOneAddrTrans_Type.__name__ = "Integer32"
_JuniAtmIfE164OneToOneAddrTrans_Object = MibTableColumn
juniAtmIfE164OneToOneAddrTrans = _JuniAtmIfE164OneToOneAddrTrans_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 2, 1, 22),
    _JuniAtmIfE164OneToOneAddrTrans_Type()
)
juniAtmIfE164OneToOneAddrTrans.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAtmIfE164OneToOneAddrTrans.setStatus("obsolete")


class _JuniAtmIfOamCellFilter_Type(Integer32):
    """Custom type juniAtmIfOamCellFilter based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("oamCellFilterAlarm", 1),
          ("oamCellFilterAll", 0))
    )


_JuniAtmIfOamCellFilter_Type.__name__ = "Integer32"
_JuniAtmIfOamCellFilter_Object = MibTableColumn
juniAtmIfOamCellFilter = _JuniAtmIfOamCellFilter_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 2, 1, 23),
    _JuniAtmIfOamCellFilter_Type()
)
juniAtmIfOamCellFilter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAtmIfOamCellFilter.setStatus("current")
_JuniAtmIfCacUsedBandwidthUpper_Type = Unsigned32
_JuniAtmIfCacUsedBandwidthUpper_Object = MibTableColumn
juniAtmIfCacUsedBandwidthUpper = _JuniAtmIfCacUsedBandwidthUpper_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 2, 1, 24),
    _JuniAtmIfCacUsedBandwidthUpper_Type()
)
juniAtmIfCacUsedBandwidthUpper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAtmIfCacUsedBandwidthUpper.setStatus("current")
_JuniAtmIfCacUsedBandwidthLower_Type = Unsigned32
_JuniAtmIfCacUsedBandwidthLower_Object = MibTableColumn
juniAtmIfCacUsedBandwidthLower = _JuniAtmIfCacUsedBandwidthLower_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 2, 1, 25),
    _JuniAtmIfCacUsedBandwidthLower_Type()
)
juniAtmIfCacUsedBandwidthLower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAtmIfCacUsedBandwidthLower.setStatus("current")


class _JuniAtmIfAssociatedVcClassId_Type(Unsigned32):
    """Custom type juniAtmIfAssociatedVcClassId based on Unsigned32"""
    defaultValue = 0


_JuniAtmIfAssociatedVcClassId_Object = MibTableColumn
juniAtmIfAssociatedVcClassId = _JuniAtmIfAssociatedVcClassId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 2, 1, 26),
    _JuniAtmIfAssociatedVcClassId_Type()
)
juniAtmIfAssociatedVcClassId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAtmIfAssociatedVcClassId.setStatus("current")
_JuniAtmPvcStatisticsTable_Object = MibTable
juniAtmPvcStatisticsTable = _JuniAtmPvcStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 3)
)
if mibBuilder.loadTexts:
    juniAtmPvcStatisticsTable.setStatus("current")
_JuniAtmPvcStatisticsEntry_Object = MibTableRow
juniAtmPvcStatisticsEntry = _JuniAtmPvcStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 3, 1)
)
juniAtmPvcStatisticsEntry.setIndexNames(
    (0, "Juniper-UNI-ATM-MIB", "juniAtmPvcStatsIfIndex"),
    (0, "Juniper-UNI-ATM-MIB", "juniAtmPvcStatsVpi"),
    (0, "Juniper-UNI-ATM-MIB", "juniAtmPvcStatsVci"),
)
if mibBuilder.loadTexts:
    juniAtmPvcStatisticsEntry.setStatus("current")
_JuniAtmPvcStatsIfIndex_Type = InterfaceIndex
_JuniAtmPvcStatsIfIndex_Object = MibTableColumn
juniAtmPvcStatsIfIndex = _JuniAtmPvcStatsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 3, 1, 1),
    _JuniAtmPvcStatsIfIndex_Type()
)
juniAtmPvcStatsIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniAtmPvcStatsIfIndex.setStatus("current")
_JuniAtmPvcStatsVpi_Type = AtmVpIdentifier
_JuniAtmPvcStatsVpi_Object = MibTableColumn
juniAtmPvcStatsVpi = _JuniAtmPvcStatsVpi_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 3, 1, 2),
    _JuniAtmPvcStatsVpi_Type()
)
juniAtmPvcStatsVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniAtmPvcStatsVpi.setStatus("current")
_JuniAtmPvcStatsVci_Type = AtmVcIdentifier
_JuniAtmPvcStatsVci_Object = MibTableColumn
juniAtmPvcStatsVci = _JuniAtmPvcStatsVci_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 3, 1, 3),
    _JuniAtmPvcStatsVci_Type()
)
juniAtmPvcStatsVci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniAtmPvcStatsVci.setStatus("current")
_JuniAtmPvcStatsInCells_Type = Counter64
_JuniAtmPvcStatsInCells_Object = MibTableColumn
juniAtmPvcStatsInCells = _JuniAtmPvcStatsInCells_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 3, 1, 4),
    _JuniAtmPvcStatsInCells_Type()
)
juniAtmPvcStatsInCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAtmPvcStatsInCells.setStatus("current")
_JuniAtmPvcStatsInCellOctets_Type = Counter64
_JuniAtmPvcStatsInCellOctets_Object = MibTableColumn
juniAtmPvcStatsInCellOctets = _JuniAtmPvcStatsInCellOctets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 3, 1, 5),
    _JuniAtmPvcStatsInCellOctets_Type()
)
juniAtmPvcStatsInCellOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAtmPvcStatsInCellOctets.setStatus("current")
_JuniAtmPvcStatsInPackets_Type = Counter64
_JuniAtmPvcStatsInPackets_Object = MibTableColumn
juniAtmPvcStatsInPackets = _JuniAtmPvcStatsInPackets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 3, 1, 6),
    _JuniAtmPvcStatsInPackets_Type()
)
juniAtmPvcStatsInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAtmPvcStatsInPackets.setStatus("current")
_JuniAtmPvcStatsInPacketOctets_Type = Counter64
_JuniAtmPvcStatsInPacketOctets_Object = MibTableColumn
juniAtmPvcStatsInPacketOctets = _JuniAtmPvcStatsInPacketOctets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 3, 1, 7),
    _JuniAtmPvcStatsInPacketOctets_Type()
)
juniAtmPvcStatsInPacketOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAtmPvcStatsInPacketOctets.setStatus("current")
_JuniAtmPvcStatsOutCells_Type = Counter64
_JuniAtmPvcStatsOutCells_Object = MibTableColumn
juniAtmPvcStatsOutCells = _JuniAtmPvcStatsOutCells_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 3, 1, 8),
    _JuniAtmPvcStatsOutCells_Type()
)
juniAtmPvcStatsOutCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAtmPvcStatsOutCells.setStatus("current")
_JuniAtmPvcStatsOutCellOctets_Type = Counter64
_JuniAtmPvcStatsOutCellOctets_Object = MibTableColumn
juniAtmPvcStatsOutCellOctets = _JuniAtmPvcStatsOutCellOctets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 3, 1, 9),
    _JuniAtmPvcStatsOutCellOctets_Type()
)
juniAtmPvcStatsOutCellOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAtmPvcStatsOutCellOctets.setStatus("current")
_JuniAtmPvcStatsOutPackets_Type = Counter64
_JuniAtmPvcStatsOutPackets_Object = MibTableColumn
juniAtmPvcStatsOutPackets = _JuniAtmPvcStatsOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 3, 1, 10),
    _JuniAtmPvcStatsOutPackets_Type()
)
juniAtmPvcStatsOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAtmPvcStatsOutPackets.setStatus("current")
_JuniAtmPvcStatsOutPacketOctets_Type = Counter64
_JuniAtmPvcStatsOutPacketOctets_Object = MibTableColumn
juniAtmPvcStatsOutPacketOctets = _JuniAtmPvcStatsOutPacketOctets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 3, 1, 11),
    _JuniAtmPvcStatsOutPacketOctets_Type()
)
juniAtmPvcStatsOutPacketOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAtmPvcStatsOutPacketOctets.setStatus("current")
_JuniAtmPvcStatsInCellErrors_Type = Counter32
_JuniAtmPvcStatsInCellErrors_Object = MibTableColumn
juniAtmPvcStatsInCellErrors = _JuniAtmPvcStatsInCellErrors_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 3, 1, 12),
    _JuniAtmPvcStatsInCellErrors_Type()
)
juniAtmPvcStatsInCellErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAtmPvcStatsInCellErrors.setStatus("current")
_JuniAtmPvcStatsinPacketErrors_Type = Counter32
_JuniAtmPvcStatsinPacketErrors_Object = MibTableColumn
juniAtmPvcStatsinPacketErrors = _JuniAtmPvcStatsinPacketErrors_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 3, 1, 13),
    _JuniAtmPvcStatsinPacketErrors_Type()
)
juniAtmPvcStatsinPacketErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAtmPvcStatsinPacketErrors.setStatus("current")
_JuniAtmPvcStatsOutCellErrors_Type = Counter32
_JuniAtmPvcStatsOutCellErrors_Object = MibTableColumn
juniAtmPvcStatsOutCellErrors = _JuniAtmPvcStatsOutCellErrors_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 3, 1, 14),
    _JuniAtmPvcStatsOutCellErrors_Type()
)
juniAtmPvcStatsOutCellErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAtmPvcStatsOutCellErrors.setStatus("current")
_JuniAtmPvcStatsOutPacketErrors_Type = Counter32
_JuniAtmPvcStatsOutPacketErrors_Object = MibTableColumn
juniAtmPvcStatsOutPacketErrors = _JuniAtmPvcStatsOutPacketErrors_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 3, 1, 15),
    _JuniAtmPvcStatsOutPacketErrors_Type()
)
juniAtmPvcStatsOutPacketErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAtmPvcStatsOutPacketErrors.setStatus("current")
_JuniAtmPvcStatsInPacketDiscards_Type = Counter32
_JuniAtmPvcStatsInPacketDiscards_Object = MibTableColumn
juniAtmPvcStatsInPacketDiscards = _JuniAtmPvcStatsInPacketDiscards_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 3, 1, 16),
    _JuniAtmPvcStatsInPacketDiscards_Type()
)
juniAtmPvcStatsInPacketDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAtmPvcStatsInPacketDiscards.setStatus("current")
_JuniAtmPvcStatsInPacketOctetDiscards_Type = Counter32
_JuniAtmPvcStatsInPacketOctetDiscards_Object = MibTableColumn
juniAtmPvcStatsInPacketOctetDiscards = _JuniAtmPvcStatsInPacketOctetDiscards_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 3, 1, 17),
    _JuniAtmPvcStatsInPacketOctetDiscards_Type()
)
juniAtmPvcStatsInPacketOctetDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAtmPvcStatsInPacketOctetDiscards.setStatus("current")
_JuniAtmPvcStatsInPacketUnknownProtocol_Type = Counter32
_JuniAtmPvcStatsInPacketUnknownProtocol_Object = MibTableColumn
juniAtmPvcStatsInPacketUnknownProtocol = _JuniAtmPvcStatsInPacketUnknownProtocol_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 3, 1, 18),
    _JuniAtmPvcStatsInPacketUnknownProtocol_Type()
)
juniAtmPvcStatsInPacketUnknownProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAtmPvcStatsInPacketUnknownProtocol.setStatus("current")
_JuniAtmVpTunnelTable_Object = MibTable
juniAtmVpTunnelTable = _JuniAtmVpTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 4)
)
if mibBuilder.loadTexts:
    juniAtmVpTunnelTable.setStatus("current")
_JuniAtmVpTunnelEntry_Object = MibTableRow
juniAtmVpTunnelEntry = _JuniAtmVpTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 4, 1)
)
juniAtmVpTunnelEntry.setIndexNames(
    (0, "Juniper-UNI-ATM-MIB", "juniAtmVpTunnelIfIndex"),
    (0, "Juniper-UNI-ATM-MIB", "juniAtmVpTunnelVpi"),
)
if mibBuilder.loadTexts:
    juniAtmVpTunnelEntry.setStatus("current")
_JuniAtmVpTunnelIfIndex_Type = InterfaceIndex
_JuniAtmVpTunnelIfIndex_Object = MibTableColumn
juniAtmVpTunnelIfIndex = _JuniAtmVpTunnelIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 4, 1, 1),
    _JuniAtmVpTunnelIfIndex_Type()
)
juniAtmVpTunnelIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniAtmVpTunnelIfIndex.setStatus("current")
_JuniAtmVpTunnelVpi_Type = AtmVpIdentifier
_JuniAtmVpTunnelVpi_Object = MibTableColumn
juniAtmVpTunnelVpi = _JuniAtmVpTunnelVpi_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 4, 1, 2),
    _JuniAtmVpTunnelVpi_Type()
)
juniAtmVpTunnelVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniAtmVpTunnelVpi.setStatus("current")


class _JuniAtmVpTunnelKbps_Type(Integer32):
    """Custom type juniAtmVpTunnelKbps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JuniAtmVpTunnelKbps_Type.__name__ = "Integer32"
_JuniAtmVpTunnelKbps_Object = MibTableColumn
juniAtmVpTunnelKbps = _JuniAtmVpTunnelKbps_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 4, 1, 3),
    _JuniAtmVpTunnelKbps_Type()
)
juniAtmVpTunnelKbps.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAtmVpTunnelKbps.setStatus("current")
if mibBuilder.loadTexts:
    juniAtmVpTunnelKbps.setUnits("kbps")
_JuniAtmVpTunnelRowStatus_Type = RowStatus
_JuniAtmVpTunnelRowStatus_Object = MibTableColumn
juniAtmVpTunnelRowStatus = _JuniAtmVpTunnelRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 4, 1, 4),
    _JuniAtmVpTunnelRowStatus_Type()
)
juniAtmVpTunnelRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAtmVpTunnelRowStatus.setStatus("current")


class _JuniAtmVpTunnelServiceCategory_Type(Integer32):
    """Custom type juniAtmVpTunnelServiceCategory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cbr", 2),
          ("nrtVbr", 1))
    )


_JuniAtmVpTunnelServiceCategory_Type.__name__ = "Integer32"
_JuniAtmVpTunnelServiceCategory_Object = MibTableColumn
juniAtmVpTunnelServiceCategory = _JuniAtmVpTunnelServiceCategory_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 4, 1, 5),
    _JuniAtmVpTunnelServiceCategory_Type()
)
juniAtmVpTunnelServiceCategory.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAtmVpTunnelServiceCategory.setStatus("current")
_JuniAtmIfCapabilityTable_Object = MibTable
juniAtmIfCapabilityTable = _JuniAtmIfCapabilityTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 5)
)
if mibBuilder.loadTexts:
    juniAtmIfCapabilityTable.setStatus("current")
_JuniAtmIfCapabilityEntry_Object = MibTableRow
juniAtmIfCapabilityEntry = _JuniAtmIfCapabilityEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 5, 1)
)
juniAtmIfCapabilityEntry.setIndexNames(
    (0, "Juniper-UNI-ATM-MIB", "juniAtmIfCapabilityIndex"),
)
if mibBuilder.loadTexts:
    juniAtmIfCapabilityEntry.setStatus("current")
_JuniAtmIfCapabilityIndex_Type = InterfaceIndex
_JuniAtmIfCapabilityIndex_Object = MibTableColumn
juniAtmIfCapabilityIndex = _JuniAtmIfCapabilityIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 5, 1, 1),
    _JuniAtmIfCapabilityIndex_Type()
)
juniAtmIfCapabilityIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniAtmIfCapabilityIndex.setStatus("current")
_JuniAtmIfCapabilityTrafficShaping_Type = TruthValue
_JuniAtmIfCapabilityTrafficShaping_Object = MibTableColumn
juniAtmIfCapabilityTrafficShaping = _JuniAtmIfCapabilityTrafficShaping_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 5, 1, 2),
    _JuniAtmIfCapabilityTrafficShaping_Type()
)
juniAtmIfCapabilityTrafficShaping.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAtmIfCapabilityTrafficShaping.setStatus("current")
_JuniAtmIfCapabilityOam_Type = TruthValue
_JuniAtmIfCapabilityOam_Object = MibTableColumn
juniAtmIfCapabilityOam = _JuniAtmIfCapabilityOam_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 5, 1, 3),
    _JuniAtmIfCapabilityOam_Type()
)
juniAtmIfCapabilityOam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAtmIfCapabilityOam.setStatus("current")


class _JuniAtmIfCapabilityDefaultVcPerVp_Type(Integer32):
    """Custom type juniAtmIfCapabilityDefaultVcPerVp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_JuniAtmIfCapabilityDefaultVcPerVp_Type.__name__ = "Integer32"
_JuniAtmIfCapabilityDefaultVcPerVp_Object = MibTableColumn
juniAtmIfCapabilityDefaultVcPerVp = _JuniAtmIfCapabilityDefaultVcPerVp_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 5, 1, 4),
    _JuniAtmIfCapabilityDefaultVcPerVp_Type()
)
juniAtmIfCapabilityDefaultVcPerVp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAtmIfCapabilityDefaultVcPerVp.setStatus("current")


class _JuniAtmIfCapabilityNumVpiVciBits_Type(Integer32):
    """Custom type juniAtmIfCapabilityNumVpiVciBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 28),
    )


_JuniAtmIfCapabilityNumVpiVciBits_Type.__name__ = "Integer32"
_JuniAtmIfCapabilityNumVpiVciBits_Object = MibTableColumn
juniAtmIfCapabilityNumVpiVciBits = _JuniAtmIfCapabilityNumVpiVciBits_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 5, 1, 5),
    _JuniAtmIfCapabilityNumVpiVciBits_Type()
)
juniAtmIfCapabilityNumVpiVciBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAtmIfCapabilityNumVpiVciBits.setStatus("current")


class _JuniAtmIfCapabilityMaxVcd_Type(Integer32):
    """Custom type juniAtmIfCapabilityMaxVcd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JuniAtmIfCapabilityMaxVcd_Type.__name__ = "Integer32"
_JuniAtmIfCapabilityMaxVcd_Object = MibTableColumn
juniAtmIfCapabilityMaxVcd = _JuniAtmIfCapabilityMaxVcd_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 5, 1, 6),
    _JuniAtmIfCapabilityMaxVcd_Type()
)
juniAtmIfCapabilityMaxVcd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAtmIfCapabilityMaxVcd.setStatus("current")
_JuniAtmIfCapabilityMaxVpi_Type = AtmVpIdentifier
_JuniAtmIfCapabilityMaxVpi_Object = MibTableColumn
juniAtmIfCapabilityMaxVpi = _JuniAtmIfCapabilityMaxVpi_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 5, 1, 7),
    _JuniAtmIfCapabilityMaxVpi_Type()
)
juniAtmIfCapabilityMaxVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAtmIfCapabilityMaxVpi.setStatus("current")
_JuniAtmIfCapabilityMaxVci_Type = AtmVcIdentifier
_JuniAtmIfCapabilityMaxVci_Object = MibTableColumn
juniAtmIfCapabilityMaxVci = _JuniAtmIfCapabilityMaxVci_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 5, 1, 8),
    _JuniAtmIfCapabilityMaxVci_Type()
)
juniAtmIfCapabilityMaxVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAtmIfCapabilityMaxVci.setStatus("current")
_JuniAtmIfCapabilityOamCellFilter_Type = TruthValue
_JuniAtmIfCapabilityOamCellFilter_Object = MibTableColumn
juniAtmIfCapabilityOamCellFilter = _JuniAtmIfCapabilityOamCellFilter_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 5, 1, 9),
    _JuniAtmIfCapabilityOamCellFilter_Type()
)
juniAtmIfCapabilityOamCellFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAtmIfCapabilityOamCellFilter.setStatus("current")
_JuniAtmIfSvcSignallingTable_Object = MibTable
juniAtmIfSvcSignallingTable = _JuniAtmIfSvcSignallingTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 6)
)
if mibBuilder.loadTexts:
    juniAtmIfSvcSignallingTable.setStatus("deprecated")
_JuniAtmIfSvcSignallingEntry_Object = MibTableRow
juniAtmIfSvcSignallingEntry = _JuniAtmIfSvcSignallingEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 6, 1)
)
juniAtmIfSvcSignallingEntry.setIndexNames(
    (0, "Juniper-UNI-ATM-MIB", "juniAtmIfIndex"),
)
if mibBuilder.loadTexts:
    juniAtmIfSvcSignallingEntry.setStatus("deprecated")


class _JuniAtmIfSvcSignallingVpi_Type(AtmVpIdentifier):
    """Custom type juniAtmIfSvcSignallingVpi based on AtmVpIdentifier"""
    defaultValue = 0


_JuniAtmIfSvcSignallingVpi_Object = MibTableColumn
juniAtmIfSvcSignallingVpi = _JuniAtmIfSvcSignallingVpi_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 6, 1, 1),
    _JuniAtmIfSvcSignallingVpi_Type()
)
juniAtmIfSvcSignallingVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniAtmIfSvcSignallingVpi.setStatus("deprecated")


class _JuniAtmIfSvcSignallingVci_Type(AtmVcIdentifier):
    """Custom type juniAtmIfSvcSignallingVci based on AtmVcIdentifier"""
    defaultValue = 5


_JuniAtmIfSvcSignallingVci_Object = MibTableColumn
juniAtmIfSvcSignallingVci = _JuniAtmIfSvcSignallingVci_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 6, 1, 2),
    _JuniAtmIfSvcSignallingVci_Type()
)
juniAtmIfSvcSignallingVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniAtmIfSvcSignallingVci.setStatus("deprecated")


class _JuniAtmIfSvcSignallingVcd_Type(Integer32):
    """Custom type juniAtmIfSvcSignallingVcd based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JuniAtmIfSvcSignallingVcd_Type.__name__ = "Integer32"
_JuniAtmIfSvcSignallingVcd_Object = MibTableColumn
juniAtmIfSvcSignallingVcd = _JuniAtmIfSvcSignallingVcd_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 6, 1, 3),
    _JuniAtmIfSvcSignallingVcd_Type()
)
juniAtmIfSvcSignallingVcd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniAtmIfSvcSignallingVcd.setStatus("deprecated")
_JuniAtmIfSvcSignallingAdminStatus_Type = AtmVorXAdminStatus
_JuniAtmIfSvcSignallingAdminStatus_Object = MibTableColumn
juniAtmIfSvcSignallingAdminStatus = _JuniAtmIfSvcSignallingAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 6, 1, 4),
    _JuniAtmIfSvcSignallingAdminStatus_Type()
)
juniAtmIfSvcSignallingAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniAtmIfSvcSignallingAdminStatus.setStatus("deprecated")
_JuniAtmIfPnniRccTable_Object = MibTable
juniAtmIfPnniRccTable = _JuniAtmIfPnniRccTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 7)
)
if mibBuilder.loadTexts:
    juniAtmIfPnniRccTable.setStatus("obsolete")
_JuniAtmIfPnniRccEntry_Object = MibTableRow
juniAtmIfPnniRccEntry = _JuniAtmIfPnniRccEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 7, 1)
)
juniAtmIfPnniRccEntry.setIndexNames(
    (0, "Juniper-UNI-ATM-MIB", "juniAtmIfIndex"),
)
if mibBuilder.loadTexts:
    juniAtmIfPnniRccEntry.setStatus("obsolete")


class _JuniAtmIfPnniRccVpi_Type(AtmVpIdentifier):
    """Custom type juniAtmIfPnniRccVpi based on AtmVpIdentifier"""
    defaultValue = 0


_JuniAtmIfPnniRccVpi_Object = MibTableColumn
juniAtmIfPnniRccVpi = _JuniAtmIfPnniRccVpi_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 7, 1, 1),
    _JuniAtmIfPnniRccVpi_Type()
)
juniAtmIfPnniRccVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniAtmIfPnniRccVpi.setStatus("obsolete")


class _JuniAtmIfPnniRccVci_Type(AtmVcIdentifier):
    """Custom type juniAtmIfPnniRccVci based on AtmVcIdentifier"""
    defaultValue = 18


_JuniAtmIfPnniRccVci_Object = MibTableColumn
juniAtmIfPnniRccVci = _JuniAtmIfPnniRccVci_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 7, 1, 2),
    _JuniAtmIfPnniRccVci_Type()
)
juniAtmIfPnniRccVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniAtmIfPnniRccVci.setStatus("obsolete")


class _JuniAtmIfPnniRccVcd_Type(Integer32):
    """Custom type juniAtmIfPnniRccVcd based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JuniAtmIfPnniRccVcd_Type.__name__ = "Integer32"
_JuniAtmIfPnniRccVcd_Object = MibTableColumn
juniAtmIfPnniRccVcd = _JuniAtmIfPnniRccVcd_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 7, 1, 3),
    _JuniAtmIfPnniRccVcd_Type()
)
juniAtmIfPnniRccVcd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniAtmIfPnniRccVcd.setStatus("obsolete")
_JuniAtmIfPnniRccAdminStatus_Type = AtmVorXAdminStatus
_JuniAtmIfPnniRccAdminStatus_Object = MibTableColumn
juniAtmIfPnniRccAdminStatus = _JuniAtmIfPnniRccAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 7, 1, 4),
    _JuniAtmIfPnniRccAdminStatus_Type()
)
juniAtmIfPnniRccAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniAtmIfPnniRccAdminStatus.setStatus("obsolete")
_JuniAtmOamF4FlowEndToEndCfgTable_Object = MibTable
juniAtmOamF4FlowEndToEndCfgTable = _JuniAtmOamF4FlowEndToEndCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 8)
)
if mibBuilder.loadTexts:
    juniAtmOamF4FlowEndToEndCfgTable.setStatus("current")
_JuniAtmOamF4FlowEndToEndCfgEntry_Object = MibTableRow
juniAtmOamF4FlowEndToEndCfgEntry = _JuniAtmOamF4FlowEndToEndCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 8, 1)
)
juniAtmOamF4FlowEndToEndCfgEntry.setIndexNames(
    (0, "Juniper-UNI-ATM-MIB", "juniAtmOamF4FlowEndToEndIfIndex"),
    (0, "Juniper-UNI-ATM-MIB", "juniAtmOamF4FlowEndToEndVpi"),
)
if mibBuilder.loadTexts:
    juniAtmOamF4FlowEndToEndCfgEntry.setStatus("current")
_JuniAtmOamF4FlowEndToEndIfIndex_Type = InterfaceIndex
_JuniAtmOamF4FlowEndToEndIfIndex_Object = MibTableColumn
juniAtmOamF4FlowEndToEndIfIndex = _JuniAtmOamF4FlowEndToEndIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 8, 1, 1),
    _JuniAtmOamF4FlowEndToEndIfIndex_Type()
)
juniAtmOamF4FlowEndToEndIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniAtmOamF4FlowEndToEndIfIndex.setStatus("current")


class _JuniAtmOamF4FlowEndToEndVpi_Type(Integer32):
    """Custom type juniAtmOamF4FlowEndToEndVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_JuniAtmOamF4FlowEndToEndVpi_Type.__name__ = "Integer32"
_JuniAtmOamF4FlowEndToEndVpi_Object = MibTableColumn
juniAtmOamF4FlowEndToEndVpi = _JuniAtmOamF4FlowEndToEndVpi_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 8, 1, 2),
    _JuniAtmOamF4FlowEndToEndVpi_Type()
)
juniAtmOamF4FlowEndToEndVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniAtmOamF4FlowEndToEndVpi.setStatus("current")


class _JuniAtmOamF4FlowEndToEndLoopbackTimer_Type(Integer32):
    """Custom type juniAtmOamF4FlowEndToEndLoopbackTimer based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 600),
    )


_JuniAtmOamF4FlowEndToEndLoopbackTimer_Type.__name__ = "Integer32"
_JuniAtmOamF4FlowEndToEndLoopbackTimer_Object = MibTableColumn
juniAtmOamF4FlowEndToEndLoopbackTimer = _JuniAtmOamF4FlowEndToEndLoopbackTimer_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 8, 1, 3),
    _JuniAtmOamF4FlowEndToEndLoopbackTimer_Type()
)
juniAtmOamF4FlowEndToEndLoopbackTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAtmOamF4FlowEndToEndLoopbackTimer.setStatus("current")
if mibBuilder.loadTexts:
    juniAtmOamF4FlowEndToEndLoopbackTimer.setUnits("seconds")


class _JuniAtmOamF4FlowEndToEndCCSink_Type(TruthValue):
    """Custom type juniAtmOamF4FlowEndToEndCCSink based on TruthValue"""


_JuniAtmOamF4FlowEndToEndCCSink_Object = MibTableColumn
juniAtmOamF4FlowEndToEndCCSink = _JuniAtmOamF4FlowEndToEndCCSink_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 8, 1, 4),
    _JuniAtmOamF4FlowEndToEndCCSink_Type()
)
juniAtmOamF4FlowEndToEndCCSink.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAtmOamF4FlowEndToEndCCSink.setStatus("current")


class _JuniAtmOamF4FlowEndToEndCCSource_Type(TruthValue):
    """Custom type juniAtmOamF4FlowEndToEndCCSource based on TruthValue"""


_JuniAtmOamF4FlowEndToEndCCSource_Object = MibTableColumn
juniAtmOamF4FlowEndToEndCCSource = _JuniAtmOamF4FlowEndToEndCCSource_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 8, 1, 5),
    _JuniAtmOamF4FlowEndToEndCCSource_Type()
)
juniAtmOamF4FlowEndToEndCCSource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAtmOamF4FlowEndToEndCCSource.setStatus("current")
_JuniAtmOamF4FlowEndToEndRowStatus_Type = RowStatus
_JuniAtmOamF4FlowEndToEndRowStatus_Object = MibTableColumn
juniAtmOamF4FlowEndToEndRowStatus = _JuniAtmOamF4FlowEndToEndRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 8, 1, 6),
    _JuniAtmOamF4FlowEndToEndRowStatus_Type()
)
juniAtmOamF4FlowEndToEndRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAtmOamF4FlowEndToEndRowStatus.setStatus("current")
_JuniAtmOamF4FlowSegmentCfgTable_Object = MibTable
juniAtmOamF4FlowSegmentCfgTable = _JuniAtmOamF4FlowSegmentCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 9)
)
if mibBuilder.loadTexts:
    juniAtmOamF4FlowSegmentCfgTable.setStatus("current")
_JuniAtmOamF4FlowSegmentCfgEntry_Object = MibTableRow
juniAtmOamF4FlowSegmentCfgEntry = _JuniAtmOamF4FlowSegmentCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 9, 1)
)
juniAtmOamF4FlowSegmentCfgEntry.setIndexNames(
    (0, "Juniper-UNI-ATM-MIB", "juniAtmOamF4FlowSegmentIfIndex"),
    (0, "Juniper-UNI-ATM-MIB", "juniAtmOamF4FlowSegmentVpi"),
)
if mibBuilder.loadTexts:
    juniAtmOamF4FlowSegmentCfgEntry.setStatus("current")
_JuniAtmOamF4FlowSegmentIfIndex_Type = InterfaceIndex
_JuniAtmOamF4FlowSegmentIfIndex_Object = MibTableColumn
juniAtmOamF4FlowSegmentIfIndex = _JuniAtmOamF4FlowSegmentIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 9, 1, 1),
    _JuniAtmOamF4FlowSegmentIfIndex_Type()
)
juniAtmOamF4FlowSegmentIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniAtmOamF4FlowSegmentIfIndex.setStatus("current")


class _JuniAtmOamF4FlowSegmentVpi_Type(Integer32):
    """Custom type juniAtmOamF4FlowSegmentVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_JuniAtmOamF4FlowSegmentVpi_Type.__name__ = "Integer32"
_JuniAtmOamF4FlowSegmentVpi_Object = MibTableColumn
juniAtmOamF4FlowSegmentVpi = _JuniAtmOamF4FlowSegmentVpi_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 9, 1, 2),
    _JuniAtmOamF4FlowSegmentVpi_Type()
)
juniAtmOamF4FlowSegmentVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniAtmOamF4FlowSegmentVpi.setStatus("current")


class _JuniAtmOamF4FlowSegmentCCSink_Type(TruthValue):
    """Custom type juniAtmOamF4FlowSegmentCCSink based on TruthValue"""


_JuniAtmOamF4FlowSegmentCCSink_Object = MibTableColumn
juniAtmOamF4FlowSegmentCCSink = _JuniAtmOamF4FlowSegmentCCSink_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 9, 1, 3),
    _JuniAtmOamF4FlowSegmentCCSink_Type()
)
juniAtmOamF4FlowSegmentCCSink.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAtmOamF4FlowSegmentCCSink.setStatus("current")


class _JuniAtmOamF4FlowSegmentCCSource_Type(TruthValue):
    """Custom type juniAtmOamF4FlowSegmentCCSource based on TruthValue"""


_JuniAtmOamF4FlowSegmentCCSource_Object = MibTableColumn
juniAtmOamF4FlowSegmentCCSource = _JuniAtmOamF4FlowSegmentCCSource_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 9, 1, 4),
    _JuniAtmOamF4FlowSegmentCCSource_Type()
)
juniAtmOamF4FlowSegmentCCSource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAtmOamF4FlowSegmentCCSource.setStatus("current")
_JuniAtmOamF4FlowSegmentRowStatus_Type = RowStatus
_JuniAtmOamF4FlowSegmentRowStatus_Object = MibTableColumn
juniAtmOamF4FlowSegmentRowStatus = _JuniAtmOamF4FlowSegmentRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 9, 1, 5),
    _JuniAtmOamF4FlowSegmentRowStatus_Type()
)
juniAtmOamF4FlowSegmentRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAtmOamF4FlowSegmentRowStatus.setStatus("current")
_JuniAtmVpDescrTable_Object = MibTable
juniAtmVpDescrTable = _JuniAtmVpDescrTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 10)
)
if mibBuilder.loadTexts:
    juniAtmVpDescrTable.setStatus("current")
_JuniAtmVpDescrEntry_Object = MibTableRow
juniAtmVpDescrEntry = _JuniAtmVpDescrEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 10, 1)
)
juniAtmVpDescrEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ATM-MIB", "atmVplVpi"),
)
if mibBuilder.loadTexts:
    juniAtmVpDescrEntry.setStatus("current")


class _JuniAtmVpDescription_Type(SnmpAdminString):
    """Custom type juniAtmVpDescription based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_JuniAtmVpDescription_Type.__name__ = "SnmpAdminString"
_JuniAtmVpDescription_Object = MibTableColumn
juniAtmVpDescription = _JuniAtmVpDescription_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 10, 1, 1),
    _JuniAtmVpDescription_Type()
)
juniAtmVpDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniAtmVpDescription.setStatus("current")
_JuniAtmF4FlowOamEndToEndStatsTable_Object = MibTable
juniAtmF4FlowOamEndToEndStatsTable = _JuniAtmF4FlowOamEndToEndStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 11)
)
if mibBuilder.loadTexts:
    juniAtmF4FlowOamEndToEndStatsTable.setStatus("current")
_JuniAtmF4FlowOamEndToEndStatsEntry_Object = MibTableRow
juniAtmF4FlowOamEndToEndStatsEntry = _JuniAtmF4FlowOamEndToEndStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 11, 1)
)
juniAtmF4FlowOamEndToEndStatsEntry.setIndexNames(
    (0, "Juniper-UNI-ATM-MIB", "juniAtmOamF4FlowEndToEndIfIndex"),
    (0, "Juniper-UNI-ATM-MIB", "juniAtmOamF4FlowEndToEndVpi"),
)
if mibBuilder.loadTexts:
    juniAtmF4FlowOamEndToEndStatsEntry.setStatus("current")
_JuniAtmF4FlowInOamEndAisCells_Type = Counter32
_JuniAtmF4FlowInOamEndAisCells_Object = MibTableColumn
juniAtmF4FlowInOamEndAisCells = _JuniAtmF4FlowInOamEndAisCells_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 11, 1, 1),
    _JuniAtmF4FlowInOamEndAisCells_Type()
)
juniAtmF4FlowInOamEndAisCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAtmF4FlowInOamEndAisCells.setStatus("current")
if mibBuilder.loadTexts:
    juniAtmF4FlowInOamEndAisCells.setUnits("cells")
_JuniAtmF4FlowInOamEndRdiCells_Type = Counter32
_JuniAtmF4FlowInOamEndRdiCells_Object = MibTableColumn
juniAtmF4FlowInOamEndRdiCells = _JuniAtmF4FlowInOamEndRdiCells_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 11, 1, 2),
    _JuniAtmF4FlowInOamEndRdiCells_Type()
)
juniAtmF4FlowInOamEndRdiCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAtmF4FlowInOamEndRdiCells.setStatus("current")
if mibBuilder.loadTexts:
    juniAtmF4FlowInOamEndRdiCells.setUnits("cells")
_JuniAtmF4FlowInOamEndCCCells_Type = Counter32
_JuniAtmF4FlowInOamEndCCCells_Object = MibTableColumn
juniAtmF4FlowInOamEndCCCells = _JuniAtmF4FlowInOamEndCCCells_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 11, 1, 3),
    _JuniAtmF4FlowInOamEndCCCells_Type()
)
juniAtmF4FlowInOamEndCCCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAtmF4FlowInOamEndCCCells.setStatus("current")
if mibBuilder.loadTexts:
    juniAtmF4FlowInOamEndCCCells.setUnits("cells")
_JuniAtmF4FlowInOamEndCCActDeActCells_Type = Counter32
_JuniAtmF4FlowInOamEndCCActDeActCells_Object = MibTableColumn
juniAtmF4FlowInOamEndCCActDeActCells = _JuniAtmF4FlowInOamEndCCActDeActCells_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 11, 1, 4),
    _JuniAtmF4FlowInOamEndCCActDeActCells_Type()
)
juniAtmF4FlowInOamEndCCActDeActCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAtmF4FlowInOamEndCCActDeActCells.setStatus("current")
if mibBuilder.loadTexts:
    juniAtmF4FlowInOamEndCCActDeActCells.setUnits("cells")
_JuniAtmF4FlowInOamEndLoopbackCells_Type = Counter32
_JuniAtmF4FlowInOamEndLoopbackCells_Object = MibTableColumn
juniAtmF4FlowInOamEndLoopbackCells = _JuniAtmF4FlowInOamEndLoopbackCells_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 11, 1, 5),
    _JuniAtmF4FlowInOamEndLoopbackCells_Type()
)
juniAtmF4FlowInOamEndLoopbackCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAtmF4FlowInOamEndLoopbackCells.setStatus("current")
if mibBuilder.loadTexts:
    juniAtmF4FlowInOamEndLoopbackCells.setUnits("cells")
_JuniAtmF4FlowOutEndRdiCells_Type = Counter32
_JuniAtmF4FlowOutEndRdiCells_Object = MibTableColumn
juniAtmF4FlowOutEndRdiCells = _JuniAtmF4FlowOutEndRdiCells_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 11, 1, 6),
    _JuniAtmF4FlowOutEndRdiCells_Type()
)
juniAtmF4FlowOutEndRdiCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAtmF4FlowOutEndRdiCells.setStatus("current")
if mibBuilder.loadTexts:
    juniAtmF4FlowOutEndRdiCells.setUnits("cells")
_JuniAtmF4FlowOutEndCCCells_Type = Counter32
_JuniAtmF4FlowOutEndCCCells_Object = MibTableColumn
juniAtmF4FlowOutEndCCCells = _JuniAtmF4FlowOutEndCCCells_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 11, 1, 7),
    _JuniAtmF4FlowOutEndCCCells_Type()
)
juniAtmF4FlowOutEndCCCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAtmF4FlowOutEndCCCells.setStatus("current")
if mibBuilder.loadTexts:
    juniAtmF4FlowOutEndCCCells.setUnits("cells")
_JuniAtmF4FlowOutEndCCActDeActCells_Type = Counter32
_JuniAtmF4FlowOutEndCCActDeActCells_Object = MibTableColumn
juniAtmF4FlowOutEndCCActDeActCells = _JuniAtmF4FlowOutEndCCActDeActCells_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 11, 1, 8),
    _JuniAtmF4FlowOutEndCCActDeActCells_Type()
)
juniAtmF4FlowOutEndCCActDeActCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAtmF4FlowOutEndCCActDeActCells.setStatus("current")
if mibBuilder.loadTexts:
    juniAtmF4FlowOutEndCCActDeActCells.setUnits("cells")
_JuniAtmF4FlowOutEndToEndLoopbackCells_Type = Counter32
_JuniAtmF4FlowOutEndToEndLoopbackCells_Object = MibTableColumn
juniAtmF4FlowOutEndToEndLoopbackCells = _JuniAtmF4FlowOutEndToEndLoopbackCells_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 11, 1, 9),
    _JuniAtmF4FlowOutEndToEndLoopbackCells_Type()
)
juniAtmF4FlowOutEndToEndLoopbackCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAtmF4FlowOutEndToEndLoopbackCells.setStatus("current")
if mibBuilder.loadTexts:
    juniAtmF4FlowOutEndToEndLoopbackCells.setUnits("cells")


class _JuniAtmF4FlowEndActualLoopbackFreq_Type(Integer32):
    """Custom type juniAtmF4FlowEndActualLoopbackFreq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_JuniAtmF4FlowEndActualLoopbackFreq_Type.__name__ = "Integer32"
_JuniAtmF4FlowEndActualLoopbackFreq_Object = MibTableColumn
juniAtmF4FlowEndActualLoopbackFreq = _JuniAtmF4FlowEndActualLoopbackFreq_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 11, 1, 10),
    _JuniAtmF4FlowEndActualLoopbackFreq_Type()
)
juniAtmF4FlowEndActualLoopbackFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAtmF4FlowEndActualLoopbackFreq.setStatus("current")
if mibBuilder.loadTexts:
    juniAtmF4FlowEndActualLoopbackFreq.setUnits("seconds")
_JuniAtmF4FlowEndLastTimeChanged_Type = TimeTicks
_JuniAtmF4FlowEndLastTimeChanged_Object = MibTableColumn
juniAtmF4FlowEndLastTimeChanged = _JuniAtmF4FlowEndLastTimeChanged_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 11, 1, 11),
    _JuniAtmF4FlowEndLastTimeChanged_Type()
)
juniAtmF4FlowEndLastTimeChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAtmF4FlowEndLastTimeChanged.setStatus("current")


class _JuniAtmF4FlowOamEndVpOperationState_Type(Integer32):
    """Custom type juniAtmF4FlowOamEndVpOperationState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("vcAisState", 0),
          ("vcDown", 5),
          ("vcDownRetry", 2),
          ("vcInVpAisState", 10),
          ("vcInVpRdiState", 9),
          ("vcNotManaged", 6),
          ("vcRdiState", 1),
          ("vcSegRdiState", 12),
          ("vcSegmentAisState", 11),
          ("vcUp", 4),
          ("vcUpRetry", 3),
          ("vpAisState", 7),
          ("vpRdiState", 8))
    )


_JuniAtmF4FlowOamEndVpOperationState_Type.__name__ = "Integer32"
_JuniAtmF4FlowOamEndVpOperationState_Object = MibTableColumn
juniAtmF4FlowOamEndVpOperationState = _JuniAtmF4FlowOamEndVpOperationState_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 11, 1, 12),
    _JuniAtmF4FlowOamEndVpOperationState_Type()
)
juniAtmF4FlowOamEndVpOperationState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAtmF4FlowOamEndVpOperationState.setStatus("current")


class _JuniAtmF4FlowOamEndVpAdminState_Type(Integer32):
    """Custom type juniAtmF4FlowOamEndVpAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("down", 0),
          ("up", 1))
    )


_JuniAtmF4FlowOamEndVpAdminState_Type.__name__ = "Integer32"
_JuniAtmF4FlowOamEndVpAdminState_Object = MibTableColumn
juniAtmF4FlowOamEndVpAdminState = _JuniAtmF4FlowOamEndVpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 11, 1, 13),
    _JuniAtmF4FlowOamEndVpAdminState_Type()
)
juniAtmF4FlowOamEndVpAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAtmF4FlowOamEndVpAdminState.setStatus("current")
_JuniAtmF4FlowEndInOamCells_Type = Counter32
_JuniAtmF4FlowEndInOamCells_Object = MibTableColumn
juniAtmF4FlowEndInOamCells = _JuniAtmF4FlowEndInOamCells_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 11, 1, 14),
    _JuniAtmF4FlowEndInOamCells_Type()
)
juniAtmF4FlowEndInOamCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAtmF4FlowEndInOamCells.setStatus("current")
if mibBuilder.loadTexts:
    juniAtmF4FlowEndInOamCells.setUnits("cells")
_JuniAtmF4FlowEndOutOamCells_Type = Counter32
_JuniAtmF4FlowEndOutOamCells_Object = MibTableColumn
juniAtmF4FlowEndOutOamCells = _JuniAtmF4FlowEndOutOamCells_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 11, 1, 15),
    _JuniAtmF4FlowEndOutOamCells_Type()
)
juniAtmF4FlowEndOutOamCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAtmF4FlowEndOutOamCells.setStatus("current")
if mibBuilder.loadTexts:
    juniAtmF4FlowEndOutOamCells.setUnits("cells")
_JuniAtmF4FlowEndInOamCellsDropped_Type = Counter32
_JuniAtmF4FlowEndInOamCellsDropped_Object = MibTableColumn
juniAtmF4FlowEndInOamCellsDropped = _JuniAtmF4FlowEndInOamCellsDropped_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 11, 1, 16),
    _JuniAtmF4FlowEndInOamCellsDropped_Type()
)
juniAtmF4FlowEndInOamCellsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAtmF4FlowEndInOamCellsDropped.setStatus("current")
if mibBuilder.loadTexts:
    juniAtmF4FlowEndInOamCellsDropped.setUnits("cells")
_JuniAtmF4FlowEndToEndInLoopbackCmds_Type = Counter32
_JuniAtmF4FlowEndToEndInLoopbackCmds_Object = MibTableColumn
juniAtmF4FlowEndToEndInLoopbackCmds = _JuniAtmF4FlowEndToEndInLoopbackCmds_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 11, 1, 17),
    _JuniAtmF4FlowEndToEndInLoopbackCmds_Type()
)
juniAtmF4FlowEndToEndInLoopbackCmds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAtmF4FlowEndToEndInLoopbackCmds.setStatus("current")
if mibBuilder.loadTexts:
    juniAtmF4FlowEndToEndInLoopbackCmds.setUnits("cells")
_JuniAtmF4FlowEndToEndInLoopbackRsps_Type = Counter32
_JuniAtmF4FlowEndToEndInLoopbackRsps_Object = MibTableColumn
juniAtmF4FlowEndToEndInLoopbackRsps = _JuniAtmF4FlowEndToEndInLoopbackRsps_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 11, 1, 18),
    _JuniAtmF4FlowEndToEndInLoopbackRsps_Type()
)
juniAtmF4FlowEndToEndInLoopbackRsps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAtmF4FlowEndToEndInLoopbackRsps.setStatus("current")
if mibBuilder.loadTexts:
    juniAtmF4FlowEndToEndInLoopbackRsps.setUnits("cells")
_JuniAtmF4FlowEndToEndOutLoopbackCmds_Type = Counter32
_JuniAtmF4FlowEndToEndOutLoopbackCmds_Object = MibTableColumn
juniAtmF4FlowEndToEndOutLoopbackCmds = _JuniAtmF4FlowEndToEndOutLoopbackCmds_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 11, 1, 19),
    _JuniAtmF4FlowEndToEndOutLoopbackCmds_Type()
)
juniAtmF4FlowEndToEndOutLoopbackCmds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAtmF4FlowEndToEndOutLoopbackCmds.setStatus("current")
if mibBuilder.loadTexts:
    juniAtmF4FlowEndToEndOutLoopbackCmds.setUnits("cells")
_JuniAtmF4FlowEndToEndOutLoopbackRsps_Type = Counter32
_JuniAtmF4FlowEndToEndOutLoopbackRsps_Object = MibTableColumn
juniAtmF4FlowEndToEndOutLoopbackRsps = _JuniAtmF4FlowEndToEndOutLoopbackRsps_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 11, 1, 20),
    _JuniAtmF4FlowEndToEndOutLoopbackRsps_Type()
)
juniAtmF4FlowEndToEndOutLoopbackRsps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAtmF4FlowEndToEndOutLoopbackRsps.setStatus("current")
if mibBuilder.loadTexts:
    juniAtmF4FlowEndToEndOutLoopbackRsps.setUnits("cells")
_JuniAtmF4FlowOamSegmentStatsTable_Object = MibTable
juniAtmF4FlowOamSegmentStatsTable = _JuniAtmF4FlowOamSegmentStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 12)
)
if mibBuilder.loadTexts:
    juniAtmF4FlowOamSegmentStatsTable.setStatus("current")
_JuniAtmF4FlowOamSegmentStatsEntry_Object = MibTableRow
juniAtmF4FlowOamSegmentStatsEntry = _JuniAtmF4FlowOamSegmentStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 12, 1)
)
juniAtmF4FlowOamSegmentStatsEntry.setIndexNames(
    (0, "Juniper-UNI-ATM-MIB", "juniAtmOamF4FlowSegmentIfIndex"),
    (0, "Juniper-UNI-ATM-MIB", "juniAtmOamF4FlowSegmentVpi"),
)
if mibBuilder.loadTexts:
    juniAtmF4FlowOamSegmentStatsEntry.setStatus("current")
_JuniAtmF4FlowInOamSegmentAisCells_Type = Counter32
_JuniAtmF4FlowInOamSegmentAisCells_Object = MibTableColumn
juniAtmF4FlowInOamSegmentAisCells = _JuniAtmF4FlowInOamSegmentAisCells_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 12, 1, 1),
    _JuniAtmF4FlowInOamSegmentAisCells_Type()
)
juniAtmF4FlowInOamSegmentAisCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAtmF4FlowInOamSegmentAisCells.setStatus("current")
if mibBuilder.loadTexts:
    juniAtmF4FlowInOamSegmentAisCells.setUnits("cells")
_JuniAtmF4FlowInOamSegmentRdiCells_Type = Counter32
_JuniAtmF4FlowInOamSegmentRdiCells_Object = MibTableColumn
juniAtmF4FlowInOamSegmentRdiCells = _JuniAtmF4FlowInOamSegmentRdiCells_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 12, 1, 2),
    _JuniAtmF4FlowInOamSegmentRdiCells_Type()
)
juniAtmF4FlowInOamSegmentRdiCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAtmF4FlowInOamSegmentRdiCells.setStatus("current")
if mibBuilder.loadTexts:
    juniAtmF4FlowInOamSegmentRdiCells.setUnits("cells")
_JuniAtmF4FlowInOamSegmentCCCells_Type = Counter32
_JuniAtmF4FlowInOamSegmentCCCells_Object = MibTableColumn
juniAtmF4FlowInOamSegmentCCCells = _JuniAtmF4FlowInOamSegmentCCCells_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 12, 1, 3),
    _JuniAtmF4FlowInOamSegmentCCCells_Type()
)
juniAtmF4FlowInOamSegmentCCCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAtmF4FlowInOamSegmentCCCells.setStatus("current")
if mibBuilder.loadTexts:
    juniAtmF4FlowInOamSegmentCCCells.setUnits("cells")
_JuniAtmF4FlowInOamSegmentCCActDeActCells_Type = Counter32
_JuniAtmF4FlowInOamSegmentCCActDeActCells_Object = MibTableColumn
juniAtmF4FlowInOamSegmentCCActDeActCells = _JuniAtmF4FlowInOamSegmentCCActDeActCells_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 12, 1, 4),
    _JuniAtmF4FlowInOamSegmentCCActDeActCells_Type()
)
juniAtmF4FlowInOamSegmentCCActDeActCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAtmF4FlowInOamSegmentCCActDeActCells.setStatus("current")
if mibBuilder.loadTexts:
    juniAtmF4FlowInOamSegmentCCActDeActCells.setUnits("cells")
_JuniAtmF4FlowInOamSegmentLoopbackCells_Type = Counter32
_JuniAtmF4FlowInOamSegmentLoopbackCells_Object = MibTableColumn
juniAtmF4FlowInOamSegmentLoopbackCells = _JuniAtmF4FlowInOamSegmentLoopbackCells_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 12, 1, 5),
    _JuniAtmF4FlowInOamSegmentLoopbackCells_Type()
)
juniAtmF4FlowInOamSegmentLoopbackCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAtmF4FlowInOamSegmentLoopbackCells.setStatus("current")
if mibBuilder.loadTexts:
    juniAtmF4FlowInOamSegmentLoopbackCells.setUnits("cells")
_JuniAtmF4FlowOutSegmentRdiCells_Type = Counter32
_JuniAtmF4FlowOutSegmentRdiCells_Object = MibTableColumn
juniAtmF4FlowOutSegmentRdiCells = _JuniAtmF4FlowOutSegmentRdiCells_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 12, 1, 6),
    _JuniAtmF4FlowOutSegmentRdiCells_Type()
)
juniAtmF4FlowOutSegmentRdiCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAtmF4FlowOutSegmentRdiCells.setStatus("current")
if mibBuilder.loadTexts:
    juniAtmF4FlowOutSegmentRdiCells.setUnits("cells")
_JuniAtmF4FlowOutSegmentCCCells_Type = Counter32
_JuniAtmF4FlowOutSegmentCCCells_Object = MibTableColumn
juniAtmF4FlowOutSegmentCCCells = _JuniAtmF4FlowOutSegmentCCCells_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 12, 1, 7),
    _JuniAtmF4FlowOutSegmentCCCells_Type()
)
juniAtmF4FlowOutSegmentCCCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAtmF4FlowOutSegmentCCCells.setStatus("current")
if mibBuilder.loadTexts:
    juniAtmF4FlowOutSegmentCCCells.setUnits("cells")
_JuniAtmF4FlowOutSegmentCCActDeActCells_Type = Counter32
_JuniAtmF4FlowOutSegmentCCActDeActCells_Object = MibTableColumn
juniAtmF4FlowOutSegmentCCActDeActCells = _JuniAtmF4FlowOutSegmentCCActDeActCells_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 12, 1, 8),
    _JuniAtmF4FlowOutSegmentCCActDeActCells_Type()
)
juniAtmF4FlowOutSegmentCCActDeActCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAtmF4FlowOutSegmentCCActDeActCells.setStatus("current")
if mibBuilder.loadTexts:
    juniAtmF4FlowOutSegmentCCActDeActCells.setUnits("cells")
_JuniAtmF4FlowOutSegmentLoopbackCells_Type = Counter32
_JuniAtmF4FlowOutSegmentLoopbackCells_Object = MibTableColumn
juniAtmF4FlowOutSegmentLoopbackCells = _JuniAtmF4FlowOutSegmentLoopbackCells_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 12, 1, 9),
    _JuniAtmF4FlowOutSegmentLoopbackCells_Type()
)
juniAtmF4FlowOutSegmentLoopbackCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAtmF4FlowOutSegmentLoopbackCells.setStatus("current")
if mibBuilder.loadTexts:
    juniAtmF4FlowOutSegmentLoopbackCells.setUnits("cells")
_JuniAtmF4FlowSegmentLastTimeChanged_Type = TimeTicks
_JuniAtmF4FlowSegmentLastTimeChanged_Object = MibTableColumn
juniAtmF4FlowSegmentLastTimeChanged = _JuniAtmF4FlowSegmentLastTimeChanged_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 12, 1, 10),
    _JuniAtmF4FlowSegmentLastTimeChanged_Type()
)
juniAtmF4FlowSegmentLastTimeChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAtmF4FlowSegmentLastTimeChanged.setStatus("current")


class _JuniAtmF4FlowOamSegmentVpOperationState_Type(Integer32):
    """Custom type juniAtmF4FlowOamSegmentVpOperationState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("vcAisState", 0),
          ("vcDown", 5),
          ("vcDownRetry", 2),
          ("vcInVpAisState", 10),
          ("vcInVpRdiState", 9),
          ("vcNotManaged", 6),
          ("vcRdiState", 1),
          ("vcSegRdiState", 12),
          ("vcSegmentAisState", 11),
          ("vcUp", 4),
          ("vcUpRetry", 3),
          ("vpAisState", 7),
          ("vpRdiState", 8))
    )


_JuniAtmF4FlowOamSegmentVpOperationState_Type.__name__ = "Integer32"
_JuniAtmF4FlowOamSegmentVpOperationState_Object = MibTableColumn
juniAtmF4FlowOamSegmentVpOperationState = _JuniAtmF4FlowOamSegmentVpOperationState_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 12, 1, 11),
    _JuniAtmF4FlowOamSegmentVpOperationState_Type()
)
juniAtmF4FlowOamSegmentVpOperationState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAtmF4FlowOamSegmentVpOperationState.setStatus("current")


class _JuniAtmF4FlowOamSegmentVpAdminState_Type(Integer32):
    """Custom type juniAtmF4FlowOamSegmentVpAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("down", 0),
          ("up", 1))
    )


_JuniAtmF4FlowOamSegmentVpAdminState_Type.__name__ = "Integer32"
_JuniAtmF4FlowOamSegmentVpAdminState_Object = MibTableColumn
juniAtmF4FlowOamSegmentVpAdminState = _JuniAtmF4FlowOamSegmentVpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 12, 1, 12),
    _JuniAtmF4FlowOamSegmentVpAdminState_Type()
)
juniAtmF4FlowOamSegmentVpAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAtmF4FlowOamSegmentVpAdminState.setStatus("current")
_JuniAtmF4FlowSegmentInOamCells_Type = Counter32
_JuniAtmF4FlowSegmentInOamCells_Object = MibTableColumn
juniAtmF4FlowSegmentInOamCells = _JuniAtmF4FlowSegmentInOamCells_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 12, 1, 13),
    _JuniAtmF4FlowSegmentInOamCells_Type()
)
juniAtmF4FlowSegmentInOamCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAtmF4FlowSegmentInOamCells.setStatus("current")
if mibBuilder.loadTexts:
    juniAtmF4FlowSegmentInOamCells.setUnits("cells")
_JuniAtmF4FlowSegmentOutOamCells_Type = Counter32
_JuniAtmF4FlowSegmentOutOamCells_Object = MibTableColumn
juniAtmF4FlowSegmentOutOamCells = _JuniAtmF4FlowSegmentOutOamCells_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 12, 1, 14),
    _JuniAtmF4FlowSegmentOutOamCells_Type()
)
juniAtmF4FlowSegmentOutOamCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAtmF4FlowSegmentOutOamCells.setStatus("current")
if mibBuilder.loadTexts:
    juniAtmF4FlowSegmentOutOamCells.setUnits("cells")
_JuniAtmF4FlowSegmentInOamCellsDropped_Type = Counter32
_JuniAtmF4FlowSegmentInOamCellsDropped_Object = MibTableColumn
juniAtmF4FlowSegmentInOamCellsDropped = _JuniAtmF4FlowSegmentInOamCellsDropped_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 12, 1, 15),
    _JuniAtmF4FlowSegmentInOamCellsDropped_Type()
)
juniAtmF4FlowSegmentInOamCellsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAtmF4FlowSegmentInOamCellsDropped.setStatus("current")
if mibBuilder.loadTexts:
    juniAtmF4FlowSegmentInOamCellsDropped.setUnits("cells")
_JuniAtmF4FlowSegmentInLoopbackCmds_Type = Counter32
_JuniAtmF4FlowSegmentInLoopbackCmds_Object = MibTableColumn
juniAtmF4FlowSegmentInLoopbackCmds = _JuniAtmF4FlowSegmentInLoopbackCmds_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 12, 1, 16),
    _JuniAtmF4FlowSegmentInLoopbackCmds_Type()
)
juniAtmF4FlowSegmentInLoopbackCmds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAtmF4FlowSegmentInLoopbackCmds.setStatus("current")
if mibBuilder.loadTexts:
    juniAtmF4FlowSegmentInLoopbackCmds.setUnits("cells")
_JuniAtmF4FlowSegmentInLoopbackRsps_Type = Counter32
_JuniAtmF4FlowSegmentInLoopbackRsps_Object = MibTableColumn
juniAtmF4FlowSegmentInLoopbackRsps = _JuniAtmF4FlowSegmentInLoopbackRsps_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 12, 1, 17),
    _JuniAtmF4FlowSegmentInLoopbackRsps_Type()
)
juniAtmF4FlowSegmentInLoopbackRsps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAtmF4FlowSegmentInLoopbackRsps.setStatus("current")
if mibBuilder.loadTexts:
    juniAtmF4FlowSegmentInLoopbackRsps.setUnits("cells")
_JuniAtmF4FlowSegmentOutLoopbackCmds_Type = Counter32
_JuniAtmF4FlowSegmentOutLoopbackCmds_Object = MibTableColumn
juniAtmF4FlowSegmentOutLoopbackCmds = _JuniAtmF4FlowSegmentOutLoopbackCmds_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 12, 1, 18),
    _JuniAtmF4FlowSegmentOutLoopbackCmds_Type()
)
juniAtmF4FlowSegmentOutLoopbackCmds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAtmF4FlowSegmentOutLoopbackCmds.setStatus("current")
if mibBuilder.loadTexts:
    juniAtmF4FlowSegmentOutLoopbackCmds.setUnits("cells")
_JuniAtmF4FlowSegmentOutLoopbackRsps_Type = Counter32
_JuniAtmF4FlowSegmentOutLoopbackRsps_Object = MibTableColumn
juniAtmF4FlowSegmentOutLoopbackRsps = _JuniAtmF4FlowSegmentOutLoopbackRsps_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 12, 1, 19),
    _JuniAtmF4FlowSegmentOutLoopbackRsps_Type()
)
juniAtmF4FlowSegmentOutLoopbackRsps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAtmF4FlowSegmentOutLoopbackRsps.setStatus("current")
if mibBuilder.loadTexts:
    juniAtmF4FlowSegmentOutLoopbackRsps.setUnits("cells")
_JuniAtmMartiniTimeoutTimerTable_Object = MibTable
juniAtmMartiniTimeoutTimerTable = _JuniAtmMartiniTimeoutTimerTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 13)
)
if mibBuilder.loadTexts:
    juniAtmMartiniTimeoutTimerTable.setStatus("current")
_JuniAtmMartiniTimeoutTimerEntry_Object = MibTableRow
juniAtmMartiniTimeoutTimerEntry = _JuniAtmMartiniTimeoutTimerEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 13, 1)
)
juniAtmMartiniTimeoutTimerEntry.setIndexNames(
    (0, "Juniper-UNI-ATM-MIB", "juniAtmMartiniTimeoutTimerIndex"),
)
if mibBuilder.loadTexts:
    juniAtmMartiniTimeoutTimerEntry.setStatus("current")


class _JuniAtmMartiniTimeoutTimerIndex_Type(Integer32):
    """Custom type juniAtmMartiniTimeoutTimerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("timer1", 1),
          ("timer2", 2),
          ("timer3", 3))
    )


_JuniAtmMartiniTimeoutTimerIndex_Type.__name__ = "Integer32"
_JuniAtmMartiniTimeoutTimerIndex_Object = MibTableColumn
juniAtmMartiniTimeoutTimerIndex = _JuniAtmMartiniTimeoutTimerIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 13, 1, 1),
    _JuniAtmMartiniTimeoutTimerIndex_Type()
)
juniAtmMartiniTimeoutTimerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniAtmMartiniTimeoutTimerIndex.setStatus("current")


class _JuniAtmMartiniTimeoutTimerValue_Type(Integer32):
    """Custom type juniAtmMartiniTimeoutTimerValue based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 4095),
    )


_JuniAtmMartiniTimeoutTimerValue_Type.__name__ = "Integer32"
_JuniAtmMartiniTimeoutTimerValue_Object = MibTableColumn
juniAtmMartiniTimeoutTimerValue = _JuniAtmMartiniTimeoutTimerValue_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 13, 1, 2),
    _JuniAtmMartiniTimeoutTimerValue_Type()
)
juniAtmMartiniTimeoutTimerValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniAtmMartiniTimeoutTimerValue.setStatus("current")
_JuniAtmVpStatsTable_Object = MibTable
juniAtmVpStatsTable = _JuniAtmVpStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 14)
)
if mibBuilder.loadTexts:
    juniAtmVpStatsTable.setStatus("current")
_JuniAtmVpStatsEntry_Object = MibTableRow
juniAtmVpStatsEntry = _JuniAtmVpStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 14, 1)
)
juniAtmVpStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ATM-MIB", "atmVplVpi"),
)
if mibBuilder.loadTexts:
    juniAtmVpStatsEntry.setStatus("current")
_JuniAtmVpStatsIfIndex_Type = InterfaceIndex
_JuniAtmVpStatsIfIndex_Object = MibTableColumn
juniAtmVpStatsIfIndex = _JuniAtmVpStatsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 14, 1, 1),
    _JuniAtmVpStatsIfIndex_Type()
)
juniAtmVpStatsIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniAtmVpStatsIfIndex.setStatus("current")
_JuniAtmVpStatsVpi_Type = AtmVpIdentifier
_JuniAtmVpStatsVpi_Object = MibTableColumn
juniAtmVpStatsVpi = _JuniAtmVpStatsVpi_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 14, 1, 2),
    _JuniAtmVpStatsVpi_Type()
)
juniAtmVpStatsVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniAtmVpStatsVpi.setStatus("current")
_JuniAtmVpStatsInCells_Type = Counter64
_JuniAtmVpStatsInCells_Object = MibTableColumn
juniAtmVpStatsInCells = _JuniAtmVpStatsInCells_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 14, 1, 3),
    _JuniAtmVpStatsInCells_Type()
)
juniAtmVpStatsInCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAtmVpStatsInCells.setStatus("current")
_JuniAtmVpStatsInPackets_Type = Counter64
_JuniAtmVpStatsInPackets_Object = MibTableColumn
juniAtmVpStatsInPackets = _JuniAtmVpStatsInPackets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 14, 1, 4),
    _JuniAtmVpStatsInPackets_Type()
)
juniAtmVpStatsInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAtmVpStatsInPackets.setStatus("current")
_JuniAtmVpStatsInPacketOctets_Type = Counter64
_JuniAtmVpStatsInPacketOctets_Object = MibTableColumn
juniAtmVpStatsInPacketOctets = _JuniAtmVpStatsInPacketOctets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 14, 1, 5),
    _JuniAtmVpStatsInPacketOctets_Type()
)
juniAtmVpStatsInPacketOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAtmVpStatsInPacketOctets.setStatus("current")
_JuniAtmVpStatsOutCells_Type = Counter64
_JuniAtmVpStatsOutCells_Object = MibTableColumn
juniAtmVpStatsOutCells = _JuniAtmVpStatsOutCells_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 14, 1, 6),
    _JuniAtmVpStatsOutCells_Type()
)
juniAtmVpStatsOutCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAtmVpStatsOutCells.setStatus("current")
_JuniAtmVpStatsOutPackets_Type = Counter64
_JuniAtmVpStatsOutPackets_Object = MibTableColumn
juniAtmVpStatsOutPackets = _JuniAtmVpStatsOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 14, 1, 7),
    _JuniAtmVpStatsOutPackets_Type()
)
juniAtmVpStatsOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAtmVpStatsOutPackets.setStatus("current")
_JuniAtmVpStatsOutPacketOctets_Type = Counter64
_JuniAtmVpStatsOutPacketOctets_Object = MibTableColumn
juniAtmVpStatsOutPacketOctets = _JuniAtmVpStatsOutPacketOctets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 14, 1, 8),
    _JuniAtmVpStatsOutPacketOctets_Type()
)
juniAtmVpStatsOutPacketOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAtmVpStatsOutPacketOctets.setStatus("current")
_JuniAtmVpStatsInPacketErrors_Type = Counter32
_JuniAtmVpStatsInPacketErrors_Object = MibTableColumn
juniAtmVpStatsInPacketErrors = _JuniAtmVpStatsInPacketErrors_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 14, 1, 9),
    _JuniAtmVpStatsInPacketErrors_Type()
)
juniAtmVpStatsInPacketErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAtmVpStatsInPacketErrors.setStatus("current")
_JuniAtmVpStatsOutPacketErrors_Type = Counter32
_JuniAtmVpStatsOutPacketErrors_Object = MibTableColumn
juniAtmVpStatsOutPacketErrors = _JuniAtmVpStatsOutPacketErrors_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 14, 1, 10),
    _JuniAtmVpStatsOutPacketErrors_Type()
)
juniAtmVpStatsOutPacketErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAtmVpStatsOutPacketErrors.setStatus("current")
_JuniAtmVpStatsInPacketDiscards_Type = Counter32
_JuniAtmVpStatsInPacketDiscards_Object = MibTableColumn
juniAtmVpStatsInPacketDiscards = _JuniAtmVpStatsInPacketDiscards_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 14, 1, 11),
    _JuniAtmVpStatsInPacketDiscards_Type()
)
juniAtmVpStatsInPacketDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAtmVpStatsInPacketDiscards.setStatus("current")
_JuniAtmVpStatsInPacketOctetDiscards_Type = Counter32
_JuniAtmVpStatsInPacketOctetDiscards_Object = MibTableColumn
juniAtmVpStatsInPacketOctetDiscards = _JuniAtmVpStatsInPacketOctetDiscards_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 14, 1, 12),
    _JuniAtmVpStatsInPacketOctetDiscards_Type()
)
juniAtmVpStatsInPacketOctetDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAtmVpStatsInPacketOctetDiscards.setStatus("current")
_JuniAtmVpStatsInPacketUnknownProtocol_Type = Counter32
_JuniAtmVpStatsInPacketUnknownProtocol_Object = MibTableColumn
juniAtmVpStatsInPacketUnknownProtocol = _JuniAtmVpStatsInPacketUnknownProtocol_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 14, 1, 13),
    _JuniAtmVpStatsInPacketUnknownProtocol_Type()
)
juniAtmVpStatsInPacketUnknownProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAtmVpStatsInPacketUnknownProtocol.setStatus("current")
_JuniAtmVpStatsCrcErrors_Type = Counter32
_JuniAtmVpStatsCrcErrors_Object = MibTableColumn
juniAtmVpStatsCrcErrors = _JuniAtmVpStatsCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 14, 1, 14),
    _JuniAtmVpStatsCrcErrors_Type()
)
juniAtmVpStatsCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAtmVpStatsCrcErrors.setStatus("current")
_JuniAtmVpStatsSarTimeouts_Type = Counter32
_JuniAtmVpStatsSarTimeouts_Object = MibTableColumn
juniAtmVpStatsSarTimeouts = _JuniAtmVpStatsSarTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 14, 1, 15),
    _JuniAtmVpStatsSarTimeouts_Type()
)
juniAtmVpStatsSarTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAtmVpStatsSarTimeouts.setStatus("current")
_JuniAtmVpStatsOverSizedPackets_Type = Counter32
_JuniAtmVpStatsOverSizedPackets_Object = MibTableColumn
juniAtmVpStatsOverSizedPackets = _JuniAtmVpStatsOverSizedPackets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 1, 14, 1, 16),
    _JuniAtmVpStatsOverSizedPackets_Type()
)
juniAtmVpStatsOverSizedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAtmVpStatsOverSizedPackets.setStatus("current")
_JuniAtmAal5IfLayer_ObjectIdentity = ObjectIdentity
juniAtmAal5IfLayer = _JuniAtmAal5IfLayer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 2)
)
_JuniAtmAal5NextIfIndex_Type = JuniNextIfIndex
_JuniAtmAal5NextIfIndex_Object = MibScalar
juniAtmAal5NextIfIndex = _JuniAtmAal5NextIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 2, 1),
    _JuniAtmAal5NextIfIndex_Type()
)
juniAtmAal5NextIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAtmAal5NextIfIndex.setStatus("current")
_JuniAtmAal5IfTable_Object = MibTable
juniAtmAal5IfTable = _JuniAtmAal5IfTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 2, 2)
)
if mibBuilder.loadTexts:
    juniAtmAal5IfTable.setStatus("current")
_JuniAtmAal5IfEntry_Object = MibTableRow
juniAtmAal5IfEntry = _JuniAtmAal5IfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 2, 2, 1)
)
juniAtmAal5IfEntry.setIndexNames(
    (0, "Juniper-UNI-ATM-MIB", "juniAtmAal5IfIndex"),
)
if mibBuilder.loadTexts:
    juniAtmAal5IfEntry.setStatus("current")
_JuniAtmAal5IfIndex_Type = InterfaceIndex
_JuniAtmAal5IfIndex_Object = MibTableColumn
juniAtmAal5IfIndex = _JuniAtmAal5IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 2, 2, 1, 1),
    _JuniAtmAal5IfIndex_Type()
)
juniAtmAal5IfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniAtmAal5IfIndex.setStatus("current")
_JuniAtmAal5IfRowStatus_Type = RowStatus
_JuniAtmAal5IfRowStatus_Object = MibTableColumn
juniAtmAal5IfRowStatus = _JuniAtmAal5IfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 2, 2, 1, 2),
    _JuniAtmAal5IfRowStatus_Type()
)
juniAtmAal5IfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAtmAal5IfRowStatus.setStatus("current")
_JuniAtmAal5IfLowerIfIndex_Type = InterfaceIndexOrZero
_JuniAtmAal5IfLowerIfIndex_Object = MibTableColumn
juniAtmAal5IfLowerIfIndex = _JuniAtmAal5IfLowerIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 2, 2, 1, 3),
    _JuniAtmAal5IfLowerIfIndex_Type()
)
juniAtmAal5IfLowerIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAtmAal5IfLowerIfIndex.setStatus("current")
_JuniAtmBulkCircuitsNameTable_Object = MibTable
juniAtmBulkCircuitsNameTable = _JuniAtmBulkCircuitsNameTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 2, 3)
)
if mibBuilder.loadTexts:
    juniAtmBulkCircuitsNameTable.setStatus("current")
_JuniAtmBulkCircuitsNameEntry_Object = MibTableRow
juniAtmBulkCircuitsNameEntry = _JuniAtmBulkCircuitsNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 2, 3, 1)
)
juniAtmBulkCircuitsNameEntry.setIndexNames(
    (0, "Juniper-UNI-ATM-MIB", "juniAtmBulkCircuitsNameAal5IfIndex"),
    (0, "Juniper-UNI-ATM-MIB", "juniAtmBulkCircuitsNameName"),
)
if mibBuilder.loadTexts:
    juniAtmBulkCircuitsNameEntry.setStatus("current")
_JuniAtmBulkCircuitsNameAal5IfIndex_Type = InterfaceIndex
_JuniAtmBulkCircuitsNameAal5IfIndex_Object = MibTableColumn
juniAtmBulkCircuitsNameAal5IfIndex = _JuniAtmBulkCircuitsNameAal5IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 2, 3, 1, 1),
    _JuniAtmBulkCircuitsNameAal5IfIndex_Type()
)
juniAtmBulkCircuitsNameAal5IfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniAtmBulkCircuitsNameAal5IfIndex.setStatus("current")


class _JuniAtmBulkCircuitsNameName_Type(DisplayString):
    """Custom type juniAtmBulkCircuitsNameName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_JuniAtmBulkCircuitsNameName_Type.__name__ = "DisplayString"
_JuniAtmBulkCircuitsNameName_Object = MibTableColumn
juniAtmBulkCircuitsNameName = _JuniAtmBulkCircuitsNameName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 2, 3, 1, 2),
    _JuniAtmBulkCircuitsNameName_Type()
)
juniAtmBulkCircuitsNameName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniAtmBulkCircuitsNameName.setStatus("current")
_JuniAtmBulkCircuitsNameRowStatus_Type = RowStatus
_JuniAtmBulkCircuitsNameRowStatus_Object = MibTableColumn
juniAtmBulkCircuitsNameRowStatus = _JuniAtmBulkCircuitsNameRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 2, 3, 1, 3),
    _JuniAtmBulkCircuitsNameRowStatus_Type()
)
juniAtmBulkCircuitsNameRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAtmBulkCircuitsNameRowStatus.setStatus("current")
_JuniAtmBulkCircuitsNameId_Type = Unsigned32
_JuniAtmBulkCircuitsNameId_Object = MibTableColumn
juniAtmBulkCircuitsNameId = _JuniAtmBulkCircuitsNameId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 2, 3, 1, 4),
    _JuniAtmBulkCircuitsNameId_Type()
)
juniAtmBulkCircuitsNameId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAtmBulkCircuitsNameId.setStatus("current")
_JuniAtmBulkCircuitsIdTable_Object = MibTable
juniAtmBulkCircuitsIdTable = _JuniAtmBulkCircuitsIdTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 2, 4)
)
if mibBuilder.loadTexts:
    juniAtmBulkCircuitsIdTable.setStatus("current")
_JuniAtmBulkCircuitsIdEntry_Object = MibTableRow
juniAtmBulkCircuitsIdEntry = _JuniAtmBulkCircuitsIdEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 2, 4, 1)
)
juniAtmBulkCircuitsIdEntry.setIndexNames(
    (0, "Juniper-UNI-ATM-MIB", "juniAtmBulkCircuitsIdAal5IfIndex"),
    (0, "Juniper-UNI-ATM-MIB", "juniAtmBulkCircuitsIdId"),
)
if mibBuilder.loadTexts:
    juniAtmBulkCircuitsIdEntry.setStatus("current")
_JuniAtmBulkCircuitsIdAal5IfIndex_Type = InterfaceIndex
_JuniAtmBulkCircuitsIdAal5IfIndex_Object = MibTableColumn
juniAtmBulkCircuitsIdAal5IfIndex = _JuniAtmBulkCircuitsIdAal5IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 2, 4, 1, 1),
    _JuniAtmBulkCircuitsIdAal5IfIndex_Type()
)
juniAtmBulkCircuitsIdAal5IfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniAtmBulkCircuitsIdAal5IfIndex.setStatus("current")
_JuniAtmBulkCircuitsIdId_Type = Unsigned32
_JuniAtmBulkCircuitsIdId_Object = MibTableColumn
juniAtmBulkCircuitsIdId = _JuniAtmBulkCircuitsIdId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 2, 4, 1, 2),
    _JuniAtmBulkCircuitsIdId_Type()
)
juniAtmBulkCircuitsIdId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniAtmBulkCircuitsIdId.setStatus("current")


class _JuniAtmBulkCircuitsIdName_Type(DisplayString):
    """Custom type juniAtmBulkCircuitsIdName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_JuniAtmBulkCircuitsIdName_Type.__name__ = "DisplayString"
_JuniAtmBulkCircuitsIdName_Object = MibTableColumn
juniAtmBulkCircuitsIdName = _JuniAtmBulkCircuitsIdName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 2, 4, 1, 3),
    _JuniAtmBulkCircuitsIdName_Type()
)
juniAtmBulkCircuitsIdName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAtmBulkCircuitsIdName.setStatus("current")
_JuniAtmBulkCircuitsIdNextInstance_Type = Unsigned32
_JuniAtmBulkCircuitsIdNextInstance_Object = MibTableColumn
juniAtmBulkCircuitsIdNextInstance = _JuniAtmBulkCircuitsIdNextInstance_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 2, 4, 1, 4),
    _JuniAtmBulkCircuitsIdNextInstance_Type()
)
juniAtmBulkCircuitsIdNextInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAtmBulkCircuitsIdNextInstance.setStatus("current")
_JuniAtmBulkCircuitsTable_Object = MibTable
juniAtmBulkCircuitsTable = _JuniAtmBulkCircuitsTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 2, 5)
)
if mibBuilder.loadTexts:
    juniAtmBulkCircuitsTable.setStatus("current")
_JuniAtmBulkCircuitsEntry_Object = MibTableRow
juniAtmBulkCircuitsEntry = _JuniAtmBulkCircuitsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 2, 5, 1)
)
juniAtmBulkCircuitsEntry.setIndexNames(
    (0, "Juniper-UNI-ATM-MIB", "juniAtmBulkCircuitsAal5IfIndex"),
    (0, "Juniper-UNI-ATM-MIB", "juniAtmBulkCircuitsId"),
    (0, "Juniper-UNI-ATM-MIB", "juniAtmBulkCircuitsInstance"),
)
if mibBuilder.loadTexts:
    juniAtmBulkCircuitsEntry.setStatus("current")
_JuniAtmBulkCircuitsAal5IfIndex_Type = InterfaceIndex
_JuniAtmBulkCircuitsAal5IfIndex_Object = MibTableColumn
juniAtmBulkCircuitsAal5IfIndex = _JuniAtmBulkCircuitsAal5IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 2, 5, 1, 1),
    _JuniAtmBulkCircuitsAal5IfIndex_Type()
)
juniAtmBulkCircuitsAal5IfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniAtmBulkCircuitsAal5IfIndex.setStatus("current")
_JuniAtmBulkCircuitsId_Type = Unsigned32
_JuniAtmBulkCircuitsId_Object = MibTableColumn
juniAtmBulkCircuitsId = _JuniAtmBulkCircuitsId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 2, 5, 1, 2),
    _JuniAtmBulkCircuitsId_Type()
)
juniAtmBulkCircuitsId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniAtmBulkCircuitsId.setStatus("current")
_JuniAtmBulkCircuitsInstance_Type = Unsigned32
_JuniAtmBulkCircuitsInstance_Object = MibTableColumn
juniAtmBulkCircuitsInstance = _JuniAtmBulkCircuitsInstance_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 2, 5, 1, 3),
    _JuniAtmBulkCircuitsInstance_Type()
)
juniAtmBulkCircuitsInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniAtmBulkCircuitsInstance.setStatus("current")
_JuniAtmBulkCircuitsRowStatus_Type = RowStatus
_JuniAtmBulkCircuitsRowStatus_Object = MibTableColumn
juniAtmBulkCircuitsRowStatus = _JuniAtmBulkCircuitsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 2, 5, 1, 4),
    _JuniAtmBulkCircuitsRowStatus_Type()
)
juniAtmBulkCircuitsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAtmBulkCircuitsRowStatus.setStatus("current")
_JuniAtmBulkCircuitsMinVpi_Type = AtmVpIdentifier
_JuniAtmBulkCircuitsMinVpi_Object = MibTableColumn
juniAtmBulkCircuitsMinVpi = _JuniAtmBulkCircuitsMinVpi_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 2, 5, 1, 5),
    _JuniAtmBulkCircuitsMinVpi_Type()
)
juniAtmBulkCircuitsMinVpi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAtmBulkCircuitsMinVpi.setStatus("current")
_JuniAtmBulkCircuitsMaxVpi_Type = AtmVpIdentifier
_JuniAtmBulkCircuitsMaxVpi_Object = MibTableColumn
juniAtmBulkCircuitsMaxVpi = _JuniAtmBulkCircuitsMaxVpi_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 2, 5, 1, 6),
    _JuniAtmBulkCircuitsMaxVpi_Type()
)
juniAtmBulkCircuitsMaxVpi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAtmBulkCircuitsMaxVpi.setStatus("current")
_JuniAtmBulkCircuitsMinVci_Type = AtmVcIdentifier
_JuniAtmBulkCircuitsMinVci_Object = MibTableColumn
juniAtmBulkCircuitsMinVci = _JuniAtmBulkCircuitsMinVci_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 2, 5, 1, 7),
    _JuniAtmBulkCircuitsMinVci_Type()
)
juniAtmBulkCircuitsMinVci.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAtmBulkCircuitsMinVci.setStatus("current")
_JuniAtmBulkCircuitsMaxVci_Type = AtmVcIdentifier
_JuniAtmBulkCircuitsMaxVci_Object = MibTableColumn
juniAtmBulkCircuitsMaxVci = _JuniAtmBulkCircuitsMaxVci_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 2, 5, 1, 8),
    _JuniAtmBulkCircuitsMaxVci_Type()
)
juniAtmBulkCircuitsMaxVci.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAtmBulkCircuitsMaxVci.setStatus("current")


class _JuniAtmBulkCircuitsAdminState_Type(JuniEnable):
    """Custom type juniAtmBulkCircuitsAdminState based on JuniEnable"""


_JuniAtmBulkCircuitsAdminState_Object = MibTableColumn
juniAtmBulkCircuitsAdminState = _JuniAtmBulkCircuitsAdminState_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 2, 5, 1, 9),
    _JuniAtmBulkCircuitsAdminState_Type()
)
juniAtmBulkCircuitsAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAtmBulkCircuitsAdminState.setStatus("current")
_JuniAtmProfileOverrideAssignIfCircuitTable_Object = MibTable
juniAtmProfileOverrideAssignIfCircuitTable = _JuniAtmProfileOverrideAssignIfCircuitTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 2, 6)
)
if mibBuilder.loadTexts:
    juniAtmProfileOverrideAssignIfCircuitTable.setStatus("current")
_JuniAtmProfileOverrideAssignIfCircuitEntry_Object = MibTableRow
juniAtmProfileOverrideAssignIfCircuitEntry = _JuniAtmProfileOverrideAssignIfCircuitEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 2, 6, 1)
)
juniAtmProfileOverrideAssignIfCircuitEntry.setIndexNames(
    (0, "Juniper-UNI-ATM-MIB", "juniAtmProfileOverrideAssignIfCircuitAal5Index"),
    (0, "Juniper-UNI-ATM-MIB", "juniAtmProfileOverrideAssignIfCircuitRangeId"),
    (0, "Juniper-UNI-ATM-MIB", "juniAtmProfileOverrideAssignIfCircuitVpi"),
    (0, "Juniper-UNI-ATM-MIB", "juniAtmProfileOverrideAssignIfCircuitVci"),
)
if mibBuilder.loadTexts:
    juniAtmProfileOverrideAssignIfCircuitEntry.setStatus("current")
_JuniAtmProfileOverrideAssignIfCircuitAal5Index_Type = InterfaceIndex
_JuniAtmProfileOverrideAssignIfCircuitAal5Index_Object = MibTableColumn
juniAtmProfileOverrideAssignIfCircuitAal5Index = _JuniAtmProfileOverrideAssignIfCircuitAal5Index_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 2, 6, 1, 1),
    _JuniAtmProfileOverrideAssignIfCircuitAal5Index_Type()
)
juniAtmProfileOverrideAssignIfCircuitAal5Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniAtmProfileOverrideAssignIfCircuitAal5Index.setStatus("current")
_JuniAtmProfileOverrideAssignIfCircuitRangeId_Type = Unsigned32
_JuniAtmProfileOverrideAssignIfCircuitRangeId_Object = MibTableColumn
juniAtmProfileOverrideAssignIfCircuitRangeId = _JuniAtmProfileOverrideAssignIfCircuitRangeId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 2, 6, 1, 2),
    _JuniAtmProfileOverrideAssignIfCircuitRangeId_Type()
)
juniAtmProfileOverrideAssignIfCircuitRangeId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniAtmProfileOverrideAssignIfCircuitRangeId.setStatus("current")
_JuniAtmProfileOverrideAssignIfCircuitVpi_Type = AtmVpIdentifier
_JuniAtmProfileOverrideAssignIfCircuitVpi_Object = MibTableColumn
juniAtmProfileOverrideAssignIfCircuitVpi = _JuniAtmProfileOverrideAssignIfCircuitVpi_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 2, 6, 1, 3),
    _JuniAtmProfileOverrideAssignIfCircuitVpi_Type()
)
juniAtmProfileOverrideAssignIfCircuitVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniAtmProfileOverrideAssignIfCircuitVpi.setStatus("current")
_JuniAtmProfileOverrideAssignIfCircuitVci_Type = AtmVcIdentifier
_JuniAtmProfileOverrideAssignIfCircuitVci_Object = MibTableColumn
juniAtmProfileOverrideAssignIfCircuitVci = _JuniAtmProfileOverrideAssignIfCircuitVci_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 2, 6, 1, 4),
    _JuniAtmProfileOverrideAssignIfCircuitVci_Type()
)
juniAtmProfileOverrideAssignIfCircuitVci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniAtmProfileOverrideAssignIfCircuitVci.setStatus("current")
_JuniAtmProfileOverrideAssignIfCircuitRowStatus_Type = RowStatus
_JuniAtmProfileOverrideAssignIfCircuitRowStatus_Object = MibTableColumn
juniAtmProfileOverrideAssignIfCircuitRowStatus = _JuniAtmProfileOverrideAssignIfCircuitRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 2, 6, 1, 5),
    _JuniAtmProfileOverrideAssignIfCircuitRowStatus_Type()
)
juniAtmProfileOverrideAssignIfCircuitRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAtmProfileOverrideAssignIfCircuitRowStatus.setStatus("current")
_JuniAtmProfileOverrideAssignIfCircuitProfileId_Type = Unsigned32
_JuniAtmProfileOverrideAssignIfCircuitProfileId_Object = MibTableColumn
juniAtmProfileOverrideAssignIfCircuitProfileId = _JuniAtmProfileOverrideAssignIfCircuitProfileId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 2, 6, 1, 6),
    _JuniAtmProfileOverrideAssignIfCircuitProfileId_Type()
)
juniAtmProfileOverrideAssignIfCircuitProfileId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAtmProfileOverrideAssignIfCircuitProfileId.setStatus("current")


class _JuniAtmProfileOverrideAssignIfCircuitOperStatus_Type(Integer32):
    """Custom type juniAtmProfileOverrideAssignIfCircuitOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 0))
    )


_JuniAtmProfileOverrideAssignIfCircuitOperStatus_Type.__name__ = "Integer32"
_JuniAtmProfileOverrideAssignIfCircuitOperStatus_Object = MibTableColumn
juniAtmProfileOverrideAssignIfCircuitOperStatus = _JuniAtmProfileOverrideAssignIfCircuitOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 2, 6, 1, 7),
    _JuniAtmProfileOverrideAssignIfCircuitOperStatus_Type()
)
juniAtmProfileOverrideAssignIfCircuitOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAtmProfileOverrideAssignIfCircuitOperStatus.setStatus("current")
_JuniAtmSubIfLayer_ObjectIdentity = ObjectIdentity
juniAtmSubIfLayer = _JuniAtmSubIfLayer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3)
)
_JuniAtmSubIfNextIfIndex_Type = JuniNextIfIndex
_JuniAtmSubIfNextIfIndex_Object = MibScalar
juniAtmSubIfNextIfIndex = _JuniAtmSubIfNextIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 1),
    _JuniAtmSubIfNextIfIndex_Type()
)
juniAtmSubIfNextIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAtmSubIfNextIfIndex.setStatus("current")
_JuniAtmSubIfTable_Object = MibTable
juniAtmSubIfTable = _JuniAtmSubIfTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 2)
)
if mibBuilder.loadTexts:
    juniAtmSubIfTable.setStatus("current")
_JuniAtmSubIfEntry_Object = MibTableRow
juniAtmSubIfEntry = _JuniAtmSubIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 2, 1)
)
juniAtmSubIfEntry.setIndexNames(
    (0, "Juniper-UNI-ATM-MIB", "juniAtmSubIfIndex"),
)
if mibBuilder.loadTexts:
    juniAtmSubIfEntry.setStatus("current")
_JuniAtmSubIfIndex_Type = InterfaceIndex
_JuniAtmSubIfIndex_Object = MibTableColumn
juniAtmSubIfIndex = _JuniAtmSubIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 2, 1, 1),
    _JuniAtmSubIfIndex_Type()
)
juniAtmSubIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniAtmSubIfIndex.setStatus("current")
_JuniAtmSubIfRowStatus_Type = RowStatus
_JuniAtmSubIfRowStatus_Object = MibTableColumn
juniAtmSubIfRowStatus = _JuniAtmSubIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 2, 1, 2),
    _JuniAtmSubIfRowStatus_Type()
)
juniAtmSubIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAtmSubIfRowStatus.setStatus("current")


class _JuniAtmSubIfDistinguisher_Type(Integer32):
    """Custom type juniAtmSubIfDistinguisher based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JuniAtmSubIfDistinguisher_Type.__name__ = "Integer32"
_JuniAtmSubIfDistinguisher_Object = MibTableColumn
juniAtmSubIfDistinguisher = _JuniAtmSubIfDistinguisher_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 2, 1, 3),
    _JuniAtmSubIfDistinguisher_Type()
)
juniAtmSubIfDistinguisher.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAtmSubIfDistinguisher.setStatus("current")
_JuniAtmSubIfLowerIfIndex_Type = InterfaceIndexOrZero
_JuniAtmSubIfLowerIfIndex_Object = MibTableColumn
juniAtmSubIfLowerIfIndex = _JuniAtmSubIfLowerIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 2, 1, 4),
    _JuniAtmSubIfLowerIfIndex_Type()
)
juniAtmSubIfLowerIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAtmSubIfLowerIfIndex.setStatus("current")


class _JuniAtmSubIfNbma_Type(TruthValue):
    """Custom type juniAtmSubIfNbma based on TruthValue"""


_JuniAtmSubIfNbma_Object = MibTableColumn
juniAtmSubIfNbma = _JuniAtmSubIfNbma_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 2, 1, 5),
    _JuniAtmSubIfNbma_Type()
)
juniAtmSubIfNbma.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAtmSubIfNbma.setStatus("current")


class _JuniAtmSubIfAddress_Type(AtmAddr):
    """Custom type juniAtmSubIfAddress based on AtmAddr"""
    defaultHexValue = ""

    subtypeSpec = AtmAddr.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(7, 7),
        ValueSizeConstraint(20, 20),
    )


_JuniAtmSubIfAddress_Type.__name__ = "AtmAddr"
_JuniAtmSubIfAddress_Object = MibTableColumn
juniAtmSubIfAddress = _JuniAtmSubIfAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 2, 1, 6),
    _JuniAtmSubIfAddress_Type()
)
juniAtmSubIfAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAtmSubIfAddress.setStatus("deprecated")


class _JuniAtmSubIfMtu_Type(Integer32):
    """Custom type juniAtmSubIfMtu based on Integer32"""
    defaultValue = 9180

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JuniAtmSubIfMtu_Type.__name__ = "Integer32"
_JuniAtmSubIfMtu_Object = MibTableColumn
juniAtmSubIfMtu = _JuniAtmSubIfMtu_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 2, 1, 7),
    _JuniAtmSubIfMtu_Type()
)
juniAtmSubIfMtu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAtmSubIfMtu.setStatus("current")


class _JuniAtmSubIfAdvisoryRxSpeed_Type(Integer32):
    """Custom type juniAtmSubIfAdvisoryRxSpeed based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JuniAtmSubIfAdvisoryRxSpeed_Type.__name__ = "Integer32"
_JuniAtmSubIfAdvisoryRxSpeed_Object = MibTableColumn
juniAtmSubIfAdvisoryRxSpeed = _JuniAtmSubIfAdvisoryRxSpeed_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 2, 1, 8),
    _JuniAtmSubIfAdvisoryRxSpeed_Type()
)
juniAtmSubIfAdvisoryRxSpeed.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAtmSubIfAdvisoryRxSpeed.setStatus("current")


class _JuniAtmSubIfMartiniMaxCellsPerPacket_Type(Integer32):
    """Custom type juniAtmSubIfMartiniMaxCellsPerPacket based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 190),
    )


_JuniAtmSubIfMartiniMaxCellsPerPacket_Type.__name__ = "Integer32"
_JuniAtmSubIfMartiniMaxCellsPerPacket_Object = MibTableColumn
juniAtmSubIfMartiniMaxCellsPerPacket = _JuniAtmSubIfMartiniMaxCellsPerPacket_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 2, 1, 9),
    _JuniAtmSubIfMartiniMaxCellsPerPacket_Type()
)
juniAtmSubIfMartiniMaxCellsPerPacket.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAtmSubIfMartiniMaxCellsPerPacket.setStatus("current")


class _JuniAtmSubIfMartiniTimeoutTimerId_Type(Integer32):
    """Custom type juniAtmSubIfMartiniTimeoutTimerId based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_JuniAtmSubIfMartiniTimeoutTimerId_Type.__name__ = "Integer32"
_JuniAtmSubIfMartiniTimeoutTimerId_Object = MibTableColumn
juniAtmSubIfMartiniTimeoutTimerId = _JuniAtmSubIfMartiniTimeoutTimerId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 2, 1, 10),
    _JuniAtmSubIfMartiniTimeoutTimerId_Type()
)
juniAtmSubIfMartiniTimeoutTimerId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAtmSubIfMartiniTimeoutTimerId.setStatus("current")


class _JuniAtmSubIfAssociatedVcClassId_Type(Unsigned32):
    """Custom type juniAtmSubIfAssociatedVcClassId based on Unsigned32"""
    defaultValue = 0


_JuniAtmSubIfAssociatedVcClassId_Object = MibTableColumn
juniAtmSubIfAssociatedVcClassId = _JuniAtmSubIfAssociatedVcClassId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 2, 1, 11),
    _JuniAtmSubIfAssociatedVcClassId_Type()
)
juniAtmSubIfAssociatedVcClassId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAtmSubIfAssociatedVcClassId.setStatus("current")
_JuniAtmSubIfVccTable_Object = MibTable
juniAtmSubIfVccTable = _JuniAtmSubIfVccTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 3)
)
if mibBuilder.loadTexts:
    juniAtmSubIfVccTable.setStatus("current")
_JuniAtmSubIfVccEntry_Object = MibTableRow
juniAtmSubIfVccEntry = _JuniAtmSubIfVccEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 3, 1)
)
juniAtmSubIfVccEntry.setIndexNames(
    (0, "Juniper-UNI-ATM-MIB", "juniAtmSubIfIndex"),
    (0, "Juniper-UNI-ATM-MIB", "juniAtmSubIfVccVpi"),
    (0, "Juniper-UNI-ATM-MIB", "juniAtmSubIfVccVci"),
)
if mibBuilder.loadTexts:
    juniAtmSubIfVccEntry.setStatus("current")
_JuniAtmSubIfVccVpi_Type = AtmVpIdentifier
_JuniAtmSubIfVccVpi_Object = MibTableColumn
juniAtmSubIfVccVpi = _JuniAtmSubIfVccVpi_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 3, 1, 1),
    _JuniAtmSubIfVccVpi_Type()
)
juniAtmSubIfVccVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniAtmSubIfVccVpi.setStatus("current")
_JuniAtmSubIfVccVci_Type = AtmVcIdentifier
_JuniAtmSubIfVccVci_Object = MibTableColumn
juniAtmSubIfVccVci = _JuniAtmSubIfVccVci_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 3, 1, 2),
    _JuniAtmSubIfVccVci_Type()
)
juniAtmSubIfVccVci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniAtmSubIfVccVci.setStatus("current")
_JuniAtmSubIfVccRowStatus_Type = RowStatus
_JuniAtmSubIfVccRowStatus_Object = MibTableColumn
juniAtmSubIfVccRowStatus = _JuniAtmSubIfVccRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 3, 1, 3),
    _JuniAtmSubIfVccRowStatus_Type()
)
juniAtmSubIfVccRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAtmSubIfVccRowStatus.setStatus("current")


class _JuniAtmSubIfVccVcd_Type(Integer32):
    """Custom type juniAtmSubIfVccVcd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JuniAtmSubIfVccVcd_Type.__name__ = "Integer32"
_JuniAtmSubIfVccVcd_Object = MibTableColumn
juniAtmSubIfVccVcd = _JuniAtmSubIfVccVcd_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 3, 1, 4),
    _JuniAtmSubIfVccVcd_Type()
)
juniAtmSubIfVccVcd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAtmSubIfVccVcd.setStatus("current")


class _JuniAtmSubIfVccType_Type(Integer32):
    """Custom type juniAtmSubIfVccType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("aal0", 4),
          ("aal5", 3),
          ("autoconfig", 2),
          ("rfc1483Llc", 1),
          ("rfc1483VcMux", 0))
    )


_JuniAtmSubIfVccType_Type.__name__ = "Integer32"
_JuniAtmSubIfVccType_Object = MibTableColumn
juniAtmSubIfVccType = _JuniAtmSubIfVccType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 3, 1, 5),
    _JuniAtmSubIfVccType_Type()
)
juniAtmSubIfVccType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAtmSubIfVccType.setStatus("current")


class _JuniAtmSubIfVccServiceCategory_Type(Integer32):
    """Custom type juniAtmSubIfVccServiceCategory based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("cbr", 3),
          ("nrtVbr", 2),
          ("rtVbr", 4),
          ("ubr", 0),
          ("ubrPcr", 1))
    )


_JuniAtmSubIfVccServiceCategory_Type.__name__ = "Integer32"
_JuniAtmSubIfVccServiceCategory_Object = MibTableColumn
juniAtmSubIfVccServiceCategory = _JuniAtmSubIfVccServiceCategory_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 3, 1, 6),
    _JuniAtmSubIfVccServiceCategory_Type()
)
juniAtmSubIfVccServiceCategory.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAtmSubIfVccServiceCategory.setStatus("current")


class _JuniAtmSubIfVccPcr_Type(Integer32):
    """Custom type juniAtmSubIfVccPcr based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JuniAtmSubIfVccPcr_Type.__name__ = "Integer32"
_JuniAtmSubIfVccPcr_Object = MibTableColumn
juniAtmSubIfVccPcr = _JuniAtmSubIfVccPcr_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 3, 1, 7),
    _JuniAtmSubIfVccPcr_Type()
)
juniAtmSubIfVccPcr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAtmSubIfVccPcr.setStatus("current")
if mibBuilder.loadTexts:
    juniAtmSubIfVccPcr.setUnits("kbps")


class _JuniAtmSubIfVccScr_Type(Integer32):
    """Custom type juniAtmSubIfVccScr based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JuniAtmSubIfVccScr_Type.__name__ = "Integer32"
_JuniAtmSubIfVccScr_Object = MibTableColumn
juniAtmSubIfVccScr = _JuniAtmSubIfVccScr_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 3, 1, 8),
    _JuniAtmSubIfVccScr_Type()
)
juniAtmSubIfVccScr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAtmSubIfVccScr.setStatus("current")
if mibBuilder.loadTexts:
    juniAtmSubIfVccScr.setUnits("kbps")


class _JuniAtmSubIfVccMbs_Type(Integer32):
    """Custom type juniAtmSubIfVccMbs based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_JuniAtmSubIfVccMbs_Type.__name__ = "Integer32"
_JuniAtmSubIfVccMbs_Object = MibTableColumn
juniAtmSubIfVccMbs = _JuniAtmSubIfVccMbs_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 3, 1, 9),
    _JuniAtmSubIfVccMbs_Type()
)
juniAtmSubIfVccMbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAtmSubIfVccMbs.setStatus("current")
if mibBuilder.loadTexts:
    juniAtmSubIfVccMbs.setUnits("cells")
_JuniAtmSubIfInverseArp_Type = TruthValue
_JuniAtmSubIfInverseArp_Object = MibTableColumn
juniAtmSubIfInverseArp = _JuniAtmSubIfInverseArp_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 3, 1, 10),
    _JuniAtmSubIfInverseArp_Type()
)
juniAtmSubIfInverseArp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAtmSubIfInverseArp.setStatus("current")


class _JuniAtmSubIfInverseArpRefresh_Type(Integer32):
    """Custom type juniAtmSubIfInverseArpRefresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_JuniAtmSubIfInverseArpRefresh_Type.__name__ = "Integer32"
_JuniAtmSubIfInverseArpRefresh_Object = MibTableColumn
juniAtmSubIfInverseArpRefresh = _JuniAtmSubIfInverseArpRefresh_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 3, 1, 11),
    _JuniAtmSubIfInverseArpRefresh_Type()
)
juniAtmSubIfInverseArpRefresh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAtmSubIfInverseArpRefresh.setStatus("current")
if mibBuilder.loadTexts:
    juniAtmSubIfInverseArpRefresh.setUnits("minutes")


class _JuniAtmSubIfVccAssociatedVcClassId_Type(Unsigned32):
    """Custom type juniAtmSubIfVccAssociatedVcClassId based on Unsigned32"""
    defaultValue = 0


_JuniAtmSubIfVccAssociatedVcClassId_Object = MibTableColumn
juniAtmSubIfVccAssociatedVcClassId = _JuniAtmSubIfVccAssociatedVcClassId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 3, 1, 12),
    _JuniAtmSubIfVccAssociatedVcClassId_Type()
)
juniAtmSubIfVccAssociatedVcClassId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAtmSubIfVccAssociatedVcClassId.setStatus("current")
_JuniAtmCircuitOamTable_Object = MibTable
juniAtmCircuitOamTable = _JuniAtmCircuitOamTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 4)
)
if mibBuilder.loadTexts:
    juniAtmCircuitOamTable.setStatus("current")
_JuniAtmCircuitOamEntry_Object = MibTableRow
juniAtmCircuitOamEntry = _JuniAtmCircuitOamEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 4, 1)
)
juniAtmCircuitOamEntry.setIndexNames(
    (0, "Juniper-UNI-ATM-MIB", "juniAtmCircuitOamIfIndex"),
    (0, "Juniper-UNI-ATM-MIB", "juniAtmCircuitOamVpi"),
    (0, "Juniper-UNI-ATM-MIB", "juniAtmCircuitOamVci"),
)
if mibBuilder.loadTexts:
    juniAtmCircuitOamEntry.setStatus("current")
_JuniAtmCircuitOamIfIndex_Type = InterfaceIndex
_JuniAtmCircuitOamIfIndex_Object = MibTableColumn
juniAtmCircuitOamIfIndex = _JuniAtmCircuitOamIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 4, 1, 1),
    _JuniAtmCircuitOamIfIndex_Type()
)
juniAtmCircuitOamIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniAtmCircuitOamIfIndex.setStatus("current")
_JuniAtmCircuitOamVpi_Type = AtmVpIdentifier
_JuniAtmCircuitOamVpi_Object = MibTableColumn
juniAtmCircuitOamVpi = _JuniAtmCircuitOamVpi_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 4, 1, 2),
    _JuniAtmCircuitOamVpi_Type()
)
juniAtmCircuitOamVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniAtmCircuitOamVpi.setStatus("current")
_JuniAtmCircuitOamVci_Type = AtmVcIdentifier
_JuniAtmCircuitOamVci_Object = MibTableColumn
juniAtmCircuitOamVci = _JuniAtmCircuitOamVci_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 4, 1, 3),
    _JuniAtmCircuitOamVci_Type()
)
juniAtmCircuitOamVci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniAtmCircuitOamVci.setStatus("current")


class _JuniAtmCircuitOamAdminStatus_Type(Integer32):
    """Custom type juniAtmCircuitOamAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("oamAdminStateDisabled", 1),
          ("oamAdminStateEnabled", 2))
    )


_JuniAtmCircuitOamAdminStatus_Type.__name__ = "Integer32"
_JuniAtmCircuitOamAdminStatus_Object = MibTableColumn
juniAtmCircuitOamAdminStatus = _JuniAtmCircuitOamAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 4, 1, 4),
    _JuniAtmCircuitOamAdminStatus_Type()
)
juniAtmCircuitOamAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniAtmCircuitOamAdminStatus.setStatus("current")


class _JuniAtmCircuitOamLoopbackOperStatus_Type(Integer32):
    """Custom type juniAtmCircuitOamLoopbackOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("oamOperStatusDisabled", 1),
          ("oamOperStatusFailed", 4),
          ("oamOperStatusNotSupported", 0),
          ("oamOperStatusReceived", 3),
          ("oamOperStatusSent", 2))
    )


_JuniAtmCircuitOamLoopbackOperStatus_Type.__name__ = "Integer32"
_JuniAtmCircuitOamLoopbackOperStatus_Object = MibTableColumn
juniAtmCircuitOamLoopbackOperStatus = _JuniAtmCircuitOamLoopbackOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 4, 1, 5),
    _JuniAtmCircuitOamLoopbackOperStatus_Type()
)
juniAtmCircuitOamLoopbackOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAtmCircuitOamLoopbackOperStatus.setStatus("current")


class _JuniAtmCircuitVcOamOperStatus_Type(Integer32):
    """Custom type juniAtmCircuitVcOamOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("oamVcOperStateAisState", 0),
          ("oamVcOperStateDown", 5),
          ("oamVcOperStateDownRetry", 2),
          ("oamVcOperStateGenAis", 13),
          ("oamVcOperStateNotManaged", 6),
          ("oamVcOperStateRdiState", 1),
          ("oamVcOperStateSegAis", 11),
          ("oamVcOperStateSegRdi", 12),
          ("oamVcOperStateUp", 4),
          ("oamVcOperStateUpRetry", 3),
          ("oamVcOperStateVcInVpRdi", 9),
          ("oamVcOperStateVpAis", 7),
          ("oamVcOperStateVpRdi", 8),
          ("oamVcoperStateVcInVpAis", 10))
    )


_JuniAtmCircuitVcOamOperStatus_Type.__name__ = "Integer32"
_JuniAtmCircuitVcOamOperStatus_Object = MibTableColumn
juniAtmCircuitVcOamOperStatus = _JuniAtmCircuitVcOamOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 4, 1, 6),
    _JuniAtmCircuitVcOamOperStatus_Type()
)
juniAtmCircuitVcOamOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAtmCircuitVcOamOperStatus.setStatus("current")


class _JuniAtmCircuitOamLoopbackFrequency_Type(Integer32):
    """Custom type juniAtmCircuitOamLoopbackFrequency based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_JuniAtmCircuitOamLoopbackFrequency_Type.__name__ = "Integer32"
_JuniAtmCircuitOamLoopbackFrequency_Object = MibTableColumn
juniAtmCircuitOamLoopbackFrequency = _JuniAtmCircuitOamLoopbackFrequency_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 4, 1, 7),
    _JuniAtmCircuitOamLoopbackFrequency_Type()
)
juniAtmCircuitOamLoopbackFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniAtmCircuitOamLoopbackFrequency.setStatus("current")
if mibBuilder.loadTexts:
    juniAtmCircuitOamLoopbackFrequency.setUnits("seconds")
_JuniAtmCircuitInOamF5Cells_Type = Counter32
_JuniAtmCircuitInOamF5Cells_Object = MibTableColumn
juniAtmCircuitInOamF5Cells = _JuniAtmCircuitInOamF5Cells_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 4, 1, 8),
    _JuniAtmCircuitInOamF5Cells_Type()
)
juniAtmCircuitInOamF5Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAtmCircuitInOamF5Cells.setStatus("current")
if mibBuilder.loadTexts:
    juniAtmCircuitInOamF5Cells.setUnits("cells")
_JuniAtmCircuitInOamCellsDropped_Type = Counter32
_JuniAtmCircuitInOamCellsDropped_Object = MibTableColumn
juniAtmCircuitInOamCellsDropped = _JuniAtmCircuitInOamCellsDropped_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 4, 1, 9),
    _JuniAtmCircuitInOamCellsDropped_Type()
)
juniAtmCircuitInOamCellsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAtmCircuitInOamCellsDropped.setStatus("current")
if mibBuilder.loadTexts:
    juniAtmCircuitInOamCellsDropped.setUnits("cells")
_JuniAtmCircuitOutOamF5Cells_Type = Counter32
_JuniAtmCircuitOutOamF5Cells_Object = MibTableColumn
juniAtmCircuitOutOamF5Cells = _JuniAtmCircuitOutOamF5Cells_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 4, 1, 10),
    _JuniAtmCircuitOutOamF5Cells_Type()
)
juniAtmCircuitOutOamF5Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAtmCircuitOutOamF5Cells.setStatus("current")
if mibBuilder.loadTexts:
    juniAtmCircuitOutOamF5Cells.setUnits("cells")
_JuniAtmCircuitInOamF5EndToEndLoopbackCells_Type = Counter32
_JuniAtmCircuitInOamF5EndToEndLoopbackCells_Object = MibTableColumn
juniAtmCircuitInOamF5EndToEndLoopbackCells = _JuniAtmCircuitInOamF5EndToEndLoopbackCells_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 4, 1, 11),
    _JuniAtmCircuitInOamF5EndToEndLoopbackCells_Type()
)
juniAtmCircuitInOamF5EndToEndLoopbackCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAtmCircuitInOamF5EndToEndLoopbackCells.setStatus("current")
if mibBuilder.loadTexts:
    juniAtmCircuitInOamF5EndToEndLoopbackCells.setUnits("cells")
_JuniAtmCircuitInOamF5SegmentLoopbackCells_Type = Counter32
_JuniAtmCircuitInOamF5SegmentLoopbackCells_Object = MibTableColumn
juniAtmCircuitInOamF5SegmentLoopbackCells = _JuniAtmCircuitInOamF5SegmentLoopbackCells_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 4, 1, 12),
    _JuniAtmCircuitInOamF5SegmentLoopbackCells_Type()
)
juniAtmCircuitInOamF5SegmentLoopbackCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAtmCircuitInOamF5SegmentLoopbackCells.setStatus("current")
if mibBuilder.loadTexts:
    juniAtmCircuitInOamF5SegmentLoopbackCells.setUnits("cells")
_JuniAtmCircuitInOamF5AisCells_Type = Counter32
_JuniAtmCircuitInOamF5AisCells_Object = MibTableColumn
juniAtmCircuitInOamF5AisCells = _JuniAtmCircuitInOamF5AisCells_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 4, 1, 13),
    _JuniAtmCircuitInOamF5AisCells_Type()
)
juniAtmCircuitInOamF5AisCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAtmCircuitInOamF5AisCells.setStatus("current")
if mibBuilder.loadTexts:
    juniAtmCircuitInOamF5AisCells.setUnits("cells")
_JuniAtmCircuitInOamF5RdiCells_Type = Counter32
_JuniAtmCircuitInOamF5RdiCells_Object = MibTableColumn
juniAtmCircuitInOamF5RdiCells = _JuniAtmCircuitInOamF5RdiCells_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 4, 1, 14),
    _JuniAtmCircuitInOamF5RdiCells_Type()
)
juniAtmCircuitInOamF5RdiCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAtmCircuitInOamF5RdiCells.setStatus("current")
if mibBuilder.loadTexts:
    juniAtmCircuitInOamF5RdiCells.setUnits("cells")
_JuniAtmCircuitOutOamF5EndToEndLoopbackCells_Type = Counter32
_JuniAtmCircuitOutOamF5EndToEndLoopbackCells_Object = MibTableColumn
juniAtmCircuitOutOamF5EndToEndLoopbackCells = _JuniAtmCircuitOutOamF5EndToEndLoopbackCells_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 4, 1, 15),
    _JuniAtmCircuitOutOamF5EndToEndLoopbackCells_Type()
)
juniAtmCircuitOutOamF5EndToEndLoopbackCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAtmCircuitOutOamF5EndToEndLoopbackCells.setStatus("current")
if mibBuilder.loadTexts:
    juniAtmCircuitOutOamF5EndToEndLoopbackCells.setUnits("cells")
_JuniAtmCircuitOutOamF5SegmentLoopbackCells_Type = Counter32
_JuniAtmCircuitOutOamF5SegmentLoopbackCells_Object = MibTableColumn
juniAtmCircuitOutOamF5SegmentLoopbackCells = _JuniAtmCircuitOutOamF5SegmentLoopbackCells_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 4, 1, 16),
    _JuniAtmCircuitOutOamF5SegmentLoopbackCells_Type()
)
juniAtmCircuitOutOamF5SegmentLoopbackCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAtmCircuitOutOamF5SegmentLoopbackCells.setStatus("current")
if mibBuilder.loadTexts:
    juniAtmCircuitOutOamF5SegmentLoopbackCells.setUnits("cells")
_JuniAtmCircuitOutOamF5RdiCells_Type = Counter32
_JuniAtmCircuitOutOamF5RdiCells_Object = MibTableColumn
juniAtmCircuitOutOamF5RdiCells = _JuniAtmCircuitOutOamF5RdiCells_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 4, 1, 17),
    _JuniAtmCircuitOutOamF5RdiCells_Type()
)
juniAtmCircuitOutOamF5RdiCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAtmCircuitOutOamF5RdiCells.setStatus("current")
if mibBuilder.loadTexts:
    juniAtmCircuitOutOamF5RdiCells.setUnits("cells")
_JuniAtmCircuitInOamF5EndToEndLoopbackCmds_Type = Counter32
_JuniAtmCircuitInOamF5EndToEndLoopbackCmds_Object = MibTableColumn
juniAtmCircuitInOamF5EndToEndLoopbackCmds = _JuniAtmCircuitInOamF5EndToEndLoopbackCmds_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 4, 1, 18),
    _JuniAtmCircuitInOamF5EndToEndLoopbackCmds_Type()
)
juniAtmCircuitInOamF5EndToEndLoopbackCmds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAtmCircuitInOamF5EndToEndLoopbackCmds.setStatus("current")
if mibBuilder.loadTexts:
    juniAtmCircuitInOamF5EndToEndLoopbackCmds.setUnits("cells")
_JuniAtmCircuitInOamF5EndToEndLoopbackRsps_Type = Counter32
_JuniAtmCircuitInOamF5EndToEndLoopbackRsps_Object = MibTableColumn
juniAtmCircuitInOamF5EndToEndLoopbackRsps = _JuniAtmCircuitInOamF5EndToEndLoopbackRsps_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 4, 1, 19),
    _JuniAtmCircuitInOamF5EndToEndLoopbackRsps_Type()
)
juniAtmCircuitInOamF5EndToEndLoopbackRsps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAtmCircuitInOamF5EndToEndLoopbackRsps.setStatus("current")
if mibBuilder.loadTexts:
    juniAtmCircuitInOamF5EndToEndLoopbackRsps.setUnits("cells")
_JuniAtmCircuitInOamF5SegmentLoopbackCmds_Type = Counter32
_JuniAtmCircuitInOamF5SegmentLoopbackCmds_Object = MibTableColumn
juniAtmCircuitInOamF5SegmentLoopbackCmds = _JuniAtmCircuitInOamF5SegmentLoopbackCmds_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 4, 1, 20),
    _JuniAtmCircuitInOamF5SegmentLoopbackCmds_Type()
)
juniAtmCircuitInOamF5SegmentLoopbackCmds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAtmCircuitInOamF5SegmentLoopbackCmds.setStatus("current")
if mibBuilder.loadTexts:
    juniAtmCircuitInOamF5SegmentLoopbackCmds.setUnits("cells")
_JuniAtmCircuitInOamF5SegmentLoopbackRsps_Type = Counter32
_JuniAtmCircuitInOamF5SegmentLoopbackRsps_Object = MibTableColumn
juniAtmCircuitInOamF5SegmentLoopbackRsps = _JuniAtmCircuitInOamF5SegmentLoopbackRsps_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 4, 1, 21),
    _JuniAtmCircuitInOamF5SegmentLoopbackRsps_Type()
)
juniAtmCircuitInOamF5SegmentLoopbackRsps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAtmCircuitInOamF5SegmentLoopbackRsps.setStatus("current")
if mibBuilder.loadTexts:
    juniAtmCircuitInOamF5SegmentLoopbackRsps.setUnits("cells")
_JuniAtmCircuitOutOamF5EndToEndLoopbackCmds_Type = Counter32
_JuniAtmCircuitOutOamF5EndToEndLoopbackCmds_Object = MibTableColumn
juniAtmCircuitOutOamF5EndToEndLoopbackCmds = _JuniAtmCircuitOutOamF5EndToEndLoopbackCmds_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 4, 1, 22),
    _JuniAtmCircuitOutOamF5EndToEndLoopbackCmds_Type()
)
juniAtmCircuitOutOamF5EndToEndLoopbackCmds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAtmCircuitOutOamF5EndToEndLoopbackCmds.setStatus("current")
if mibBuilder.loadTexts:
    juniAtmCircuitOutOamF5EndToEndLoopbackCmds.setUnits("cells")
_JuniAtmCircuitOutOamF5EndToEndLoopbackRsps_Type = Counter32
_JuniAtmCircuitOutOamF5EndToEndLoopbackRsps_Object = MibTableColumn
juniAtmCircuitOutOamF5EndToEndLoopbackRsps = _JuniAtmCircuitOutOamF5EndToEndLoopbackRsps_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 4, 1, 23),
    _JuniAtmCircuitOutOamF5EndToEndLoopbackRsps_Type()
)
juniAtmCircuitOutOamF5EndToEndLoopbackRsps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAtmCircuitOutOamF5EndToEndLoopbackRsps.setStatus("current")
if mibBuilder.loadTexts:
    juniAtmCircuitOutOamF5EndToEndLoopbackRsps.setUnits("cells")
_JuniAtmCircuitOutOamF5SegmentLoopbackCmds_Type = Counter32
_JuniAtmCircuitOutOamF5SegmentLoopbackCmds_Object = MibTableColumn
juniAtmCircuitOutOamF5SegmentLoopbackCmds = _JuniAtmCircuitOutOamF5SegmentLoopbackCmds_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 4, 1, 24),
    _JuniAtmCircuitOutOamF5SegmentLoopbackCmds_Type()
)
juniAtmCircuitOutOamF5SegmentLoopbackCmds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAtmCircuitOutOamF5SegmentLoopbackCmds.setStatus("current")
if mibBuilder.loadTexts:
    juniAtmCircuitOutOamF5SegmentLoopbackCmds.setUnits("cells")
_JuniAtmCircuitOutOamF5SegmentLoopbackRsps_Type = Counter32
_JuniAtmCircuitOutOamF5SegmentLoopbackRsps_Object = MibTableColumn
juniAtmCircuitOutOamF5SegmentLoopbackRsps = _JuniAtmCircuitOutOamF5SegmentLoopbackRsps_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 4, 1, 25),
    _JuniAtmCircuitOutOamF5SegmentLoopbackRsps_Type()
)
juniAtmCircuitOutOamF5SegmentLoopbackRsps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAtmCircuitOutOamF5SegmentLoopbackRsps.setStatus("current")
if mibBuilder.loadTexts:
    juniAtmCircuitOutOamF5SegmentLoopbackRsps.setUnits("cells")


class _JuniAtmCircuitOamUpCount_Type(Integer32):
    """Custom type juniAtmCircuitOamUpCount based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_JuniAtmCircuitOamUpCount_Type.__name__ = "Integer32"
_JuniAtmCircuitOamUpCount_Object = MibTableColumn
juniAtmCircuitOamUpCount = _JuniAtmCircuitOamUpCount_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 4, 1, 26),
    _JuniAtmCircuitOamUpCount_Type()
)
juniAtmCircuitOamUpCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniAtmCircuitOamUpCount.setStatus("current")
if mibBuilder.loadTexts:
    juniAtmCircuitOamUpCount.setUnits("cells")


class _JuniAtmCircuitOamDownCount_Type(Integer32):
    """Custom type juniAtmCircuitOamDownCount based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_JuniAtmCircuitOamDownCount_Type.__name__ = "Integer32"
_JuniAtmCircuitOamDownCount_Object = MibTableColumn
juniAtmCircuitOamDownCount = _JuniAtmCircuitOamDownCount_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 4, 1, 27),
    _JuniAtmCircuitOamDownCount_Type()
)
juniAtmCircuitOamDownCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniAtmCircuitOamDownCount.setStatus("current")
if mibBuilder.loadTexts:
    juniAtmCircuitOamDownCount.setUnits("cells")


class _JuniAtmCircuitOamRetryFrequency_Type(Integer32):
    """Custom type juniAtmCircuitOamRetryFrequency based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_JuniAtmCircuitOamRetryFrequency_Type.__name__ = "Integer32"
_JuniAtmCircuitOamRetryFrequency_Object = MibTableColumn
juniAtmCircuitOamRetryFrequency = _JuniAtmCircuitOamRetryFrequency_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 4, 1, 28),
    _JuniAtmCircuitOamRetryFrequency_Type()
)
juniAtmCircuitOamRetryFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniAtmCircuitOamRetryFrequency.setStatus("current")
if mibBuilder.loadTexts:
    juniAtmCircuitOamRetryFrequency.setUnits("seconds")


class _JuniAtmCircuitOamAlarmDownCount_Type(Integer32):
    """Custom type juniAtmCircuitOamAlarmDownCount based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_JuniAtmCircuitOamAlarmDownCount_Type.__name__ = "Integer32"
_JuniAtmCircuitOamAlarmDownCount_Object = MibTableColumn
juniAtmCircuitOamAlarmDownCount = _JuniAtmCircuitOamAlarmDownCount_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 4, 1, 29),
    _JuniAtmCircuitOamAlarmDownCount_Type()
)
juniAtmCircuitOamAlarmDownCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniAtmCircuitOamAlarmDownCount.setStatus("current")
if mibBuilder.loadTexts:
    juniAtmCircuitOamAlarmDownCount.setUnits("cells")


class _JuniAtmCircuitOamAlarmClearTimeout_Type(Integer32):
    """Custom type juniAtmCircuitOamAlarmClearTimeout based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 60),
    )


_JuniAtmCircuitOamAlarmClearTimeout_Type.__name__ = "Integer32"
_JuniAtmCircuitOamAlarmClearTimeout_Object = MibTableColumn
juniAtmCircuitOamAlarmClearTimeout = _JuniAtmCircuitOamAlarmClearTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 4, 1, 30),
    _JuniAtmCircuitOamAlarmClearTimeout_Type()
)
juniAtmCircuitOamAlarmClearTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniAtmCircuitOamAlarmClearTimeout.setStatus("current")
if mibBuilder.loadTexts:
    juniAtmCircuitOamAlarmClearTimeout.setUnits("seconds")
_JuniAtmSubIfVccTrafficShapingTable_Object = MibTable
juniAtmSubIfVccTrafficShapingTable = _JuniAtmSubIfVccTrafficShapingTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 5)
)
if mibBuilder.loadTexts:
    juniAtmSubIfVccTrafficShapingTable.setStatus("current")
_JuniAtmSubIfVccTrafficShapingEntry_Object = MibTableRow
juniAtmSubIfVccTrafficShapingEntry = _JuniAtmSubIfVccTrafficShapingEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 5, 1)
)
if mibBuilder.loadTexts:
    juniAtmSubIfVccTrafficShapingEntry.setStatus("current")
_JuniAtmSubIfVccTrafficShapingCdvt_Type = Unsigned32
_JuniAtmSubIfVccTrafficShapingCdvt_Object = MibTableColumn
juniAtmSubIfVccTrafficShapingCdvt = _JuniAtmSubIfVccTrafficShapingCdvt_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 5, 1, 1),
    _JuniAtmSubIfVccTrafficShapingCdvt_Type()
)
juniAtmSubIfVccTrafficShapingCdvt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAtmSubIfVccTrafficShapingCdvt.setStatus("current")
if mibBuilder.loadTexts:
    juniAtmSubIfVccTrafficShapingCdvt.setUnits("tenths of a microsecond")
_JuniAtmSubIfVccTrafficShapingClp0_Type = TruthValue
_JuniAtmSubIfVccTrafficShapingClp0_Object = MibTableColumn
juniAtmSubIfVccTrafficShapingClp0 = _JuniAtmSubIfVccTrafficShapingClp0_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 5, 1, 2),
    _JuniAtmSubIfVccTrafficShapingClp0_Type()
)
juniAtmSubIfVccTrafficShapingClp0.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAtmSubIfVccTrafficShapingClp0.setStatus("current")
_JuniAtmSubIfVccTrafficShapingTagging_Type = TruthValue
_JuniAtmSubIfVccTrafficShapingTagging_Object = MibTableColumn
juniAtmSubIfVccTrafficShapingTagging = _JuniAtmSubIfVccTrafficShapingTagging_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 5, 1, 3),
    _JuniAtmSubIfVccTrafficShapingTagging_Type()
)
juniAtmSubIfVccTrafficShapingTagging.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAtmSubIfVccTrafficShapingTagging.setStatus("current")
_JuniAtmSubIfVccTrafficShapingPoliceObserve_Type = TruthValue
_JuniAtmSubIfVccTrafficShapingPoliceObserve_Object = MibTableColumn
juniAtmSubIfVccTrafficShapingPoliceObserve = _JuniAtmSubIfVccTrafficShapingPoliceObserve_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 5, 1, 4),
    _JuniAtmSubIfVccTrafficShapingPoliceObserve_Type()
)
juniAtmSubIfVccTrafficShapingPoliceObserve.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAtmSubIfVccTrafficShapingPoliceObserve.setStatus("current")
_JuniAtmSubIfVccTrafficShapingPacketShaping_Type = TruthValue
_JuniAtmSubIfVccTrafficShapingPacketShaping_Object = MibTableColumn
juniAtmSubIfVccTrafficShapingPacketShaping = _JuniAtmSubIfVccTrafficShapingPacketShaping_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 5, 1, 5),
    _JuniAtmSubIfVccTrafficShapingPacketShaping_Type()
)
juniAtmSubIfVccTrafficShapingPacketShaping.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAtmSubIfVccTrafficShapingPacketShaping.setStatus("current")
_JuniAtmSubIfSvcConfigTable_Object = MibTable
juniAtmSubIfSvcConfigTable = _JuniAtmSubIfSvcConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 6)
)
if mibBuilder.loadTexts:
    juniAtmSubIfSvcConfigTable.setStatus("deprecated")
_JuniAtmSubIfSvcConfigEntry_Object = MibTableRow
juniAtmSubIfSvcConfigEntry = _JuniAtmSubIfSvcConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 6, 1)
)
juniAtmSubIfSvcConfigEntry.setIndexNames(
    (0, "Juniper-UNI-ATM-MIB", "juniAtmSubIfIndex"),
)
if mibBuilder.loadTexts:
    juniAtmSubIfSvcConfigEntry.setStatus("deprecated")
_JuniAtmSubIfSvcRowStatus_Type = RowStatus
_JuniAtmSubIfSvcRowStatus_Object = MibTableColumn
juniAtmSubIfSvcRowStatus = _JuniAtmSubIfSvcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 6, 1, 1),
    _JuniAtmSubIfSvcRowStatus_Type()
)
juniAtmSubIfSvcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAtmSubIfSvcRowStatus.setStatus("deprecated")


class _JuniAtmSubIfSvcConfigDestAtmAddress_Type(AtmAddr):
    """Custom type juniAtmSubIfSvcConfigDestAtmAddress based on AtmAddr"""
    subtypeSpec = AtmAddr.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_JuniAtmSubIfSvcConfigDestAtmAddress_Type.__name__ = "AtmAddr"
_JuniAtmSubIfSvcConfigDestAtmAddress_Object = MibTableColumn
juniAtmSubIfSvcConfigDestAtmAddress = _JuniAtmSubIfSvcConfigDestAtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 6, 1, 2),
    _JuniAtmSubIfSvcConfigDestAtmAddress_Type()
)
juniAtmSubIfSvcConfigDestAtmAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAtmSubIfSvcConfigDestAtmAddress.setStatus("deprecated")


class _JuniAtmSubIfSvcConfigCircuitType_Type(Integer32):
    """Custom type juniAtmSubIfSvcConfigCircuitType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("rfc1483Llc", 1),
          ("rfc1483VcMux", 0))
    )


_JuniAtmSubIfSvcConfigCircuitType_Type.__name__ = "Integer32"
_JuniAtmSubIfSvcConfigCircuitType_Object = MibTableColumn
juniAtmSubIfSvcConfigCircuitType = _JuniAtmSubIfSvcConfigCircuitType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 6, 1, 3),
    _JuniAtmSubIfSvcConfigCircuitType_Type()
)
juniAtmSubIfSvcConfigCircuitType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAtmSubIfSvcConfigCircuitType.setStatus("deprecated")


class _JuniAtmSubIfSvcConfigServiceCategory_Type(Integer32):
    """Custom type juniAtmSubIfSvcConfigServiceCategory based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("cbr", 3),
          ("nrtVbr", 2),
          ("rtVbr", 4),
          ("ubr", 0),
          ("ubrPcr", 1))
    )


_JuniAtmSubIfSvcConfigServiceCategory_Type.__name__ = "Integer32"
_JuniAtmSubIfSvcConfigServiceCategory_Object = MibTableColumn
juniAtmSubIfSvcConfigServiceCategory = _JuniAtmSubIfSvcConfigServiceCategory_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 6, 1, 4),
    _JuniAtmSubIfSvcConfigServiceCategory_Type()
)
juniAtmSubIfSvcConfigServiceCategory.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAtmSubIfSvcConfigServiceCategory.setStatus("deprecated")


class _JuniAtmSubIfSvcConfigPcr_Type(Unsigned32):
    """Custom type juniAtmSubIfSvcConfigPcr based on Unsigned32"""
    defaultValue = 0


_JuniAtmSubIfSvcConfigPcr_Object = MibTableColumn
juniAtmSubIfSvcConfigPcr = _JuniAtmSubIfSvcConfigPcr_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 6, 1, 5),
    _JuniAtmSubIfSvcConfigPcr_Type()
)
juniAtmSubIfSvcConfigPcr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAtmSubIfSvcConfigPcr.setStatus("deprecated")
if mibBuilder.loadTexts:
    juniAtmSubIfSvcConfigPcr.setUnits("kbps")


class _JuniAtmSubIfSvcConfigScr_Type(Unsigned32):
    """Custom type juniAtmSubIfSvcConfigScr based on Unsigned32"""
    defaultValue = 0


_JuniAtmSubIfSvcConfigScr_Object = MibTableColumn
juniAtmSubIfSvcConfigScr = _JuniAtmSubIfSvcConfigScr_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 6, 1, 6),
    _JuniAtmSubIfSvcConfigScr_Type()
)
juniAtmSubIfSvcConfigScr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAtmSubIfSvcConfigScr.setStatus("deprecated")
if mibBuilder.loadTexts:
    juniAtmSubIfSvcConfigScr.setUnits("kbps")


class _JuniAtmSubIfSvcConfigMbs_Type(Unsigned32):
    """Custom type juniAtmSubIfSvcConfigMbs based on Unsigned32"""
    defaultValue = 0


_JuniAtmSubIfSvcConfigMbs_Object = MibTableColumn
juniAtmSubIfSvcConfigMbs = _JuniAtmSubIfSvcConfigMbs_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 6, 1, 7),
    _JuniAtmSubIfSvcConfigMbs_Type()
)
juniAtmSubIfSvcConfigMbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAtmSubIfSvcConfigMbs.setStatus("deprecated")
if mibBuilder.loadTexts:
    juniAtmSubIfSvcConfigMbs.setUnits("cells")
_JuniAtmSubIfSvcConfigCdvt_Type = Unsigned32
_JuniAtmSubIfSvcConfigCdvt_Object = MibTableColumn
juniAtmSubIfSvcConfigCdvt = _JuniAtmSubIfSvcConfigCdvt_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 6, 1, 8),
    _JuniAtmSubIfSvcConfigCdvt_Type()
)
juniAtmSubIfSvcConfigCdvt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAtmSubIfSvcConfigCdvt.setStatus("obsolete")
if mibBuilder.loadTexts:
    juniAtmSubIfSvcConfigCdvt.setUnits("100us")
_JuniAtmSubIfSvcConfigClp0_Type = TruthValue
_JuniAtmSubIfSvcConfigClp0_Object = MibTableColumn
juniAtmSubIfSvcConfigClp0 = _JuniAtmSubIfSvcConfigClp0_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 6, 1, 9),
    _JuniAtmSubIfSvcConfigClp0_Type()
)
juniAtmSubIfSvcConfigClp0.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAtmSubIfSvcConfigClp0.setStatus("deprecated")
_JuniAtmSubIfSvcConfigTagging_Type = TruthValue
_JuniAtmSubIfSvcConfigTagging_Object = MibTableColumn
juniAtmSubIfSvcConfigTagging = _JuniAtmSubIfSvcConfigTagging_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 6, 1, 10),
    _JuniAtmSubIfSvcConfigTagging_Type()
)
juniAtmSubIfSvcConfigTagging.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAtmSubIfSvcConfigTagging.setStatus("deprecated")
_JuniAtmSubIfSvcConfigObserve_Type = TruthValue
_JuniAtmSubIfSvcConfigObserve_Object = MibTableColumn
juniAtmSubIfSvcConfigObserve = _JuniAtmSubIfSvcConfigObserve_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 6, 1, 11),
    _JuniAtmSubIfSvcConfigObserve_Type()
)
juniAtmSubIfSvcConfigObserve.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAtmSubIfSvcConfigObserve.setStatus("obsolete")
_JuniAtmSubIfSvcConfigPacketDiscard_Type = TruthValue
_JuniAtmSubIfSvcConfigPacketDiscard_Object = MibTableColumn
juniAtmSubIfSvcConfigPacketDiscard = _JuniAtmSubIfSvcConfigPacketDiscard_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 6, 1, 12),
    _JuniAtmSubIfSvcConfigPacketDiscard_Type()
)
juniAtmSubIfSvcConfigPacketDiscard.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAtmSubIfSvcConfigPacketDiscard.setStatus("deprecated")


class _JuniAtmSubIfSvcConfigDestE164Address_Type(AtmAddr):
    """Custom type juniAtmSubIfSvcConfigDestE164Address based on AtmAddr"""
    subtypeSpec = AtmAddr.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(8, 8),
    )


_JuniAtmSubIfSvcConfigDestE164Address_Type.__name__ = "AtmAddr"
_JuniAtmSubIfSvcConfigDestE164Address_Object = MibTableColumn
juniAtmSubIfSvcConfigDestE164Address = _JuniAtmSubIfSvcConfigDestE164Address_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 6, 1, 13),
    _JuniAtmSubIfSvcConfigDestE164Address_Type()
)
juniAtmSubIfSvcConfigDestE164Address.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAtmSubIfSvcConfigDestE164Address.setStatus("obsolete")


class _JuniAtmSubIfDescriptionExport_Type(TruthValue):
    """Custom type juniAtmSubIfDescriptionExport based on TruthValue"""


_JuniAtmSubIfDescriptionExport_Object = MibScalar
juniAtmSubIfDescriptionExport = _JuniAtmSubIfDescriptionExport_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 3, 7),
    _JuniAtmSubIfDescriptionExport_Type()
)
juniAtmSubIfDescriptionExport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniAtmSubIfDescriptionExport.setStatus("current")
_JuniAtmNbma_ObjectIdentity = ObjectIdentity
juniAtmNbma = _JuniAtmNbma_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 4)
)
_JuniAtmNbmaMapTable_Object = MibTable
juniAtmNbmaMapTable = _JuniAtmNbmaMapTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 4, 1)
)
if mibBuilder.loadTexts:
    juniAtmNbmaMapTable.setStatus("current")
_JuniAtmNbmaMapEntry_Object = MibTableRow
juniAtmNbmaMapEntry = _JuniAtmNbmaMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 4, 1, 1)
)
juniAtmNbmaMapEntry.setIndexNames(
    (0, "Juniper-UNI-ATM-MIB", "juniAtmNbmaMapName"),
    (0, "Juniper-UNI-ATM-MIB", "juniAtmNbmaMapVcd"),
)
if mibBuilder.loadTexts:
    juniAtmNbmaMapEntry.setStatus("current")
_JuniAtmNbmaMapName_Type = JuniAtmNbmaMapName
_JuniAtmNbmaMapName_Object = MibTableColumn
juniAtmNbmaMapName = _JuniAtmNbmaMapName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 4, 1, 1, 1),
    _JuniAtmNbmaMapName_Type()
)
juniAtmNbmaMapName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniAtmNbmaMapName.setStatus("current")


class _JuniAtmNbmaMapVcd_Type(Integer32):
    """Custom type juniAtmNbmaMapVcd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JuniAtmNbmaMapVcd_Type.__name__ = "Integer32"
_JuniAtmNbmaMapVcd_Object = MibTableColumn
juniAtmNbmaMapVcd = _JuniAtmNbmaMapVcd_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 4, 1, 1, 2),
    _JuniAtmNbmaMapVcd_Type()
)
juniAtmNbmaMapVcd.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniAtmNbmaMapVcd.setStatus("current")
_JuniAtmNbmaMapIpAddress_Type = IpAddress
_JuniAtmNbmaMapIpAddress_Object = MibTableColumn
juniAtmNbmaMapIpAddress = _JuniAtmNbmaMapIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 4, 1, 1, 3),
    _JuniAtmNbmaMapIpAddress_Type()
)
juniAtmNbmaMapIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAtmNbmaMapIpAddress.setStatus("current")
_JuniAtmNbmaMapVpi_Type = AtmVpIdentifier
_JuniAtmNbmaMapVpi_Object = MibTableColumn
juniAtmNbmaMapVpi = _JuniAtmNbmaMapVpi_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 4, 1, 1, 4),
    _JuniAtmNbmaMapVpi_Type()
)
juniAtmNbmaMapVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAtmNbmaMapVpi.setStatus("current")
_JuniAtmNbmaMapVci_Type = AtmVcIdentifier
_JuniAtmNbmaMapVci_Object = MibTableColumn
juniAtmNbmaMapVci = _JuniAtmNbmaMapVci_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 4, 1, 1, 5),
    _JuniAtmNbmaMapVci_Type()
)
juniAtmNbmaMapVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAtmNbmaMapVci.setStatus("current")
_JuniAtmNbmaMapIfIndex_Type = InterfaceIndexOrZero
_JuniAtmNbmaMapIfIndex_Object = MibTableColumn
juniAtmNbmaMapIfIndex = _JuniAtmNbmaMapIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 4, 1, 1, 6),
    _JuniAtmNbmaMapIfIndex_Type()
)
juniAtmNbmaMapIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAtmNbmaMapIfIndex.setStatus("current")
_JuniAtmNbmaMapBroadcast_Type = TruthValue
_JuniAtmNbmaMapBroadcast_Object = MibTableColumn
juniAtmNbmaMapBroadcast = _JuniAtmNbmaMapBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 4, 1, 1, 7),
    _JuniAtmNbmaMapBroadcast_Type()
)
juniAtmNbmaMapBroadcast.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAtmNbmaMapBroadcast.setStatus("current")
_JuniAtmNbmaMapRowStatus_Type = RowStatus
_JuniAtmNbmaMapRowStatus_Object = MibTableColumn
juniAtmNbmaMapRowStatus = _JuniAtmNbmaMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 4, 1, 1, 8),
    _JuniAtmNbmaMapRowStatus_Type()
)
juniAtmNbmaMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAtmNbmaMapRowStatus.setStatus("current")
_JuniAtmNbmaMapListTable_Object = MibTable
juniAtmNbmaMapListTable = _JuniAtmNbmaMapListTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 4, 2)
)
if mibBuilder.loadTexts:
    juniAtmNbmaMapListTable.setStatus("current")
_JuniAtmNbmaMapListEntry_Object = MibTableRow
juniAtmNbmaMapListEntry = _JuniAtmNbmaMapListEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 4, 2, 1)
)
juniAtmNbmaMapListEntry.setIndexNames(
    (1, "Juniper-UNI-ATM-MIB", "juniAtmNbmaMapListName"),
)
if mibBuilder.loadTexts:
    juniAtmNbmaMapListEntry.setStatus("current")
_JuniAtmNbmaMapListName_Type = JuniAtmNbmaMapName
_JuniAtmNbmaMapListName_Object = MibTableColumn
juniAtmNbmaMapListName = _JuniAtmNbmaMapListName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 4, 2, 1, 1),
    _JuniAtmNbmaMapListName_Type()
)
juniAtmNbmaMapListName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniAtmNbmaMapListName.setStatus("current")
_JuniAtmNbmaMapListRowStatus_Type = RowStatus
_JuniAtmNbmaMapListRowStatus_Object = MibTableColumn
juniAtmNbmaMapListRowStatus = _JuniAtmNbmaMapListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 4, 2, 1, 2),
    _JuniAtmNbmaMapListRowStatus_Type()
)
juniAtmNbmaMapListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAtmNbmaMapListRowStatus.setStatus("current")
_JuniAtmPing_ObjectIdentity = ObjectIdentity
juniAtmPing = _JuniAtmPing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 5)
)
_JuniAtmPingTestTypes_ObjectIdentity = ObjectIdentity
juniAtmPingTestTypes = _JuniAtmPingTestTypes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 5, 1)
)
_JuniAtmPingTestOamSeg_ObjectIdentity = ObjectIdentity
juniAtmPingTestOamSeg = _JuniAtmPingTestOamSeg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 5, 1, 1)
)
if mibBuilder.loadTexts:
    juniAtmPingTestOamSeg.setStatus("current")
_JuniAtmPingTestOamE2E_ObjectIdentity = ObjectIdentity
juniAtmPingTestOamE2E = _JuniAtmPingTestOamE2E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 5, 1, 2)
)
if mibBuilder.loadTexts:
    juniAtmPingTestOamE2E.setStatus("current")
_JuniAtmVpPingTable_Object = MibTable
juniAtmVpPingTable = _JuniAtmVpPingTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 5, 2)
)
if mibBuilder.loadTexts:
    juniAtmVpPingTable.setStatus("current")
_JuniAtmVpPingEntry_Object = MibTableRow
juniAtmVpPingEntry = _JuniAtmVpPingEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 5, 2, 1)
)
juniAtmVpPingEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ATM-MIB", "atmVplVpi"),
    (0, "ATM-FORUM-SNMP-M4-MIB", "atmfM4VpTestObject"),
)
if mibBuilder.loadTexts:
    juniAtmVpPingEntry.setStatus("current")


class _JuniAtmVpPingProbeCount_Type(Unsigned32):
    """Custom type juniAtmVpPingProbeCount based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_JuniAtmVpPingProbeCount_Type.__name__ = "Unsigned32"
_JuniAtmVpPingProbeCount_Object = MibTableColumn
juniAtmVpPingProbeCount = _JuniAtmVpPingProbeCount_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 5, 2, 1, 1),
    _JuniAtmVpPingProbeCount_Type()
)
juniAtmVpPingProbeCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniAtmVpPingProbeCount.setStatus("current")
if mibBuilder.loadTexts:
    juniAtmVpPingProbeCount.setUnits("probes")


class _JuniAtmVpPingTimeOut_Type(Unsigned32):
    """Custom type juniAtmVpPingTimeOut based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_JuniAtmVpPingTimeOut_Type.__name__ = "Unsigned32"
_JuniAtmVpPingTimeOut_Object = MibTableColumn
juniAtmVpPingTimeOut = _JuniAtmVpPingTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 5, 2, 1, 2),
    _JuniAtmVpPingTimeOut_Type()
)
juniAtmVpPingTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniAtmVpPingTimeOut.setStatus("current")
if mibBuilder.loadTexts:
    juniAtmVpPingTimeOut.setUnits("seconds")


class _JuniAtmVpPingCtlTrapGeneration_Type(Bits):
    """Custom type juniAtmVpPingCtlTrapGeneration based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        ("testCompletion", 0)
    )

_JuniAtmVpPingCtlTrapGeneration_Type.__name__ = "Bits"
_JuniAtmVpPingCtlTrapGeneration_Object = MibTableColumn
juniAtmVpPingCtlTrapGeneration = _JuniAtmVpPingCtlTrapGeneration_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 5, 2, 1, 3),
    _JuniAtmVpPingCtlTrapGeneration_Type()
)
juniAtmVpPingCtlTrapGeneration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniAtmVpPingCtlTrapGeneration.setStatus("current")


class _JuniAtmVpPingSentProbes_Type(Unsigned32):
    """Custom type juniAtmVpPingSentProbes based on Unsigned32"""
    defaultValue = 0


_JuniAtmVpPingSentProbes_Object = MibTableColumn
juniAtmVpPingSentProbes = _JuniAtmVpPingSentProbes_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 5, 2, 1, 4),
    _JuniAtmVpPingSentProbes_Type()
)
juniAtmVpPingSentProbes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAtmVpPingSentProbes.setStatus("current")
if mibBuilder.loadTexts:
    juniAtmVpPingSentProbes.setUnits("probes")


class _JuniAtmVpPingProbeResponses_Type(Unsigned32):
    """Custom type juniAtmVpPingProbeResponses based on Unsigned32"""
    defaultValue = 0


_JuniAtmVpPingProbeResponses_Object = MibTableColumn
juniAtmVpPingProbeResponses = _JuniAtmVpPingProbeResponses_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 5, 2, 1, 5),
    _JuniAtmVpPingProbeResponses_Type()
)
juniAtmVpPingProbeResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAtmVpPingProbeResponses.setStatus("current")
if mibBuilder.loadTexts:
    juniAtmVpPingProbeResponses.setUnits("probes")


class _JuniAtmVpPingStartTime_Type(TimeStamp):
    """Custom type juniAtmVpPingStartTime based on TimeStamp"""
    defaultValue = 0


_JuniAtmVpPingStartTime_Object = MibTableColumn
juniAtmVpPingStartTime = _JuniAtmVpPingStartTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 5, 2, 1, 6),
    _JuniAtmVpPingStartTime_Type()
)
juniAtmVpPingStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAtmVpPingStartTime.setStatus("current")
_JuniAtmVpPingMinRtt_Type = Unsigned32
_JuniAtmVpPingMinRtt_Object = MibTableColumn
juniAtmVpPingMinRtt = _JuniAtmVpPingMinRtt_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 5, 2, 1, 7),
    _JuniAtmVpPingMinRtt_Type()
)
juniAtmVpPingMinRtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAtmVpPingMinRtt.setStatus("current")
if mibBuilder.loadTexts:
    juniAtmVpPingMinRtt.setUnits("milliseconds")
_JuniAtmVpPingMaxRtt_Type = Unsigned32
_JuniAtmVpPingMaxRtt_Object = MibTableColumn
juniAtmVpPingMaxRtt = _JuniAtmVpPingMaxRtt_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 5, 2, 1, 8),
    _JuniAtmVpPingMaxRtt_Type()
)
juniAtmVpPingMaxRtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAtmVpPingMaxRtt.setStatus("current")
if mibBuilder.loadTexts:
    juniAtmVpPingMaxRtt.setUnits("milliseconds")
_JuniAtmVpPingAverageRtt_Type = Unsigned32
_JuniAtmVpPingAverageRtt_Object = MibTableColumn
juniAtmVpPingAverageRtt = _JuniAtmVpPingAverageRtt_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 5, 2, 1, 9),
    _JuniAtmVpPingAverageRtt_Type()
)
juniAtmVpPingAverageRtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAtmVpPingAverageRtt.setStatus("current")
if mibBuilder.loadTexts:
    juniAtmVpPingAverageRtt.setUnits("milliseconds")
_JuniAtmVcPingTable_Object = MibTable
juniAtmVcPingTable = _JuniAtmVcPingTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 5, 3)
)
if mibBuilder.loadTexts:
    juniAtmVcPingTable.setStatus("current")
_JuniAtmVcPingEntry_Object = MibTableRow
juniAtmVcPingEntry = _JuniAtmVcPingEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 5, 3, 1)
)
juniAtmVcPingEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ATM-MIB", "atmVclVpi"),
    (0, "ATM-MIB", "atmVclVci"),
    (0, "ATM-FORUM-SNMP-M4-MIB", "atmfM4VcTestObject"),
)
if mibBuilder.loadTexts:
    juniAtmVcPingEntry.setStatus("current")


class _JuniAtmVcPingProbeCount_Type(Unsigned32):
    """Custom type juniAtmVcPingProbeCount based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_JuniAtmVcPingProbeCount_Type.__name__ = "Unsigned32"
_JuniAtmVcPingProbeCount_Object = MibTableColumn
juniAtmVcPingProbeCount = _JuniAtmVcPingProbeCount_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 5, 3, 1, 1),
    _JuniAtmVcPingProbeCount_Type()
)
juniAtmVcPingProbeCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniAtmVcPingProbeCount.setStatus("current")
if mibBuilder.loadTexts:
    juniAtmVcPingProbeCount.setUnits("probes")


class _JuniAtmVcPingTimeOut_Type(Unsigned32):
    """Custom type juniAtmVcPingTimeOut based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_JuniAtmVcPingTimeOut_Type.__name__ = "Unsigned32"
_JuniAtmVcPingTimeOut_Object = MibTableColumn
juniAtmVcPingTimeOut = _JuniAtmVcPingTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 5, 3, 1, 2),
    _JuniAtmVcPingTimeOut_Type()
)
juniAtmVcPingTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniAtmVcPingTimeOut.setStatus("current")
if mibBuilder.loadTexts:
    juniAtmVcPingTimeOut.setUnits("seconds")


class _JuniAtmVcPingCtlTrapGeneration_Type(Bits):
    """Custom type juniAtmVcPingCtlTrapGeneration based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        ("testCompletion", 0)
    )

_JuniAtmVcPingCtlTrapGeneration_Type.__name__ = "Bits"
_JuniAtmVcPingCtlTrapGeneration_Object = MibTableColumn
juniAtmVcPingCtlTrapGeneration = _JuniAtmVcPingCtlTrapGeneration_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 5, 3, 1, 3),
    _JuniAtmVcPingCtlTrapGeneration_Type()
)
juniAtmVcPingCtlTrapGeneration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniAtmVcPingCtlTrapGeneration.setStatus("current")


class _JuniAtmVcPingSentProbes_Type(Unsigned32):
    """Custom type juniAtmVcPingSentProbes based on Unsigned32"""
    defaultValue = 0


_JuniAtmVcPingSentProbes_Object = MibTableColumn
juniAtmVcPingSentProbes = _JuniAtmVcPingSentProbes_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 5, 3, 1, 4),
    _JuniAtmVcPingSentProbes_Type()
)
juniAtmVcPingSentProbes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAtmVcPingSentProbes.setStatus("current")
if mibBuilder.loadTexts:
    juniAtmVcPingSentProbes.setUnits("probes")


class _JuniAtmVcPingProbeResponses_Type(Unsigned32):
    """Custom type juniAtmVcPingProbeResponses based on Unsigned32"""
    defaultValue = 0


_JuniAtmVcPingProbeResponses_Object = MibTableColumn
juniAtmVcPingProbeResponses = _JuniAtmVcPingProbeResponses_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 5, 3, 1, 5),
    _JuniAtmVcPingProbeResponses_Type()
)
juniAtmVcPingProbeResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAtmVcPingProbeResponses.setStatus("current")
if mibBuilder.loadTexts:
    juniAtmVcPingProbeResponses.setUnits("probes")


class _JuniAtmVcPingStartTime_Type(TimeStamp):
    """Custom type juniAtmVcPingStartTime based on TimeStamp"""
    defaultValue = 0


_JuniAtmVcPingStartTime_Object = MibTableColumn
juniAtmVcPingStartTime = _JuniAtmVcPingStartTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 5, 3, 1, 6),
    _JuniAtmVcPingStartTime_Type()
)
juniAtmVcPingStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAtmVcPingStartTime.setStatus("current")
_JuniAtmVcPingMinRtt_Type = Unsigned32
_JuniAtmVcPingMinRtt_Object = MibTableColumn
juniAtmVcPingMinRtt = _JuniAtmVcPingMinRtt_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 5, 3, 1, 7),
    _JuniAtmVcPingMinRtt_Type()
)
juniAtmVcPingMinRtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAtmVcPingMinRtt.setStatus("current")
if mibBuilder.loadTexts:
    juniAtmVcPingMinRtt.setUnits("milliseconds")
_JuniAtmVcPingMaxRtt_Type = Unsigned32
_JuniAtmVcPingMaxRtt_Object = MibTableColumn
juniAtmVcPingMaxRtt = _JuniAtmVcPingMaxRtt_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 5, 3, 1, 8),
    _JuniAtmVcPingMaxRtt_Type()
)
juniAtmVcPingMaxRtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAtmVcPingMaxRtt.setStatus("current")
if mibBuilder.loadTexts:
    juniAtmVcPingMaxRtt.setUnits("milliseconds")
_JuniAtmVcPingAverageRtt_Type = Unsigned32
_JuniAtmVcPingAverageRtt_Object = MibTableColumn
juniAtmVcPingAverageRtt = _JuniAtmVcPingAverageRtt_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 5, 3, 1, 9),
    _JuniAtmVcPingAverageRtt_Type()
)
juniAtmVcPingAverageRtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAtmVcPingAverageRtt.setStatus("current")
if mibBuilder.loadTexts:
    juniAtmVcPingAverageRtt.setUnits("milliseconds")
_JuniAtmPingTestCode_ObjectIdentity = ObjectIdentity
juniAtmPingTestCode = _JuniAtmPingTestCode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 5, 4)
)
_JuniAtmPingTestCodeOamDisabled_ObjectIdentity = ObjectIdentity
juniAtmPingTestCodeOamDisabled = _JuniAtmPingTestCodeOamDisabled_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 5, 4, 1)
)
if mibBuilder.loadTexts:
    juniAtmPingTestCodeOamDisabled.setStatus("current")
_JuniAtmPingTestCodeCircuitDown_ObjectIdentity = ObjectIdentity
juniAtmPingTestCodeCircuitDown = _JuniAtmPingTestCodeCircuitDown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 5, 4, 2)
)
if mibBuilder.loadTexts:
    juniAtmPingTestCodeCircuitDown.setStatus("current")
_JuniAtmPingTestCodeStopped_ObjectIdentity = ObjectIdentity
juniAtmPingTestCodeStopped = _JuniAtmPingTestCodeStopped_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 5, 4, 3)
)
if mibBuilder.loadTexts:
    juniAtmPingTestCodeStopped.setStatus("current")
_JuniAtmPingTestCodeOamVcOperState_ObjectIdentity = ObjectIdentity
juniAtmPingTestCodeOamVcOperState = _JuniAtmPingTestCodeOamVcOperState_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 5, 4, 4)
)
if mibBuilder.loadTexts:
    juniAtmPingTestCodeOamVcOperState.setStatus("current")
_JuniAtmPingTestCodeMaxPingCountReached_ObjectIdentity = ObjectIdentity
juniAtmPingTestCodeMaxPingCountReached = _JuniAtmPingTestCodeMaxPingCountReached_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 5, 4, 5)
)
if mibBuilder.loadTexts:
    juniAtmPingTestCodeMaxPingCountReached.setStatus("current")
_JuniAtmPingTestCodeInvalidParams_ObjectIdentity = ObjectIdentity
juniAtmPingTestCodeInvalidParams = _JuniAtmPingTestCodeInvalidParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 5, 4, 6)
)
if mibBuilder.loadTexts:
    juniAtmPingTestCodeInvalidParams.setStatus("current")
_JuniAtmLocation_ObjectIdentity = ObjectIdentity
juniAtmLocation = _JuniAtmLocation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 6)
)
_JuniAtmSubIfLocationType_Type = JuniInterfaceLocationType
_JuniAtmSubIfLocationType_Object = MibScalar
juniAtmSubIfLocationType = _JuniAtmSubIfLocationType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 6, 1),
    _JuniAtmSubIfLocationType_Type()
)
juniAtmSubIfLocationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAtmSubIfLocationType.setStatus("current")
_JuniAtmSubIfLocationTable_Object = MibTable
juniAtmSubIfLocationTable = _JuniAtmSubIfLocationTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 6, 2)
)
if mibBuilder.loadTexts:
    juniAtmSubIfLocationTable.setStatus("current")
_JuniAtmSubIfLocationEntry_Object = MibTableRow
juniAtmSubIfLocationEntry = _JuniAtmSubIfLocationEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 6, 2, 1)
)
juniAtmSubIfLocationEntry.setIndexNames(
    (0, "Juniper-UNI-ATM-MIB", "juniAtmSubIfLocationIndex"),
    (0, "Juniper-UNI-ATM-MIB", "juniAtmSubIfDistinguisher"),
)
if mibBuilder.loadTexts:
    juniAtmSubIfLocationEntry.setStatus("current")
_JuniAtmSubIfLocationIndex_Type = JuniInterfaceLocationValue
_JuniAtmSubIfLocationIndex_Object = MibTableColumn
juniAtmSubIfLocationIndex = _JuniAtmSubIfLocationIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 6, 2, 1, 1),
    _JuniAtmSubIfLocationIndex_Type()
)
juniAtmSubIfLocationIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniAtmSubIfLocationIndex.setStatus("current")
_JuniAtmSubIfLocationIfIndex_Type = InterfaceIndex
_JuniAtmSubIfLocationIfIndex_Object = MibTableColumn
juniAtmSubIfLocationIfIndex = _JuniAtmSubIfLocationIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 6, 2, 1, 2),
    _JuniAtmSubIfLocationIfIndex_Type()
)
juniAtmSubIfLocationIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAtmSubIfLocationIfIndex.setStatus("current")
_JuniAtmVcClass_ObjectIdentity = ObjectIdentity
juniAtmVcClass = _JuniAtmVcClass_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 7)
)
_JuniAtmVcClassNameTable_Object = MibTable
juniAtmVcClassNameTable = _JuniAtmVcClassNameTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 7, 1)
)
if mibBuilder.loadTexts:
    juniAtmVcClassNameTable.setStatus("current")
_JuniAtmVcClassNameEntry_Object = MibTableRow
juniAtmVcClassNameEntry = _JuniAtmVcClassNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 7, 1, 1)
)
juniAtmVcClassNameEntry.setIndexNames(
    (1, "Juniper-UNI-ATM-MIB", "juniAtmVcClassName"),
)
if mibBuilder.loadTexts:
    juniAtmVcClassNameEntry.setStatus("current")


class _JuniAtmVcClassName_Type(DisplayString):
    """Custom type juniAtmVcClassName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_JuniAtmVcClassName_Type.__name__ = "DisplayString"
_JuniAtmVcClassName_Object = MibTableColumn
juniAtmVcClassName = _JuniAtmVcClassName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 7, 1, 1, 1),
    _JuniAtmVcClassName_Type()
)
juniAtmVcClassName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAtmVcClassName.setStatus("current")
_JuniAtmVcClassNameRowStatus_Type = RowStatus
_JuniAtmVcClassNameRowStatus_Object = MibTableColumn
juniAtmVcClassNameRowStatus = _JuniAtmVcClassNameRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 7, 1, 1, 2),
    _JuniAtmVcClassNameRowStatus_Type()
)
juniAtmVcClassNameRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAtmVcClassNameRowStatus.setStatus("current")
_JuniAtmVcClassNameId_Type = Unsigned32
_JuniAtmVcClassNameId_Object = MibTableColumn
juniAtmVcClassNameId = _JuniAtmVcClassNameId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 7, 1, 1, 3),
    _JuniAtmVcClassNameId_Type()
)
juniAtmVcClassNameId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAtmVcClassNameId.setStatus("current")
_JuniAtmVcClassIdTable_Object = MibTable
juniAtmVcClassIdTable = _JuniAtmVcClassIdTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 7, 2)
)
if mibBuilder.loadTexts:
    juniAtmVcClassIdTable.setStatus("current")
_JuniAtmVcClassIdEntry_Object = MibTableRow
juniAtmVcClassIdEntry = _JuniAtmVcClassIdEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 7, 2, 1)
)
juniAtmVcClassIdEntry.setIndexNames(
    (0, "Juniper-UNI-ATM-MIB", "juniAtmVcClassIdId"),
)
if mibBuilder.loadTexts:
    juniAtmVcClassIdEntry.setStatus("current")
_JuniAtmVcClassIdId_Type = Unsigned32
_JuniAtmVcClassIdId_Object = MibTableColumn
juniAtmVcClassIdId = _JuniAtmVcClassIdId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 7, 2, 1, 1),
    _JuniAtmVcClassIdId_Type()
)
juniAtmVcClassIdId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniAtmVcClassIdId.setStatus("current")


class _JuniAtmVcClassIdName_Type(DisplayString):
    """Custom type juniAtmVcClassIdName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_JuniAtmVcClassIdName_Type.__name__ = "DisplayString"
_JuniAtmVcClassIdName_Object = MibTableColumn
juniAtmVcClassIdName = _JuniAtmVcClassIdName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 7, 2, 1, 2),
    _JuniAtmVcClassIdName_Type()
)
juniAtmVcClassIdName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAtmVcClassIdName.setStatus("current")
_JuniAtmVcClassTable_Object = MibTable
juniAtmVcClassTable = _JuniAtmVcClassTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 7, 3)
)
if mibBuilder.loadTexts:
    juniAtmVcClassTable.setStatus("current")
_JuniAtmVcClassEntry_Object = MibTableRow
juniAtmVcClassEntry = _JuniAtmVcClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 7, 3, 1)
)
juniAtmVcClassEntry.setIndexNames(
    (0, "Juniper-UNI-ATM-MIB", "juniAtmVcClassId"),
)
if mibBuilder.loadTexts:
    juniAtmVcClassEntry.setStatus("current")
_JuniAtmVcClassId_Type = Unsigned32
_JuniAtmVcClassId_Object = MibTableColumn
juniAtmVcClassId = _JuniAtmVcClassId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 7, 3, 1, 1),
    _JuniAtmVcClassId_Type()
)
juniAtmVcClassId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniAtmVcClassId.setStatus("current")


class _JuniAtmVcClassVccType_Type(Integer32):
    """Custom type juniAtmVcClassVccType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("aal0", 4),
          ("aal5", 3),
          ("autoconfig", 2),
          ("rfc1483Llc", 1),
          ("rfc1483VcMux", 0))
    )


_JuniAtmVcClassVccType_Type.__name__ = "Integer32"
_JuniAtmVcClassVccType_Object = MibTableColumn
juniAtmVcClassVccType = _JuniAtmVcClassVccType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 7, 3, 1, 2),
    _JuniAtmVcClassVccType_Type()
)
juniAtmVcClassVccType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniAtmVcClassVccType.setStatus("current")


class _JuniAtmVcClassVccServiceCategory_Type(Integer32):
    """Custom type juniAtmVcClassVccServiceCategory based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("cbr", 3),
          ("nrtVbr", 2),
          ("rtVbr", 4),
          ("ubr", 0),
          ("ubrPcr", 1))
    )


_JuniAtmVcClassVccServiceCategory_Type.__name__ = "Integer32"
_JuniAtmVcClassVccServiceCategory_Object = MibTableColumn
juniAtmVcClassVccServiceCategory = _JuniAtmVcClassVccServiceCategory_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 7, 3, 1, 3),
    _JuniAtmVcClassVccServiceCategory_Type()
)
juniAtmVcClassVccServiceCategory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniAtmVcClassVccServiceCategory.setStatus("current")


class _JuniAtmVcClassVccPcr_Type(Integer32):
    """Custom type juniAtmVcClassVccPcr based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JuniAtmVcClassVccPcr_Type.__name__ = "Integer32"
_JuniAtmVcClassVccPcr_Object = MibTableColumn
juniAtmVcClassVccPcr = _JuniAtmVcClassVccPcr_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 7, 3, 1, 4),
    _JuniAtmVcClassVccPcr_Type()
)
juniAtmVcClassVccPcr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniAtmVcClassVccPcr.setStatus("current")
if mibBuilder.loadTexts:
    juniAtmVcClassVccPcr.setUnits("kbps")


class _JuniAtmVcClassVccScr_Type(Integer32):
    """Custom type juniAtmVcClassVccScr based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JuniAtmVcClassVccScr_Type.__name__ = "Integer32"
_JuniAtmVcClassVccScr_Object = MibTableColumn
juniAtmVcClassVccScr = _JuniAtmVcClassVccScr_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 7, 3, 1, 5),
    _JuniAtmVcClassVccScr_Type()
)
juniAtmVcClassVccScr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniAtmVcClassVccScr.setStatus("current")
if mibBuilder.loadTexts:
    juniAtmVcClassVccScr.setUnits("kbps")


class _JuniAtmVcClassVccMbs_Type(Integer32):
    """Custom type juniAtmVcClassVccMbs based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_JuniAtmVcClassVccMbs_Type.__name__ = "Integer32"
_JuniAtmVcClassVccMbs_Object = MibTableColumn
juniAtmVcClassVccMbs = _JuniAtmVcClassVccMbs_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 7, 3, 1, 6),
    _JuniAtmVcClassVccMbs_Type()
)
juniAtmVcClassVccMbs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniAtmVcClassVccMbs.setStatus("current")
if mibBuilder.loadTexts:
    juniAtmVcClassVccMbs.setUnits("cells")


class _JuniAtmVcClassVccOamAdminStatus_Type(Integer32):
    """Custom type juniAtmVcClassVccOamAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("oamAdminStateDisabled", 1),
          ("oamAdminStateEnabled", 2))
    )


_JuniAtmVcClassVccOamAdminStatus_Type.__name__ = "Integer32"
_JuniAtmVcClassVccOamAdminStatus_Object = MibTableColumn
juniAtmVcClassVccOamAdminStatus = _JuniAtmVcClassVccOamAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 7, 3, 1, 7),
    _JuniAtmVcClassVccOamAdminStatus_Type()
)
juniAtmVcClassVccOamAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniAtmVcClassVccOamAdminStatus.setStatus("current")


class _JuniAtmVcClassVccOamLoopbackFrequency_Type(Integer32):
    """Custom type juniAtmVcClassVccOamLoopbackFrequency based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_JuniAtmVcClassVccOamLoopbackFrequency_Type.__name__ = "Integer32"
_JuniAtmVcClassVccOamLoopbackFrequency_Object = MibTableColumn
juniAtmVcClassVccOamLoopbackFrequency = _JuniAtmVcClassVccOamLoopbackFrequency_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 7, 3, 1, 8),
    _JuniAtmVcClassVccOamLoopbackFrequency_Type()
)
juniAtmVcClassVccOamLoopbackFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniAtmVcClassVccOamLoopbackFrequency.setStatus("current")
if mibBuilder.loadTexts:
    juniAtmVcClassVccOamLoopbackFrequency.setUnits("seconds")


class _JuniAtmVcClassVccOamUpCount_Type(Integer32):
    """Custom type juniAtmVcClassVccOamUpCount based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_JuniAtmVcClassVccOamUpCount_Type.__name__ = "Integer32"
_JuniAtmVcClassVccOamUpCount_Object = MibTableColumn
juniAtmVcClassVccOamUpCount = _JuniAtmVcClassVccOamUpCount_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 7, 3, 1, 9),
    _JuniAtmVcClassVccOamUpCount_Type()
)
juniAtmVcClassVccOamUpCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniAtmVcClassVccOamUpCount.setStatus("current")
if mibBuilder.loadTexts:
    juniAtmVcClassVccOamUpCount.setUnits("cells")


class _JuniAtmVcClassVccOamDownCount_Type(Integer32):
    """Custom type juniAtmVcClassVccOamDownCount based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_JuniAtmVcClassVccOamDownCount_Type.__name__ = "Integer32"
_JuniAtmVcClassVccOamDownCount_Object = MibTableColumn
juniAtmVcClassVccOamDownCount = _JuniAtmVcClassVccOamDownCount_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 7, 3, 1, 10),
    _JuniAtmVcClassVccOamDownCount_Type()
)
juniAtmVcClassVccOamDownCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniAtmVcClassVccOamDownCount.setStatus("current")
if mibBuilder.loadTexts:
    juniAtmVcClassVccOamDownCount.setUnits("cells")


class _JuniAtmVcClassVccOamRetryFrequency_Type(Integer32):
    """Custom type juniAtmVcClassVccOamRetryFrequency based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_JuniAtmVcClassVccOamRetryFrequency_Type.__name__ = "Integer32"
_JuniAtmVcClassVccOamRetryFrequency_Object = MibTableColumn
juniAtmVcClassVccOamRetryFrequency = _JuniAtmVcClassVccOamRetryFrequency_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 7, 3, 1, 11),
    _JuniAtmVcClassVccOamRetryFrequency_Type()
)
juniAtmVcClassVccOamRetryFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniAtmVcClassVccOamRetryFrequency.setStatus("current")
if mibBuilder.loadTexts:
    juniAtmVcClassVccOamRetryFrequency.setUnits("seconds")


class _JuniAtmVcClassVccOamAlarmDownCount_Type(Integer32):
    """Custom type juniAtmVcClassVccOamAlarmDownCount based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_JuniAtmVcClassVccOamAlarmDownCount_Type.__name__ = "Integer32"
_JuniAtmVcClassVccOamAlarmDownCount_Object = MibTableColumn
juniAtmVcClassVccOamAlarmDownCount = _JuniAtmVcClassVccOamAlarmDownCount_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 7, 3, 1, 12),
    _JuniAtmVcClassVccOamAlarmDownCount_Type()
)
juniAtmVcClassVccOamAlarmDownCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniAtmVcClassVccOamAlarmDownCount.setStatus("current")
if mibBuilder.loadTexts:
    juniAtmVcClassVccOamAlarmDownCount.setUnits("cells")


class _JuniAtmVcClassVccOamAlarmClearTimeout_Type(Integer32):
    """Custom type juniAtmVcClassVccOamAlarmClearTimeout based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 60),
    )


_JuniAtmVcClassVccOamAlarmClearTimeout_Type.__name__ = "Integer32"
_JuniAtmVcClassVccOamAlarmClearTimeout_Object = MibTableColumn
juniAtmVcClassVccOamAlarmClearTimeout = _JuniAtmVcClassVccOamAlarmClearTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 7, 3, 1, 13),
    _JuniAtmVcClassVccOamAlarmClearTimeout_Type()
)
juniAtmVcClassVccOamAlarmClearTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniAtmVcClassVccOamAlarmClearTimeout.setStatus("current")
if mibBuilder.loadTexts:
    juniAtmVcClassVccOamAlarmClearTimeout.setUnits("seconds")
_JuniAtmVcClassVccInverseArp_Type = TruthValue
_JuniAtmVcClassVccInverseArp_Object = MibTableColumn
juniAtmVcClassVccInverseArp = _JuniAtmVcClassVccInverseArp_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 7, 3, 1, 14),
    _JuniAtmVcClassVccInverseArp_Type()
)
juniAtmVcClassVccInverseArp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniAtmVcClassVccInverseArp.setStatus("current")


class _JuniAtmVcClassVccInverseArpRefresh_Type(Integer32):
    """Custom type juniAtmVcClassVccInverseArpRefresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_JuniAtmVcClassVccInverseArpRefresh_Type.__name__ = "Integer32"
_JuniAtmVcClassVccInverseArpRefresh_Object = MibTableColumn
juniAtmVcClassVccInverseArpRefresh = _JuniAtmVcClassVccInverseArpRefresh_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 1, 7, 3, 1, 15),
    _JuniAtmVcClassVccInverseArpRefresh_Type()
)
juniAtmVcClassVccInverseArpRefresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniAtmVcClassVccInverseArpRefresh.setStatus("current")
if mibBuilder.loadTexts:
    juniAtmVcClassVccInverseArpRefresh.setUnits("minutes")
_JuniAtmTraps_ObjectIdentity = ObjectIdentity
juniAtmTraps = _JuniAtmTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 3)
)
_JuniAtmTrapPrefix_ObjectIdentity = ObjectIdentity
juniAtmTrapPrefix = _JuniAtmTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 3, 0)
)
_JuniAtmConformance_ObjectIdentity = ObjectIdentity
juniAtmConformance = _JuniAtmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 4)
)
_JuniAtmCompliances_ObjectIdentity = ObjectIdentity
juniAtmCompliances = _JuniAtmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 4, 1)
)
_JuniAtmGroups_ObjectIdentity = ObjectIdentity
juniAtmGroups = _JuniAtmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 4, 2)
)
juniAtmSubIfVccEntry.registerAugmentions(
    ("Juniper-UNI-ATM-MIB",
     "juniAtmSubIfVccTrafficShapingEntry")
)
juniAtmSubIfVccTrafficShapingEntry.setIndexNames(*juniAtmSubIfVccEntry.getIndexNames())

# Managed Objects groups

juniAtmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 4, 2, 1)
)
juniAtmGroup.setObjects(
      *(("Juniper-UNI-ATM-MIB", "juniAtmNextIfIndex"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfRowStatus"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfLowerIfIndex"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfIlmiVpi"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfIlmiVci"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfIlmiVcd"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfIlmiPollFrequency"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfIlmiAdminState"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfUniVersion"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfOamCellRxAdminState"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfInCells"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfOutCells"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfVcCount"),
        ("Juniper-UNI-ATM-MIB", "juniAtmPvcStatsInCells"),
        ("Juniper-UNI-ATM-MIB", "juniAtmPvcStatsInCellOctets"),
        ("Juniper-UNI-ATM-MIB", "juniAtmPvcStatsInPackets"),
        ("Juniper-UNI-ATM-MIB", "juniAtmPvcStatsInPacketOctets"),
        ("Juniper-UNI-ATM-MIB", "juniAtmPvcStatsOutCells"),
        ("Juniper-UNI-ATM-MIB", "juniAtmPvcStatsOutCellOctets"),
        ("Juniper-UNI-ATM-MIB", "juniAtmPvcStatsOutPackets"),
        ("Juniper-UNI-ATM-MIB", "juniAtmPvcStatsOutPacketOctets"),
        ("Juniper-UNI-ATM-MIB", "juniAtmPvcStatsInCellErrors"),
        ("Juniper-UNI-ATM-MIB", "juniAtmPvcStatsinPacketErrors"),
        ("Juniper-UNI-ATM-MIB", "juniAtmPvcStatsOutCellErrors"),
        ("Juniper-UNI-ATM-MIB", "juniAtmPvcStatsOutPacketErrors"),
        ("Juniper-UNI-ATM-MIB", "juniAtmPvcStatsInPacketDiscards"),
        ("Juniper-UNI-ATM-MIB", "juniAtmPvcStatsInPacketOctetDiscards"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfCapabilityTrafficShaping"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfCapabilityOam"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfCapabilityDefaultVcPerVp"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfCapabilityNumVpiVciBits"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfCapabilityMaxVcd"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfCapabilityMaxVpi"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfCapabilityMaxVci"))
)
if mibBuilder.loadTexts:
    juniAtmGroup.setStatus("obsolete")

juniAtmAal5Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 4, 2, 2)
)
juniAtmAal5Group.setObjects(
      *(("Juniper-UNI-ATM-MIB", "juniAtmAal5NextIfIndex"),
        ("Juniper-UNI-ATM-MIB", "juniAtmAal5IfRowStatus"),
        ("Juniper-UNI-ATM-MIB", "juniAtmAal5IfLowerIfIndex"))
)
if mibBuilder.loadTexts:
    juniAtmAal5Group.setStatus("current")

juniAtmSubIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 4, 2, 3)
)
juniAtmSubIfGroup.setObjects(
      *(("Juniper-UNI-ATM-MIB", "juniAtmSubIfNextIfIndex"),
        ("Juniper-UNI-ATM-MIB", "juniAtmSubIfRowStatus"),
        ("Juniper-UNI-ATM-MIB", "juniAtmSubIfDistinguisher"),
        ("Juniper-UNI-ATM-MIB", "juniAtmSubIfLowerIfIndex"),
        ("Juniper-UNI-ATM-MIB", "juniAtmSubIfVccRowStatus"),
        ("Juniper-UNI-ATM-MIB", "juniAtmSubIfVccVcd"),
        ("Juniper-UNI-ATM-MIB", "juniAtmSubIfVccType"),
        ("Juniper-UNI-ATM-MIB", "juniAtmSubIfVccServiceCategory"),
        ("Juniper-UNI-ATM-MIB", "juniAtmSubIfVccPcr"),
        ("Juniper-UNI-ATM-MIB", "juniAtmSubIfVccScr"),
        ("Juniper-UNI-ATM-MIB", "juniAtmSubIfVccMbs"),
        ("Juniper-UNI-ATM-MIB", "juniAtmCircuitOamAdminStatus"),
        ("Juniper-UNI-ATM-MIB", "juniAtmCircuitOamLoopbackOperStatus"),
        ("Juniper-UNI-ATM-MIB", "juniAtmCircuitVcOamOperStatus"),
        ("Juniper-UNI-ATM-MIB", "juniAtmCircuitOamLoopbackFrequency"),
        ("Juniper-UNI-ATM-MIB", "juniAtmCircuitInOamF5Cells"),
        ("Juniper-UNI-ATM-MIB", "juniAtmCircuitInOamCellsDropped"),
        ("Juniper-UNI-ATM-MIB", "juniAtmCircuitOutOamF5Cells"),
        ("Juniper-UNI-ATM-MIB", "juniAtmCircuitInOamF5EndToEndLoopbackCells"),
        ("Juniper-UNI-ATM-MIB", "juniAtmCircuitInOamF5SegmentLoopbackCells"),
        ("Juniper-UNI-ATM-MIB", "juniAtmCircuitInOamF5AisCells"),
        ("Juniper-UNI-ATM-MIB", "juniAtmCircuitInOamF5RdiCells"),
        ("Juniper-UNI-ATM-MIB", "juniAtmCircuitOutOamF5EndToEndLoopbackCells"),
        ("Juniper-UNI-ATM-MIB", "juniAtmCircuitOutOamF5SegmentLoopbackCells"),
        ("Juniper-UNI-ATM-MIB", "juniAtmCircuitOutOamF5RdiCells"))
)
if mibBuilder.loadTexts:
    juniAtmSubIfGroup.setStatus("obsolete")

juniAtmVpTunnelGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 4, 2, 4)
)
juniAtmVpTunnelGroup.setObjects(
      *(("Juniper-UNI-ATM-MIB", "juniAtmVpTunnelKbps"),
        ("Juniper-UNI-ATM-MIB", "juniAtmVpTunnelRowStatus"),
        ("Juniper-UNI-ATM-MIB", "juniAtmVpTunnelServiceCategory"))
)
if mibBuilder.loadTexts:
    juniAtmVpTunnelGroup.setStatus("current")

juniAtmNbmaMapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 4, 2, 5)
)
juniAtmNbmaMapGroup.setObjects(
      *(("Juniper-UNI-ATM-MIB", "juniAtmNbmaMapIpAddress"),
        ("Juniper-UNI-ATM-MIB", "juniAtmNbmaMapVpi"),
        ("Juniper-UNI-ATM-MIB", "juniAtmNbmaMapVci"),
        ("Juniper-UNI-ATM-MIB", "juniAtmNbmaMapIfIndex"),
        ("Juniper-UNI-ATM-MIB", "juniAtmNbmaMapBroadcast"),
        ("Juniper-UNI-ATM-MIB", "juniAtmNbmaMapRowStatus"),
        ("Juniper-UNI-ATM-MIB", "juniAtmNbmaMapListRowStatus"))
)
if mibBuilder.loadTexts:
    juniAtmNbmaMapGroup.setStatus("current")

juniAtmSubIfGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 4, 2, 6)
)
juniAtmSubIfGroup2.setObjects(
      *(("Juniper-UNI-ATM-MIB", "juniAtmSubIfNextIfIndex"),
        ("Juniper-UNI-ATM-MIB", "juniAtmSubIfRowStatus"),
        ("Juniper-UNI-ATM-MIB", "juniAtmSubIfDistinguisher"),
        ("Juniper-UNI-ATM-MIB", "juniAtmSubIfLowerIfIndex"),
        ("Juniper-UNI-ATM-MIB", "juniAtmSubIfNbma"),
        ("Juniper-UNI-ATM-MIB", "juniAtmSubIfVccRowStatus"),
        ("Juniper-UNI-ATM-MIB", "juniAtmSubIfVccVcd"),
        ("Juniper-UNI-ATM-MIB", "juniAtmSubIfVccType"),
        ("Juniper-UNI-ATM-MIB", "juniAtmSubIfVccServiceCategory"),
        ("Juniper-UNI-ATM-MIB", "juniAtmSubIfVccPcr"),
        ("Juniper-UNI-ATM-MIB", "juniAtmSubIfVccScr"),
        ("Juniper-UNI-ATM-MIB", "juniAtmSubIfVccMbs"),
        ("Juniper-UNI-ATM-MIB", "juniAtmSubIfInverseArp"),
        ("Juniper-UNI-ATM-MIB", "juniAtmSubIfInverseArpRefresh"),
        ("Juniper-UNI-ATM-MIB", "juniAtmCircuitOamAdminStatus"),
        ("Juniper-UNI-ATM-MIB", "juniAtmCircuitOamLoopbackOperStatus"),
        ("Juniper-UNI-ATM-MIB", "juniAtmCircuitVcOamOperStatus"),
        ("Juniper-UNI-ATM-MIB", "juniAtmCircuitOamLoopbackFrequency"),
        ("Juniper-UNI-ATM-MIB", "juniAtmCircuitInOamF5Cells"),
        ("Juniper-UNI-ATM-MIB", "juniAtmCircuitInOamCellsDropped"),
        ("Juniper-UNI-ATM-MIB", "juniAtmCircuitOutOamF5Cells"),
        ("Juniper-UNI-ATM-MIB", "juniAtmCircuitInOamF5EndToEndLoopbackCells"),
        ("Juniper-UNI-ATM-MIB", "juniAtmCircuitInOamF5SegmentLoopbackCells"),
        ("Juniper-UNI-ATM-MIB", "juniAtmCircuitInOamF5AisCells"),
        ("Juniper-UNI-ATM-MIB", "juniAtmCircuitInOamF5RdiCells"),
        ("Juniper-UNI-ATM-MIB", "juniAtmCircuitOutOamF5EndToEndLoopbackCells"),
        ("Juniper-UNI-ATM-MIB", "juniAtmCircuitOutOamF5SegmentLoopbackCells"),
        ("Juniper-UNI-ATM-MIB", "juniAtmCircuitOutOamF5RdiCells"))
)
if mibBuilder.loadTexts:
    juniAtmSubIfGroup2.setStatus("obsolete")

juniAtmVpPingControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 4, 2, 7)
)
juniAtmVpPingControlGroup.setObjects(
      *(("Juniper-UNI-ATM-MIB", "juniAtmVpPingProbeCount"),
        ("Juniper-UNI-ATM-MIB", "juniAtmVpPingTimeOut"),
        ("Juniper-UNI-ATM-MIB", "juniAtmVpPingCtlTrapGeneration"),
        ("Juniper-UNI-ATM-MIB", "juniAtmVpPingSentProbes"),
        ("Juniper-UNI-ATM-MIB", "juniAtmVpPingProbeResponses"),
        ("Juniper-UNI-ATM-MIB", "juniAtmVpPingStartTime"),
        ("Juniper-UNI-ATM-MIB", "juniAtmVpPingMinRtt"),
        ("Juniper-UNI-ATM-MIB", "juniAtmVpPingMaxRtt"),
        ("Juniper-UNI-ATM-MIB", "juniAtmVpPingAverageRtt"))
)
if mibBuilder.loadTexts:
    juniAtmVpPingControlGroup.setStatus("current")

juniAtmVcPingControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 4, 2, 8)
)
juniAtmVcPingControlGroup.setObjects(
      *(("Juniper-UNI-ATM-MIB", "juniAtmVcPingProbeCount"),
        ("Juniper-UNI-ATM-MIB", "juniAtmVcPingTimeOut"),
        ("Juniper-UNI-ATM-MIB", "juniAtmVcPingCtlTrapGeneration"),
        ("Juniper-UNI-ATM-MIB", "juniAtmVcPingSentProbes"),
        ("Juniper-UNI-ATM-MIB", "juniAtmVcPingProbeResponses"),
        ("Juniper-UNI-ATM-MIB", "juniAtmVcPingStartTime"),
        ("Juniper-UNI-ATM-MIB", "juniAtmVcPingMinRtt"),
        ("Juniper-UNI-ATM-MIB", "juniAtmVcPingMaxRtt"),
        ("Juniper-UNI-ATM-MIB", "juniAtmVcPingAverageRtt"))
)
if mibBuilder.loadTexts:
    juniAtmVcPingControlGroup.setStatus("current")

juniAtmGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 4, 2, 10)
)
juniAtmGroup2.setObjects(
      *(("Juniper-UNI-ATM-MIB", "juniAtmNextIfIndex"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfRowStatus"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfLowerIfIndex"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfIlmiVpi"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfIlmiVci"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfIlmiVcd"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfIlmiPollFrequency"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfIlmiAdminState"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfUniVersion"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfOamCellRxAdminState"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfInCells"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfOutCells"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfVcCount"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfMapGroup"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfOamCellFilter"),
        ("Juniper-UNI-ATM-MIB", "juniAtmPvcStatsInCells"),
        ("Juniper-UNI-ATM-MIB", "juniAtmPvcStatsInCellOctets"),
        ("Juniper-UNI-ATM-MIB", "juniAtmPvcStatsInPackets"),
        ("Juniper-UNI-ATM-MIB", "juniAtmPvcStatsInPacketOctets"),
        ("Juniper-UNI-ATM-MIB", "juniAtmPvcStatsOutCells"),
        ("Juniper-UNI-ATM-MIB", "juniAtmPvcStatsOutCellOctets"),
        ("Juniper-UNI-ATM-MIB", "juniAtmPvcStatsOutPackets"),
        ("Juniper-UNI-ATM-MIB", "juniAtmPvcStatsOutPacketOctets"),
        ("Juniper-UNI-ATM-MIB", "juniAtmPvcStatsInCellErrors"),
        ("Juniper-UNI-ATM-MIB", "juniAtmPvcStatsinPacketErrors"),
        ("Juniper-UNI-ATM-MIB", "juniAtmPvcStatsOutCellErrors"),
        ("Juniper-UNI-ATM-MIB", "juniAtmPvcStatsOutPacketErrors"),
        ("Juniper-UNI-ATM-MIB", "juniAtmPvcStatsInPacketDiscards"),
        ("Juniper-UNI-ATM-MIB", "juniAtmPvcStatsInPacketOctetDiscards"),
        ("Juniper-UNI-ATM-MIB", "juniAtmPvcStatsInPacketUnknownProtocol"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfCapabilityTrafficShaping"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfCapabilityOam"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfCapabilityDefaultVcPerVp"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfCapabilityNumVpiVciBits"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfCapabilityMaxVcd"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfCapabilityMaxVpi"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfCapabilityMaxVci"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfCapabilityOamCellFilter"))
)
if mibBuilder.loadTexts:
    juniAtmGroup2.setStatus("obsolete")

juniAtmTrafficShapingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 4, 2, 11)
)
juniAtmTrafficShapingGroup.setObjects(
      *(("Juniper-UNI-ATM-MIB", "juniAtmSubIfVccTrafficShapingCdvt"),
        ("Juniper-UNI-ATM-MIB", "juniAtmSubIfVccTrafficShapingClp0"),
        ("Juniper-UNI-ATM-MIB", "juniAtmSubIfVccTrafficShapingTagging"),
        ("Juniper-UNI-ATM-MIB", "juniAtmSubIfVccTrafficShapingPoliceObserve"),
        ("Juniper-UNI-ATM-MIB", "juniAtmSubIfVccTrafficShapingPacketShaping"))
)
if mibBuilder.loadTexts:
    juniAtmTrafficShapingGroup.setStatus("current")

juniAtmGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 4, 2, 12)
)
juniAtmGroup3.setObjects(
      *(("Juniper-UNI-ATM-MIB", "juniAtmNextIfIndex"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfRowStatus"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfLowerIfIndex"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfIlmiVpi"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfIlmiVci"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfIlmiVcd"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfIlmiPollFrequency"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfIlmiAdminState"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfUniVersion"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfOamCellRxAdminState"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfInCells"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfOutCells"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfVcCount"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfMapGroup"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfCacAdminState"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfCacUbrWeight"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfCacSubscriptionBandwidth"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfCacAvailableBandwidth"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfOamCellFilter"),
        ("Juniper-UNI-ATM-MIB", "juniAtmPvcStatsInCells"),
        ("Juniper-UNI-ATM-MIB", "juniAtmPvcStatsInCellOctets"),
        ("Juniper-UNI-ATM-MIB", "juniAtmPvcStatsInPackets"),
        ("Juniper-UNI-ATM-MIB", "juniAtmPvcStatsInPacketOctets"),
        ("Juniper-UNI-ATM-MIB", "juniAtmPvcStatsOutCells"),
        ("Juniper-UNI-ATM-MIB", "juniAtmPvcStatsOutCellOctets"),
        ("Juniper-UNI-ATM-MIB", "juniAtmPvcStatsOutPackets"),
        ("Juniper-UNI-ATM-MIB", "juniAtmPvcStatsOutPacketOctets"),
        ("Juniper-UNI-ATM-MIB", "juniAtmPvcStatsInCellErrors"),
        ("Juniper-UNI-ATM-MIB", "juniAtmPvcStatsinPacketErrors"),
        ("Juniper-UNI-ATM-MIB", "juniAtmPvcStatsOutCellErrors"),
        ("Juniper-UNI-ATM-MIB", "juniAtmPvcStatsOutPacketErrors"),
        ("Juniper-UNI-ATM-MIB", "juniAtmPvcStatsInPacketDiscards"),
        ("Juniper-UNI-ATM-MIB", "juniAtmPvcStatsInPacketOctetDiscards"),
        ("Juniper-UNI-ATM-MIB", "juniAtmPvcStatsInPacketUnknownProtocol"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfCapabilityTrafficShaping"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfCapabilityOam"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfCapabilityDefaultVcPerVp"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfCapabilityNumVpiVciBits"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfCapabilityMaxVcd"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfCapabilityMaxVpi"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfCapabilityMaxVci"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfCapabilityOamCellFilter"))
)
if mibBuilder.loadTexts:
    juniAtmGroup3.setStatus("obsolete")

juniAtmGroup4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 4, 2, 13)
)
juniAtmGroup4.setObjects(
      *(("Juniper-UNI-ATM-MIB", "juniAtmNextIfIndex"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfRowStatus"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfLowerIfIndex"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfIlmiVpi"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfIlmiVci"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfIlmiVcd"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfIlmiPollFrequency"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfIlmiAdminState"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfUniVersion"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfOamCellRxAdminState"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfInCells"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfOutCells"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfVcCount"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfMapGroup"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfCacAdminState"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfCacUbrWeight"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfCacSubscriptionBandwidth"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfCacAvailableBandwidth"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfOamCellFilter"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfCacUsedBandwidthUpper"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfCacUsedBandwidthLower"),
        ("Juniper-UNI-ATM-MIB", "juniAtmPvcStatsInCells"),
        ("Juniper-UNI-ATM-MIB", "juniAtmPvcStatsInCellOctets"),
        ("Juniper-UNI-ATM-MIB", "juniAtmPvcStatsInPackets"),
        ("Juniper-UNI-ATM-MIB", "juniAtmPvcStatsInPacketOctets"),
        ("Juniper-UNI-ATM-MIB", "juniAtmPvcStatsOutCells"),
        ("Juniper-UNI-ATM-MIB", "juniAtmPvcStatsOutCellOctets"),
        ("Juniper-UNI-ATM-MIB", "juniAtmPvcStatsOutPackets"),
        ("Juniper-UNI-ATM-MIB", "juniAtmPvcStatsOutPacketOctets"),
        ("Juniper-UNI-ATM-MIB", "juniAtmPvcStatsInCellErrors"),
        ("Juniper-UNI-ATM-MIB", "juniAtmPvcStatsinPacketErrors"),
        ("Juniper-UNI-ATM-MIB", "juniAtmPvcStatsOutCellErrors"),
        ("Juniper-UNI-ATM-MIB", "juniAtmPvcStatsOutPacketErrors"),
        ("Juniper-UNI-ATM-MIB", "juniAtmPvcStatsInPacketDiscards"),
        ("Juniper-UNI-ATM-MIB", "juniAtmPvcStatsInPacketOctetDiscards"),
        ("Juniper-UNI-ATM-MIB", "juniAtmPvcStatsInPacketUnknownProtocol"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfCapabilityTrafficShaping"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfCapabilityOam"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfCapabilityDefaultVcPerVp"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfCapabilityNumVpiVciBits"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfCapabilityMaxVcd"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfCapabilityMaxVpi"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfCapabilityMaxVci"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfCapabilityOamCellFilter"))
)
if mibBuilder.loadTexts:
    juniAtmGroup4.setStatus("obsolete")

juniAtmSvcGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 4, 2, 14)
)
juniAtmSvcGroup.setObjects(
      *(("Juniper-UNI-ATM-MIB", "juniAtmIfSvcSignallingVpi"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfSvcSignallingVci"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfSvcSignallingVcd"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfSvcSignallingAdminStatus"),
        ("Juniper-UNI-ATM-MIB", "juniAtmSubIfSvcRowStatus"),
        ("Juniper-UNI-ATM-MIB", "juniAtmSubIfSvcConfigDestAtmAddress"),
        ("Juniper-UNI-ATM-MIB", "juniAtmSubIfSvcConfigCircuitType"),
        ("Juniper-UNI-ATM-MIB", "juniAtmSubIfSvcConfigServiceCategory"),
        ("Juniper-UNI-ATM-MIB", "juniAtmSubIfSvcConfigPcr"),
        ("Juniper-UNI-ATM-MIB", "juniAtmSubIfSvcConfigScr"),
        ("Juniper-UNI-ATM-MIB", "juniAtmSubIfSvcConfigMbs"),
        ("Juniper-UNI-ATM-MIB", "juniAtmSubIfSvcConfigCdvt"),
        ("Juniper-UNI-ATM-MIB", "juniAtmSubIfSvcConfigClp0"),
        ("Juniper-UNI-ATM-MIB", "juniAtmSubIfSvcConfigTagging"),
        ("Juniper-UNI-ATM-MIB", "juniAtmSubIfSvcConfigObserve"),
        ("Juniper-UNI-ATM-MIB", "juniAtmSubIfSvcConfigPacketDiscard"))
)
if mibBuilder.loadTexts:
    juniAtmSvcGroup.setStatus("obsolete")

juniAtmSubIfGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 4, 2, 15)
)
juniAtmSubIfGroup3.setObjects(
      *(("Juniper-UNI-ATM-MIB", "juniAtmSubIfNextIfIndex"),
        ("Juniper-UNI-ATM-MIB", "juniAtmSubIfRowStatus"),
        ("Juniper-UNI-ATM-MIB", "juniAtmSubIfDistinguisher"),
        ("Juniper-UNI-ATM-MIB", "juniAtmSubIfLowerIfIndex"),
        ("Juniper-UNI-ATM-MIB", "juniAtmSubIfNbma"),
        ("Juniper-UNI-ATM-MIB", "juniAtmSubIfAddress"),
        ("Juniper-UNI-ATM-MIB", "juniAtmSubIfVccRowStatus"),
        ("Juniper-UNI-ATM-MIB", "juniAtmSubIfVccVcd"),
        ("Juniper-UNI-ATM-MIB", "juniAtmSubIfVccType"),
        ("Juniper-UNI-ATM-MIB", "juniAtmSubIfVccServiceCategory"),
        ("Juniper-UNI-ATM-MIB", "juniAtmSubIfVccPcr"),
        ("Juniper-UNI-ATM-MIB", "juniAtmSubIfVccScr"),
        ("Juniper-UNI-ATM-MIB", "juniAtmSubIfVccMbs"),
        ("Juniper-UNI-ATM-MIB", "juniAtmSubIfInverseArp"),
        ("Juniper-UNI-ATM-MIB", "juniAtmSubIfInverseArpRefresh"),
        ("Juniper-UNI-ATM-MIB", "juniAtmCircuitOamAdminStatus"),
        ("Juniper-UNI-ATM-MIB", "juniAtmCircuitOamLoopbackOperStatus"),
        ("Juniper-UNI-ATM-MIB", "juniAtmCircuitVcOamOperStatus"),
        ("Juniper-UNI-ATM-MIB", "juniAtmCircuitOamLoopbackFrequency"),
        ("Juniper-UNI-ATM-MIB", "juniAtmCircuitInOamF5Cells"),
        ("Juniper-UNI-ATM-MIB", "juniAtmCircuitInOamCellsDropped"),
        ("Juniper-UNI-ATM-MIB", "juniAtmCircuitOutOamF5Cells"),
        ("Juniper-UNI-ATM-MIB", "juniAtmCircuitInOamF5EndToEndLoopbackCells"),
        ("Juniper-UNI-ATM-MIB", "juniAtmCircuitInOamF5SegmentLoopbackCells"),
        ("Juniper-UNI-ATM-MIB", "juniAtmCircuitInOamF5AisCells"),
        ("Juniper-UNI-ATM-MIB", "juniAtmCircuitInOamF5RdiCells"),
        ("Juniper-UNI-ATM-MIB", "juniAtmCircuitOutOamF5EndToEndLoopbackCells"),
        ("Juniper-UNI-ATM-MIB", "juniAtmCircuitOutOamF5SegmentLoopbackCells"),
        ("Juniper-UNI-ATM-MIB", "juniAtmCircuitOutOamF5RdiCells"))
)
if mibBuilder.loadTexts:
    juniAtmSubIfGroup3.setStatus("obsolete")

juniAtmGroup5 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 4, 2, 16)
)
juniAtmGroup5.setObjects(
      *(("Juniper-UNI-ATM-MIB", "juniAtmNextIfIndex"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfRowStatus"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfLowerIfIndex"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfIlmiVpi"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfIlmiVci"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfIlmiVcd"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfIlmiPollFrequency"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfIlmiAdminState"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfUniVersion"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfOamCellRxAdminState"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfInCells"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfOutCells"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfVcCount"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfMapGroup"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfCacAdminState"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfCacUbrWeight"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfCacSubscriptionBandwidth"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfCacAvailableBandwidth"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfCacAvailableBandwidthRx"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfE164Autoconversion"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfE164Gateway"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfE164OneToOneAddrTrans"),
        ("Juniper-UNI-ATM-MIB", "juniAtmPvcStatsInCells"),
        ("Juniper-UNI-ATM-MIB", "juniAtmPvcStatsInCellOctets"),
        ("Juniper-UNI-ATM-MIB", "juniAtmPvcStatsInPackets"),
        ("Juniper-UNI-ATM-MIB", "juniAtmPvcStatsInPacketOctets"),
        ("Juniper-UNI-ATM-MIB", "juniAtmPvcStatsOutCells"),
        ("Juniper-UNI-ATM-MIB", "juniAtmPvcStatsOutCellOctets"),
        ("Juniper-UNI-ATM-MIB", "juniAtmPvcStatsOutPackets"),
        ("Juniper-UNI-ATM-MIB", "juniAtmPvcStatsOutPacketOctets"),
        ("Juniper-UNI-ATM-MIB", "juniAtmPvcStatsInCellErrors"),
        ("Juniper-UNI-ATM-MIB", "juniAtmPvcStatsinPacketErrors"),
        ("Juniper-UNI-ATM-MIB", "juniAtmPvcStatsOutCellErrors"),
        ("Juniper-UNI-ATM-MIB", "juniAtmPvcStatsOutPacketErrors"),
        ("Juniper-UNI-ATM-MIB", "juniAtmPvcStatsInPacketDiscards"),
        ("Juniper-UNI-ATM-MIB", "juniAtmPvcStatsInPacketOctetDiscards"),
        ("Juniper-UNI-ATM-MIB", "juniAtmPvcStatsInPacketUnknownProtocol"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfCapabilityTrafficShaping"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfCapabilityOam"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfCapabilityDefaultVcPerVp"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfCapabilityNumVpiVciBits"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfCapabilityMaxVcd"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfCapabilityMaxVpi"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfCapabilityMaxVci"))
)
if mibBuilder.loadTexts:
    juniAtmGroup5.setStatus("obsolete")

juniAtmSvcGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 4, 2, 17)
)
juniAtmSvcGroup2.setObjects(
      *(("Juniper-UNI-ATM-MIB", "juniAtmIfSvcSignallingVpi"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfSvcSignallingVci"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfSvcSignallingVcd"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfSvcSignallingAdminStatus"),
        ("Juniper-UNI-ATM-MIB", "juniAtmSubIfSvcRowStatus"),
        ("Juniper-UNI-ATM-MIB", "juniAtmSubIfSvcConfigDestAtmAddress"),
        ("Juniper-UNI-ATM-MIB", "juniAtmSubIfSvcConfigCircuitType"),
        ("Juniper-UNI-ATM-MIB", "juniAtmSubIfSvcConfigServiceCategory"),
        ("Juniper-UNI-ATM-MIB", "juniAtmSubIfSvcConfigPcr"),
        ("Juniper-UNI-ATM-MIB", "juniAtmSubIfSvcConfigScr"),
        ("Juniper-UNI-ATM-MIB", "juniAtmSubIfSvcConfigMbs"),
        ("Juniper-UNI-ATM-MIB", "juniAtmSubIfSvcConfigClp0"),
        ("Juniper-UNI-ATM-MIB", "juniAtmSubIfSvcConfigTagging"),
        ("Juniper-UNI-ATM-MIB", "juniAtmSubIfSvcConfigPacketDiscard"),
        ("Juniper-UNI-ATM-MIB", "juniAtmSubIfSvcConfigDestE164Address"))
)
if mibBuilder.loadTexts:
    juniAtmSvcGroup2.setStatus("current")

juniAtmPnniGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 4, 2, 18)
)
juniAtmPnniGroup.setObjects(
      *(("Juniper-UNI-ATM-MIB", "juniAtmIfPnniRccVpi"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfPnniRccVci"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfPnniRccVcd"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfPnniRccAdminStatus"))
)
if mibBuilder.loadTexts:
    juniAtmPnniGroup.setStatus("current")

juniAtmSubIfGroup4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 4, 2, 19)
)
juniAtmSubIfGroup4.setObjects(
      *(("Juniper-UNI-ATM-MIB", "juniAtmSubIfNextIfIndex"),
        ("Juniper-UNI-ATM-MIB", "juniAtmSubIfRowStatus"),
        ("Juniper-UNI-ATM-MIB", "juniAtmSubIfDistinguisher"),
        ("Juniper-UNI-ATM-MIB", "juniAtmSubIfLowerIfIndex"),
        ("Juniper-UNI-ATM-MIB", "juniAtmSubIfNbma"),
        ("Juniper-UNI-ATM-MIB", "juniAtmSubIfAddress"),
        ("Juniper-UNI-ATM-MIB", "juniAtmSubIfMtu"),
        ("Juniper-UNI-ATM-MIB", "juniAtmSubIfVccRowStatus"),
        ("Juniper-UNI-ATM-MIB", "juniAtmSubIfVccVcd"),
        ("Juniper-UNI-ATM-MIB", "juniAtmSubIfVccType"),
        ("Juniper-UNI-ATM-MIB", "juniAtmSubIfVccServiceCategory"),
        ("Juniper-UNI-ATM-MIB", "juniAtmSubIfVccPcr"),
        ("Juniper-UNI-ATM-MIB", "juniAtmSubIfVccScr"),
        ("Juniper-UNI-ATM-MIB", "juniAtmSubIfVccMbs"),
        ("Juniper-UNI-ATM-MIB", "juniAtmSubIfInverseArp"),
        ("Juniper-UNI-ATM-MIB", "juniAtmSubIfInverseArpRefresh"),
        ("Juniper-UNI-ATM-MIB", "juniAtmCircuitOamAdminStatus"),
        ("Juniper-UNI-ATM-MIB", "juniAtmCircuitOamLoopbackOperStatus"),
        ("Juniper-UNI-ATM-MIB", "juniAtmCircuitVcOamOperStatus"),
        ("Juniper-UNI-ATM-MIB", "juniAtmCircuitOamLoopbackFrequency"),
        ("Juniper-UNI-ATM-MIB", "juniAtmCircuitInOamF5Cells"),
        ("Juniper-UNI-ATM-MIB", "juniAtmCircuitInOamCellsDropped"),
        ("Juniper-UNI-ATM-MIB", "juniAtmCircuitOutOamF5Cells"),
        ("Juniper-UNI-ATM-MIB", "juniAtmCircuitInOamF5EndToEndLoopbackCells"),
        ("Juniper-UNI-ATM-MIB", "juniAtmCircuitInOamF5SegmentLoopbackCells"),
        ("Juniper-UNI-ATM-MIB", "juniAtmCircuitInOamF5AisCells"),
        ("Juniper-UNI-ATM-MIB", "juniAtmCircuitInOamF5RdiCells"),
        ("Juniper-UNI-ATM-MIB", "juniAtmCircuitOutOamF5EndToEndLoopbackCells"),
        ("Juniper-UNI-ATM-MIB", "juniAtmCircuitOutOamF5SegmentLoopbackCells"),
        ("Juniper-UNI-ATM-MIB", "juniAtmCircuitOutOamF5RdiCells"))
)
if mibBuilder.loadTexts:
    juniAtmSubIfGroup4.setStatus("obsolete")

juniAtmF4OamCircuitGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 4, 2, 20)
)
juniAtmF4OamCircuitGroup.setObjects(
      *(("Juniper-UNI-ATM-MIB", "juniAtmOamF4FlowEndToEndLoopbackTimer"),
        ("Juniper-UNI-ATM-MIB", "juniAtmOamF4FlowEndToEndCCSink"),
        ("Juniper-UNI-ATM-MIB", "juniAtmOamF4FlowEndToEndCCSource"),
        ("Juniper-UNI-ATM-MIB", "juniAtmOamF4FlowEndToEndRowStatus"),
        ("Juniper-UNI-ATM-MIB", "juniAtmOamF4FlowSegmentCCSink"),
        ("Juniper-UNI-ATM-MIB", "juniAtmOamF4FlowSegmentCCSource"),
        ("Juniper-UNI-ATM-MIB", "juniAtmOamF4FlowSegmentRowStatus"),
        ("Juniper-UNI-ATM-MIB", "juniAtmF4FlowInOamEndAisCells"),
        ("Juniper-UNI-ATM-MIB", "juniAtmF4FlowInOamEndRdiCells"),
        ("Juniper-UNI-ATM-MIB", "juniAtmF4FlowInOamEndCCCells"),
        ("Juniper-UNI-ATM-MIB", "juniAtmF4FlowInOamEndCCActDeActCells"),
        ("Juniper-UNI-ATM-MIB", "juniAtmF4FlowInOamEndLoopbackCells"),
        ("Juniper-UNI-ATM-MIB", "juniAtmF4FlowOutEndRdiCells"),
        ("Juniper-UNI-ATM-MIB", "juniAtmF4FlowOutEndCCCells"),
        ("Juniper-UNI-ATM-MIB", "juniAtmF4FlowOutEndCCActDeActCells"),
        ("Juniper-UNI-ATM-MIB", "juniAtmF4FlowOutEndToEndLoopbackCells"),
        ("Juniper-UNI-ATM-MIB", "juniAtmF4FlowEndActualLoopbackFreq"),
        ("Juniper-UNI-ATM-MIB", "juniAtmF4FlowEndLastTimeChanged"),
        ("Juniper-UNI-ATM-MIB", "juniAtmF4FlowOamEndVpOperationState"),
        ("Juniper-UNI-ATM-MIB", "juniAtmF4FlowOamEndVpAdminState"),
        ("Juniper-UNI-ATM-MIB", "juniAtmF4FlowEndInOamCells"),
        ("Juniper-UNI-ATM-MIB", "juniAtmF4FlowEndOutOamCells"),
        ("Juniper-UNI-ATM-MIB", "juniAtmF4FlowEndInOamCellsDropped"),
        ("Juniper-UNI-ATM-MIB", "juniAtmF4FlowInOamSegmentAisCells"),
        ("Juniper-UNI-ATM-MIB", "juniAtmF4FlowInOamSegmentRdiCells"),
        ("Juniper-UNI-ATM-MIB", "juniAtmF4FlowInOamSegmentCCCells"),
        ("Juniper-UNI-ATM-MIB", "juniAtmF4FlowInOamSegmentCCActDeActCells"),
        ("Juniper-UNI-ATM-MIB", "juniAtmF4FlowInOamSegmentLoopbackCells"),
        ("Juniper-UNI-ATM-MIB", "juniAtmF4FlowOutSegmentRdiCells"),
        ("Juniper-UNI-ATM-MIB", "juniAtmF4FlowOutSegmentCCCells"),
        ("Juniper-UNI-ATM-MIB", "juniAtmF4FlowOutSegmentCCActDeActCells"),
        ("Juniper-UNI-ATM-MIB", "juniAtmF4FlowOutSegmentLoopbackCells"),
        ("Juniper-UNI-ATM-MIB", "juniAtmF4FlowSegmentLastTimeChanged"),
        ("Juniper-UNI-ATM-MIB", "juniAtmF4FlowOamSegmentVpOperationState"),
        ("Juniper-UNI-ATM-MIB", "juniAtmF4FlowOamSegmentVpAdminState"),
        ("Juniper-UNI-ATM-MIB", "juniAtmF4FlowSegmentInOamCells"),
        ("Juniper-UNI-ATM-MIB", "juniAtmF4FlowSegmentOutOamCells"),
        ("Juniper-UNI-ATM-MIB", "juniAtmF4FlowSegmentInOamCellsDropped"))
)
if mibBuilder.loadTexts:
    juniAtmF4OamCircuitGroup.setStatus("obsolete")

juniAtmGroup6 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 4, 2, 21)
)
juniAtmGroup6.setObjects(
      *(("Juniper-UNI-ATM-MIB", "juniAtmNextIfIndex"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfRowStatus"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfLowerIfIndex"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfIlmiVpi"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfIlmiVci"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfIlmiVcd"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfIlmiPollFrequency"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfIlmiAdminState"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfUniVersion"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfOamCellRxAdminState"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfInCells"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfOutCells"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfVcCount"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfMapGroup"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfCacAdminState"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfCacUbrWeight"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfCacSubscriptionBandwidth"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfCacAvailableBandwidth"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfCacAvailableBandwidthRx"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfE164Autoconversion"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfE164Gateway"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfE164OneToOneAddrTrans"),
        ("Juniper-UNI-ATM-MIB", "juniAtmPvcStatsInCells"),
        ("Juniper-UNI-ATM-MIB", "juniAtmPvcStatsInCellOctets"),
        ("Juniper-UNI-ATM-MIB", "juniAtmPvcStatsInPackets"),
        ("Juniper-UNI-ATM-MIB", "juniAtmPvcStatsInPacketOctets"),
        ("Juniper-UNI-ATM-MIB", "juniAtmPvcStatsOutCells"),
        ("Juniper-UNI-ATM-MIB", "juniAtmPvcStatsOutCellOctets"),
        ("Juniper-UNI-ATM-MIB", "juniAtmPvcStatsOutPackets"),
        ("Juniper-UNI-ATM-MIB", "juniAtmPvcStatsOutPacketOctets"),
        ("Juniper-UNI-ATM-MIB", "juniAtmPvcStatsInCellErrors"),
        ("Juniper-UNI-ATM-MIB", "juniAtmPvcStatsinPacketErrors"),
        ("Juniper-UNI-ATM-MIB", "juniAtmPvcStatsOutCellErrors"),
        ("Juniper-UNI-ATM-MIB", "juniAtmPvcStatsOutPacketErrors"),
        ("Juniper-UNI-ATM-MIB", "juniAtmPvcStatsInPacketDiscards"),
        ("Juniper-UNI-ATM-MIB", "juniAtmPvcStatsInPacketOctetDiscards"),
        ("Juniper-UNI-ATM-MIB", "juniAtmPvcStatsInPacketUnknownProtocol"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfCapabilityTrafficShaping"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfCapabilityOam"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfCapabilityDefaultVcPerVp"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfCapabilityNumVpiVciBits"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfCapabilityMaxVcd"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfCapabilityMaxVpi"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfCapabilityMaxVci"),
        ("Juniper-UNI-ATM-MIB", "juniAtmVpDescription"),
        ("Juniper-UNI-ATM-MIB", "juniAtmBulkCircuitsNameRowStatus"),
        ("Juniper-UNI-ATM-MIB", "juniAtmBulkCircuitsNameId"),
        ("Juniper-UNI-ATM-MIB", "juniAtmBulkCircuitsIdName"),
        ("Juniper-UNI-ATM-MIB", "juniAtmBulkCircuitsIdNextInstance"),
        ("Juniper-UNI-ATM-MIB", "juniAtmBulkCircuitsRowStatus"),
        ("Juniper-UNI-ATM-MIB", "juniAtmBulkCircuitsMinVpi"),
        ("Juniper-UNI-ATM-MIB", "juniAtmBulkCircuitsMaxVpi"),
        ("Juniper-UNI-ATM-MIB", "juniAtmBulkCircuitsMinVci"),
        ("Juniper-UNI-ATM-MIB", "juniAtmBulkCircuitsMaxVci"))
)
if mibBuilder.loadTexts:
    juniAtmGroup6.setStatus("obsolete")

juniAtmLocationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 4, 2, 22)
)
juniAtmLocationGroup.setObjects(
      *(("Juniper-UNI-ATM-MIB", "juniAtmSubIfLocationType"),
        ("Juniper-UNI-ATM-MIB", "juniAtmSubIfLocationIfIndex"))
)
if mibBuilder.loadTexts:
    juniAtmLocationGroup.setStatus("current")

juniAtmSubIfGroup5 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 4, 2, 23)
)
juniAtmSubIfGroup5.setObjects(
      *(("Juniper-UNI-ATM-MIB", "juniAtmSubIfNextIfIndex"),
        ("Juniper-UNI-ATM-MIB", "juniAtmSubIfRowStatus"),
        ("Juniper-UNI-ATM-MIB", "juniAtmSubIfDistinguisher"),
        ("Juniper-UNI-ATM-MIB", "juniAtmSubIfLowerIfIndex"),
        ("Juniper-UNI-ATM-MIB", "juniAtmSubIfNbma"),
        ("Juniper-UNI-ATM-MIB", "juniAtmSubIfAddress"),
        ("Juniper-UNI-ATM-MIB", "juniAtmSubIfMtu"),
        ("Juniper-UNI-ATM-MIB", "juniAtmSubIfAdvisoryRxSpeed"),
        ("Juniper-UNI-ATM-MIB", "juniAtmSubIfVccRowStatus"),
        ("Juniper-UNI-ATM-MIB", "juniAtmSubIfVccVcd"),
        ("Juniper-UNI-ATM-MIB", "juniAtmSubIfVccType"),
        ("Juniper-UNI-ATM-MIB", "juniAtmSubIfVccServiceCategory"),
        ("Juniper-UNI-ATM-MIB", "juniAtmSubIfVccPcr"),
        ("Juniper-UNI-ATM-MIB", "juniAtmSubIfVccScr"),
        ("Juniper-UNI-ATM-MIB", "juniAtmSubIfVccMbs"),
        ("Juniper-UNI-ATM-MIB", "juniAtmSubIfInverseArp"),
        ("Juniper-UNI-ATM-MIB", "juniAtmSubIfInverseArpRefresh"),
        ("Juniper-UNI-ATM-MIB", "juniAtmCircuitOamAdminStatus"),
        ("Juniper-UNI-ATM-MIB", "juniAtmCircuitOamLoopbackOperStatus"),
        ("Juniper-UNI-ATM-MIB", "juniAtmCircuitVcOamOperStatus"),
        ("Juniper-UNI-ATM-MIB", "juniAtmCircuitOamLoopbackFrequency"),
        ("Juniper-UNI-ATM-MIB", "juniAtmCircuitInOamF5Cells"),
        ("Juniper-UNI-ATM-MIB", "juniAtmCircuitInOamCellsDropped"),
        ("Juniper-UNI-ATM-MIB", "juniAtmCircuitOutOamF5Cells"),
        ("Juniper-UNI-ATM-MIB", "juniAtmCircuitInOamF5EndToEndLoopbackCells"),
        ("Juniper-UNI-ATM-MIB", "juniAtmCircuitInOamF5SegmentLoopbackCells"),
        ("Juniper-UNI-ATM-MIB", "juniAtmCircuitInOamF5AisCells"),
        ("Juniper-UNI-ATM-MIB", "juniAtmCircuitInOamF5RdiCells"),
        ("Juniper-UNI-ATM-MIB", "juniAtmCircuitOutOamF5EndToEndLoopbackCells"),
        ("Juniper-UNI-ATM-MIB", "juniAtmCircuitOutOamF5SegmentLoopbackCells"),
        ("Juniper-UNI-ATM-MIB", "juniAtmCircuitOutOamF5RdiCells"),
        ("Juniper-UNI-ATM-MIB", "juniAtmSubIfDescriptionExport"))
)
if mibBuilder.loadTexts:
    juniAtmSubIfGroup5.setStatus("obsolete")

juniAtmMartiniGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 4, 2, 24)
)
juniAtmMartiniGroup.setObjects(
      *(("Juniper-UNI-ATM-MIB", "juniAtmMartiniTimeoutTimerValue"),
        ("Juniper-UNI-ATM-MIB", "juniAtmSubIfMartiniMaxCellsPerPacket"),
        ("Juniper-UNI-ATM-MIB", "juniAtmSubIfMartiniTimeoutTimerId"))
)
if mibBuilder.loadTexts:
    juniAtmMartiniGroup.setStatus("current")

juniAtmGroup7 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 4, 2, 25)
)
juniAtmGroup7.setObjects(
      *(("Juniper-UNI-ATM-MIB", "juniAtmNextIfIndex"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfRowStatus"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfLowerIfIndex"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfIlmiVpi"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfIlmiVci"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfIlmiVcd"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfIlmiPollFrequency"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfIlmiAdminState"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfUniVersion"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfOamCellRxAdminState"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfInCells"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfOutCells"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfVcCount"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfMapGroup"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfCacAdminState"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfCacUbrWeight"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfCacSubscriptionBandwidth"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfCacAvailableBandwidth"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfCacAvailableBandwidthRx"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfE164Autoconversion"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfE164Gateway"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfE164OneToOneAddrTrans"),
        ("Juniper-UNI-ATM-MIB", "juniAtmPvcStatsInCells"),
        ("Juniper-UNI-ATM-MIB", "juniAtmPvcStatsInCellOctets"),
        ("Juniper-UNI-ATM-MIB", "juniAtmPvcStatsInPackets"),
        ("Juniper-UNI-ATM-MIB", "juniAtmPvcStatsInPacketOctets"),
        ("Juniper-UNI-ATM-MIB", "juniAtmPvcStatsOutCells"),
        ("Juniper-UNI-ATM-MIB", "juniAtmPvcStatsOutCellOctets"),
        ("Juniper-UNI-ATM-MIB", "juniAtmPvcStatsOutPackets"),
        ("Juniper-UNI-ATM-MIB", "juniAtmPvcStatsOutPacketOctets"),
        ("Juniper-UNI-ATM-MIB", "juniAtmPvcStatsInCellErrors"),
        ("Juniper-UNI-ATM-MIB", "juniAtmPvcStatsinPacketErrors"),
        ("Juniper-UNI-ATM-MIB", "juniAtmPvcStatsOutCellErrors"),
        ("Juniper-UNI-ATM-MIB", "juniAtmPvcStatsOutPacketErrors"),
        ("Juniper-UNI-ATM-MIB", "juniAtmPvcStatsInPacketDiscards"),
        ("Juniper-UNI-ATM-MIB", "juniAtmPvcStatsInPacketOctetDiscards"),
        ("Juniper-UNI-ATM-MIB", "juniAtmPvcStatsInPacketUnknownProtocol"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfCapabilityTrafficShaping"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfCapabilityOam"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfCapabilityDefaultVcPerVp"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfCapabilityNumVpiVciBits"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfCapabilityMaxVcd"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfCapabilityMaxVpi"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfCapabilityMaxVci"),
        ("Juniper-UNI-ATM-MIB", "juniAtmVpDescription"),
        ("Juniper-UNI-ATM-MIB", "juniAtmBulkCircuitsNameRowStatus"),
        ("Juniper-UNI-ATM-MIB", "juniAtmBulkCircuitsNameId"),
        ("Juniper-UNI-ATM-MIB", "juniAtmBulkCircuitsIdName"),
        ("Juniper-UNI-ATM-MIB", "juniAtmBulkCircuitsIdNextInstance"),
        ("Juniper-UNI-ATM-MIB", "juniAtmBulkCircuitsRowStatus"),
        ("Juniper-UNI-ATM-MIB", "juniAtmBulkCircuitsMinVpi"),
        ("Juniper-UNI-ATM-MIB", "juniAtmBulkCircuitsMaxVpi"),
        ("Juniper-UNI-ATM-MIB", "juniAtmBulkCircuitsMinVci"),
        ("Juniper-UNI-ATM-MIB", "juniAtmBulkCircuitsMaxVci"),
        ("Juniper-UNI-ATM-MIB", "juniAtmBulkCircuitsAdminState"),
        ("Juniper-UNI-ATM-MIB", "juniAtmProfileOverrideAssignIfCircuitRowStatus"),
        ("Juniper-UNI-ATM-MIB", "juniAtmProfileOverrideAssignIfCircuitProfileId"),
        ("Juniper-UNI-ATM-MIB", "juniAtmProfileOverrideAssignIfCircuitOperStatus"))
)
if mibBuilder.loadTexts:
    juniAtmGroup7.setStatus("obsolete")

juniAtmGroup8 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 4, 2, 26)
)
juniAtmGroup8.setObjects(
      *(("Juniper-UNI-ATM-MIB", "juniAtmNextIfIndex"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfRowStatus"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfLowerIfIndex"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfIlmiVpi"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfIlmiVci"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfIlmiVcd"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfIlmiPollFrequency"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfIlmiAdminState"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfUniVersion"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfOamCellRxAdminState"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfInCells"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfOutCells"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfVcCount"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfMapGroup"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfCacAdminState"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfCacUbrWeight"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfCacSubscriptionBandwidth"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfCacAvailableBandwidth"),
        ("Juniper-UNI-ATM-MIB", "juniAtmPvcStatsInCells"),
        ("Juniper-UNI-ATM-MIB", "juniAtmPvcStatsInCellOctets"),
        ("Juniper-UNI-ATM-MIB", "juniAtmPvcStatsInPackets"),
        ("Juniper-UNI-ATM-MIB", "juniAtmPvcStatsInPacketOctets"),
        ("Juniper-UNI-ATM-MIB", "juniAtmPvcStatsOutCells"),
        ("Juniper-UNI-ATM-MIB", "juniAtmPvcStatsOutCellOctets"),
        ("Juniper-UNI-ATM-MIB", "juniAtmPvcStatsOutPackets"),
        ("Juniper-UNI-ATM-MIB", "juniAtmPvcStatsOutPacketOctets"),
        ("Juniper-UNI-ATM-MIB", "juniAtmPvcStatsInCellErrors"),
        ("Juniper-UNI-ATM-MIB", "juniAtmPvcStatsinPacketErrors"),
        ("Juniper-UNI-ATM-MIB", "juniAtmPvcStatsOutCellErrors"),
        ("Juniper-UNI-ATM-MIB", "juniAtmPvcStatsOutPacketErrors"),
        ("Juniper-UNI-ATM-MIB", "juniAtmPvcStatsInPacketDiscards"),
        ("Juniper-UNI-ATM-MIB", "juniAtmPvcStatsInPacketOctetDiscards"),
        ("Juniper-UNI-ATM-MIB", "juniAtmPvcStatsInPacketUnknownProtocol"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfCapabilityTrafficShaping"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfCapabilityOam"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfCapabilityDefaultVcPerVp"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfCapabilityNumVpiVciBits"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfCapabilityMaxVcd"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfCapabilityMaxVpi"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfCapabilityMaxVci"),
        ("Juniper-UNI-ATM-MIB", "juniAtmVpDescription"),
        ("Juniper-UNI-ATM-MIB", "juniAtmBulkCircuitsNameRowStatus"),
        ("Juniper-UNI-ATM-MIB", "juniAtmBulkCircuitsNameId"),
        ("Juniper-UNI-ATM-MIB", "juniAtmBulkCircuitsIdName"),
        ("Juniper-UNI-ATM-MIB", "juniAtmBulkCircuitsIdNextInstance"),
        ("Juniper-UNI-ATM-MIB", "juniAtmBulkCircuitsRowStatus"),
        ("Juniper-UNI-ATM-MIB", "juniAtmBulkCircuitsMinVpi"),
        ("Juniper-UNI-ATM-MIB", "juniAtmBulkCircuitsMaxVpi"),
        ("Juniper-UNI-ATM-MIB", "juniAtmBulkCircuitsMinVci"),
        ("Juniper-UNI-ATM-MIB", "juniAtmBulkCircuitsMaxVci"),
        ("Juniper-UNI-ATM-MIB", "juniAtmBulkCircuitsAdminState"),
        ("Juniper-UNI-ATM-MIB", "juniAtmProfileOverrideAssignIfCircuitRowStatus"),
        ("Juniper-UNI-ATM-MIB", "juniAtmProfileOverrideAssignIfCircuitProfileId"),
        ("Juniper-UNI-ATM-MIB", "juniAtmProfileOverrideAssignIfCircuitOperStatus"))
)
if mibBuilder.loadTexts:
    juniAtmGroup8.setStatus("obsolete")

juniAtmVpStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 4, 2, 27)
)
juniAtmVpStatsGroup.setObjects(
      *(("Juniper-UNI-ATM-MIB", "juniAtmVpStatsInCells"),
        ("Juniper-UNI-ATM-MIB", "juniAtmVpStatsInPackets"),
        ("Juniper-UNI-ATM-MIB", "juniAtmVpStatsInPacketOctets"),
        ("Juniper-UNI-ATM-MIB", "juniAtmVpStatsOutCells"),
        ("Juniper-UNI-ATM-MIB", "juniAtmVpStatsOutPackets"),
        ("Juniper-UNI-ATM-MIB", "juniAtmVpStatsOutPacketOctets"),
        ("Juniper-UNI-ATM-MIB", "juniAtmVpStatsInPacketErrors"),
        ("Juniper-UNI-ATM-MIB", "juniAtmVpStatsOutPacketErrors"),
        ("Juniper-UNI-ATM-MIB", "juniAtmVpStatsInPacketDiscards"),
        ("Juniper-UNI-ATM-MIB", "juniAtmVpStatsInPacketOctetDiscards"),
        ("Juniper-UNI-ATM-MIB", "juniAtmVpStatsInPacketUnknownProtocol"),
        ("Juniper-UNI-ATM-MIB", "juniAtmVpStatsCrcErrors"),
        ("Juniper-UNI-ATM-MIB", "juniAtmVpStatsSarTimeouts"),
        ("Juniper-UNI-ATM-MIB", "juniAtmVpStatsOverSizedPackets"))
)
if mibBuilder.loadTexts:
    juniAtmVpStatsGroup.setStatus("current")

juniAtmSubIfGroup6 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 4, 2, 28)
)
juniAtmSubIfGroup6.setObjects(
      *(("Juniper-UNI-ATM-MIB", "juniAtmSubIfNextIfIndex"),
        ("Juniper-UNI-ATM-MIB", "juniAtmSubIfRowStatus"),
        ("Juniper-UNI-ATM-MIB", "juniAtmSubIfDistinguisher"),
        ("Juniper-UNI-ATM-MIB", "juniAtmSubIfLowerIfIndex"),
        ("Juniper-UNI-ATM-MIB", "juniAtmSubIfNbma"),
        ("Juniper-UNI-ATM-MIB", "juniAtmSubIfAddress"),
        ("Juniper-UNI-ATM-MIB", "juniAtmSubIfMtu"),
        ("Juniper-UNI-ATM-MIB", "juniAtmSubIfAdvisoryRxSpeed"),
        ("Juniper-UNI-ATM-MIB", "juniAtmSubIfVccRowStatus"),
        ("Juniper-UNI-ATM-MIB", "juniAtmSubIfVccVcd"),
        ("Juniper-UNI-ATM-MIB", "juniAtmSubIfVccType"),
        ("Juniper-UNI-ATM-MIB", "juniAtmSubIfVccServiceCategory"),
        ("Juniper-UNI-ATM-MIB", "juniAtmSubIfVccPcr"),
        ("Juniper-UNI-ATM-MIB", "juniAtmSubIfVccScr"),
        ("Juniper-UNI-ATM-MIB", "juniAtmSubIfVccMbs"),
        ("Juniper-UNI-ATM-MIB", "juniAtmSubIfInverseArp"),
        ("Juniper-UNI-ATM-MIB", "juniAtmSubIfInverseArpRefresh"),
        ("Juniper-UNI-ATM-MIB", "juniAtmCircuitOamAdminStatus"),
        ("Juniper-UNI-ATM-MIB", "juniAtmCircuitOamLoopbackOperStatus"),
        ("Juniper-UNI-ATM-MIB", "juniAtmCircuitVcOamOperStatus"),
        ("Juniper-UNI-ATM-MIB", "juniAtmCircuitOamLoopbackFrequency"),
        ("Juniper-UNI-ATM-MIB", "juniAtmCircuitInOamF5Cells"),
        ("Juniper-UNI-ATM-MIB", "juniAtmCircuitInOamCellsDropped"),
        ("Juniper-UNI-ATM-MIB", "juniAtmCircuitOutOamF5Cells"),
        ("Juniper-UNI-ATM-MIB", "juniAtmCircuitInOamF5EndToEndLoopbackCells"),
        ("Juniper-UNI-ATM-MIB", "juniAtmCircuitInOamF5SegmentLoopbackCells"),
        ("Juniper-UNI-ATM-MIB", "juniAtmCircuitInOamF5AisCells"),
        ("Juniper-UNI-ATM-MIB", "juniAtmCircuitInOamF5RdiCells"),
        ("Juniper-UNI-ATM-MIB", "juniAtmCircuitOutOamF5EndToEndLoopbackCells"),
        ("Juniper-UNI-ATM-MIB", "juniAtmCircuitOutOamF5SegmentLoopbackCells"),
        ("Juniper-UNI-ATM-MIB", "juniAtmCircuitOutOamF5RdiCells"),
        ("Juniper-UNI-ATM-MIB", "juniAtmCircuitInOamF5EndToEndLoopbackCmds"),
        ("Juniper-UNI-ATM-MIB", "juniAtmCircuitInOamF5EndToEndLoopbackRsps"),
        ("Juniper-UNI-ATM-MIB", "juniAtmCircuitInOamF5SegmentLoopbackCmds"),
        ("Juniper-UNI-ATM-MIB", "juniAtmCircuitInOamF5SegmentLoopbackRsps"),
        ("Juniper-UNI-ATM-MIB", "juniAtmCircuitOutOamF5EndToEndLoopbackCmds"),
        ("Juniper-UNI-ATM-MIB", "juniAtmCircuitOutOamF5EndToEndLoopbackRsps"),
        ("Juniper-UNI-ATM-MIB", "juniAtmCircuitOutOamF5SegmentLoopbackCmds"),
        ("Juniper-UNI-ATM-MIB", "juniAtmCircuitOutOamF5SegmentLoopbackRsps"),
        ("Juniper-UNI-ATM-MIB", "juniAtmCircuitOamUpCount"),
        ("Juniper-UNI-ATM-MIB", "juniAtmCircuitOamDownCount"),
        ("Juniper-UNI-ATM-MIB", "juniAtmCircuitOamRetryFrequency"),
        ("Juniper-UNI-ATM-MIB", "juniAtmCircuitOamAlarmDownCount"),
        ("Juniper-UNI-ATM-MIB", "juniAtmCircuitOamAlarmClearTimeout"),
        ("Juniper-UNI-ATM-MIB", "juniAtmSubIfDescriptionExport"))
)
if mibBuilder.loadTexts:
    juniAtmSubIfGroup6.setStatus("obsolete")

juniAtmF4OamCircuitGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 4, 2, 29)
)
juniAtmF4OamCircuitGroup2.setObjects(
      *(("Juniper-UNI-ATM-MIB", "juniAtmOamF4FlowEndToEndLoopbackTimer"),
        ("Juniper-UNI-ATM-MIB", "juniAtmOamF4FlowEndToEndCCSink"),
        ("Juniper-UNI-ATM-MIB", "juniAtmOamF4FlowEndToEndCCSource"),
        ("Juniper-UNI-ATM-MIB", "juniAtmOamF4FlowEndToEndRowStatus"),
        ("Juniper-UNI-ATM-MIB", "juniAtmOamF4FlowSegmentCCSink"),
        ("Juniper-UNI-ATM-MIB", "juniAtmOamF4FlowSegmentCCSource"),
        ("Juniper-UNI-ATM-MIB", "juniAtmOamF4FlowSegmentRowStatus"),
        ("Juniper-UNI-ATM-MIB", "juniAtmF4FlowInOamEndAisCells"),
        ("Juniper-UNI-ATM-MIB", "juniAtmF4FlowInOamEndRdiCells"),
        ("Juniper-UNI-ATM-MIB", "juniAtmF4FlowInOamEndCCCells"),
        ("Juniper-UNI-ATM-MIB", "juniAtmF4FlowInOamEndCCActDeActCells"),
        ("Juniper-UNI-ATM-MIB", "juniAtmF4FlowInOamEndLoopbackCells"),
        ("Juniper-UNI-ATM-MIB", "juniAtmF4FlowOutEndRdiCells"),
        ("Juniper-UNI-ATM-MIB", "juniAtmF4FlowOutEndCCCells"),
        ("Juniper-UNI-ATM-MIB", "juniAtmF4FlowOutEndCCActDeActCells"),
        ("Juniper-UNI-ATM-MIB", "juniAtmF4FlowOutEndToEndLoopbackCells"),
        ("Juniper-UNI-ATM-MIB", "juniAtmF4FlowEndActualLoopbackFreq"),
        ("Juniper-UNI-ATM-MIB", "juniAtmF4FlowEndLastTimeChanged"),
        ("Juniper-UNI-ATM-MIB", "juniAtmF4FlowOamEndVpOperationState"),
        ("Juniper-UNI-ATM-MIB", "juniAtmF4FlowOamEndVpAdminState"),
        ("Juniper-UNI-ATM-MIB", "juniAtmF4FlowEndInOamCells"),
        ("Juniper-UNI-ATM-MIB", "juniAtmF4FlowEndOutOamCells"),
        ("Juniper-UNI-ATM-MIB", "juniAtmF4FlowEndInOamCellsDropped"),
        ("Juniper-UNI-ATM-MIB", "juniAtmF4FlowInOamSegmentAisCells"),
        ("Juniper-UNI-ATM-MIB", "juniAtmF4FlowInOamSegmentRdiCells"),
        ("Juniper-UNI-ATM-MIB", "juniAtmF4FlowInOamSegmentCCCells"),
        ("Juniper-UNI-ATM-MIB", "juniAtmF4FlowInOamSegmentCCActDeActCells"),
        ("Juniper-UNI-ATM-MIB", "juniAtmF4FlowInOamSegmentLoopbackCells"),
        ("Juniper-UNI-ATM-MIB", "juniAtmF4FlowOutSegmentRdiCells"),
        ("Juniper-UNI-ATM-MIB", "juniAtmF4FlowOutSegmentCCCells"),
        ("Juniper-UNI-ATM-MIB", "juniAtmF4FlowOutSegmentCCActDeActCells"),
        ("Juniper-UNI-ATM-MIB", "juniAtmF4FlowOutSegmentLoopbackCells"),
        ("Juniper-UNI-ATM-MIB", "juniAtmF4FlowSegmentLastTimeChanged"),
        ("Juniper-UNI-ATM-MIB", "juniAtmF4FlowOamSegmentVpOperationState"),
        ("Juniper-UNI-ATM-MIB", "juniAtmF4FlowOamSegmentVpAdminState"),
        ("Juniper-UNI-ATM-MIB", "juniAtmF4FlowSegmentInOamCells"),
        ("Juniper-UNI-ATM-MIB", "juniAtmF4FlowSegmentOutOamCells"),
        ("Juniper-UNI-ATM-MIB", "juniAtmF4FlowSegmentInOamCellsDropped"),
        ("Juniper-UNI-ATM-MIB", "juniAtmF4FlowEndToEndInLoopbackCmds"),
        ("Juniper-UNI-ATM-MIB", "juniAtmF4FlowEndToEndInLoopbackRsps"),
        ("Juniper-UNI-ATM-MIB", "juniAtmF4FlowSegmentInLoopbackCmds"),
        ("Juniper-UNI-ATM-MIB", "juniAtmF4FlowSegmentInLoopbackRsps"),
        ("Juniper-UNI-ATM-MIB", "juniAtmF4FlowEndToEndOutLoopbackCmds"),
        ("Juniper-UNI-ATM-MIB", "juniAtmF4FlowEndToEndOutLoopbackRsps"),
        ("Juniper-UNI-ATM-MIB", "juniAtmF4FlowSegmentOutLoopbackCmds"),
        ("Juniper-UNI-ATM-MIB", "juniAtmF4FlowSegmentOutLoopbackRsps"))
)
if mibBuilder.loadTexts:
    juniAtmF4OamCircuitGroup2.setStatus("current")

juniAtmGroup9 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 4, 2, 30)
)
juniAtmGroup9.setObjects(
      *(("Juniper-UNI-ATM-MIB", "juniAtmNextIfIndex"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfRowStatus"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfLowerIfIndex"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfIlmiVpi"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfIlmiVci"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfIlmiVcd"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfIlmiPollFrequency"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfIlmiAdminState"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfUniVersion"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfOamCellRxAdminState"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfInCells"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfOutCells"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfVcCount"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfMapGroup"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfCacAdminState"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfCacUbrWeight"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfCacSubscriptionBandwidth"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfCacAvailableBandwidth"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfAssociatedVcClassId"),
        ("Juniper-UNI-ATM-MIB", "juniAtmPvcStatsInCells"),
        ("Juniper-UNI-ATM-MIB", "juniAtmPvcStatsInCellOctets"),
        ("Juniper-UNI-ATM-MIB", "juniAtmPvcStatsInPackets"),
        ("Juniper-UNI-ATM-MIB", "juniAtmPvcStatsInPacketOctets"),
        ("Juniper-UNI-ATM-MIB", "juniAtmPvcStatsOutCells"),
        ("Juniper-UNI-ATM-MIB", "juniAtmPvcStatsOutCellOctets"),
        ("Juniper-UNI-ATM-MIB", "juniAtmPvcStatsOutPackets"),
        ("Juniper-UNI-ATM-MIB", "juniAtmPvcStatsOutPacketOctets"),
        ("Juniper-UNI-ATM-MIB", "juniAtmPvcStatsInCellErrors"),
        ("Juniper-UNI-ATM-MIB", "juniAtmPvcStatsinPacketErrors"),
        ("Juniper-UNI-ATM-MIB", "juniAtmPvcStatsOutCellErrors"),
        ("Juniper-UNI-ATM-MIB", "juniAtmPvcStatsOutPacketErrors"),
        ("Juniper-UNI-ATM-MIB", "juniAtmPvcStatsInPacketDiscards"),
        ("Juniper-UNI-ATM-MIB", "juniAtmPvcStatsInPacketOctetDiscards"),
        ("Juniper-UNI-ATM-MIB", "juniAtmPvcStatsInPacketUnknownProtocol"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfCapabilityTrafficShaping"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfCapabilityOam"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfCapabilityDefaultVcPerVp"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfCapabilityNumVpiVciBits"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfCapabilityMaxVcd"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfCapabilityMaxVpi"),
        ("Juniper-UNI-ATM-MIB", "juniAtmIfCapabilityMaxVci"),
        ("Juniper-UNI-ATM-MIB", "juniAtmVpDescription"),
        ("Juniper-UNI-ATM-MIB", "juniAtmBulkCircuitsNameRowStatus"),
        ("Juniper-UNI-ATM-MIB", "juniAtmBulkCircuitsNameId"),
        ("Juniper-UNI-ATM-MIB", "juniAtmBulkCircuitsIdName"),
        ("Juniper-UNI-ATM-MIB", "juniAtmBulkCircuitsIdNextInstance"),
        ("Juniper-UNI-ATM-MIB", "juniAtmBulkCircuitsRowStatus"),
        ("Juniper-UNI-ATM-MIB", "juniAtmBulkCircuitsMinVpi"),
        ("Juniper-UNI-ATM-MIB", "juniAtmBulkCircuitsMaxVpi"),
        ("Juniper-UNI-ATM-MIB", "juniAtmBulkCircuitsMinVci"),
        ("Juniper-UNI-ATM-MIB", "juniAtmBulkCircuitsMaxVci"),
        ("Juniper-UNI-ATM-MIB", "juniAtmBulkCircuitsAdminState"),
        ("Juniper-UNI-ATM-MIB", "juniAtmProfileOverrideAssignIfCircuitRowStatus"),
        ("Juniper-UNI-ATM-MIB", "juniAtmProfileOverrideAssignIfCircuitProfileId"),
        ("Juniper-UNI-ATM-MIB", "juniAtmProfileOverrideAssignIfCircuitOperStatus"))
)
if mibBuilder.loadTexts:
    juniAtmGroup9.setStatus("current")

juniAtmSubIfGroup7 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 4, 2, 31)
)
juniAtmSubIfGroup7.setObjects(
      *(("Juniper-UNI-ATM-MIB", "juniAtmSubIfNextIfIndex"),
        ("Juniper-UNI-ATM-MIB", "juniAtmSubIfRowStatus"),
        ("Juniper-UNI-ATM-MIB", "juniAtmSubIfDistinguisher"),
        ("Juniper-UNI-ATM-MIB", "juniAtmSubIfLowerIfIndex"),
        ("Juniper-UNI-ATM-MIB", "juniAtmSubIfNbma"),
        ("Juniper-UNI-ATM-MIB", "juniAtmSubIfAddress"),
        ("Juniper-UNI-ATM-MIB", "juniAtmSubIfMtu"),
        ("Juniper-UNI-ATM-MIB", "juniAtmSubIfAdvisoryRxSpeed"),
        ("Juniper-UNI-ATM-MIB", "juniAtmSubIfAssociatedVcClassId"),
        ("Juniper-UNI-ATM-MIB", "juniAtmSubIfVccRowStatus"),
        ("Juniper-UNI-ATM-MIB", "juniAtmSubIfVccVcd"),
        ("Juniper-UNI-ATM-MIB", "juniAtmSubIfVccType"),
        ("Juniper-UNI-ATM-MIB", "juniAtmSubIfVccServiceCategory"),
        ("Juniper-UNI-ATM-MIB", "juniAtmSubIfVccPcr"),
        ("Juniper-UNI-ATM-MIB", "juniAtmSubIfVccScr"),
        ("Juniper-UNI-ATM-MIB", "juniAtmSubIfVccMbs"),
        ("Juniper-UNI-ATM-MIB", "juniAtmSubIfInverseArp"),
        ("Juniper-UNI-ATM-MIB", "juniAtmSubIfInverseArpRefresh"),
        ("Juniper-UNI-ATM-MIB", "juniAtmSubIfVccAssociatedVcClassId"),
        ("Juniper-UNI-ATM-MIB", "juniAtmCircuitOamAdminStatus"),
        ("Juniper-UNI-ATM-MIB", "juniAtmCircuitOamLoopbackOperStatus"),
        ("Juniper-UNI-ATM-MIB", "juniAtmCircuitVcOamOperStatus"),
        ("Juniper-UNI-ATM-MIB", "juniAtmCircuitOamLoopbackFrequency"),
        ("Juniper-UNI-ATM-MIB", "juniAtmCircuitInOamF5Cells"),
        ("Juniper-UNI-ATM-MIB", "juniAtmCircuitInOamCellsDropped"),
        ("Juniper-UNI-ATM-MIB", "juniAtmCircuitOutOamF5Cells"),
        ("Juniper-UNI-ATM-MIB", "juniAtmCircuitInOamF5EndToEndLoopbackCells"),
        ("Juniper-UNI-ATM-MIB", "juniAtmCircuitInOamF5SegmentLoopbackCells"),
        ("Juniper-UNI-ATM-MIB", "juniAtmCircuitInOamF5AisCells"),
        ("Juniper-UNI-ATM-MIB", "juniAtmCircuitInOamF5RdiCells"),
        ("Juniper-UNI-ATM-MIB", "juniAtmCircuitOutOamF5EndToEndLoopbackCells"),
        ("Juniper-UNI-ATM-MIB", "juniAtmCircuitOutOamF5SegmentLoopbackCells"),
        ("Juniper-UNI-ATM-MIB", "juniAtmCircuitOutOamF5RdiCells"),
        ("Juniper-UNI-ATM-MIB", "juniAtmCircuitInOamF5EndToEndLoopbackCmds"),
        ("Juniper-UNI-ATM-MIB", "juniAtmCircuitInOamF5EndToEndLoopbackRsps"),
        ("Juniper-UNI-ATM-MIB", "juniAtmCircuitInOamF5SegmentLoopbackCmds"),
        ("Juniper-UNI-ATM-MIB", "juniAtmCircuitInOamF5SegmentLoopbackRsps"),
        ("Juniper-UNI-ATM-MIB", "juniAtmCircuitOutOamF5EndToEndLoopbackCmds"),
        ("Juniper-UNI-ATM-MIB", "juniAtmCircuitOutOamF5EndToEndLoopbackRsps"),
        ("Juniper-UNI-ATM-MIB", "juniAtmCircuitOutOamF5SegmentLoopbackCmds"),
        ("Juniper-UNI-ATM-MIB", "juniAtmCircuitOutOamF5SegmentLoopbackRsps"),
        ("Juniper-UNI-ATM-MIB", "juniAtmCircuitOamUpCount"),
        ("Juniper-UNI-ATM-MIB", "juniAtmCircuitOamDownCount"),
        ("Juniper-UNI-ATM-MIB", "juniAtmCircuitOamRetryFrequency"),
        ("Juniper-UNI-ATM-MIB", "juniAtmCircuitOamAlarmDownCount"),
        ("Juniper-UNI-ATM-MIB", "juniAtmCircuitOamAlarmClearTimeout"),
        ("Juniper-UNI-ATM-MIB", "juniAtmSubIfDescriptionExport"))
)
if mibBuilder.loadTexts:
    juniAtmSubIfGroup7.setStatus("current")

juniAtmVcClassGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 4, 2, 32)
)
juniAtmVcClassGroup.setObjects(
      *(("Juniper-UNI-ATM-MIB", "juniAtmVcClassName"),
        ("Juniper-UNI-ATM-MIB", "juniAtmVcClassNameRowStatus"),
        ("Juniper-UNI-ATM-MIB", "juniAtmVcClassNameId"),
        ("Juniper-UNI-ATM-MIB", "juniAtmVcClassIdName"),
        ("Juniper-UNI-ATM-MIB", "juniAtmVcClassVccType"),
        ("Juniper-UNI-ATM-MIB", "juniAtmVcClassVccServiceCategory"),
        ("Juniper-UNI-ATM-MIB", "juniAtmVcClassVccPcr"),
        ("Juniper-UNI-ATM-MIB", "juniAtmVcClassVccScr"),
        ("Juniper-UNI-ATM-MIB", "juniAtmVcClassVccMbs"),
        ("Juniper-UNI-ATM-MIB", "juniAtmVcClassVccOamAdminStatus"),
        ("Juniper-UNI-ATM-MIB", "juniAtmVcClassVccOamLoopbackFrequency"),
        ("Juniper-UNI-ATM-MIB", "juniAtmVcClassVccOamUpCount"),
        ("Juniper-UNI-ATM-MIB", "juniAtmVcClassVccOamDownCount"),
        ("Juniper-UNI-ATM-MIB", "juniAtmVcClassVccOamRetryFrequency"),
        ("Juniper-UNI-ATM-MIB", "juniAtmVcClassVccOamAlarmDownCount"),
        ("Juniper-UNI-ATM-MIB", "juniAtmVcClassVccOamAlarmClearTimeout"),
        ("Juniper-UNI-ATM-MIB", "juniAtmVcClassVccInverseArp"),
        ("Juniper-UNI-ATM-MIB", "juniAtmVcClassVccInverseArpRefresh"))
)
if mibBuilder.loadTexts:
    juniAtmVcClassGroup.setStatus("current")


# Notification objects

juniAtmVpPingTestCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 3, 0, 1)
)
juniAtmVpPingTestCompleted.setObjects(
      *(("ATM-FORUM-SNMP-M4-MIB", "atmfM4VpTestId"),
        ("ATM-FORUM-SNMP-M4-MIB", "atmfM4VpTestType"),
        ("ATM-FORUM-SNMP-M4-MIB", "atmfM4VpTestResult"),
        ("Juniper-UNI-ATM-MIB", "juniAtmVpPingProbeCount"),
        ("Juniper-UNI-ATM-MIB", "juniAtmVpPingSentProbes"),
        ("Juniper-UNI-ATM-MIB", "juniAtmVpPingProbeResponses"),
        ("Juniper-UNI-ATM-MIB", "juniAtmVpPingMinRtt"),
        ("Juniper-UNI-ATM-MIB", "juniAtmVpPingMaxRtt"),
        ("Juniper-UNI-ATM-MIB", "juniAtmVpPingAverageRtt"),
        ("ATM-FORUM-SNMP-M4-MIB", "atmfM4VpTestCode"))
)
if mibBuilder.loadTexts:
    juniAtmVpPingTestCompleted.setStatus(
        "current"
    )

juniAtmVcPingTestCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 3, 0, 2)
)
juniAtmVcPingTestCompleted.setObjects(
      *(("ATM-FORUM-SNMP-M4-MIB", "atmfM4VcTestId"),
        ("ATM-FORUM-SNMP-M4-MIB", "atmfM4VcTestType"),
        ("ATM-FORUM-SNMP-M4-MIB", "atmfM4VcTestResult"),
        ("Juniper-UNI-ATM-MIB", "juniAtmVcPingProbeCount"),
        ("Juniper-UNI-ATM-MIB", "juniAtmVcPingSentProbes"),
        ("Juniper-UNI-ATM-MIB", "juniAtmVcPingProbeResponses"),
        ("Juniper-UNI-ATM-MIB", "juniAtmVcPingMinRtt"),
        ("Juniper-UNI-ATM-MIB", "juniAtmVcPingMaxRtt"),
        ("Juniper-UNI-ATM-MIB", "juniAtmVcPingAverageRtt"),
        ("ATM-FORUM-SNMP-M4-MIB", "atmfM4VcTestCode"))
)
if mibBuilder.loadTexts:
    juniAtmVcPingTestCompleted.setStatus(
        "current"
    )


# Notifications groups

juniAtmPingTrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 4, 2, 9)
)
juniAtmPingTrapGroup.setObjects(
      *(("Juniper-UNI-ATM-MIB", "juniAtmVpPingTestCompleted"),
        ("Juniper-UNI-ATM-MIB", "juniAtmVcPingTestCompleted"))
)
if mibBuilder.loadTexts:
    juniAtmPingTrapGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

juniAtmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 4, 1, 1)
)
if mibBuilder.loadTexts:
    juniAtmCompliance.setStatus(
        "obsolete"
    )

juniAtmCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 4, 1, 2)
)
if mibBuilder.loadTexts:
    juniAtmCompliance2.setStatus(
        "obsolete"
    )

juniAtmCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 4, 1, 3)
)
if mibBuilder.loadTexts:
    juniAtmCompliance3.setStatus(
        "obsolete"
    )

juniAtmCompliance4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 4, 1, 4)
)
if mibBuilder.loadTexts:
    juniAtmCompliance4.setStatus(
        "obsolete"
    )

juniAtmCompliance5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 4, 1, 5)
)
if mibBuilder.loadTexts:
    juniAtmCompliance5.setStatus(
        "obsolete"
    )

juniAtmCompliance6 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 4, 1, 6)
)
if mibBuilder.loadTexts:
    juniAtmCompliance6.setStatus(
        "obsolete"
    )

juniAtmCompliance7 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 4, 1, 7)
)
if mibBuilder.loadTexts:
    juniAtmCompliance7.setStatus(
        "obsolete"
    )

juniAtmCompliance8 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 4, 1, 8)
)
if mibBuilder.loadTexts:
    juniAtmCompliance8.setStatus(
        "obsolete"
    )

juniAtmCompliance9 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 4, 1, 9)
)
if mibBuilder.loadTexts:
    juniAtmCompliance9.setStatus(
        "obsolete"
    )

juniAtmCompliance10 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 4, 1, 10)
)
if mibBuilder.loadTexts:
    juniAtmCompliance10.setStatus(
        "obsolete"
    )

juniAtmCompliance11 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 4, 1, 11)
)
if mibBuilder.loadTexts:
    juniAtmCompliance11.setStatus(
        "obsolete"
    )

juniAtmCompliance12 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 4, 1, 12)
)
if mibBuilder.loadTexts:
    juniAtmCompliance12.setStatus(
        "obsolete"
    )

juniAtmCompliance13 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 4, 1, 13)
)
if mibBuilder.loadTexts:
    juniAtmCompliance13.setStatus(
        "obsolete"
    )

juniAtmCompliance14 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 8, 4, 1, 14)
)
if mibBuilder.loadTexts:
    juniAtmCompliance14.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Juniper-UNI-ATM-MIB",
    **{"JuniAtmNbmaMapName": JuniAtmNbmaMapName,
       "JuniAtmNbmaMapNameOrNull": JuniAtmNbmaMapNameOrNull,
       "JuniAtmLocationType": JuniAtmLocationType,
       "JuniAtmLocationValue": JuniAtmLocationValue,
       "juniAtmMIB": juniAtmMIB,
       "juniAtmObjects": juniAtmObjects,
       "juniAtmIfLayer": juniAtmIfLayer,
       "juniAtmNextIfIndex": juniAtmNextIfIndex,
       "juniAtmIfTable": juniAtmIfTable,
       "juniAtmIfEntry": juniAtmIfEntry,
       "juniAtmIfIndex": juniAtmIfIndex,
       "juniAtmIfRowStatus": juniAtmIfRowStatus,
       "juniAtmIfLowerIfIndex": juniAtmIfLowerIfIndex,
       "juniAtmIfIlmiVpi": juniAtmIfIlmiVpi,
       "juniAtmIfIlmiVci": juniAtmIfIlmiVci,
       "juniAtmIfIlmiVcd": juniAtmIfIlmiVcd,
       "juniAtmIfIlmiPollFrequency": juniAtmIfIlmiPollFrequency,
       "juniAtmIfIlmiAdminState": juniAtmIfIlmiAdminState,
       "juniAtmIfUniVersion": juniAtmIfUniVersion,
       "juniAtmIfOamCellRxAdminState": juniAtmIfOamCellRxAdminState,
       "juniAtmIfInCells": juniAtmIfInCells,
       "juniAtmIfOutCells": juniAtmIfOutCells,
       "juniAtmIfVcCount": juniAtmIfVcCount,
       "juniAtmIfMapGroup": juniAtmIfMapGroup,
       "juniAtmIfCacAdminState": juniAtmIfCacAdminState,
       "juniAtmIfCacUbrWeight": juniAtmIfCacUbrWeight,
       "juniAtmIfCacSubscriptionBandwidth": juniAtmIfCacSubscriptionBandwidth,
       "juniAtmIfCacAvailableBandwidth": juniAtmIfCacAvailableBandwidth,
       "juniAtmIfCacAvailableBandwidthRx": juniAtmIfCacAvailableBandwidthRx,
       "juniAtmIfE164Autoconversion": juniAtmIfE164Autoconversion,
       "juniAtmIfE164Gateway": juniAtmIfE164Gateway,
       "juniAtmIfE164OneToOneAddrTrans": juniAtmIfE164OneToOneAddrTrans,
       "juniAtmIfOamCellFilter": juniAtmIfOamCellFilter,
       "juniAtmIfCacUsedBandwidthUpper": juniAtmIfCacUsedBandwidthUpper,
       "juniAtmIfCacUsedBandwidthLower": juniAtmIfCacUsedBandwidthLower,
       "juniAtmIfAssociatedVcClassId": juniAtmIfAssociatedVcClassId,
       "juniAtmPvcStatisticsTable": juniAtmPvcStatisticsTable,
       "juniAtmPvcStatisticsEntry": juniAtmPvcStatisticsEntry,
       "juniAtmPvcStatsIfIndex": juniAtmPvcStatsIfIndex,
       "juniAtmPvcStatsVpi": juniAtmPvcStatsVpi,
       "juniAtmPvcStatsVci": juniAtmPvcStatsVci,
       "juniAtmPvcStatsInCells": juniAtmPvcStatsInCells,
       "juniAtmPvcStatsInCellOctets": juniAtmPvcStatsInCellOctets,
       "juniAtmPvcStatsInPackets": juniAtmPvcStatsInPackets,
       "juniAtmPvcStatsInPacketOctets": juniAtmPvcStatsInPacketOctets,
       "juniAtmPvcStatsOutCells": juniAtmPvcStatsOutCells,
       "juniAtmPvcStatsOutCellOctets": juniAtmPvcStatsOutCellOctets,
       "juniAtmPvcStatsOutPackets": juniAtmPvcStatsOutPackets,
       "juniAtmPvcStatsOutPacketOctets": juniAtmPvcStatsOutPacketOctets,
       "juniAtmPvcStatsInCellErrors": juniAtmPvcStatsInCellErrors,
       "juniAtmPvcStatsinPacketErrors": juniAtmPvcStatsinPacketErrors,
       "juniAtmPvcStatsOutCellErrors": juniAtmPvcStatsOutCellErrors,
       "juniAtmPvcStatsOutPacketErrors": juniAtmPvcStatsOutPacketErrors,
       "juniAtmPvcStatsInPacketDiscards": juniAtmPvcStatsInPacketDiscards,
       "juniAtmPvcStatsInPacketOctetDiscards": juniAtmPvcStatsInPacketOctetDiscards,
       "juniAtmPvcStatsInPacketUnknownProtocol": juniAtmPvcStatsInPacketUnknownProtocol,
       "juniAtmVpTunnelTable": juniAtmVpTunnelTable,
       "juniAtmVpTunnelEntry": juniAtmVpTunnelEntry,
       "juniAtmVpTunnelIfIndex": juniAtmVpTunnelIfIndex,
       "juniAtmVpTunnelVpi": juniAtmVpTunnelVpi,
       "juniAtmVpTunnelKbps": juniAtmVpTunnelKbps,
       "juniAtmVpTunnelRowStatus": juniAtmVpTunnelRowStatus,
       "juniAtmVpTunnelServiceCategory": juniAtmVpTunnelServiceCategory,
       "juniAtmIfCapabilityTable": juniAtmIfCapabilityTable,
       "juniAtmIfCapabilityEntry": juniAtmIfCapabilityEntry,
       "juniAtmIfCapabilityIndex": juniAtmIfCapabilityIndex,
       "juniAtmIfCapabilityTrafficShaping": juniAtmIfCapabilityTrafficShaping,
       "juniAtmIfCapabilityOam": juniAtmIfCapabilityOam,
       "juniAtmIfCapabilityDefaultVcPerVp": juniAtmIfCapabilityDefaultVcPerVp,
       "juniAtmIfCapabilityNumVpiVciBits": juniAtmIfCapabilityNumVpiVciBits,
       "juniAtmIfCapabilityMaxVcd": juniAtmIfCapabilityMaxVcd,
       "juniAtmIfCapabilityMaxVpi": juniAtmIfCapabilityMaxVpi,
       "juniAtmIfCapabilityMaxVci": juniAtmIfCapabilityMaxVci,
       "juniAtmIfCapabilityOamCellFilter": juniAtmIfCapabilityOamCellFilter,
       "juniAtmIfSvcSignallingTable": juniAtmIfSvcSignallingTable,
       "juniAtmIfSvcSignallingEntry": juniAtmIfSvcSignallingEntry,
       "juniAtmIfSvcSignallingVpi": juniAtmIfSvcSignallingVpi,
       "juniAtmIfSvcSignallingVci": juniAtmIfSvcSignallingVci,
       "juniAtmIfSvcSignallingVcd": juniAtmIfSvcSignallingVcd,
       "juniAtmIfSvcSignallingAdminStatus": juniAtmIfSvcSignallingAdminStatus,
       "juniAtmIfPnniRccTable": juniAtmIfPnniRccTable,
       "juniAtmIfPnniRccEntry": juniAtmIfPnniRccEntry,
       "juniAtmIfPnniRccVpi": juniAtmIfPnniRccVpi,
       "juniAtmIfPnniRccVci": juniAtmIfPnniRccVci,
       "juniAtmIfPnniRccVcd": juniAtmIfPnniRccVcd,
       "juniAtmIfPnniRccAdminStatus": juniAtmIfPnniRccAdminStatus,
       "juniAtmOamF4FlowEndToEndCfgTable": juniAtmOamF4FlowEndToEndCfgTable,
       "juniAtmOamF4FlowEndToEndCfgEntry": juniAtmOamF4FlowEndToEndCfgEntry,
       "juniAtmOamF4FlowEndToEndIfIndex": juniAtmOamF4FlowEndToEndIfIndex,
       "juniAtmOamF4FlowEndToEndVpi": juniAtmOamF4FlowEndToEndVpi,
       "juniAtmOamF4FlowEndToEndLoopbackTimer": juniAtmOamF4FlowEndToEndLoopbackTimer,
       "juniAtmOamF4FlowEndToEndCCSink": juniAtmOamF4FlowEndToEndCCSink,
       "juniAtmOamF4FlowEndToEndCCSource": juniAtmOamF4FlowEndToEndCCSource,
       "juniAtmOamF4FlowEndToEndRowStatus": juniAtmOamF4FlowEndToEndRowStatus,
       "juniAtmOamF4FlowSegmentCfgTable": juniAtmOamF4FlowSegmentCfgTable,
       "juniAtmOamF4FlowSegmentCfgEntry": juniAtmOamF4FlowSegmentCfgEntry,
       "juniAtmOamF4FlowSegmentIfIndex": juniAtmOamF4FlowSegmentIfIndex,
       "juniAtmOamF4FlowSegmentVpi": juniAtmOamF4FlowSegmentVpi,
       "juniAtmOamF4FlowSegmentCCSink": juniAtmOamF4FlowSegmentCCSink,
       "juniAtmOamF4FlowSegmentCCSource": juniAtmOamF4FlowSegmentCCSource,
       "juniAtmOamF4FlowSegmentRowStatus": juniAtmOamF4FlowSegmentRowStatus,
       "juniAtmVpDescrTable": juniAtmVpDescrTable,
       "juniAtmVpDescrEntry": juniAtmVpDescrEntry,
       "juniAtmVpDescription": juniAtmVpDescription,
       "juniAtmF4FlowOamEndToEndStatsTable": juniAtmF4FlowOamEndToEndStatsTable,
       "juniAtmF4FlowOamEndToEndStatsEntry": juniAtmF4FlowOamEndToEndStatsEntry,
       "juniAtmF4FlowInOamEndAisCells": juniAtmF4FlowInOamEndAisCells,
       "juniAtmF4FlowInOamEndRdiCells": juniAtmF4FlowInOamEndRdiCells,
       "juniAtmF4FlowInOamEndCCCells": juniAtmF4FlowInOamEndCCCells,
       "juniAtmF4FlowInOamEndCCActDeActCells": juniAtmF4FlowInOamEndCCActDeActCells,
       "juniAtmF4FlowInOamEndLoopbackCells": juniAtmF4FlowInOamEndLoopbackCells,
       "juniAtmF4FlowOutEndRdiCells": juniAtmF4FlowOutEndRdiCells,
       "juniAtmF4FlowOutEndCCCells": juniAtmF4FlowOutEndCCCells,
       "juniAtmF4FlowOutEndCCActDeActCells": juniAtmF4FlowOutEndCCActDeActCells,
       "juniAtmF4FlowOutEndToEndLoopbackCells": juniAtmF4FlowOutEndToEndLoopbackCells,
       "juniAtmF4FlowEndActualLoopbackFreq": juniAtmF4FlowEndActualLoopbackFreq,
       "juniAtmF4FlowEndLastTimeChanged": juniAtmF4FlowEndLastTimeChanged,
       "juniAtmF4FlowOamEndVpOperationState": juniAtmF4FlowOamEndVpOperationState,
       "juniAtmF4FlowOamEndVpAdminState": juniAtmF4FlowOamEndVpAdminState,
       "juniAtmF4FlowEndInOamCells": juniAtmF4FlowEndInOamCells,
       "juniAtmF4FlowEndOutOamCells": juniAtmF4FlowEndOutOamCells,
       "juniAtmF4FlowEndInOamCellsDropped": juniAtmF4FlowEndInOamCellsDropped,
       "juniAtmF4FlowEndToEndInLoopbackCmds": juniAtmF4FlowEndToEndInLoopbackCmds,
       "juniAtmF4FlowEndToEndInLoopbackRsps": juniAtmF4FlowEndToEndInLoopbackRsps,
       "juniAtmF4FlowEndToEndOutLoopbackCmds": juniAtmF4FlowEndToEndOutLoopbackCmds,
       "juniAtmF4FlowEndToEndOutLoopbackRsps": juniAtmF4FlowEndToEndOutLoopbackRsps,
       "juniAtmF4FlowOamSegmentStatsTable": juniAtmF4FlowOamSegmentStatsTable,
       "juniAtmF4FlowOamSegmentStatsEntry": juniAtmF4FlowOamSegmentStatsEntry,
       "juniAtmF4FlowInOamSegmentAisCells": juniAtmF4FlowInOamSegmentAisCells,
       "juniAtmF4FlowInOamSegmentRdiCells": juniAtmF4FlowInOamSegmentRdiCells,
       "juniAtmF4FlowInOamSegmentCCCells": juniAtmF4FlowInOamSegmentCCCells,
       "juniAtmF4FlowInOamSegmentCCActDeActCells": juniAtmF4FlowInOamSegmentCCActDeActCells,
       "juniAtmF4FlowInOamSegmentLoopbackCells": juniAtmF4FlowInOamSegmentLoopbackCells,
       "juniAtmF4FlowOutSegmentRdiCells": juniAtmF4FlowOutSegmentRdiCells,
       "juniAtmF4FlowOutSegmentCCCells": juniAtmF4FlowOutSegmentCCCells,
       "juniAtmF4FlowOutSegmentCCActDeActCells": juniAtmF4FlowOutSegmentCCActDeActCells,
       "juniAtmF4FlowOutSegmentLoopbackCells": juniAtmF4FlowOutSegmentLoopbackCells,
       "juniAtmF4FlowSegmentLastTimeChanged": juniAtmF4FlowSegmentLastTimeChanged,
       "juniAtmF4FlowOamSegmentVpOperationState": juniAtmF4FlowOamSegmentVpOperationState,
       "juniAtmF4FlowOamSegmentVpAdminState": juniAtmF4FlowOamSegmentVpAdminState,
       "juniAtmF4FlowSegmentInOamCells": juniAtmF4FlowSegmentInOamCells,
       "juniAtmF4FlowSegmentOutOamCells": juniAtmF4FlowSegmentOutOamCells,
       "juniAtmF4FlowSegmentInOamCellsDropped": juniAtmF4FlowSegmentInOamCellsDropped,
       "juniAtmF4FlowSegmentInLoopbackCmds": juniAtmF4FlowSegmentInLoopbackCmds,
       "juniAtmF4FlowSegmentInLoopbackRsps": juniAtmF4FlowSegmentInLoopbackRsps,
       "juniAtmF4FlowSegmentOutLoopbackCmds": juniAtmF4FlowSegmentOutLoopbackCmds,
       "juniAtmF4FlowSegmentOutLoopbackRsps": juniAtmF4FlowSegmentOutLoopbackRsps,
       "juniAtmMartiniTimeoutTimerTable": juniAtmMartiniTimeoutTimerTable,
       "juniAtmMartiniTimeoutTimerEntry": juniAtmMartiniTimeoutTimerEntry,
       "juniAtmMartiniTimeoutTimerIndex": juniAtmMartiniTimeoutTimerIndex,
       "juniAtmMartiniTimeoutTimerValue": juniAtmMartiniTimeoutTimerValue,
       "juniAtmVpStatsTable": juniAtmVpStatsTable,
       "juniAtmVpStatsEntry": juniAtmVpStatsEntry,
       "juniAtmVpStatsIfIndex": juniAtmVpStatsIfIndex,
       "juniAtmVpStatsVpi": juniAtmVpStatsVpi,
       "juniAtmVpStatsInCells": juniAtmVpStatsInCells,
       "juniAtmVpStatsInPackets": juniAtmVpStatsInPackets,
       "juniAtmVpStatsInPacketOctets": juniAtmVpStatsInPacketOctets,
       "juniAtmVpStatsOutCells": juniAtmVpStatsOutCells,
       "juniAtmVpStatsOutPackets": juniAtmVpStatsOutPackets,
       "juniAtmVpStatsOutPacketOctets": juniAtmVpStatsOutPacketOctets,
       "juniAtmVpStatsInPacketErrors": juniAtmVpStatsInPacketErrors,
       "juniAtmVpStatsOutPacketErrors": juniAtmVpStatsOutPacketErrors,
       "juniAtmVpStatsInPacketDiscards": juniAtmVpStatsInPacketDiscards,
       "juniAtmVpStatsInPacketOctetDiscards": juniAtmVpStatsInPacketOctetDiscards,
       "juniAtmVpStatsInPacketUnknownProtocol": juniAtmVpStatsInPacketUnknownProtocol,
       "juniAtmVpStatsCrcErrors": juniAtmVpStatsCrcErrors,
       "juniAtmVpStatsSarTimeouts": juniAtmVpStatsSarTimeouts,
       "juniAtmVpStatsOverSizedPackets": juniAtmVpStatsOverSizedPackets,
       "juniAtmAal5IfLayer": juniAtmAal5IfLayer,
       "juniAtmAal5NextIfIndex": juniAtmAal5NextIfIndex,
       "juniAtmAal5IfTable": juniAtmAal5IfTable,
       "juniAtmAal5IfEntry": juniAtmAal5IfEntry,
       "juniAtmAal5IfIndex": juniAtmAal5IfIndex,
       "juniAtmAal5IfRowStatus": juniAtmAal5IfRowStatus,
       "juniAtmAal5IfLowerIfIndex": juniAtmAal5IfLowerIfIndex,
       "juniAtmBulkCircuitsNameTable": juniAtmBulkCircuitsNameTable,
       "juniAtmBulkCircuitsNameEntry": juniAtmBulkCircuitsNameEntry,
       "juniAtmBulkCircuitsNameAal5IfIndex": juniAtmBulkCircuitsNameAal5IfIndex,
       "juniAtmBulkCircuitsNameName": juniAtmBulkCircuitsNameName,
       "juniAtmBulkCircuitsNameRowStatus": juniAtmBulkCircuitsNameRowStatus,
       "juniAtmBulkCircuitsNameId": juniAtmBulkCircuitsNameId,
       "juniAtmBulkCircuitsIdTable": juniAtmBulkCircuitsIdTable,
       "juniAtmBulkCircuitsIdEntry": juniAtmBulkCircuitsIdEntry,
       "juniAtmBulkCircuitsIdAal5IfIndex": juniAtmBulkCircuitsIdAal5IfIndex,
       "juniAtmBulkCircuitsIdId": juniAtmBulkCircuitsIdId,
       "juniAtmBulkCircuitsIdName": juniAtmBulkCircuitsIdName,
       "juniAtmBulkCircuitsIdNextInstance": juniAtmBulkCircuitsIdNextInstance,
       "juniAtmBulkCircuitsTable": juniAtmBulkCircuitsTable,
       "juniAtmBulkCircuitsEntry": juniAtmBulkCircuitsEntry,
       "juniAtmBulkCircuitsAal5IfIndex": juniAtmBulkCircuitsAal5IfIndex,
       "juniAtmBulkCircuitsId": juniAtmBulkCircuitsId,
       "juniAtmBulkCircuitsInstance": juniAtmBulkCircuitsInstance,
       "juniAtmBulkCircuitsRowStatus": juniAtmBulkCircuitsRowStatus,
       "juniAtmBulkCircuitsMinVpi": juniAtmBulkCircuitsMinVpi,
       "juniAtmBulkCircuitsMaxVpi": juniAtmBulkCircuitsMaxVpi,
       "juniAtmBulkCircuitsMinVci": juniAtmBulkCircuitsMinVci,
       "juniAtmBulkCircuitsMaxVci": juniAtmBulkCircuitsMaxVci,
       "juniAtmBulkCircuitsAdminState": juniAtmBulkCircuitsAdminState,
       "juniAtmProfileOverrideAssignIfCircuitTable": juniAtmProfileOverrideAssignIfCircuitTable,
       "juniAtmProfileOverrideAssignIfCircuitEntry": juniAtmProfileOverrideAssignIfCircuitEntry,
       "juniAtmProfileOverrideAssignIfCircuitAal5Index": juniAtmProfileOverrideAssignIfCircuitAal5Index,
       "juniAtmProfileOverrideAssignIfCircuitRangeId": juniAtmProfileOverrideAssignIfCircuitRangeId,
       "juniAtmProfileOverrideAssignIfCircuitVpi": juniAtmProfileOverrideAssignIfCircuitVpi,
       "juniAtmProfileOverrideAssignIfCircuitVci": juniAtmProfileOverrideAssignIfCircuitVci,
       "juniAtmProfileOverrideAssignIfCircuitRowStatus": juniAtmProfileOverrideAssignIfCircuitRowStatus,
       "juniAtmProfileOverrideAssignIfCircuitProfileId": juniAtmProfileOverrideAssignIfCircuitProfileId,
       "juniAtmProfileOverrideAssignIfCircuitOperStatus": juniAtmProfileOverrideAssignIfCircuitOperStatus,
       "juniAtmSubIfLayer": juniAtmSubIfLayer,
       "juniAtmSubIfNextIfIndex": juniAtmSubIfNextIfIndex,
       "juniAtmSubIfTable": juniAtmSubIfTable,
       "juniAtmSubIfEntry": juniAtmSubIfEntry,
       "juniAtmSubIfIndex": juniAtmSubIfIndex,
       "juniAtmSubIfRowStatus": juniAtmSubIfRowStatus,
       "juniAtmSubIfDistinguisher": juniAtmSubIfDistinguisher,
       "juniAtmSubIfLowerIfIndex": juniAtmSubIfLowerIfIndex,
       "juniAtmSubIfNbma": juniAtmSubIfNbma,
       "juniAtmSubIfAddress": juniAtmSubIfAddress,
       "juniAtmSubIfMtu": juniAtmSubIfMtu,
       "juniAtmSubIfAdvisoryRxSpeed": juniAtmSubIfAdvisoryRxSpeed,
       "juniAtmSubIfMartiniMaxCellsPerPacket": juniAtmSubIfMartiniMaxCellsPerPacket,
       "juniAtmSubIfMartiniTimeoutTimerId": juniAtmSubIfMartiniTimeoutTimerId,
       "juniAtmSubIfAssociatedVcClassId": juniAtmSubIfAssociatedVcClassId,
       "juniAtmSubIfVccTable": juniAtmSubIfVccTable,
       "juniAtmSubIfVccEntry": juniAtmSubIfVccEntry,
       "juniAtmSubIfVccVpi": juniAtmSubIfVccVpi,
       "juniAtmSubIfVccVci": juniAtmSubIfVccVci,
       "juniAtmSubIfVccRowStatus": juniAtmSubIfVccRowStatus,
       "juniAtmSubIfVccVcd": juniAtmSubIfVccVcd,
       "juniAtmSubIfVccType": juniAtmSubIfVccType,
       "juniAtmSubIfVccServiceCategory": juniAtmSubIfVccServiceCategory,
       "juniAtmSubIfVccPcr": juniAtmSubIfVccPcr,
       "juniAtmSubIfVccScr": juniAtmSubIfVccScr,
       "juniAtmSubIfVccMbs": juniAtmSubIfVccMbs,
       "juniAtmSubIfInverseArp": juniAtmSubIfInverseArp,
       "juniAtmSubIfInverseArpRefresh": juniAtmSubIfInverseArpRefresh,
       "juniAtmSubIfVccAssociatedVcClassId": juniAtmSubIfVccAssociatedVcClassId,
       "juniAtmCircuitOamTable": juniAtmCircuitOamTable,
       "juniAtmCircuitOamEntry": juniAtmCircuitOamEntry,
       "juniAtmCircuitOamIfIndex": juniAtmCircuitOamIfIndex,
       "juniAtmCircuitOamVpi": juniAtmCircuitOamVpi,
       "juniAtmCircuitOamVci": juniAtmCircuitOamVci,
       "juniAtmCircuitOamAdminStatus": juniAtmCircuitOamAdminStatus,
       "juniAtmCircuitOamLoopbackOperStatus": juniAtmCircuitOamLoopbackOperStatus,
       "juniAtmCircuitVcOamOperStatus": juniAtmCircuitVcOamOperStatus,
       "juniAtmCircuitOamLoopbackFrequency": juniAtmCircuitOamLoopbackFrequency,
       "juniAtmCircuitInOamF5Cells": juniAtmCircuitInOamF5Cells,
       "juniAtmCircuitInOamCellsDropped": juniAtmCircuitInOamCellsDropped,
       "juniAtmCircuitOutOamF5Cells": juniAtmCircuitOutOamF5Cells,
       "juniAtmCircuitInOamF5EndToEndLoopbackCells": juniAtmCircuitInOamF5EndToEndLoopbackCells,
       "juniAtmCircuitInOamF5SegmentLoopbackCells": juniAtmCircuitInOamF5SegmentLoopbackCells,
       "juniAtmCircuitInOamF5AisCells": juniAtmCircuitInOamF5AisCells,
       "juniAtmCircuitInOamF5RdiCells": juniAtmCircuitInOamF5RdiCells,
       "juniAtmCircuitOutOamF5EndToEndLoopbackCells": juniAtmCircuitOutOamF5EndToEndLoopbackCells,
       "juniAtmCircuitOutOamF5SegmentLoopbackCells": juniAtmCircuitOutOamF5SegmentLoopbackCells,
       "juniAtmCircuitOutOamF5RdiCells": juniAtmCircuitOutOamF5RdiCells,
       "juniAtmCircuitInOamF5EndToEndLoopbackCmds": juniAtmCircuitInOamF5EndToEndLoopbackCmds,
       "juniAtmCircuitInOamF5EndToEndLoopbackRsps": juniAtmCircuitInOamF5EndToEndLoopbackRsps,
       "juniAtmCircuitInOamF5SegmentLoopbackCmds": juniAtmCircuitInOamF5SegmentLoopbackCmds,
       "juniAtmCircuitInOamF5SegmentLoopbackRsps": juniAtmCircuitInOamF5SegmentLoopbackRsps,
       "juniAtmCircuitOutOamF5EndToEndLoopbackCmds": juniAtmCircuitOutOamF5EndToEndLoopbackCmds,
       "juniAtmCircuitOutOamF5EndToEndLoopbackRsps": juniAtmCircuitOutOamF5EndToEndLoopbackRsps,
       "juniAtmCircuitOutOamF5SegmentLoopbackCmds": juniAtmCircuitOutOamF5SegmentLoopbackCmds,
       "juniAtmCircuitOutOamF5SegmentLoopbackRsps": juniAtmCircuitOutOamF5SegmentLoopbackRsps,
       "juniAtmCircuitOamUpCount": juniAtmCircuitOamUpCount,
       "juniAtmCircuitOamDownCount": juniAtmCircuitOamDownCount,
       "juniAtmCircuitOamRetryFrequency": juniAtmCircuitOamRetryFrequency,
       "juniAtmCircuitOamAlarmDownCount": juniAtmCircuitOamAlarmDownCount,
       "juniAtmCircuitOamAlarmClearTimeout": juniAtmCircuitOamAlarmClearTimeout,
       "juniAtmSubIfVccTrafficShapingTable": juniAtmSubIfVccTrafficShapingTable,
       "juniAtmSubIfVccTrafficShapingEntry": juniAtmSubIfVccTrafficShapingEntry,
       "juniAtmSubIfVccTrafficShapingCdvt": juniAtmSubIfVccTrafficShapingCdvt,
       "juniAtmSubIfVccTrafficShapingClp0": juniAtmSubIfVccTrafficShapingClp0,
       "juniAtmSubIfVccTrafficShapingTagging": juniAtmSubIfVccTrafficShapingTagging,
       "juniAtmSubIfVccTrafficShapingPoliceObserve": juniAtmSubIfVccTrafficShapingPoliceObserve,
       "juniAtmSubIfVccTrafficShapingPacketShaping": juniAtmSubIfVccTrafficShapingPacketShaping,
       "juniAtmSubIfSvcConfigTable": juniAtmSubIfSvcConfigTable,
       "juniAtmSubIfSvcConfigEntry": juniAtmSubIfSvcConfigEntry,
       "juniAtmSubIfSvcRowStatus": juniAtmSubIfSvcRowStatus,
       "juniAtmSubIfSvcConfigDestAtmAddress": juniAtmSubIfSvcConfigDestAtmAddress,
       "juniAtmSubIfSvcConfigCircuitType": juniAtmSubIfSvcConfigCircuitType,
       "juniAtmSubIfSvcConfigServiceCategory": juniAtmSubIfSvcConfigServiceCategory,
       "juniAtmSubIfSvcConfigPcr": juniAtmSubIfSvcConfigPcr,
       "juniAtmSubIfSvcConfigScr": juniAtmSubIfSvcConfigScr,
       "juniAtmSubIfSvcConfigMbs": juniAtmSubIfSvcConfigMbs,
       "juniAtmSubIfSvcConfigCdvt": juniAtmSubIfSvcConfigCdvt,
       "juniAtmSubIfSvcConfigClp0": juniAtmSubIfSvcConfigClp0,
       "juniAtmSubIfSvcConfigTagging": juniAtmSubIfSvcConfigTagging,
       "juniAtmSubIfSvcConfigObserve": juniAtmSubIfSvcConfigObserve,
       "juniAtmSubIfSvcConfigPacketDiscard": juniAtmSubIfSvcConfigPacketDiscard,
       "juniAtmSubIfSvcConfigDestE164Address": juniAtmSubIfSvcConfigDestE164Address,
       "juniAtmSubIfDescriptionExport": juniAtmSubIfDescriptionExport,
       "juniAtmNbma": juniAtmNbma,
       "juniAtmNbmaMapTable": juniAtmNbmaMapTable,
       "juniAtmNbmaMapEntry": juniAtmNbmaMapEntry,
       "juniAtmNbmaMapName": juniAtmNbmaMapName,
       "juniAtmNbmaMapVcd": juniAtmNbmaMapVcd,
       "juniAtmNbmaMapIpAddress": juniAtmNbmaMapIpAddress,
       "juniAtmNbmaMapVpi": juniAtmNbmaMapVpi,
       "juniAtmNbmaMapVci": juniAtmNbmaMapVci,
       "juniAtmNbmaMapIfIndex": juniAtmNbmaMapIfIndex,
       "juniAtmNbmaMapBroadcast": juniAtmNbmaMapBroadcast,
       "juniAtmNbmaMapRowStatus": juniAtmNbmaMapRowStatus,
       "juniAtmNbmaMapListTable": juniAtmNbmaMapListTable,
       "juniAtmNbmaMapListEntry": juniAtmNbmaMapListEntry,
       "juniAtmNbmaMapListName": juniAtmNbmaMapListName,
       "juniAtmNbmaMapListRowStatus": juniAtmNbmaMapListRowStatus,
       "juniAtmPing": juniAtmPing,
       "juniAtmPingTestTypes": juniAtmPingTestTypes,
       "juniAtmPingTestOamSeg": juniAtmPingTestOamSeg,
       "juniAtmPingTestOamE2E": juniAtmPingTestOamE2E,
       "juniAtmVpPingTable": juniAtmVpPingTable,
       "juniAtmVpPingEntry": juniAtmVpPingEntry,
       "juniAtmVpPingProbeCount": juniAtmVpPingProbeCount,
       "juniAtmVpPingTimeOut": juniAtmVpPingTimeOut,
       "juniAtmVpPingCtlTrapGeneration": juniAtmVpPingCtlTrapGeneration,
       "juniAtmVpPingSentProbes": juniAtmVpPingSentProbes,
       "juniAtmVpPingProbeResponses": juniAtmVpPingProbeResponses,
       "juniAtmVpPingStartTime": juniAtmVpPingStartTime,
       "juniAtmVpPingMinRtt": juniAtmVpPingMinRtt,
       "juniAtmVpPingMaxRtt": juniAtmVpPingMaxRtt,
       "juniAtmVpPingAverageRtt": juniAtmVpPingAverageRtt,
       "juniAtmVcPingTable": juniAtmVcPingTable,
       "juniAtmVcPingEntry": juniAtmVcPingEntry,
       "juniAtmVcPingProbeCount": juniAtmVcPingProbeCount,
       "juniAtmVcPingTimeOut": juniAtmVcPingTimeOut,
       "juniAtmVcPingCtlTrapGeneration": juniAtmVcPingCtlTrapGeneration,
       "juniAtmVcPingSentProbes": juniAtmVcPingSentProbes,
       "juniAtmVcPingProbeResponses": juniAtmVcPingProbeResponses,
       "juniAtmVcPingStartTime": juniAtmVcPingStartTime,
       "juniAtmVcPingMinRtt": juniAtmVcPingMinRtt,
       "juniAtmVcPingMaxRtt": juniAtmVcPingMaxRtt,
       "juniAtmVcPingAverageRtt": juniAtmVcPingAverageRtt,
       "juniAtmPingTestCode": juniAtmPingTestCode,
       "juniAtmPingTestCodeOamDisabled": juniAtmPingTestCodeOamDisabled,
       "juniAtmPingTestCodeCircuitDown": juniAtmPingTestCodeCircuitDown,
       "juniAtmPingTestCodeStopped": juniAtmPingTestCodeStopped,
       "juniAtmPingTestCodeOamVcOperState": juniAtmPingTestCodeOamVcOperState,
       "juniAtmPingTestCodeMaxPingCountReached": juniAtmPingTestCodeMaxPingCountReached,
       "juniAtmPingTestCodeInvalidParams": juniAtmPingTestCodeInvalidParams,
       "juniAtmLocation": juniAtmLocation,
       "juniAtmSubIfLocationType": juniAtmSubIfLocationType,
       "juniAtmSubIfLocationTable": juniAtmSubIfLocationTable,
       "juniAtmSubIfLocationEntry": juniAtmSubIfLocationEntry,
       "juniAtmSubIfLocationIndex": juniAtmSubIfLocationIndex,
       "juniAtmSubIfLocationIfIndex": juniAtmSubIfLocationIfIndex,
       "juniAtmVcClass": juniAtmVcClass,
       "juniAtmVcClassNameTable": juniAtmVcClassNameTable,
       "juniAtmVcClassNameEntry": juniAtmVcClassNameEntry,
       "juniAtmVcClassName": juniAtmVcClassName,
       "juniAtmVcClassNameRowStatus": juniAtmVcClassNameRowStatus,
       "juniAtmVcClassNameId": juniAtmVcClassNameId,
       "juniAtmVcClassIdTable": juniAtmVcClassIdTable,
       "juniAtmVcClassIdEntry": juniAtmVcClassIdEntry,
       "juniAtmVcClassIdId": juniAtmVcClassIdId,
       "juniAtmVcClassIdName": juniAtmVcClassIdName,
       "juniAtmVcClassTable": juniAtmVcClassTable,
       "juniAtmVcClassEntry": juniAtmVcClassEntry,
       "juniAtmVcClassId": juniAtmVcClassId,
       "juniAtmVcClassVccType": juniAtmVcClassVccType,
       "juniAtmVcClassVccServiceCategory": juniAtmVcClassVccServiceCategory,
       "juniAtmVcClassVccPcr": juniAtmVcClassVccPcr,
       "juniAtmVcClassVccScr": juniAtmVcClassVccScr,
       "juniAtmVcClassVccMbs": juniAtmVcClassVccMbs,
       "juniAtmVcClassVccOamAdminStatus": juniAtmVcClassVccOamAdminStatus,
       "juniAtmVcClassVccOamLoopbackFrequency": juniAtmVcClassVccOamLoopbackFrequency,
       "juniAtmVcClassVccOamUpCount": juniAtmVcClassVccOamUpCount,
       "juniAtmVcClassVccOamDownCount": juniAtmVcClassVccOamDownCount,
       "juniAtmVcClassVccOamRetryFrequency": juniAtmVcClassVccOamRetryFrequency,
       "juniAtmVcClassVccOamAlarmDownCount": juniAtmVcClassVccOamAlarmDownCount,
       "juniAtmVcClassVccOamAlarmClearTimeout": juniAtmVcClassVccOamAlarmClearTimeout,
       "juniAtmVcClassVccInverseArp": juniAtmVcClassVccInverseArp,
       "juniAtmVcClassVccInverseArpRefresh": juniAtmVcClassVccInverseArpRefresh,
       "juniAtmTraps": juniAtmTraps,
       "juniAtmTrapPrefix": juniAtmTrapPrefix,
       "juniAtmVpPingTestCompleted": juniAtmVpPingTestCompleted,
       "juniAtmVcPingTestCompleted": juniAtmVcPingTestCompleted,
       "juniAtmConformance": juniAtmConformance,
       "juniAtmCompliances": juniAtmCompliances,
       "juniAtmCompliance": juniAtmCompliance,
       "juniAtmCompliance2": juniAtmCompliance2,
       "juniAtmCompliance3": juniAtmCompliance3,
       "juniAtmCompliance4": juniAtmCompliance4,
       "juniAtmCompliance5": juniAtmCompliance5,
       "juniAtmCompliance6": juniAtmCompliance6,
       "juniAtmCompliance7": juniAtmCompliance7,
       "juniAtmCompliance8": juniAtmCompliance8,
       "juniAtmCompliance9": juniAtmCompliance9,
       "juniAtmCompliance10": juniAtmCompliance10,
       "juniAtmCompliance11": juniAtmCompliance11,
       "juniAtmCompliance12": juniAtmCompliance12,
       "juniAtmCompliance13": juniAtmCompliance13,
       "juniAtmCompliance14": juniAtmCompliance14,
       "juniAtmGroups": juniAtmGroups,
       "juniAtmGroup": juniAtmGroup,
       "juniAtmAal5Group": juniAtmAal5Group,
       "juniAtmSubIfGroup": juniAtmSubIfGroup,
       "juniAtmVpTunnelGroup": juniAtmVpTunnelGroup,
       "juniAtmNbmaMapGroup": juniAtmNbmaMapGroup,
       "juniAtmSubIfGroup2": juniAtmSubIfGroup2,
       "juniAtmVpPingControlGroup": juniAtmVpPingControlGroup,
       "juniAtmVcPingControlGroup": juniAtmVcPingControlGroup,
       "juniAtmPingTrapGroup": juniAtmPingTrapGroup,
       "juniAtmGroup2": juniAtmGroup2,
       "juniAtmTrafficShapingGroup": juniAtmTrafficShapingGroup,
       "juniAtmGroup3": juniAtmGroup3,
       "juniAtmGroup4": juniAtmGroup4,
       "juniAtmSvcGroup": juniAtmSvcGroup,
       "juniAtmSubIfGroup3": juniAtmSubIfGroup3,
       "juniAtmGroup5": juniAtmGroup5,
       "juniAtmSvcGroup2": juniAtmSvcGroup2,
       "juniAtmPnniGroup": juniAtmPnniGroup,
       "juniAtmSubIfGroup4": juniAtmSubIfGroup4,
       "juniAtmF4OamCircuitGroup": juniAtmF4OamCircuitGroup,
       "juniAtmGroup6": juniAtmGroup6,
       "juniAtmLocationGroup": juniAtmLocationGroup,
       "juniAtmSubIfGroup5": juniAtmSubIfGroup5,
       "juniAtmMartiniGroup": juniAtmMartiniGroup,
       "juniAtmGroup7": juniAtmGroup7,
       "juniAtmGroup8": juniAtmGroup8,
       "juniAtmVpStatsGroup": juniAtmVpStatsGroup,
       "juniAtmSubIfGroup6": juniAtmSubIfGroup6,
       "juniAtmF4OamCircuitGroup2": juniAtmF4OamCircuitGroup2,
       "juniAtmGroup9": juniAtmGroup9,
       "juniAtmSubIfGroup7": juniAtmSubIfGroup7,
       "juniAtmVcClassGroup": juniAtmVcClassGroup}
)
