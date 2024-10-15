# SNMP MIB module (ADTRAN-AOS-MUX-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ADTRAN-AOS-MUX-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:34:09 2024
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

(adGenAOSCommon,
 adGenAOSConformance) = mibBuilder.importSymbols(
    "ADTRAN-AOS",
    "adGenAOSCommon",
    "adGenAOSConformance")

(adIdentity,) = mibBuilder.importSymbols(
    "ADTRAN-MIB",
    "adIdentity")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

adGenAOSMuxID = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 53, 1, 5)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AdGenAOSMux_ObjectIdentity = ObjectIdentity
adGenAOSMux = _AdGenAOSMux_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 5)
)
_AdGenAOSXConnect_ObjectIdentity = ObjectIdentity
adGenAOSXConnect = _AdGenAOSXConnect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 5, 1)
)
_AdGenAOSXConnectTable_Object = MibTable
adGenAOSXConnectTable = _AdGenAOSXConnectTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 5, 1, 1)
)
if mibBuilder.loadTexts:
    adGenAOSXConnectTable.setStatus("current")
_AdGenAOSXConnectEntry_Object = MibTableRow
adGenAOSXConnectEntry = _AdGenAOSXConnectEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 5, 1, 1, 1)
)
adGenAOSXConnectEntry.setIndexNames(
    (0, "ADTRAN-AOS-MUX-MIB", "adGenAOSXConnectIndex"),
)
if mibBuilder.loadTexts:
    adGenAOSXConnectEntry.setStatus("current")


class _AdGenAOSXConnectIndex_Type(Integer32):
    """Custom type adGenAOSXConnectIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_AdGenAOSXConnectIndex_Type.__name__ = "Integer32"
_AdGenAOSXConnectIndex_Object = MibTableColumn
adGenAOSXConnectIndex = _AdGenAOSXConnectIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 5, 1, 1, 1, 1),
    _AdGenAOSXConnectIndex_Type()
)
adGenAOSXConnectIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenAOSXConnectIndex.setStatus("current")


class _AdGenAOSXConnectFirstIfType_Type(Integer32):
    """Custom type adGenAOSXConnectFirstIfType based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("dds", 1),
          ("eth", 3),
          ("frameRelay", 7),
          ("fxs", 6),
          ("notAssigned", 0),
          ("ppp", 8),
          ("serial", 4),
          ("shdsl", 5),
          ("t1E1", 2))
    )


_AdGenAOSXConnectFirstIfType_Type.__name__ = "Integer32"
_AdGenAOSXConnectFirstIfType_Object = MibTableColumn
adGenAOSXConnectFirstIfType = _AdGenAOSXConnectFirstIfType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 5, 1, 1, 1, 2),
    _AdGenAOSXConnectFirstIfType_Type()
)
adGenAOSXConnectFirstIfType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenAOSXConnectFirstIfType.setStatus("current")


class _AdGenAOSXConnectFirstIfNumber_Type(Integer32):
    """Custom type adGenAOSXConnectFirstIfNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_AdGenAOSXConnectFirstIfNumber_Type.__name__ = "Integer32"
_AdGenAOSXConnectFirstIfNumber_Object = MibTableColumn
adGenAOSXConnectFirstIfNumber = _AdGenAOSXConnectFirstIfNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 5, 1, 1, 1, 3),
    _AdGenAOSXConnectFirstIfNumber_Type()
)
adGenAOSXConnectFirstIfNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenAOSXConnectFirstIfNumber.setStatus("current")


class _AdGenAOSXConnectFirstSubIfNumber_Type(Integer32):
    """Custom type adGenAOSXConnectFirstSubIfNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1007),
    )


_AdGenAOSXConnectFirstSubIfNumber_Type.__name__ = "Integer32"
_AdGenAOSXConnectFirstSubIfNumber_Object = MibTableColumn
adGenAOSXConnectFirstSubIfNumber = _AdGenAOSXConnectFirstSubIfNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 5, 1, 1, 1, 4),
    _AdGenAOSXConnectFirstSubIfNumber_Type()
)
adGenAOSXConnectFirstSubIfNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenAOSXConnectFirstSubIfNumber.setStatus("current")


class _AdGenAOSXConnectFirstIfSlot_Type(Integer32):
    """Custom type adGenAOSXConnectFirstIfSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_AdGenAOSXConnectFirstIfSlot_Type.__name__ = "Integer32"
_AdGenAOSXConnectFirstIfSlot_Object = MibTableColumn
adGenAOSXConnectFirstIfSlot = _AdGenAOSXConnectFirstIfSlot_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 5, 1, 1, 1, 5),
    _AdGenAOSXConnectFirstIfSlot_Type()
)
adGenAOSXConnectFirstIfSlot.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenAOSXConnectFirstIfSlot.setStatus("current")


class _AdGenAOSXConnectFirstIfPort_Type(Integer32):
    """Custom type adGenAOSXConnectFirstIfPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 48),
    )


_AdGenAOSXConnectFirstIfPort_Type.__name__ = "Integer32"
_AdGenAOSXConnectFirstIfPort_Object = MibTableColumn
adGenAOSXConnectFirstIfPort = _AdGenAOSXConnectFirstIfPort_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 5, 1, 1, 1, 6),
    _AdGenAOSXConnectFirstIfPort_Type()
)
adGenAOSXConnectFirstIfPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenAOSXConnectFirstIfPort.setStatus("current")


class _AdGenAOSXConnectFirstTdmGroup_Type(Integer32):
    """Custom type adGenAOSXConnectFirstTdmGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AdGenAOSXConnectFirstTdmGroup_Type.__name__ = "Integer32"
_AdGenAOSXConnectFirstTdmGroup_Object = MibTableColumn
adGenAOSXConnectFirstTdmGroup = _AdGenAOSXConnectFirstTdmGroup_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 5, 1, 1, 1, 7),
    _AdGenAOSXConnectFirstTdmGroup_Type()
)
adGenAOSXConnectFirstTdmGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenAOSXConnectFirstTdmGroup.setStatus("current")


class _AdGenAOSXConnectFirstTdmGroupDS0_Type(Integer32):
    """Custom type adGenAOSXConnectFirstTdmGroupDS0 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_AdGenAOSXConnectFirstTdmGroupDS0_Type.__name__ = "Integer32"
_AdGenAOSXConnectFirstTdmGroupDS0_Object = MibTableColumn
adGenAOSXConnectFirstTdmGroupDS0 = _AdGenAOSXConnectFirstTdmGroupDS0_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 5, 1, 1, 1, 8),
    _AdGenAOSXConnectFirstTdmGroupDS0_Type()
)
adGenAOSXConnectFirstTdmGroupDS0.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenAOSXConnectFirstTdmGroupDS0.setStatus("current")


class _AdGenAOSXConnectSecondIfType_Type(Integer32):
    """Custom type adGenAOSXConnectSecondIfType based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("dds", 1),
          ("eth", 3),
          ("frameRelay", 7),
          ("fxs", 6),
          ("notAssigned", 0),
          ("ppp", 8),
          ("serial", 4),
          ("shdsl", 5),
          ("t1E1", 2))
    )


_AdGenAOSXConnectSecondIfType_Type.__name__ = "Integer32"
_AdGenAOSXConnectSecondIfType_Object = MibTableColumn
adGenAOSXConnectSecondIfType = _AdGenAOSXConnectSecondIfType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 5, 1, 1, 1, 9),
    _AdGenAOSXConnectSecondIfType_Type()
)
adGenAOSXConnectSecondIfType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenAOSXConnectSecondIfType.setStatus("current")


class _AdGenAOSXConnectSecondIfNumber_Type(Integer32):
    """Custom type adGenAOSXConnectSecondIfNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_AdGenAOSXConnectSecondIfNumber_Type.__name__ = "Integer32"
_AdGenAOSXConnectSecondIfNumber_Object = MibTableColumn
adGenAOSXConnectSecondIfNumber = _AdGenAOSXConnectSecondIfNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 5, 1, 1, 1, 10),
    _AdGenAOSXConnectSecondIfNumber_Type()
)
adGenAOSXConnectSecondIfNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenAOSXConnectSecondIfNumber.setStatus("current")


class _AdGenAOSXConnectSecondSubIfNumber_Type(Integer32):
    """Custom type adGenAOSXConnectSecondSubIfNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1007),
    )


_AdGenAOSXConnectSecondSubIfNumber_Type.__name__ = "Integer32"
_AdGenAOSXConnectSecondSubIfNumber_Object = MibTableColumn
adGenAOSXConnectSecondSubIfNumber = _AdGenAOSXConnectSecondSubIfNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 5, 1, 1, 1, 11),
    _AdGenAOSXConnectSecondSubIfNumber_Type()
)
adGenAOSXConnectSecondSubIfNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenAOSXConnectSecondSubIfNumber.setStatus("current")


class _AdGenAOSXConnectSecondIfSlot_Type(Integer32):
    """Custom type adGenAOSXConnectSecondIfSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_AdGenAOSXConnectSecondIfSlot_Type.__name__ = "Integer32"
_AdGenAOSXConnectSecondIfSlot_Object = MibTableColumn
adGenAOSXConnectSecondIfSlot = _AdGenAOSXConnectSecondIfSlot_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 5, 1, 1, 1, 12),
    _AdGenAOSXConnectSecondIfSlot_Type()
)
adGenAOSXConnectSecondIfSlot.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenAOSXConnectSecondIfSlot.setStatus("current")


class _AdGenAOSXConnectSecondIfPort_Type(Integer32):
    """Custom type adGenAOSXConnectSecondIfPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 48),
    )


_AdGenAOSXConnectSecondIfPort_Type.__name__ = "Integer32"
_AdGenAOSXConnectSecondIfPort_Object = MibTableColumn
adGenAOSXConnectSecondIfPort = _AdGenAOSXConnectSecondIfPort_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 5, 1, 1, 1, 13),
    _AdGenAOSXConnectSecondIfPort_Type()
)
adGenAOSXConnectSecondIfPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenAOSXConnectSecondIfPort.setStatus("current")


class _AdGenAOSXConnectSecondTdmGroup_Type(Integer32):
    """Custom type adGenAOSXConnectSecondTdmGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AdGenAOSXConnectSecondTdmGroup_Type.__name__ = "Integer32"
_AdGenAOSXConnectSecondTdmGroup_Object = MibTableColumn
adGenAOSXConnectSecondTdmGroup = _AdGenAOSXConnectSecondTdmGroup_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 5, 1, 1, 1, 14),
    _AdGenAOSXConnectSecondTdmGroup_Type()
)
adGenAOSXConnectSecondTdmGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenAOSXConnectSecondTdmGroup.setStatus("current")


class _AdGenAOSXConnectSecondTdmGroupDS0_Type(Integer32):
    """Custom type adGenAOSXConnectSecondTdmGroupDS0 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_AdGenAOSXConnectSecondTdmGroupDS0_Type.__name__ = "Integer32"
_AdGenAOSXConnectSecondTdmGroupDS0_Object = MibTableColumn
adGenAOSXConnectSecondTdmGroupDS0 = _AdGenAOSXConnectSecondTdmGroupDS0_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 5, 1, 1, 1, 15),
    _AdGenAOSXConnectSecondTdmGroupDS0_Type()
)
adGenAOSXConnectSecondTdmGroupDS0.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenAOSXConnectSecondTdmGroupDS0.setStatus("current")


class _AdGenAOSXConnectPreserveRbs_Type(Integer32):
    """Custom type adGenAOSXConnectPreserveRbs based on Integer32"""
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


_AdGenAOSXConnectPreserveRbs_Type.__name__ = "Integer32"
_AdGenAOSXConnectPreserveRbs_Object = MibTableColumn
adGenAOSXConnectPreserveRbs = _AdGenAOSXConnectPreserveRbs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 5, 1, 1, 1, 16),
    _AdGenAOSXConnectPreserveRbs_Type()
)
adGenAOSXConnectPreserveRbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenAOSXConnectPreserveRbs.setStatus("current")
_AdGenAOSXConnectRowStatus_Type = RowStatus
_AdGenAOSXConnectRowStatus_Object = MibTableColumn
adGenAOSXConnectRowStatus = _AdGenAOSXConnectRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 5, 1, 1, 1, 17),
    _AdGenAOSXConnectRowStatus_Type()
)
adGenAOSXConnectRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenAOSXConnectRowStatus.setStatus("current")
_AdGenAOSTdmGroup_ObjectIdentity = ObjectIdentity
adGenAOSTdmGroup = _AdGenAOSTdmGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 5, 2)
)
_AdGenAOSTdmGroupTable_Object = MibTable
adGenAOSTdmGroupTable = _AdGenAOSTdmGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 5, 2, 1)
)
if mibBuilder.loadTexts:
    adGenAOSTdmGroupTable.setStatus("current")
_AdGenAOSTdmGroupEntry_Object = MibTableRow
adGenAOSTdmGroupEntry = _AdGenAOSTdmGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 5, 2, 1, 1)
)
adGenAOSTdmGroupEntry.setIndexNames(
    (0, "ADTRAN-AOS-MUX-MIB", "adGenAOSTdmGroupIfSlot"),
    (0, "ADTRAN-AOS-MUX-MIB", "adGenAOSTdmGroupIfPort"),
    (0, "ADTRAN-AOS-MUX-MIB", "adGenAOSTdmGroupID"),
)
if mibBuilder.loadTexts:
    adGenAOSTdmGroupEntry.setStatus("current")


class _AdGenAOSTdmGroupIfSlot_Type(Integer32):
    """Custom type adGenAOSTdmGroupIfSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_AdGenAOSTdmGroupIfSlot_Type.__name__ = "Integer32"
_AdGenAOSTdmGroupIfSlot_Object = MibTableColumn
adGenAOSTdmGroupIfSlot = _AdGenAOSTdmGroupIfSlot_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 5, 2, 1, 1, 1),
    _AdGenAOSTdmGroupIfSlot_Type()
)
adGenAOSTdmGroupIfSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSTdmGroupIfSlot.setStatus("current")


class _AdGenAOSTdmGroupIfPort_Type(Integer32):
    """Custom type adGenAOSTdmGroupIfPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 48),
    )


_AdGenAOSTdmGroupIfPort_Type.__name__ = "Integer32"
_AdGenAOSTdmGroupIfPort_Object = MibTableColumn
adGenAOSTdmGroupIfPort = _AdGenAOSTdmGroupIfPort_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 5, 2, 1, 1, 2),
    _AdGenAOSTdmGroupIfPort_Type()
)
adGenAOSTdmGroupIfPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSTdmGroupIfPort.setStatus("current")


class _AdGenAOSTdmGroupID_Type(Integer32):
    """Custom type adGenAOSTdmGroupID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AdGenAOSTdmGroupID_Type.__name__ = "Integer32"
_AdGenAOSTdmGroupID_Object = MibTableColumn
adGenAOSTdmGroupID = _AdGenAOSTdmGroupID_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 5, 2, 1, 1, 3),
    _AdGenAOSTdmGroupID_Type()
)
adGenAOSTdmGroupID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAOSTdmGroupID.setStatus("current")


class _AdGenAOSTdmGroupMask_Type(Integer32):
    """Custom type adGenAOSTdmGroupMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_AdGenAOSTdmGroupMask_Type.__name__ = "Integer32"
_AdGenAOSTdmGroupMask_Object = MibTableColumn
adGenAOSTdmGroupMask = _AdGenAOSTdmGroupMask_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 5, 2, 1, 1, 4),
    _AdGenAOSTdmGroupMask_Type()
)
adGenAOSTdmGroupMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSTdmGroupMask.setStatus("current")


class _AdGenAOSTdmGroupUsage_Type(Integer32):
    """Custom type adGenAOSTdmGroupUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fiftySixKbps", 1),
          ("sixtyFourKbps", 2))
    )


_AdGenAOSTdmGroupUsage_Type.__name__ = "Integer32"
_AdGenAOSTdmGroupUsage_Object = MibTableColumn
adGenAOSTdmGroupUsage = _AdGenAOSTdmGroupUsage_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 5, 2, 1, 1, 5),
    _AdGenAOSTdmGroupUsage_Type()
)
adGenAOSTdmGroupUsage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAOSTdmGroupUsage.setStatus("current")
_AdGenAOSMuxConformance_ObjectIdentity = ObjectIdentity
adGenAOSMuxConformance = _AdGenAOSMuxConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 5, 99)
)
_AdGenAOSMuxCompliance_ObjectIdentity = ObjectIdentity
adGenAOSMuxCompliance = _AdGenAOSMuxCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 5, 99, 1)
)
_AdGenAOSMuxMibGroups_ObjectIdentity = ObjectIdentity
adGenAOSMuxMibGroups = _AdGenAOSMuxMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 5, 99, 2)
)

# Managed Objects groups

adGenAOSXConnectGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 5, 99, 2, 1)
)
adGenAOSXConnectGrp.setObjects(
      *(("ADTRAN-AOS-MUX-MIB", "adGenAOSXConnectIndex"),
        ("ADTRAN-AOS-MUX-MIB", "adGenAOSXConnectFirstIfType"),
        ("ADTRAN-AOS-MUX-MIB", "adGenAOSXConnectFirstIfNumber"),
        ("ADTRAN-AOS-MUX-MIB", "adGenAOSXConnectFirstSubIfNumber"),
        ("ADTRAN-AOS-MUX-MIB", "adGenAOSXConnectFirstIfSlot"),
        ("ADTRAN-AOS-MUX-MIB", "adGenAOSXConnectFirstIfPort"),
        ("ADTRAN-AOS-MUX-MIB", "adGenAOSXConnectFirstTdmGroup"),
        ("ADTRAN-AOS-MUX-MIB", "adGenAOSXConnectFirstTdmGroupDS0"),
        ("ADTRAN-AOS-MUX-MIB", "adGenAOSXConnectSecondIfType"),
        ("ADTRAN-AOS-MUX-MIB", "adGenAOSXConnectSecondIfNumber"),
        ("ADTRAN-AOS-MUX-MIB", "adGenAOSXConnectSecondSubIfNumber"),
        ("ADTRAN-AOS-MUX-MIB", "adGenAOSXConnectSecondIfSlot"),
        ("ADTRAN-AOS-MUX-MIB", "adGenAOSXConnectSecondIfPort"),
        ("ADTRAN-AOS-MUX-MIB", "adGenAOSXConnectSecondTdmGroup"),
        ("ADTRAN-AOS-MUX-MIB", "adGenAOSXConnectSecondTdmGroupDS0"),
        ("ADTRAN-AOS-MUX-MIB", "adGenAOSXConnectPreserveRbs"),
        ("ADTRAN-AOS-MUX-MIB", "adGenAOSXConnectRowStatus"))
)
if mibBuilder.loadTexts:
    adGenAOSXConnectGrp.setStatus("current")

adGenAOSTdmGroupGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 5, 99, 2, 2)
)
adGenAOSTdmGroupGrp.setObjects(
      *(("ADTRAN-AOS-MUX-MIB", "adGenAOSTdmGroupIfSlot"),
        ("ADTRAN-AOS-MUX-MIB", "adGenAOSTdmGroupIfPort"),
        ("ADTRAN-AOS-MUX-MIB", "adGenAOSTdmGroupID"),
        ("ADTRAN-AOS-MUX-MIB", "adGenAOSTdmGroupMask"),
        ("ADTRAN-AOS-MUX-MIB", "adGenAOSTdmGroupUsage"))
)
if mibBuilder.loadTexts:
    adGenAOSTdmGroupGrp.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

adGenAOSMuxConformancemModule = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 5, 99, 1, 1)
)
if mibBuilder.loadTexts:
    adGenAOSMuxConformancemModule.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-AOS-MUX-MIB",
    **{"adGenAOSMux": adGenAOSMux,
       "adGenAOSXConnect": adGenAOSXConnect,
       "adGenAOSXConnectTable": adGenAOSXConnectTable,
       "adGenAOSXConnectEntry": adGenAOSXConnectEntry,
       "adGenAOSXConnectIndex": adGenAOSXConnectIndex,
       "adGenAOSXConnectFirstIfType": adGenAOSXConnectFirstIfType,
       "adGenAOSXConnectFirstIfNumber": adGenAOSXConnectFirstIfNumber,
       "adGenAOSXConnectFirstSubIfNumber": adGenAOSXConnectFirstSubIfNumber,
       "adGenAOSXConnectFirstIfSlot": adGenAOSXConnectFirstIfSlot,
       "adGenAOSXConnectFirstIfPort": adGenAOSXConnectFirstIfPort,
       "adGenAOSXConnectFirstTdmGroup": adGenAOSXConnectFirstTdmGroup,
       "adGenAOSXConnectFirstTdmGroupDS0": adGenAOSXConnectFirstTdmGroupDS0,
       "adGenAOSXConnectSecondIfType": adGenAOSXConnectSecondIfType,
       "adGenAOSXConnectSecondIfNumber": adGenAOSXConnectSecondIfNumber,
       "adGenAOSXConnectSecondSubIfNumber": adGenAOSXConnectSecondSubIfNumber,
       "adGenAOSXConnectSecondIfSlot": adGenAOSXConnectSecondIfSlot,
       "adGenAOSXConnectSecondIfPort": adGenAOSXConnectSecondIfPort,
       "adGenAOSXConnectSecondTdmGroup": adGenAOSXConnectSecondTdmGroup,
       "adGenAOSXConnectSecondTdmGroupDS0": adGenAOSXConnectSecondTdmGroupDS0,
       "adGenAOSXConnectPreserveRbs": adGenAOSXConnectPreserveRbs,
       "adGenAOSXConnectRowStatus": adGenAOSXConnectRowStatus,
       "adGenAOSTdmGroup": adGenAOSTdmGroup,
       "adGenAOSTdmGroupTable": adGenAOSTdmGroupTable,
       "adGenAOSTdmGroupEntry": adGenAOSTdmGroupEntry,
       "adGenAOSTdmGroupIfSlot": adGenAOSTdmGroupIfSlot,
       "adGenAOSTdmGroupIfPort": adGenAOSTdmGroupIfPort,
       "adGenAOSTdmGroupID": adGenAOSTdmGroupID,
       "adGenAOSTdmGroupMask": adGenAOSTdmGroupMask,
       "adGenAOSTdmGroupUsage": adGenAOSTdmGroupUsage,
       "adGenAOSMuxConformance": adGenAOSMuxConformance,
       "adGenAOSMuxCompliance": adGenAOSMuxCompliance,
       "adGenAOSMuxConformancemModule": adGenAOSMuxConformancemModule,
       "adGenAOSMuxMibGroups": adGenAOSMuxMibGroups,
       "adGenAOSXConnectGrp": adGenAOSXConnectGrp,
       "adGenAOSTdmGroupGrp": adGenAOSTdmGroupGrp,
       "adGenAOSMuxID": adGenAOSMuxID}
)
