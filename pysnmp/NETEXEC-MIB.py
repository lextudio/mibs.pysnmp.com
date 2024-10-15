# SNMP MIB module (NETEXEC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NETEXEC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:25:44 2024
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
 NotificationType,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
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

_Internet_ObjectIdentity = ObjectIdentity
internet = _Internet_ObjectIdentity(
    (1, 3, 6, 1)
)
_Private_ObjectIdentity = ObjectIdentity
private = _Private_ObjectIdentity(
    (1, 3, 6, 1, 4)
)
_Enterprises_ObjectIdentity = ObjectIdentity
enterprises = _Enterprises_ObjectIdentity(
    (1, 3, 6, 1, 4, 1)
)
_Tylink_ObjectIdentity = ObjectIdentity
tylink = _Tylink_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 466)
)
_Netexec_ObjectIdentity = ObjectIdentity
netexec = _Netexec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 466, 6)
)
_Dsucsu_ObjectIdentity = ObjectIdentity
dsucsu = _Dsucsu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 466, 6, 1)
)
_DsucsuSysTable_Object = MibTable
dsucsuSysTable = _DsucsuSysTable_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 1)
)
if mibBuilder.loadTexts:
    dsucsuSysTable.setStatus("mandatory")
_DsucsuSysEntry_Object = MibTableRow
dsucsuSysEntry = _DsucsuSysEntry_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 1, 1)
)
dsucsuSysEntry.setIndexNames(
    (0, "NETEXEC-MIB", "dsucsuSysSlot"),
    (0, "NETEXEC-MIB", "dsucsuSysNode"),
)
if mibBuilder.loadTexts:
    dsucsuSysEntry.setStatus("mandatory")


class _DsucsuSysSlot_Type(Integer32):
    """Custom type dsucsuSysSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_DsucsuSysSlot_Type.__name__ = "Integer32"
_DsucsuSysSlot_Object = MibTableColumn
dsucsuSysSlot = _DsucsuSysSlot_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 1, 1, 1),
    _DsucsuSysSlot_Type()
)
dsucsuSysSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsucsuSysSlot.setStatus("mandatory")


class _DsucsuSysNode_Type(Integer32):
    """Custom type dsucsuSysNode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_DsucsuSysNode_Type.__name__ = "Integer32"
_DsucsuSysNode_Object = MibTableColumn
dsucsuSysNode = _DsucsuSysNode_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 1, 1, 2),
    _DsucsuSysNode_Type()
)
dsucsuSysNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsucsuSysNode.setStatus("mandatory")


class _DsucsuSysName_Type(DisplayString):
    """Custom type dsucsuSysName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_DsucsuSysName_Type.__name__ = "DisplayString"
_DsucsuSysName_Object = MibTableColumn
dsucsuSysName = _DsucsuSysName_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 1, 1, 3),
    _DsucsuSysName_Type()
)
dsucsuSysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsucsuSysName.setStatus("mandatory")


class _DsucsuSysType_Type(Integer32):
    """Custom type dsucsuSysType based on Integer32"""
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
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("fns400", 3),
          ("ons1000", 6),
          ("ons1010n", 16),
          ("ons200", 9),
          ("ons232sp", 7),
          ("ons271sp", 8),
          ("ons400", 2),
          ("ons400e", 4),
          ("ons400n", 10),
          ("sns1000", 13),
          ("sns256", 11),
          ("sns400", 5),
          ("sns4000", 12),
          ("ty3000n", 18),
          ("ty3210", 15),
          ("ty3250", 17),
          ("ty3410", 14),
          ("ty3450n", 19),
          ("unknown", 1))
    )


_DsucsuSysType_Type.__name__ = "Integer32"
_DsucsuSysType_Object = MibTableColumn
dsucsuSysType = _DsucsuSysType_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 1, 1, 4),
    _DsucsuSysType_Type()
)
dsucsuSysType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsucsuSysType.setStatus("mandatory")


class _DsucsuSysSoftRev_Type(DisplayString):
    """Custom type dsucsuSysSoftRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_DsucsuSysSoftRev_Type.__name__ = "DisplayString"
_DsucsuSysSoftRev_Object = MibTableColumn
dsucsuSysSoftRev = _DsucsuSysSoftRev_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 1, 1, 5),
    _DsucsuSysSoftRev_Type()
)
dsucsuSysSoftRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsucsuSysSoftRev.setStatus("mandatory")


class _DsucsuSysHardRev_Type(DisplayString):
    """Custom type dsucsuSysHardRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1),
    )


_DsucsuSysHardRev_Type.__name__ = "DisplayString"
_DsucsuSysHardRev_Object = MibTableColumn
dsucsuSysHardRev = _DsucsuSysHardRev_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 1, 1, 6),
    _DsucsuSysHardRev_Type()
)
dsucsuSysHardRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsucsuSysHardRev.setStatus("mandatory")


class _DsucsuSysNumChan_Type(Integer32):
    """Custom type dsucsuSysNumChan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_DsucsuSysNumChan_Type.__name__ = "Integer32"
_DsucsuSysNumChan_Object = MibTableColumn
dsucsuSysNumChan = _DsucsuSysNumChan_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 1, 1, 7),
    _DsucsuSysNumChan_Type()
)
dsucsuSysNumChan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsucsuSysNumChan.setStatus("mandatory")
_DsucsuCfgNetTable_Object = MibTable
dsucsuCfgNetTable = _DsucsuCfgNetTable_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 2)
)
if mibBuilder.loadTexts:
    dsucsuCfgNetTable.setStatus("mandatory")
_DsucsuCfgNetEntry_Object = MibTableRow
dsucsuCfgNetEntry = _DsucsuCfgNetEntry_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 2, 1)
)
dsucsuCfgNetEntry.setIndexNames(
    (0, "NETEXEC-MIB", "dsucsuCfgNetSlot"),
    (0, "NETEXEC-MIB", "dsucsuCfgNetNode"),
    (0, "NETEXEC-MIB", "dsucsuCfgNetIndex"),
)
if mibBuilder.loadTexts:
    dsucsuCfgNetEntry.setStatus("mandatory")


class _DsucsuCfgNetSlot_Type(Integer32):
    """Custom type dsucsuCfgNetSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_DsucsuCfgNetSlot_Type.__name__ = "Integer32"
_DsucsuCfgNetSlot_Object = MibTableColumn
dsucsuCfgNetSlot = _DsucsuCfgNetSlot_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 2, 1, 1),
    _DsucsuCfgNetSlot_Type()
)
dsucsuCfgNetSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsucsuCfgNetSlot.setStatus("mandatory")


class _DsucsuCfgNetNode_Type(Integer32):
    """Custom type dsucsuCfgNetNode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_DsucsuCfgNetNode_Type.__name__ = "Integer32"
_DsucsuCfgNetNode_Object = MibTableColumn
dsucsuCfgNetNode = _DsucsuCfgNetNode_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 2, 1, 2),
    _DsucsuCfgNetNode_Type()
)
dsucsuCfgNetNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsucsuCfgNetNode.setStatus("mandatory")


class _DsucsuCfgNetIndex_Type(Integer32):
    """Custom type dsucsuCfgNetIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_DsucsuCfgNetIndex_Type.__name__ = "Integer32"
_DsucsuCfgNetIndex_Object = MibTableColumn
dsucsuCfgNetIndex = _DsucsuCfgNetIndex_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 2, 1, 3),
    _DsucsuCfgNetIndex_Type()
)
dsucsuCfgNetIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsucsuCfgNetIndex.setStatus("mandatory")


class _DsucsuCfgNetInterface_Type(Integer32):
    """Custom type dsucsuCfgNetInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dsx-1", 2),
          ("network", 1))
    )


_DsucsuCfgNetInterface_Type.__name__ = "Integer32"
_DsucsuCfgNetInterface_Object = MibTableColumn
dsucsuCfgNetInterface = _DsucsuCfgNetInterface_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 2, 1, 4),
    _DsucsuCfgNetInterface_Type()
)
dsucsuCfgNetInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsucsuCfgNetInterface.setStatus("mandatory")


class _DsucsuCfgNetType_Type(Integer32):
    """Custom type dsucsuCfgNetType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("cept-2048", 5),
          ("d4", 1),
          ("esf-54016", 2),
          ("esf-ansi", 3),
          ("nsms", 4))
    )


_DsucsuCfgNetType_Type.__name__ = "Integer32"
_DsucsuCfgNetType_Object = MibTableColumn
dsucsuCfgNetType = _DsucsuCfgNetType_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 2, 1, 5),
    _DsucsuCfgNetType_Type()
)
dsucsuCfgNetType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsucsuCfgNetType.setStatus("mandatory")


class _DsucsuCfgNetCoding_Type(Integer32):
    """Custom type dsucsuCfgNetCoding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ami", 1),
          ("b8zs", 2),
          ("hdb3", 3))
    )


_DsucsuCfgNetCoding_Type.__name__ = "Integer32"
_DsucsuCfgNetCoding_Object = MibTableColumn
dsucsuCfgNetCoding = _DsucsuCfgNetCoding_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 2, 1, 6),
    _DsucsuCfgNetCoding_Type()
)
dsucsuCfgNetCoding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsucsuCfgNetCoding.setStatus("mandatory")


class _DsucsuCfgNetClockSource_Type(Integer32):
    """Custom type dsucsuCfgNetClockSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("external-ch1", 3),
          ("external-ch3", 4),
          ("internal", 1),
          ("loop", 2),
          ("station-clock", 5))
    )


_DsucsuCfgNetClockSource_Type.__name__ = "Integer32"
_DsucsuCfgNetClockSource_Object = MibTableColumn
dsucsuCfgNetClockSource = _DsucsuCfgNetClockSource_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 2, 1, 7),
    _DsucsuCfgNetClockSource_Type()
)
dsucsuCfgNetClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsucsuCfgNetClockSource.setStatus("mandatory")


class _DsucsuCfgNetCsuEnable_Type(Integer32):
    """Custom type dsucsuCfgNetCsuEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("csu", 2),
          ("dsx1", 1))
    )


_DsucsuCfgNetCsuEnable_Type.__name__ = "Integer32"
_DsucsuCfgNetCsuEnable_Object = MibTableColumn
dsucsuCfgNetCsuEnable = _DsucsuCfgNetCsuEnable_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 2, 1, 8),
    _DsucsuCfgNetCsuEnable_Type()
)
dsucsuCfgNetCsuEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsucsuCfgNetCsuEnable.setStatus("mandatory")


class _DsucsuCfgNetCsuLBO_Type(Integer32):
    """Custom type dsucsuCfgNetCsuLBO based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("db-0", 1),
          ("db-15", 3),
          ("db-7-5", 2))
    )


_DsucsuCfgNetCsuLBO_Type.__name__ = "Integer32"
_DsucsuCfgNetCsuLBO_Object = MibTableColumn
dsucsuCfgNetCsuLBO = _DsucsuCfgNetCsuLBO_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 2, 1, 9),
    _DsucsuCfgNetCsuLBO_Type()
)
dsucsuCfgNetCsuLBO.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsucsuCfgNetCsuLBO.setStatus("mandatory")


class _DsucsuCfgNetCsuDensity_Type(Integer32):
    """Custom type dsucsuCfgNetCsuDensity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("d-1-in-16", 3),
          ("d-1-in-64", 4),
          ("d-1-in-8", 2),
          ("d-12pt5-percent", 5),
          ("none", 1))
    )


_DsucsuCfgNetCsuDensity_Type.__name__ = "Integer32"
_DsucsuCfgNetCsuDensity_Object = MibTableColumn
dsucsuCfgNetCsuDensity = _DsucsuCfgNetCsuDensity_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 2, 1, 10),
    _DsucsuCfgNetCsuDensity_Type()
)
dsucsuCfgNetCsuDensity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsucsuCfgNetCsuDensity.setStatus("mandatory")


class _DsucsuCfgNetRateMultiples_Type(Integer32):
    """Custom type dsucsuCfgNetRateMultiples based on Integer32"""
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
        *(("all-rates", 4),
          ("extended-mixed", 3),
          ("nx56", 1),
          ("nx64", 2))
    )


_DsucsuCfgNetRateMultiples_Type.__name__ = "Integer32"
_DsucsuCfgNetRateMultiples_Object = MibTableColumn
dsucsuCfgNetRateMultiples = _DsucsuCfgNetRateMultiples_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 2, 1, 11),
    _DsucsuCfgNetRateMultiples_Type()
)
dsucsuCfgNetRateMultiples.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsucsuCfgNetRateMultiples.setStatus("mandatory")


class _DsucsuCfgNetOutputPulse_Type(Integer32):
    """Custom type dsucsuCfgNetOutputPulse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("pulse-0-133-ft", 1),
          ("pulse-133-266-ft", 2),
          ("pulse-266-399-ft", 3),
          ("pulse-399-533-ft", 4),
          ("pulse-533-655-ft", 5))
    )


_DsucsuCfgNetOutputPulse_Type.__name__ = "Integer32"
_DsucsuCfgNetOutputPulse_Object = MibTableColumn
dsucsuCfgNetOutputPulse = _DsucsuCfgNetOutputPulse_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 2, 1, 12),
    _DsucsuCfgNetOutputPulse_Type()
)
dsucsuCfgNetOutputPulse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsucsuCfgNetOutputPulse.setStatus("mandatory")


class _DsucsuCfgNetTs0_Type(Integer32):
    """Custom type dsucsuCfgNetTs0 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("crc4-disable", 2),
          ("crc4-enable", 1))
    )


_DsucsuCfgNetTs0_Type.__name__ = "Integer32"
_DsucsuCfgNetTs0_Object = MibTableColumn
dsucsuCfgNetTs0 = _DsucsuCfgNetTs0_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 2, 1, 13),
    _DsucsuCfgNetTs0_Type()
)
dsucsuCfgNetTs0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsucsuCfgNetTs0.setStatus("mandatory")


class _DsucsuCfgNetTs16_Type(Integer32):
    """Custom type dsucsuCfgNetTs16 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("data", 1),
          ("multifr-align", 2))
    )


_DsucsuCfgNetTs16_Type.__name__ = "Integer32"
_DsucsuCfgNetTs16_Object = MibTableColumn
dsucsuCfgNetTs16 = _DsucsuCfgNetTs16_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 2, 1, 14),
    _DsucsuCfgNetTs16_Type()
)
dsucsuCfgNetTs16.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsucsuCfgNetTs16.setStatus("mandatory")
_DsucsuCfgDteChanTable_Object = MibTable
dsucsuCfgDteChanTable = _DsucsuCfgDteChanTable_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 4)
)
if mibBuilder.loadTexts:
    dsucsuCfgDteChanTable.setStatus("mandatory")
_DsucsuCfgDteChanEntry_Object = MibTableRow
dsucsuCfgDteChanEntry = _DsucsuCfgDteChanEntry_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 4, 1)
)
dsucsuCfgDteChanEntry.setIndexNames(
    (0, "NETEXEC-MIB", "dsucsuCfgDteChanSlot"),
    (0, "NETEXEC-MIB", "dsucsuCfgDteChanNode"),
    (0, "NETEXEC-MIB", "dsucsuCfgDteChanIndex"),
)
if mibBuilder.loadTexts:
    dsucsuCfgDteChanEntry.setStatus("mandatory")


class _DsucsuCfgDteChanSlot_Type(Integer32):
    """Custom type dsucsuCfgDteChanSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_DsucsuCfgDteChanSlot_Type.__name__ = "Integer32"
_DsucsuCfgDteChanSlot_Object = MibTableColumn
dsucsuCfgDteChanSlot = _DsucsuCfgDteChanSlot_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 4, 1, 1),
    _DsucsuCfgDteChanSlot_Type()
)
dsucsuCfgDteChanSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsucsuCfgDteChanSlot.setStatus("mandatory")


class _DsucsuCfgDteChanNode_Type(Integer32):
    """Custom type dsucsuCfgDteChanNode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_DsucsuCfgDteChanNode_Type.__name__ = "Integer32"
_DsucsuCfgDteChanNode_Object = MibTableColumn
dsucsuCfgDteChanNode = _DsucsuCfgDteChanNode_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 4, 1, 2),
    _DsucsuCfgDteChanNode_Type()
)
dsucsuCfgDteChanNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsucsuCfgDteChanNode.setStatus("mandatory")


class _DsucsuCfgDteChanIndex_Type(Integer32):
    """Custom type dsucsuCfgDteChanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_DsucsuCfgDteChanIndex_Type.__name__ = "Integer32"
_DsucsuCfgDteChanIndex_Object = MibTableColumn
dsucsuCfgDteChanIndex = _DsucsuCfgDteChanIndex_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 4, 1, 3),
    _DsucsuCfgDteChanIndex_Type()
)
dsucsuCfgDteChanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsucsuCfgDteChanIndex.setStatus("mandatory")


class _DsucsuCfgDteChanType_Type(Integer32):
    """Custom type dsucsuCfgDteChanType based on Integer32"""
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
        *(("none", 4),
          ("rs232", 1),
          ("rs449", 3),
          ("v35", 2))
    )


_DsucsuCfgDteChanType_Type.__name__ = "Integer32"
_DsucsuCfgDteChanType_Object = MibTableColumn
dsucsuCfgDteChanType = _DsucsuCfgDteChanType_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 4, 1, 4),
    _DsucsuCfgDteChanType_Type()
)
dsucsuCfgDteChanType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsucsuCfgDteChanType.setStatus("mandatory")
_DsucsuCfgDteChanRate_Type = Integer32
_DsucsuCfgDteChanRate_Object = MibTableColumn
dsucsuCfgDteChanRate = _DsucsuCfgDteChanRate_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 4, 1, 5),
    _DsucsuCfgDteChanRate_Type()
)
dsucsuCfgDteChanRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsucsuCfgDteChanRate.setStatus("mandatory")


class _DsucsuCfgDteChanEncoding_Type(Integer32):
    """Custom type dsucsuCfgDteChanEncoding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("alt", 2),
          ("b7s", 1),
          ("clr", 3))
    )


_DsucsuCfgDteChanEncoding_Type.__name__ = "Integer32"
_DsucsuCfgDteChanEncoding_Object = MibTableColumn
dsucsuCfgDteChanEncoding = _DsucsuCfgDteChanEncoding_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 4, 1, 6),
    _DsucsuCfgDteChanEncoding_Type()
)
dsucsuCfgDteChanEncoding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsucsuCfgDteChanEncoding.setStatus("mandatory")
_DsucsuCfgDteChanStartDs0_Type = Integer32
_DsucsuCfgDteChanStartDs0_Object = MibTableColumn
dsucsuCfgDteChanStartDs0 = _DsucsuCfgDteChanStartDs0_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 4, 1, 7),
    _DsucsuCfgDteChanStartDs0_Type()
)
dsucsuCfgDteChanStartDs0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsucsuCfgDteChanStartDs0.setStatus("mandatory")


class _DsucsuCfgDteChanCtrlSignal_Type(Integer32):
    """Custom type dsucsuCfgDteChanCtrlSignal based on Integer32"""
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
        *(("cts-auto", 4),
          ("cts-on", 3),
          ("rts-on", 1),
          ("rts-switch", 2))
    )


_DsucsuCfgDteChanCtrlSignal_Type.__name__ = "Integer32"
_DsucsuCfgDteChanCtrlSignal_Object = MibTableColumn
dsucsuCfgDteChanCtrlSignal = _DsucsuCfgDteChanCtrlSignal_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 4, 1, 8),
    _DsucsuCfgDteChanCtrlSignal_Type()
)
dsucsuCfgDteChanCtrlSignal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsucsuCfgDteChanCtrlSignal.setStatus("mandatory")


class _DsucsuCfgDteChanTiming_Type(Integer32):
    """Custom type dsucsuCfgDteChanTiming based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("loop1", 1),
          ("loop2", 2))
    )


_DsucsuCfgDteChanTiming_Type.__name__ = "Integer32"
_DsucsuCfgDteChanTiming_Object = MibTableColumn
dsucsuCfgDteChanTiming = _DsucsuCfgDteChanTiming_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 4, 1, 9),
    _DsucsuCfgDteChanTiming_Type()
)
dsucsuCfgDteChanTiming.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsucsuCfgDteChanTiming.setStatus("mandatory")


class _DsucsuCfgDteChanClockInvert_Type(Integer32):
    """Custom type dsucsuCfgDteChanClockInvert based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_DsucsuCfgDteChanClockInvert_Type.__name__ = "Integer32"
_DsucsuCfgDteChanClockInvert_Object = MibTableColumn
dsucsuCfgDteChanClockInvert = _DsucsuCfgDteChanClockInvert_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 4, 1, 10),
    _DsucsuCfgDteChanClockInvert_Type()
)
dsucsuCfgDteChanClockInvert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsucsuCfgDteChanClockInvert.setStatus("mandatory")


class _DsucsuCfgDteChanDataInvert_Type(Integer32):
    """Custom type dsucsuCfgDteChanDataInvert based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_DsucsuCfgDteChanDataInvert_Type.__name__ = "Integer32"
_DsucsuCfgDteChanDataInvert_Object = MibTableColumn
dsucsuCfgDteChanDataInvert = _DsucsuCfgDteChanDataInvert_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 4, 1, 11),
    _DsucsuCfgDteChanDataInvert_Type()
)
dsucsuCfgDteChanDataInvert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsucsuCfgDteChanDataInvert.setStatus("mandatory")
_DsucsuCfgFrmChanTable_Object = MibTable
dsucsuCfgFrmChanTable = _DsucsuCfgFrmChanTable_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 5)
)
if mibBuilder.loadTexts:
    dsucsuCfgFrmChanTable.setStatus("mandatory")
_DsucsuCfgFrmChanEntry_Object = MibTableRow
dsucsuCfgFrmChanEntry = _DsucsuCfgFrmChanEntry_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 5, 1)
)
dsucsuCfgFrmChanEntry.setIndexNames(
    (0, "NETEXEC-MIB", "dsucsuCfgFrmChanSlot"),
    (0, "NETEXEC-MIB", "dsucsuCfgFrmChanNode"),
    (0, "NETEXEC-MIB", "dsucsuCfgFrmChanIndex"),
)
if mibBuilder.loadTexts:
    dsucsuCfgFrmChanEntry.setStatus("mandatory")


class _DsucsuCfgFrmChanSlot_Type(Integer32):
    """Custom type dsucsuCfgFrmChanSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_DsucsuCfgFrmChanSlot_Type.__name__ = "Integer32"
_DsucsuCfgFrmChanSlot_Object = MibTableColumn
dsucsuCfgFrmChanSlot = _DsucsuCfgFrmChanSlot_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 5, 1, 1),
    _DsucsuCfgFrmChanSlot_Type()
)
dsucsuCfgFrmChanSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsucsuCfgFrmChanSlot.setStatus("mandatory")


class _DsucsuCfgFrmChanNode_Type(Integer32):
    """Custom type dsucsuCfgFrmChanNode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_DsucsuCfgFrmChanNode_Type.__name__ = "Integer32"
_DsucsuCfgFrmChanNode_Object = MibTableColumn
dsucsuCfgFrmChanNode = _DsucsuCfgFrmChanNode_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 5, 1, 2),
    _DsucsuCfgFrmChanNode_Type()
)
dsucsuCfgFrmChanNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsucsuCfgFrmChanNode.setStatus("mandatory")


class _DsucsuCfgFrmChanIndex_Type(Integer32):
    """Custom type dsucsuCfgFrmChanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_DsucsuCfgFrmChanIndex_Type.__name__ = "Integer32"
_DsucsuCfgFrmChanIndex_Object = MibTableColumn
dsucsuCfgFrmChanIndex = _DsucsuCfgFrmChanIndex_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 5, 1, 3),
    _DsucsuCfgFrmChanIndex_Type()
)
dsucsuCfgFrmChanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsucsuCfgFrmChanIndex.setStatus("mandatory")


class _DsucsuCfgFrmChanType_Type(Integer32):
    """Custom type dsucsuCfgFrmChanType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 2),
          ("pbx", 1))
    )


_DsucsuCfgFrmChanType_Type.__name__ = "Integer32"
_DsucsuCfgFrmChanType_Object = MibTableColumn
dsucsuCfgFrmChanType = _DsucsuCfgFrmChanType_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 5, 1, 4),
    _DsucsuCfgFrmChanType_Type()
)
dsucsuCfgFrmChanType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsucsuCfgFrmChanType.setStatus("mandatory")
_DsucsuCfgFrmChanNumDs0_Type = Integer32
_DsucsuCfgFrmChanNumDs0_Object = MibTableColumn
dsucsuCfgFrmChanNumDs0 = _DsucsuCfgFrmChanNumDs0_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 5, 1, 5),
    _DsucsuCfgFrmChanNumDs0_Type()
)
dsucsuCfgFrmChanNumDs0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsucsuCfgFrmChanNumDs0.setStatus("mandatory")


class _DsucsuCfgFrmChanEncoding_Type(Integer32):
    """Custom type dsucsuCfgFrmChanEncoding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ami", 1),
          ("b8zs", 2))
    )


_DsucsuCfgFrmChanEncoding_Type.__name__ = "Integer32"
_DsucsuCfgFrmChanEncoding_Object = MibTableColumn
dsucsuCfgFrmChanEncoding = _DsucsuCfgFrmChanEncoding_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 5, 1, 6),
    _DsucsuCfgFrmChanEncoding_Type()
)
dsucsuCfgFrmChanEncoding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsucsuCfgFrmChanEncoding.setStatus("mandatory")
_DsucsuCfgFrmChanStartDs0_Type = Integer32
_DsucsuCfgFrmChanStartDs0_Object = MibTableColumn
dsucsuCfgFrmChanStartDs0 = _DsucsuCfgFrmChanStartDs0_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 5, 1, 7),
    _DsucsuCfgFrmChanStartDs0_Type()
)
dsucsuCfgFrmChanStartDs0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsucsuCfgFrmChanStartDs0.setStatus("mandatory")
_DsucsuCfgFrmChanDteStartDs0_Type = Integer32
_DsucsuCfgFrmChanDteStartDs0_Object = MibTableColumn
dsucsuCfgFrmChanDteStartDs0 = _DsucsuCfgFrmChanDteStartDs0_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 5, 1, 8),
    _DsucsuCfgFrmChanDteStartDs0_Type()
)
dsucsuCfgFrmChanDteStartDs0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsucsuCfgFrmChanDteStartDs0.setStatus("mandatory")


class _DsucsuCfgFrmChanMapping_Type(Integer32):
    """Custom type dsucsuCfgFrmChanMapping based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alt-ds0", 2),
          ("ctg-ds0", 1))
    )


_DsucsuCfgFrmChanMapping_Type.__name__ = "Integer32"
_DsucsuCfgFrmChanMapping_Object = MibTableColumn
dsucsuCfgFrmChanMapping = _DsucsuCfgFrmChanMapping_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 5, 1, 9),
    _DsucsuCfgFrmChanMapping_Type()
)
dsucsuCfgFrmChanMapping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsucsuCfgFrmChanMapping.setStatus("mandatory")


class _DsucsuCfgFrmChanDs0Type_Type(Integer32):
    """Custom type dsucsuCfgFrmChanDs0Type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("data", 1),
          ("mixed", 3),
          ("voice", 2))
    )


_DsucsuCfgFrmChanDs0Type_Type.__name__ = "Integer32"
_DsucsuCfgFrmChanDs0Type_Object = MibTableColumn
dsucsuCfgFrmChanDs0Type = _DsucsuCfgFrmChanDs0Type_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 5, 1, 10),
    _DsucsuCfgFrmChanDs0Type_Type()
)
dsucsuCfgFrmChanDs0Type.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsucsuCfgFrmChanDs0Type.setStatus("mandatory")


class _DsucsuCfgFrmChanFrameType_Type(Integer32):
    """Custom type dsucsuCfgFrmChanFrameType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("d4", 1),
          ("esf", 2))
    )


_DsucsuCfgFrmChanFrameType_Type.__name__ = "Integer32"
_DsucsuCfgFrmChanFrameType_Object = MibTableColumn
dsucsuCfgFrmChanFrameType = _DsucsuCfgFrmChanFrameType_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 5, 1, 11),
    _DsucsuCfgFrmChanFrameType_Type()
)
dsucsuCfgFrmChanFrameType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsucsuCfgFrmChanFrameType.setStatus("mandatory")


class _DsucsuCfgFrmChanOutputPulse_Type(Integer32):
    """Custom type dsucsuCfgFrmChanOutputPulse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("pulse-0-133-ft", 1),
          ("pulse-133-266-ft", 2),
          ("pulse-266-399-ft", 3),
          ("pulse-399-533-ft", 4),
          ("pulse-533-655-ft", 5))
    )


_DsucsuCfgFrmChanOutputPulse_Type.__name__ = "Integer32"
_DsucsuCfgFrmChanOutputPulse_Object = MibTableColumn
dsucsuCfgFrmChanOutputPulse = _DsucsuCfgFrmChanOutputPulse_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 5, 1, 12),
    _DsucsuCfgFrmChanOutputPulse_Type()
)
dsucsuCfgFrmChanOutputPulse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsucsuCfgFrmChanOutputPulse.setStatus("mandatory")


class _DsucsuCfgFrmChanNetMapping_Type(Integer32):
    """Custom type dsucsuCfgFrmChanNetMapping based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alt-ds0", 2),
          ("ctg-ds0", 1))
    )


_DsucsuCfgFrmChanNetMapping_Type.__name__ = "Integer32"
_DsucsuCfgFrmChanNetMapping_Object = MibTableColumn
dsucsuCfgFrmChanNetMapping = _DsucsuCfgFrmChanNetMapping_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 5, 1, 13),
    _DsucsuCfgFrmChanNetMapping_Type()
)
dsucsuCfgFrmChanNetMapping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsucsuCfgFrmChanNetMapping.setStatus("mandatory")
_DsucsuConfigSupTable_Object = MibTable
dsucsuConfigSupTable = _DsucsuConfigSupTable_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 7)
)
if mibBuilder.loadTexts:
    dsucsuConfigSupTable.setStatus("mandatory")
_DsucsuConfigSupEntry_Object = MibTableRow
dsucsuConfigSupEntry = _DsucsuConfigSupEntry_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 7, 1)
)
dsucsuConfigSupEntry.setIndexNames(
    (0, "NETEXEC-MIB", "dsucsuConfigSupSlot"),
    (0, "NETEXEC-MIB", "dsucsuConfigSupNode"),
    (0, "NETEXEC-MIB", "dsucsuConfigSupIndex"),
)
if mibBuilder.loadTexts:
    dsucsuConfigSupEntry.setStatus("mandatory")


class _DsucsuConfigSupSlot_Type(Integer32):
    """Custom type dsucsuConfigSupSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_DsucsuConfigSupSlot_Type.__name__ = "Integer32"
_DsucsuConfigSupSlot_Object = MibTableColumn
dsucsuConfigSupSlot = _DsucsuConfigSupSlot_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 7, 1, 1),
    _DsucsuConfigSupSlot_Type()
)
dsucsuConfigSupSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsucsuConfigSupSlot.setStatus("mandatory")


class _DsucsuConfigSupNode_Type(Integer32):
    """Custom type dsucsuConfigSupNode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_DsucsuConfigSupNode_Type.__name__ = "Integer32"
_DsucsuConfigSupNode_Object = MibTableColumn
dsucsuConfigSupNode = _DsucsuConfigSupNode_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 7, 1, 2),
    _DsucsuConfigSupNode_Type()
)
dsucsuConfigSupNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsucsuConfigSupNode.setStatus("mandatory")


class _DsucsuConfigSupIndex_Type(Integer32):
    """Custom type dsucsuConfigSupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_DsucsuConfigSupIndex_Type.__name__ = "Integer32"
_DsucsuConfigSupIndex_Object = MibTableColumn
dsucsuConfigSupIndex = _DsucsuConfigSupIndex_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 7, 1, 3),
    _DsucsuConfigSupIndex_Type()
)
dsucsuConfigSupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsucsuConfigSupIndex.setStatus("mandatory")
_DsucsuConfigSupDs0_Type = Integer32
_DsucsuConfigSupDs0_Object = MibTableColumn
dsucsuConfigSupDs0 = _DsucsuConfigSupDs0_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 7, 1, 4),
    _DsucsuConfigSupDs0_Type()
)
dsucsuConfigSupDs0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsucsuConfigSupDs0.setStatus("mandatory")
_DsucsuCfgSupAuxTable_Object = MibTable
dsucsuCfgSupAuxTable = _DsucsuCfgSupAuxTable_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 8)
)
if mibBuilder.loadTexts:
    dsucsuCfgSupAuxTable.setStatus("mandatory")
_DsucsuCfgSupAuxEntry_Object = MibTableRow
dsucsuCfgSupAuxEntry = _DsucsuCfgSupAuxEntry_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 8, 1)
)
dsucsuCfgSupAuxEntry.setIndexNames(
    (0, "NETEXEC-MIB", "dsucsuCfgSupAuxSlot"),
    (0, "NETEXEC-MIB", "dsucsuCfgSupAuxNode"),
    (0, "NETEXEC-MIB", "dsucsuCfgSupAuxIndex"),
)
if mibBuilder.loadTexts:
    dsucsuCfgSupAuxEntry.setStatus("mandatory")


class _DsucsuCfgSupAuxSlot_Type(Integer32):
    """Custom type dsucsuCfgSupAuxSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_DsucsuCfgSupAuxSlot_Type.__name__ = "Integer32"
_DsucsuCfgSupAuxSlot_Object = MibTableColumn
dsucsuCfgSupAuxSlot = _DsucsuCfgSupAuxSlot_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 8, 1, 1),
    _DsucsuCfgSupAuxSlot_Type()
)
dsucsuCfgSupAuxSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsucsuCfgSupAuxSlot.setStatus("mandatory")


class _DsucsuCfgSupAuxNode_Type(Integer32):
    """Custom type dsucsuCfgSupAuxNode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_DsucsuCfgSupAuxNode_Type.__name__ = "Integer32"
_DsucsuCfgSupAuxNode_Object = MibTableColumn
dsucsuCfgSupAuxNode = _DsucsuCfgSupAuxNode_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 8, 1, 2),
    _DsucsuCfgSupAuxNode_Type()
)
dsucsuCfgSupAuxNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsucsuCfgSupAuxNode.setStatus("mandatory")


class _DsucsuCfgSupAuxIndex_Type(Integer32):
    """Custom type dsucsuCfgSupAuxIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_DsucsuCfgSupAuxIndex_Type.__name__ = "Integer32"
_DsucsuCfgSupAuxIndex_Object = MibTableColumn
dsucsuCfgSupAuxIndex = _DsucsuCfgSupAuxIndex_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 8, 1, 3),
    _DsucsuCfgSupAuxIndex_Type()
)
dsucsuCfgSupAuxIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsucsuCfgSupAuxIndex.setStatus("mandatory")


class _DsucsuCfgSupAuxFdl_Type(Integer32):
    """Custom type dsucsuCfgSupAuxFdl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_DsucsuCfgSupAuxFdl_Type.__name__ = "Integer32"
_DsucsuCfgSupAuxFdl_Object = MibTableColumn
dsucsuCfgSupAuxFdl = _DsucsuCfgSupAuxFdl_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 8, 1, 4),
    _DsucsuCfgSupAuxFdl_Type()
)
dsucsuCfgSupAuxFdl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsucsuCfgSupAuxFdl.setStatus("mandatory")
_DsucsuActvConfTable_Object = MibTable
dsucsuActvConfTable = _DsucsuActvConfTable_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 9)
)
if mibBuilder.loadTexts:
    dsucsuActvConfTable.setStatus("mandatory")
_DsucsuActvConfEntry_Object = MibTableRow
dsucsuActvConfEntry = _DsucsuActvConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 9, 1)
)
dsucsuActvConfEntry.setIndexNames(
    (0, "NETEXEC-MIB", "dsucsuActvConfSlot"),
    (0, "NETEXEC-MIB", "dsucsuActvConfNode"),
)
if mibBuilder.loadTexts:
    dsucsuActvConfEntry.setStatus("mandatory")


class _DsucsuActvConfSlot_Type(Integer32):
    """Custom type dsucsuActvConfSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_DsucsuActvConfSlot_Type.__name__ = "Integer32"
_DsucsuActvConfSlot_Object = MibTableColumn
dsucsuActvConfSlot = _DsucsuActvConfSlot_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 9, 1, 1),
    _DsucsuActvConfSlot_Type()
)
dsucsuActvConfSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsucsuActvConfSlot.setStatus("mandatory")


class _DsucsuActvConfNode_Type(Integer32):
    """Custom type dsucsuActvConfNode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_DsucsuActvConfNode_Type.__name__ = "Integer32"
_DsucsuActvConfNode_Object = MibTableColumn
dsucsuActvConfNode = _DsucsuActvConfNode_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 9, 1, 2),
    _DsucsuActvConfNode_Type()
)
dsucsuActvConfNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsucsuActvConfNode.setStatus("mandatory")


class _DsucsuActvConfIndex_Type(Integer32):
    """Custom type dsucsuActvConfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_DsucsuActvConfIndex_Type.__name__ = "Integer32"
_DsucsuActvConfIndex_Object = MibTableColumn
dsucsuActvConfIndex = _DsucsuActvConfIndex_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 9, 1, 3),
    _DsucsuActvConfIndex_Type()
)
dsucsuActvConfIndex.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    dsucsuActvConfIndex.setStatus("mandatory")
_DsucsuEventDesTable_Object = MibTable
dsucsuEventDesTable = _DsucsuEventDesTable_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 10)
)
if mibBuilder.loadTexts:
    dsucsuEventDesTable.setStatus("mandatory")
_DsucsuEventDesEntry_Object = MibTableRow
dsucsuEventDesEntry = _DsucsuEventDesEntry_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 10, 1)
)
dsucsuEventDesEntry.setIndexNames(
    (0, "NETEXEC-MIB", "dsucsuEventDesSlot"),
    (0, "NETEXEC-MIB", "dsucsuEventDesNode"),
)
if mibBuilder.loadTexts:
    dsucsuEventDesEntry.setStatus("mandatory")


class _DsucsuEventDesSlot_Type(Integer32):
    """Custom type dsucsuEventDesSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_DsucsuEventDesSlot_Type.__name__ = "Integer32"
_DsucsuEventDesSlot_Object = MibTableColumn
dsucsuEventDesSlot = _DsucsuEventDesSlot_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 10, 1, 1),
    _DsucsuEventDesSlot_Type()
)
dsucsuEventDesSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsucsuEventDesSlot.setStatus("mandatory")


class _DsucsuEventDesNode_Type(Integer32):
    """Custom type dsucsuEventDesNode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_DsucsuEventDesNode_Type.__name__ = "Integer32"
_DsucsuEventDesNode_Object = MibTableColumn
dsucsuEventDesNode = _DsucsuEventDesNode_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 10, 1, 2),
    _DsucsuEventDesNode_Type()
)
dsucsuEventDesNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsucsuEventDesNode.setStatus("mandatory")


class _DsucsuEventNameIndx_Type(DisplayString):
    """Custom type dsucsuEventNameIndx based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_DsucsuEventNameIndx_Type.__name__ = "DisplayString"
_DsucsuEventNameIndx_Object = MibTableColumn
dsucsuEventNameIndx = _DsucsuEventNameIndx_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 10, 1, 3),
    _DsucsuEventNameIndx_Type()
)
dsucsuEventNameIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsucsuEventNameIndx.setStatus("mandatory")


class _DsucsuEventDesName1_Type(DisplayString):
    """Custom type dsucsuEventDesName1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_DsucsuEventDesName1_Type.__name__ = "DisplayString"
_DsucsuEventDesName1_Object = MibTableColumn
dsucsuEventDesName1 = _DsucsuEventDesName1_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 10, 1, 4),
    _DsucsuEventDesName1_Type()
)
dsucsuEventDesName1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsucsuEventDesName1.setStatus("mandatory")


class _DsucsuEventDesName2_Type(DisplayString):
    """Custom type dsucsuEventDesName2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_DsucsuEventDesName2_Type.__name__ = "DisplayString"
_DsucsuEventDesName2_Object = MibTableColumn
dsucsuEventDesName2 = _DsucsuEventDesName2_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 10, 1, 5),
    _DsucsuEventDesName2_Type()
)
dsucsuEventDesName2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsucsuEventDesName2.setStatus("mandatory")


class _DsucsuEventClrDest_Type(Integer32):
    """Custom type dsucsuEventClrDest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("clearBothDest", 3),
          ("clearDest1", 1),
          ("clearDest2", 2))
    )


_DsucsuEventClrDest_Type.__name__ = "Integer32"
_DsucsuEventClrDest_Object = MibTableColumn
dsucsuEventClrDest = _DsucsuEventClrDest_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 10, 1, 6),
    _DsucsuEventClrDest_Type()
)
dsucsuEventClrDest.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    dsucsuEventClrDest.setStatus("mandatory")
_DsucsuCfgMaintTable_Object = MibTable
dsucsuCfgMaintTable = _DsucsuCfgMaintTable_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 11)
)
if mibBuilder.loadTexts:
    dsucsuCfgMaintTable.setStatus("mandatory")
_DsucsuCfgMaintEntry_Object = MibTableRow
dsucsuCfgMaintEntry = _DsucsuCfgMaintEntry_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 11, 1)
)
dsucsuCfgMaintEntry.setIndexNames(
    (0, "NETEXEC-MIB", "dsucsuCfgMaintSlot"),
    (0, "NETEXEC-MIB", "dsucsuCfgMaintNode"),
)
if mibBuilder.loadTexts:
    dsucsuCfgMaintEntry.setStatus("mandatory")


class _DsucsuCfgMaintSlot_Type(Integer32):
    """Custom type dsucsuCfgMaintSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_DsucsuCfgMaintSlot_Type.__name__ = "Integer32"
_DsucsuCfgMaintSlot_Object = MibTableColumn
dsucsuCfgMaintSlot = _DsucsuCfgMaintSlot_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 11, 1, 1),
    _DsucsuCfgMaintSlot_Type()
)
dsucsuCfgMaintSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsucsuCfgMaintSlot.setStatus("mandatory")


class _DsucsuCfgMaintNode_Type(Integer32):
    """Custom type dsucsuCfgMaintNode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_DsucsuCfgMaintNode_Type.__name__ = "Integer32"
_DsucsuCfgMaintNode_Object = MibTableColumn
dsucsuCfgMaintNode = _DsucsuCfgMaintNode_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 11, 1, 2),
    _DsucsuCfgMaintNode_Type()
)
dsucsuCfgMaintNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsucsuCfgMaintNode.setStatus("mandatory")


class _DsucsuCfgMaintChanType_Type(Integer32):
    """Custom type dsucsuCfgMaintChanType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 4),
          ("ascii", 3),
          ("disabled", 1),
          ("ext-event", 5),
          ("nsms", 2))
    )


_DsucsuCfgMaintChanType_Type.__name__ = "Integer32"
_DsucsuCfgMaintChanType_Object = MibTableColumn
dsucsuCfgMaintChanType = _DsucsuCfgMaintChanType_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 11, 1, 3),
    _DsucsuCfgMaintChanType_Type()
)
dsucsuCfgMaintChanType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsucsuCfgMaintChanType.setStatus("mandatory")


class _DsucsuCfgMaintFlowCtrl_Type(Integer32):
    """Custom type dsucsuCfgMaintFlowCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_DsucsuCfgMaintFlowCtrl_Type.__name__ = "Integer32"
_DsucsuCfgMaintFlowCtrl_Object = MibTableColumn
dsucsuCfgMaintFlowCtrl = _DsucsuCfgMaintFlowCtrl_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 11, 1, 4),
    _DsucsuCfgMaintFlowCtrl_Type()
)
dsucsuCfgMaintFlowCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsucsuCfgMaintFlowCtrl.setStatus("mandatory")


class _DsucsuCfgMaintStopBits_Type(Integer32):
    """Custom type dsucsuCfgMaintStopBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("stopbits-1", 1),
          ("stopbits-1-5", 2),
          ("stopbits-2", 3))
    )


_DsucsuCfgMaintStopBits_Type.__name__ = "Integer32"
_DsucsuCfgMaintStopBits_Object = MibTableColumn
dsucsuCfgMaintStopBits = _DsucsuCfgMaintStopBits_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 11, 1, 5),
    _DsucsuCfgMaintStopBits_Type()
)
dsucsuCfgMaintStopBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsucsuCfgMaintStopBits.setStatus("mandatory")


class _DsucsuCfgMaintParity_Type(Integer32):
    """Custom type dsucsuCfgMaintParity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("even", 3),
          ("none", 1),
          ("odd", 2))
    )


_DsucsuCfgMaintParity_Type.__name__ = "Integer32"
_DsucsuCfgMaintParity_Object = MibTableColumn
dsucsuCfgMaintParity = _DsucsuCfgMaintParity_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 11, 1, 6),
    _DsucsuCfgMaintParity_Type()
)
dsucsuCfgMaintParity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsucsuCfgMaintParity.setStatus("mandatory")


class _DsucsuCfgMaintDataBits_Type(Integer32):
    """Custom type dsucsuCfgMaintDataBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("databits-7", 1),
          ("databits-8", 2))
    )


_DsucsuCfgMaintDataBits_Type.__name__ = "Integer32"
_DsucsuCfgMaintDataBits_Object = MibTableColumn
dsucsuCfgMaintDataBits = _DsucsuCfgMaintDataBits_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 11, 1, 7),
    _DsucsuCfgMaintDataBits_Type()
)
dsucsuCfgMaintDataBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsucsuCfgMaintDataBits.setStatus("mandatory")


class _DsucsuCfgMaintBaud_Type(Integer32):
    """Custom type dsucsuCfgMaintBaud based on Integer32"""
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
        *(("baud-1200", 1),
          ("baud-2400", 2),
          ("baud-4800", 3),
          ("baud-9600", 4))
    )


_DsucsuCfgMaintBaud_Type.__name__ = "Integer32"
_DsucsuCfgMaintBaud_Object = MibTableColumn
dsucsuCfgMaintBaud = _DsucsuCfgMaintBaud_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 11, 1, 8),
    _DsucsuCfgMaintBaud_Type()
)
dsucsuCfgMaintBaud.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsucsuCfgMaintBaud.setStatus("mandatory")
_DsucsuCfgCommTable_Object = MibTable
dsucsuCfgCommTable = _DsucsuCfgCommTable_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 12)
)
if mibBuilder.loadTexts:
    dsucsuCfgCommTable.setStatus("mandatory")
_DsucsuCfgCommEntry_Object = MibTableRow
dsucsuCfgCommEntry = _DsucsuCfgCommEntry_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 12, 1)
)
dsucsuCfgCommEntry.setIndexNames(
    (0, "NETEXEC-MIB", "dsucsuCfgCommSlot"),
    (0, "NETEXEC-MIB", "dsucsuCfgCommNode"),
)
if mibBuilder.loadTexts:
    dsucsuCfgCommEntry.setStatus("mandatory")


class _DsucsuCfgCommSlot_Type(Integer32):
    """Custom type dsucsuCfgCommSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_DsucsuCfgCommSlot_Type.__name__ = "Integer32"
_DsucsuCfgCommSlot_Object = MibTableColumn
dsucsuCfgCommSlot = _DsucsuCfgCommSlot_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 12, 1, 1),
    _DsucsuCfgCommSlot_Type()
)
dsucsuCfgCommSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsucsuCfgCommSlot.setStatus("mandatory")


class _DsucsuCfgCommNode_Type(Integer32):
    """Custom type dsucsuCfgCommNode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_DsucsuCfgCommNode_Type.__name__ = "Integer32"
_DsucsuCfgCommNode_Object = MibTableColumn
dsucsuCfgCommNode = _DsucsuCfgCommNode_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 12, 1, 2),
    _DsucsuCfgCommNode_Type()
)
dsucsuCfgCommNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsucsuCfgCommNode.setStatus("mandatory")


class _DsucsuCfgCommChanType_Type(Integer32):
    """Custom type dsucsuCfgCommChanType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 4),
          ("ascii", 3),
          ("disabled", 1),
          ("ext-event", 5),
          ("nsms", 2))
    )


_DsucsuCfgCommChanType_Type.__name__ = "Integer32"
_DsucsuCfgCommChanType_Object = MibTableColumn
dsucsuCfgCommChanType = _DsucsuCfgCommChanType_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 12, 1, 3),
    _DsucsuCfgCommChanType_Type()
)
dsucsuCfgCommChanType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsucsuCfgCommChanType.setStatus("mandatory")


class _DsucsuCfgCommFlowCtrl_Type(Integer32):
    """Custom type dsucsuCfgCommFlowCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_DsucsuCfgCommFlowCtrl_Type.__name__ = "Integer32"
_DsucsuCfgCommFlowCtrl_Object = MibTableColumn
dsucsuCfgCommFlowCtrl = _DsucsuCfgCommFlowCtrl_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 12, 1, 4),
    _DsucsuCfgCommFlowCtrl_Type()
)
dsucsuCfgCommFlowCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsucsuCfgCommFlowCtrl.setStatus("mandatory")


class _DsucsuCfgCommStopBits_Type(Integer32):
    """Custom type dsucsuCfgCommStopBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("stopbits-1", 1),
          ("stopbits-1-5", 2),
          ("stopbits-2", 3))
    )


_DsucsuCfgCommStopBits_Type.__name__ = "Integer32"
_DsucsuCfgCommStopBits_Object = MibTableColumn
dsucsuCfgCommStopBits = _DsucsuCfgCommStopBits_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 12, 1, 5),
    _DsucsuCfgCommStopBits_Type()
)
dsucsuCfgCommStopBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsucsuCfgCommStopBits.setStatus("mandatory")


class _DsucsuCfgCommParity_Type(Integer32):
    """Custom type dsucsuCfgCommParity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("even", 3),
          ("none", 1),
          ("odd", 2))
    )


_DsucsuCfgCommParity_Type.__name__ = "Integer32"
_DsucsuCfgCommParity_Object = MibTableColumn
dsucsuCfgCommParity = _DsucsuCfgCommParity_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 12, 1, 6),
    _DsucsuCfgCommParity_Type()
)
dsucsuCfgCommParity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsucsuCfgCommParity.setStatus("mandatory")


class _DsucsuCfgCommDataBits_Type(Integer32):
    """Custom type dsucsuCfgCommDataBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("databits-7", 1),
          ("databits-8", 2))
    )


_DsucsuCfgCommDataBits_Type.__name__ = "Integer32"
_DsucsuCfgCommDataBits_Object = MibTableColumn
dsucsuCfgCommDataBits = _DsucsuCfgCommDataBits_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 12, 1, 7),
    _DsucsuCfgCommDataBits_Type()
)
dsucsuCfgCommDataBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsucsuCfgCommDataBits.setStatus("mandatory")


class _DsucsuCfgCommBaud_Type(Integer32):
    """Custom type dsucsuCfgCommBaud based on Integer32"""
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
        *(("baud-1200", 1),
          ("baud-2400", 2),
          ("baud-4800", 3),
          ("baud-9600", 4))
    )


_DsucsuCfgCommBaud_Type.__name__ = "Integer32"
_DsucsuCfgCommBaud_Object = MibTableColumn
dsucsuCfgCommBaud = _DsucsuCfgCommBaud_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 12, 1, 8),
    _DsucsuCfgCommBaud_Type()
)
dsucsuCfgCommBaud.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsucsuCfgCommBaud.setStatus("mandatory")
_DsucsuCfgBrdTable_Object = MibTable
dsucsuCfgBrdTable = _DsucsuCfgBrdTable_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 13)
)
if mibBuilder.loadTexts:
    dsucsuCfgBrdTable.setStatus("mandatory")
_DsucsuCfgBrdEntry_Object = MibTableRow
dsucsuCfgBrdEntry = _DsucsuCfgBrdEntry_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 13, 1)
)
dsucsuCfgBrdEntry.setIndexNames(
    (0, "NETEXEC-MIB", "dsucsuCfgBrdSlot"),
    (0, "NETEXEC-MIB", "dsucsuCfgBrdNode"),
)
if mibBuilder.loadTexts:
    dsucsuCfgBrdEntry.setStatus("mandatory")


class _DsucsuCfgBrdSlot_Type(Integer32):
    """Custom type dsucsuCfgBrdSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_DsucsuCfgBrdSlot_Type.__name__ = "Integer32"
_DsucsuCfgBrdSlot_Object = MibTableColumn
dsucsuCfgBrdSlot = _DsucsuCfgBrdSlot_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 13, 1, 1),
    _DsucsuCfgBrdSlot_Type()
)
dsucsuCfgBrdSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsucsuCfgBrdSlot.setStatus("mandatory")


class _DsucsuCfgBrdNode_Type(Integer32):
    """Custom type dsucsuCfgBrdNode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_DsucsuCfgBrdNode_Type.__name__ = "Integer32"
_DsucsuCfgBrdNode_Object = MibTableColumn
dsucsuCfgBrdNode = _DsucsuCfgBrdNode_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 13, 1, 2),
    _DsucsuCfgBrdNode_Type()
)
dsucsuCfgBrdNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsucsuCfgBrdNode.setStatus("mandatory")


class _DsucsuCfgBrdTiming_Type(Integer32):
    """Custom type dsucsuCfgBrdTiming based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("master", 1),
          ("port1", 2),
          ("port2", 3),
          ("port3", 4),
          ("port4", 5))
    )


_DsucsuCfgBrdTiming_Type.__name__ = "Integer32"
_DsucsuCfgBrdTiming_Object = MibTableColumn
dsucsuCfgBrdTiming = _DsucsuCfgBrdTiming_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 13, 1, 3),
    _DsucsuCfgBrdTiming_Type()
)
dsucsuCfgBrdTiming.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsucsuCfgBrdTiming.setStatus("mandatory")
_DsucsuCfgDacsTable_ObjectIdentity = ObjectIdentity
dsucsuCfgDacsTable = _DsucsuCfgDacsTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 14)
)
_DsucsuCfgAutoAssignTable_Object = MibTable
dsucsuCfgAutoAssignTable = _DsucsuCfgAutoAssignTable_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 14, 1)
)
if mibBuilder.loadTexts:
    dsucsuCfgAutoAssignTable.setStatus("mandatory")
_DsucsuCfgAutoAssignEntry_Object = MibTableRow
dsucsuCfgAutoAssignEntry = _DsucsuCfgAutoAssignEntry_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 14, 1, 1)
)
dsucsuCfgAutoAssignEntry.setIndexNames(
    (0, "NETEXEC-MIB", "dsucsuConnAutoSlot"),
    (0, "NETEXEC-MIB", "dsucsuConnAutoNode"),
    (0, "NETEXEC-MIB", "dsucsuConnAutoSrcPort"),
)
if mibBuilder.loadTexts:
    dsucsuCfgAutoAssignEntry.setStatus("mandatory")


class _DsucsuConnAutoSlot_Type(Integer32):
    """Custom type dsucsuConnAutoSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_DsucsuConnAutoSlot_Type.__name__ = "Integer32"
_DsucsuConnAutoSlot_Object = MibTableColumn
dsucsuConnAutoSlot = _DsucsuConnAutoSlot_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 14, 1, 1, 1),
    _DsucsuConnAutoSlot_Type()
)
dsucsuConnAutoSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsucsuConnAutoSlot.setStatus("mandatory")


class _DsucsuConnAutoNode_Type(Integer32):
    """Custom type dsucsuConnAutoNode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_DsucsuConnAutoNode_Type.__name__ = "Integer32"
_DsucsuConnAutoNode_Object = MibTableColumn
dsucsuConnAutoNode = _DsucsuConnAutoNode_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 14, 1, 1, 2),
    _DsucsuConnAutoNode_Type()
)
dsucsuConnAutoNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsucsuConnAutoNode.setStatus("mandatory")


class _DsucsuConnAutoSrcPort_Type(Integer32):
    """Custom type dsucsuConnAutoSrcPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_DsucsuConnAutoSrcPort_Type.__name__ = "Integer32"
_DsucsuConnAutoSrcPort_Object = MibTableColumn
dsucsuConnAutoSrcPort = _DsucsuConnAutoSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 14, 1, 1, 3),
    _DsucsuConnAutoSrcPort_Type()
)
dsucsuConnAutoSrcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsucsuConnAutoSrcPort.setStatus("mandatory")


class _DsucsuConnAutoStartDS0_Type(Integer32):
    """Custom type dsucsuConnAutoStartDS0 based on Integer32"""
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
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              40,
              41)
        )
    )
    namedValues = NamedValues(
        *(("ds0-01", 1),
          ("ds0-02", 2),
          ("ds0-03", 3),
          ("ds0-04", 4),
          ("ds0-05", 5),
          ("ds0-06", 6),
          ("ds0-07", 7),
          ("ds0-08", 8),
          ("ds0-09", 9),
          ("ds0-10", 10),
          ("ds0-11", 11),
          ("ds0-12", 12),
          ("ds0-13", 13),
          ("ds0-14", 14),
          ("ds0-15", 15),
          ("ds0-16", 16),
          ("ds0-17", 17),
          ("ds0-18", 18),
          ("ds0-19", 19),
          ("ds0-20", 20),
          ("ds0-21", 21),
          ("ds0-22", 22),
          ("ds0-23", 23),
          ("ds0-24", 24),
          ("no-current-connections", 40),
          ("non-continuous-ds0s", 41))
    )


_DsucsuConnAutoStartDS0_Type.__name__ = "Integer32"
_DsucsuConnAutoStartDS0_Object = MibTableColumn
dsucsuConnAutoStartDS0 = _DsucsuConnAutoStartDS0_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 14, 1, 1, 4),
    _DsucsuConnAutoStartDS0_Type()
)
dsucsuConnAutoStartDS0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsucsuConnAutoStartDS0.setStatus("mandatory")


class _DsucsuConnAutoDestPort_Type(Integer32):
    """Custom type dsucsuConnAutoDestPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              33)
        )
    )
    namedValues = NamedValues(
        *(("not-connected", 33),
          ("port1", 1),
          ("port2", 2),
          ("port3", 3),
          ("port4", 4))
    )


_DsucsuConnAutoDestPort_Type.__name__ = "Integer32"
_DsucsuConnAutoDestPort_Object = MibTableColumn
dsucsuConnAutoDestPort = _DsucsuConnAutoDestPort_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 14, 1, 1, 5),
    _DsucsuConnAutoDestPort_Type()
)
dsucsuConnAutoDestPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsucsuConnAutoDestPort.setStatus("mandatory")


class _DsucsuConnAutoType_Type(Integer32):
    """Custom type dsucsuConnAutoType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("data", 1),
          ("voice", 2))
    )


_DsucsuConnAutoType_Type.__name__ = "Integer32"
_DsucsuConnAutoType_Object = MibTableColumn
dsucsuConnAutoType = _DsucsuConnAutoType_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 14, 1, 1, 6),
    _DsucsuConnAutoType_Type()
)
dsucsuConnAutoType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsucsuConnAutoType.setStatus("mandatory")


class _DsucsuConnDteRate_Type(Integer32):
    """Custom type dsucsuConnDteRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1536000),
    )


_DsucsuConnDteRate_Type.__name__ = "Integer32"
_DsucsuConnDteRate_Object = MibTableColumn
dsucsuConnDteRate = _DsucsuConnDteRate_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 14, 1, 1, 7),
    _DsucsuConnDteRate_Type()
)
dsucsuConnDteRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsucsuConnDteRate.setStatus("mandatory")


class _DsucsuConnDteDensity_Type(Integer32):
    """Custom type dsucsuConnDteDensity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(56,
              64)
        )
    )
    namedValues = NamedValues(
        *(("bit-7-stuff", 56),
          ("clear-channel", 64))
    )


_DsucsuConnDteDensity_Type.__name__ = "Integer32"
_DsucsuConnDteDensity_Object = MibTableColumn
dsucsuConnDteDensity = _DsucsuConnDteDensity_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 14, 1, 1, 8),
    _DsucsuConnDteDensity_Type()
)
dsucsuConnDteDensity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsucsuConnDteDensity.setStatus("mandatory")


class _DsucsuConnDs0Required_Type(Integer32):
    """Custom type dsucsuConnDs0Required based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24),
    )


_DsucsuConnDs0Required_Type.__name__ = "Integer32"
_DsucsuConnDs0Required_Object = MibTableColumn
dsucsuConnDs0Required = _DsucsuConnDs0Required_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 14, 1, 1, 9),
    _DsucsuConnDs0Required_Type()
)
dsucsuConnDs0Required.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsucsuConnDs0Required.setStatus("mandatory")


class _DsucsuConnAutoStatus_Type(Integer32):
    """Custom type dsucsuConnAutoStatus based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("bandwidth-conflict", 4),
          ("connections-not-valid", 2),
          ("connections-valid", 1),
          ("incorrect-bandwidth", 3),
          ("no-current-connections", 5),
          ("port-invalid", 11),
          ("port-type-invalid", 7),
          ("port-type-valid", 6),
          ("port-valid", 10),
          ("start-ds0-invalid", 9),
          ("start-ds0-valid", 8))
    )


_DsucsuConnAutoStatus_Type.__name__ = "Integer32"
_DsucsuConnAutoStatus_Object = MibTableColumn
dsucsuConnAutoStatus = _DsucsuConnAutoStatus_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 14, 1, 1, 10),
    _DsucsuConnAutoStatus_Type()
)
dsucsuConnAutoStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsucsuConnAutoStatus.setStatus("mandatory")


class _DsucsuConnAutoUpdateCmd_Type(Integer32):
    """Custom type dsucsuConnAutoUpdateCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("update", 1)
    )


_DsucsuConnAutoUpdateCmd_Type.__name__ = "Integer32"
_DsucsuConnAutoUpdateCmd_Object = MibTableColumn
dsucsuConnAutoUpdateCmd = _DsucsuConnAutoUpdateCmd_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 14, 1, 1, 11),
    _DsucsuConnAutoUpdateCmd_Type()
)
dsucsuConnAutoUpdateCmd.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    dsucsuConnAutoUpdateCmd.setStatus("mandatory")
_DsucsuCfgCurrentConnTable_Object = MibTable
dsucsuCfgCurrentConnTable = _DsucsuCfgCurrentConnTable_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 14, 2)
)
if mibBuilder.loadTexts:
    dsucsuCfgCurrentConnTable.setStatus("mandatory")
_DsucsuCfgCurrentConnections_Object = MibTableRow
dsucsuCfgCurrentConnections = _DsucsuCfgCurrentConnections_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 14, 2, 1)
)
dsucsuCfgCurrentConnections.setIndexNames(
    (0, "NETEXEC-MIB", "dsucsuSlot"),
    (0, "NETEXEC-MIB", "dsucsuNode"),
    (0, "NETEXEC-MIB", "dsucsuT1Index"),
    (0, "NETEXEC-MIB", "dsucsuDs0"),
)
if mibBuilder.loadTexts:
    dsucsuCfgCurrentConnections.setStatus("mandatory")


class _DsucsuSlot_Type(Integer32):
    """Custom type dsucsuSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_DsucsuSlot_Type.__name__ = "Integer32"
_DsucsuSlot_Object = MibTableColumn
dsucsuSlot = _DsucsuSlot_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 14, 2, 1, 1),
    _DsucsuSlot_Type()
)
dsucsuSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsucsuSlot.setStatus("mandatory")


class _DsucsuNode_Type(Integer32):
    """Custom type dsucsuNode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_DsucsuNode_Type.__name__ = "Integer32"
_DsucsuNode_Object = MibTableColumn
dsucsuNode = _DsucsuNode_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 14, 2, 1, 2),
    _DsucsuNode_Type()
)
dsucsuNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsucsuNode.setStatus("mandatory")


class _DsucsuT1Index_Type(Integer32):
    """Custom type dsucsuT1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_DsucsuT1Index_Type.__name__ = "Integer32"
_DsucsuT1Index_Object = MibTableColumn
dsucsuT1Index = _DsucsuT1Index_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 14, 2, 1, 3),
    _DsucsuT1Index_Type()
)
dsucsuT1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsucsuT1Index.setStatus("mandatory")


class _DsucsuDs0_Type(Integer32):
    """Custom type dsucsuDs0 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_DsucsuDs0_Type.__name__ = "Integer32"
_DsucsuDs0_Object = MibTableColumn
dsucsuDs0 = _DsucsuDs0_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 14, 2, 1, 4),
    _DsucsuDs0_Type()
)
dsucsuDs0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsucsuDs0.setStatus("mandatory")


class _DsucsuDtePort_Type(Integer32):
    """Custom type dsucsuDtePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              33)
        )
    )
    namedValues = NamedValues(
        *(("not-connected", 33),
          ("port1", 1),
          ("port2", 2),
          ("port3", 3),
          ("port4", 4))
    )


_DsucsuDtePort_Type.__name__ = "Integer32"
_DsucsuDtePort_Object = MibTableColumn
dsucsuDtePort = _DsucsuDtePort_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 14, 2, 1, 5),
    _DsucsuDtePort_Type()
)
dsucsuDtePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsucsuDtePort.setStatus("mandatory")


class _DsucsuType_Type(Integer32):
    """Custom type dsucsuType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("data", 1),
          ("voice", 2))
    )


_DsucsuType_Type.__name__ = "Integer32"
_DsucsuType_Object = MibTableColumn
dsucsuType = _DsucsuType_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 14, 2, 1, 6),
    _DsucsuType_Type()
)
dsucsuType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsucsuType.setStatus("mandatory")
_DsucsuCfgEditConnTable_Object = MibTable
dsucsuCfgEditConnTable = _DsucsuCfgEditConnTable_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 14, 3)
)
if mibBuilder.loadTexts:
    dsucsuCfgEditConnTable.setStatus("mandatory")
_DsucsuCfgEditConnEntry_Object = MibTableRow
dsucsuCfgEditConnEntry = _DsucsuCfgEditConnEntry_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 14, 3, 1)
)
dsucsuCfgEditConnEntry.setIndexNames(
    (0, "NETEXEC-MIB", "dsucsuConnSlot"),
    (0, "NETEXEC-MIB", "dsucsuConnNode"),
    (0, "NETEXEC-MIB", "dsucsuConnSrcPort"),
    (0, "NETEXEC-MIB", "dsucsuConnSrcDs0"),
)
if mibBuilder.loadTexts:
    dsucsuCfgEditConnEntry.setStatus("mandatory")


class _DsucsuConnSlot_Type(Integer32):
    """Custom type dsucsuConnSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_DsucsuConnSlot_Type.__name__ = "Integer32"
_DsucsuConnSlot_Object = MibTableColumn
dsucsuConnSlot = _DsucsuConnSlot_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 14, 3, 1, 1),
    _DsucsuConnSlot_Type()
)
dsucsuConnSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsucsuConnSlot.setStatus("mandatory")


class _DsucsuConnNode_Type(Integer32):
    """Custom type dsucsuConnNode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_DsucsuConnNode_Type.__name__ = "Integer32"
_DsucsuConnNode_Object = MibTableColumn
dsucsuConnNode = _DsucsuConnNode_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 14, 3, 1, 2),
    _DsucsuConnNode_Type()
)
dsucsuConnNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsucsuConnNode.setStatus("mandatory")


class _DsucsuConnSrcPort_Type(Integer32):
    """Custom type dsucsuConnSrcPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_DsucsuConnSrcPort_Type.__name__ = "Integer32"
_DsucsuConnSrcPort_Object = MibTableColumn
dsucsuConnSrcPort = _DsucsuConnSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 14, 3, 1, 3),
    _DsucsuConnSrcPort_Type()
)
dsucsuConnSrcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsucsuConnSrcPort.setStatus("mandatory")


class _DsucsuConnSrcDs0_Type(Integer32):
    """Custom type dsucsuConnSrcDs0 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_DsucsuConnSrcDs0_Type.__name__ = "Integer32"
_DsucsuConnSrcDs0_Object = MibTableColumn
dsucsuConnSrcDs0 = _DsucsuConnSrcDs0_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 14, 3, 1, 4),
    _DsucsuConnSrcDs0_Type()
)
dsucsuConnSrcDs0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsucsuConnSrcDs0.setStatus("mandatory")


class _DsucsuConnDestPort_Type(Integer32):
    """Custom type dsucsuConnDestPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              33)
        )
    )
    namedValues = NamedValues(
        *(("not-connected", 33),
          ("port1", 1),
          ("port2", 2),
          ("port3", 3),
          ("port4", 4))
    )


_DsucsuConnDestPort_Type.__name__ = "Integer32"
_DsucsuConnDestPort_Object = MibTableColumn
dsucsuConnDestPort = _DsucsuConnDestPort_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 14, 3, 1, 5),
    _DsucsuConnDestPort_Type()
)
dsucsuConnDestPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsucsuConnDestPort.setStatus("mandatory")


class _DsucsuConnDestDs0_Type(Integer32):
    """Custom type dsucsuConnDestDs0 based on Integer32"""
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
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              40,
              41)
        )
    )
    namedValues = NamedValues(
        *(("ds0-01", 1),
          ("ds0-02", 2),
          ("ds0-03", 3),
          ("ds0-04", 4),
          ("ds0-05", 5),
          ("ds0-06", 6),
          ("ds0-07", 7),
          ("ds0-08", 8),
          ("ds0-09", 9),
          ("ds0-10", 10),
          ("ds0-11", 11),
          ("ds0-12", 12),
          ("ds0-13", 13),
          ("ds0-14", 14),
          ("ds0-15", 15),
          ("ds0-16", 16),
          ("ds0-17", 17),
          ("ds0-18", 18),
          ("ds0-19", 19),
          ("ds0-20", 20),
          ("ds0-21", 21),
          ("ds0-22", 22),
          ("ds0-23", 23),
          ("ds0-24", 24),
          ("no-current-connections", 40),
          ("non-continuous-ds0s", 41))
    )


_DsucsuConnDestDs0_Type.__name__ = "Integer32"
_DsucsuConnDestDs0_Object = MibTableColumn
dsucsuConnDestDs0 = _DsucsuConnDestDs0_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 14, 3, 1, 6),
    _DsucsuConnDestDs0_Type()
)
dsucsuConnDestDs0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsucsuConnDestDs0.setStatus("mandatory")


class _DsucsuConnType_Type(Integer32):
    """Custom type dsucsuConnType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("data", 1),
          ("voice", 2))
    )


_DsucsuConnType_Type.__name__ = "Integer32"
_DsucsuConnType_Object = MibTableColumn
dsucsuConnType = _DsucsuConnType_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 14, 3, 1, 7),
    _DsucsuConnType_Type()
)
dsucsuConnType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsucsuConnType.setStatus("mandatory")


class _DsucsuConnNumDs0s_Type(Integer32):
    """Custom type dsucsuConnNumDs0s based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_DsucsuConnNumDs0s_Type.__name__ = "Integer32"
_DsucsuConnNumDs0s_Object = MibTableColumn
dsucsuConnNumDs0s = _DsucsuConnNumDs0s_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 14, 3, 1, 8),
    _DsucsuConnNumDs0s_Type()
)
dsucsuConnNumDs0s.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsucsuConnNumDs0s.setStatus("mandatory")


class _DsucsuConnSetStatus_Type(Integer32):
    """Custom type dsucsuConnSetStatus based on Integer32"""
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("bandwidth-conflict", 4),
          ("connections-not-valid", 2),
          ("connections-valid", 1),
          ("destination-ds0-invalid", 9),
          ("destination-ds0-valid", 8),
          ("incorrect-bandwidth", 3),
          ("no-current-connections", 5),
          ("num-ds0s-invalid", 13),
          ("num-ds0s-valid", 12),
          ("port-invalid", 11),
          ("port-type-invalid", 7),
          ("port-type-valid", 6),
          ("port-valid", 10))
    )


_DsucsuConnSetStatus_Type.__name__ = "Integer32"
_DsucsuConnSetStatus_Object = MibTableColumn
dsucsuConnSetStatus = _DsucsuConnSetStatus_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 14, 3, 1, 9),
    _DsucsuConnSetStatus_Type()
)
dsucsuConnSetStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsucsuConnSetStatus.setStatus("mandatory")


class _DsucsuConnConnect_Type(Integer32):
    """Custom type dsucsuConnConnect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("connect", 1),
          ("disconnect", 2))
    )


_DsucsuConnConnect_Type.__name__ = "Integer32"
_DsucsuConnConnect_Object = MibTableColumn
dsucsuConnConnect = _DsucsuConnConnect_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 14, 3, 1, 10),
    _DsucsuConnConnect_Type()
)
dsucsuConnConnect.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    dsucsuConnConnect.setStatus("mandatory")


class _DsucsuConnUpdateRequired_Type(Integer32):
    """Custom type dsucsuConnUpdateRequired based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("update-not-required", 1),
          ("update-required", 2))
    )


_DsucsuConnUpdateRequired_Type.__name__ = "Integer32"
_DsucsuConnUpdateRequired_Object = MibTableColumn
dsucsuConnUpdateRequired = _DsucsuConnUpdateRequired_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 14, 3, 1, 11),
    _DsucsuConnUpdateRequired_Type()
)
dsucsuConnUpdateRequired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsucsuConnUpdateRequired.setStatus("mandatory")


class _DsucsuConnUpdateCmd_Type(Integer32):
    """Custom type dsucsuConnUpdateCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("update", 1)
    )


_DsucsuConnUpdateCmd_Type.__name__ = "Integer32"
_DsucsuConnUpdateCmd_Object = MibTableColumn
dsucsuConnUpdateCmd = _DsucsuConnUpdateCmd_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 14, 3, 1, 12),
    _DsucsuConnUpdateCmd_Type()
)
dsucsuConnUpdateCmd.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    dsucsuConnUpdateCmd.setStatus("mandatory")


class _DsucsuConnClearEditBuff_Type(Integer32):
    """Custom type dsucsuConnClearEditBuff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear-edit", 1)
    )


_DsucsuConnClearEditBuff_Type.__name__ = "Integer32"
_DsucsuConnClearEditBuff_Object = MibTableColumn
dsucsuConnClearEditBuff = _DsucsuConnClearEditBuff_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 14, 3, 1, 13),
    _DsucsuConnClearEditBuff_Type()
)
dsucsuConnClearEditBuff.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    dsucsuConnClearEditBuff.setStatus("mandatory")
_DsucsuDiagNetTable_Object = MibTable
dsucsuDiagNetTable = _DsucsuDiagNetTable_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 15)
)
if mibBuilder.loadTexts:
    dsucsuDiagNetTable.setStatus("mandatory")
_DsucsuDiagNetEntry_Object = MibTableRow
dsucsuDiagNetEntry = _DsucsuDiagNetEntry_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 15, 1)
)
dsucsuDiagNetEntry.setIndexNames(
    (0, "NETEXEC-MIB", "dsucsuDiagNetSlot"),
    (0, "NETEXEC-MIB", "dsucsuDiagNetNode"),
    (0, "NETEXEC-MIB", "dsucsuDiagNetIndex"),
)
if mibBuilder.loadTexts:
    dsucsuDiagNetEntry.setStatus("mandatory")


class _DsucsuDiagNetSlot_Type(Integer32):
    """Custom type dsucsuDiagNetSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_DsucsuDiagNetSlot_Type.__name__ = "Integer32"
_DsucsuDiagNetSlot_Object = MibTableColumn
dsucsuDiagNetSlot = _DsucsuDiagNetSlot_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 15, 1, 1),
    _DsucsuDiagNetSlot_Type()
)
dsucsuDiagNetSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsucsuDiagNetSlot.setStatus("mandatory")


class _DsucsuDiagNetNode_Type(Integer32):
    """Custom type dsucsuDiagNetNode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_DsucsuDiagNetNode_Type.__name__ = "Integer32"
_DsucsuDiagNetNode_Object = MibTableColumn
dsucsuDiagNetNode = _DsucsuDiagNetNode_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 15, 1, 2),
    _DsucsuDiagNetNode_Type()
)
dsucsuDiagNetNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsucsuDiagNetNode.setStatus("mandatory")


class _DsucsuDiagNetIndex_Type(Integer32):
    """Custom type dsucsuDiagNetIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_DsucsuDiagNetIndex_Type.__name__ = "Integer32"
_DsucsuDiagNetIndex_Object = MibTableColumn
dsucsuDiagNetIndex = _DsucsuDiagNetIndex_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 15, 1, 3),
    _DsucsuDiagNetIndex_Type()
)
dsucsuDiagNetIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsucsuDiagNetIndex.setStatus("mandatory")


class _DsucsuDiagNetLclNetAggLpbk_Type(Integer32):
    """Custom type dsucsuDiagNetLclNetAggLpbk based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disableLoopbackMode", 2),
          ("enableLoopbackMode", 1),
          ("notApplicable", 3))
    )


_DsucsuDiagNetLclNetAggLpbk_Type.__name__ = "Integer32"
_DsucsuDiagNetLclNetAggLpbk_Object = MibTableColumn
dsucsuDiagNetLclNetAggLpbk = _DsucsuDiagNetLclNetAggLpbk_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 15, 1, 4),
    _DsucsuDiagNetLclNetAggLpbk_Type()
)
dsucsuDiagNetLclNetAggLpbk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsucsuDiagNetLclNetAggLpbk.setStatus("mandatory")


class _DsucsuDiagNetLclNetLpbk_Type(Integer32):
    """Custom type dsucsuDiagNetLclNetLpbk based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disableLoopbackMode", 2),
          ("enableLoopbackMode", 1),
          ("notApplicable", 3))
    )


_DsucsuDiagNetLclNetLpbk_Type.__name__ = "Integer32"
_DsucsuDiagNetLclNetLpbk_Object = MibTableColumn
dsucsuDiagNetLclNetLpbk = _DsucsuDiagNetLclNetLpbk_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 15, 1, 5),
    _DsucsuDiagNetLclNetLpbk_Type()
)
dsucsuDiagNetLclNetLpbk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsucsuDiagNetLclNetLpbk.setStatus("mandatory")


class _DsucsuDiagNetLclNetPayload_Type(Integer32):
    """Custom type dsucsuDiagNetLclNetPayload based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disableLoopbackMode", 2),
          ("enableLoopbackMode", 1),
          ("notApplicable", 3))
    )


_DsucsuDiagNetLclNetPayload_Type.__name__ = "Integer32"
_DsucsuDiagNetLclNetPayload_Object = MibTableColumn
dsucsuDiagNetLclNetPayload = _DsucsuDiagNetLclNetPayload_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 15, 1, 6),
    _DsucsuDiagNetLclNetPayload_Type()
)
dsucsuDiagNetLclNetPayload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsucsuDiagNetLclNetPayload.setStatus("mandatory")


class _DsucsuDiagNetLclNetBiDir_Type(Integer32):
    """Custom type dsucsuDiagNetLclNetBiDir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disableLoopbackMode", 2),
          ("enableLoopbackMode", 1),
          ("notApplicable", 3))
    )


_DsucsuDiagNetLclNetBiDir_Type.__name__ = "Integer32"
_DsucsuDiagNetLclNetBiDir_Object = MibTableColumn
dsucsuDiagNetLclNetBiDir = _DsucsuDiagNetLclNetBiDir_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 15, 1, 7),
    _DsucsuDiagNetLclNetBiDir_Type()
)
dsucsuDiagNetLclNetBiDir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsucsuDiagNetLclNetBiDir.setStatus("mandatory")


class _DsucsuDiagNetRemCsuLpbk_Type(Integer32):
    """Custom type dsucsuDiagNetRemCsuLpbk based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 3),
          ("transmitLoopDownCode", 2),
          ("transmitLoopUpCode", 1))
    )


_DsucsuDiagNetRemCsuLpbk_Type.__name__ = "Integer32"
_DsucsuDiagNetRemCsuLpbk_Object = MibTableColumn
dsucsuDiagNetRemCsuLpbk = _DsucsuDiagNetRemCsuLpbk_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 15, 1, 8),
    _DsucsuDiagNetRemCsuLpbk_Type()
)
dsucsuDiagNetRemCsuLpbk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsucsuDiagNetRemCsuLpbk.setStatus("mandatory")


class _DsucsuDiagNetRemDsuLpbk_Type(Integer32):
    """Custom type dsucsuDiagNetRemDsuLpbk based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disableLoopbackMode", 2),
          ("enableLoopbackMode", 1),
          ("notApplicable", 3))
    )


_DsucsuDiagNetRemDsuLpbk_Type.__name__ = "Integer32"
_DsucsuDiagNetRemDsuLpbk_Object = MibTableColumn
dsucsuDiagNetRemDsuLpbk = _DsucsuDiagNetRemDsuLpbk_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 15, 1, 9),
    _DsucsuDiagNetRemDsuLpbk_Type()
)
dsucsuDiagNetRemDsuLpbk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsucsuDiagNetRemDsuLpbk.setStatus("mandatory")
_DsucsuDiagNetEvElapTime_Type = TimeTicks
_DsucsuDiagNetEvElapTime_Object = MibTableColumn
dsucsuDiagNetEvElapTime = _DsucsuDiagNetEvElapTime_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 15, 1, 10),
    _DsucsuDiagNetEvElapTime_Type()
)
dsucsuDiagNetEvElapTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsucsuDiagNetEvElapTime.setStatus("mandatory")
_DsucsuDiagNetEvCRC6Err_Type = Counter32
_DsucsuDiagNetEvCRC6Err_Object = MibTableColumn
dsucsuDiagNetEvCRC6Err = _DsucsuDiagNetEvCRC6Err_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 15, 1, 11),
    _DsucsuDiagNetEvCRC6Err_Type()
)
dsucsuDiagNetEvCRC6Err.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsucsuDiagNetEvCRC6Err.setStatus("mandatory")
_DsucsuDiagNetEvOofErr_Type = Counter32
_DsucsuDiagNetEvOofErr_Object = MibTableColumn
dsucsuDiagNetEvOofErr = _DsucsuDiagNetEvOofErr_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 15, 1, 12),
    _DsucsuDiagNetEvOofErr_Type()
)
dsucsuDiagNetEvOofErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsucsuDiagNetEvOofErr.setStatus("mandatory")
_DsucsuDiagNetErrEvents_Type = Counter32
_DsucsuDiagNetErrEvents_Object = MibTableColumn
dsucsuDiagNetErrEvents = _DsucsuDiagNetErrEvents_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 15, 1, 13),
    _DsucsuDiagNetErrEvents_Type()
)
dsucsuDiagNetErrEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsucsuDiagNetErrEvents.setStatus("mandatory")


class _DsucsuDiagNetClearEvReg_Type(Integer32):
    """Custom type dsucsuDiagNetClearEvReg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clearRegister", 1)
    )


_DsucsuDiagNetClearEvReg_Type.__name__ = "Integer32"
_DsucsuDiagNetClearEvReg_Object = MibTableColumn
dsucsuDiagNetClearEvReg = _DsucsuDiagNetClearEvReg_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 15, 1, 14),
    _DsucsuDiagNetClearEvReg_Type()
)
dsucsuDiagNetClearEvReg.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    dsucsuDiagNetClearEvReg.setStatus("mandatory")
_DsucsuDiagDteTable_Object = MibTable
dsucsuDiagDteTable = _DsucsuDiagDteTable_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 16)
)
if mibBuilder.loadTexts:
    dsucsuDiagDteTable.setStatus("mandatory")
_DsucsuDiagDteEntry_Object = MibTableRow
dsucsuDiagDteEntry = _DsucsuDiagDteEntry_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 16, 1)
)
dsucsuDiagDteEntry.setIndexNames(
    (0, "NETEXEC-MIB", "dsucsuDiagDteSlot"),
    (0, "NETEXEC-MIB", "dsucsuDiagDteNode"),
    (0, "NETEXEC-MIB", "dsucsuDiagDteIndex"),
)
if mibBuilder.loadTexts:
    dsucsuDiagDteEntry.setStatus("mandatory")


class _DsucsuDiagDteSlot_Type(Integer32):
    """Custom type dsucsuDiagDteSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_DsucsuDiagDteSlot_Type.__name__ = "Integer32"
_DsucsuDiagDteSlot_Object = MibTableColumn
dsucsuDiagDteSlot = _DsucsuDiagDteSlot_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 16, 1, 1),
    _DsucsuDiagDteSlot_Type()
)
dsucsuDiagDteSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsucsuDiagDteSlot.setStatus("mandatory")


class _DsucsuDiagDteNode_Type(Integer32):
    """Custom type dsucsuDiagDteNode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_DsucsuDiagDteNode_Type.__name__ = "Integer32"
_DsucsuDiagDteNode_Object = MibTableColumn
dsucsuDiagDteNode = _DsucsuDiagDteNode_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 16, 1, 2),
    _DsucsuDiagDteNode_Type()
)
dsucsuDiagDteNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsucsuDiagDteNode.setStatus("mandatory")


class _DsucsuDiagDteIndex_Type(Integer32):
    """Custom type dsucsuDiagDteIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_DsucsuDiagDteIndex_Type.__name__ = "Integer32"
_DsucsuDiagDteIndex_Object = MibTableColumn
dsucsuDiagDteIndex = _DsucsuDiagDteIndex_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 16, 1, 3),
    _DsucsuDiagDteIndex_Type()
)
dsucsuDiagDteIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsucsuDiagDteIndex.setStatus("mandatory")


class _DsucsuDiagDteLocalBiDir_Type(Integer32):
    """Custom type dsucsuDiagDteLocalBiDir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disableLoopbackMode", 2),
          ("enableLoopbackMode", 1),
          ("notApplicable", 3))
    )


_DsucsuDiagDteLocalBiDir_Type.__name__ = "Integer32"
_DsucsuDiagDteLocalBiDir_Object = MibTableColumn
dsucsuDiagDteLocalBiDir = _DsucsuDiagDteLocalBiDir_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 16, 1, 4),
    _DsucsuDiagDteLocalBiDir_Type()
)
dsucsuDiagDteLocalBiDir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsucsuDiagDteLocalBiDir.setStatus("mandatory")


class _DsucsuDiagDteLocalPayload_Type(Integer32):
    """Custom type dsucsuDiagDteLocalPayload based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disableLoopbackMode", 2),
          ("enableLoopbackMode", 1),
          ("notApplicable", 3))
    )


_DsucsuDiagDteLocalPayload_Type.__name__ = "Integer32"
_DsucsuDiagDteLocalPayload_Object = MibTableColumn
dsucsuDiagDteLocalPayload = _DsucsuDiagDteLocalPayload_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 16, 1, 5),
    _DsucsuDiagDteLocalPayload_Type()
)
dsucsuDiagDteLocalPayload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsucsuDiagDteLocalPayload.setStatus("mandatory")


class _DsucsuDiagDteRemLpbk_Type(Integer32):
    """Custom type dsucsuDiagDteRemLpbk based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disableLoopbackMode", 2),
          ("enableLoopbackMode", 1),
          ("notApplicable", 3))
    )


_DsucsuDiagDteRemLpbk_Type.__name__ = "Integer32"
_DsucsuDiagDteRemLpbk_Object = MibTableColumn
dsucsuDiagDteRemLpbk = _DsucsuDiagDteRemLpbk_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 16, 1, 6),
    _DsucsuDiagDteRemLpbk_Type()
)
dsucsuDiagDteRemLpbk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsucsuDiagDteRemLpbk.setStatus("mandatory")


class _DsucsuDiagDteBertTestAct_Type(Integer32):
    """Custom type dsucsuDiagDteBertTestAct based on Integer32"""
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
        *(("clearErrorBertTest", 4),
          ("injectErrorBertTest", 3),
          ("startBertTest", 1),
          ("stopBertTest", 2))
    )


_DsucsuDiagDteBertTestAct_Type.__name__ = "Integer32"
_DsucsuDiagDteBertTestAct_Object = MibTableColumn
dsucsuDiagDteBertTestAct = _DsucsuDiagDteBertTestAct_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 16, 1, 7),
    _DsucsuDiagDteBertTestAct_Type()
)
dsucsuDiagDteBertTestAct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsucsuDiagDteBertTestAct.setStatus("mandatory")


class _DsucsuDiagDteBertHourStrt_Type(Integer32):
    """Custom type dsucsuDiagDteBertHourStrt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_DsucsuDiagDteBertHourStrt_Type.__name__ = "Integer32"
_DsucsuDiagDteBertHourStrt_Object = MibTableColumn
dsucsuDiagDteBertHourStrt = _DsucsuDiagDteBertHourStrt_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 16, 1, 8),
    _DsucsuDiagDteBertHourStrt_Type()
)
dsucsuDiagDteBertHourStrt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsucsuDiagDteBertHourStrt.setStatus("mandatory")


class _DsucsuDiagDteBertMinStrt_Type(Integer32):
    """Custom type dsucsuDiagDteBertMinStrt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_DsucsuDiagDteBertMinStrt_Type.__name__ = "Integer32"
_DsucsuDiagDteBertMinStrt_Object = MibTableColumn
dsucsuDiagDteBertMinStrt = _DsucsuDiagDteBertMinStrt_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 16, 1, 9),
    _DsucsuDiagDteBertMinStrt_Type()
)
dsucsuDiagDteBertMinStrt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsucsuDiagDteBertMinStrt.setStatus("mandatory")
_DsucsuDiagDteBertTimeElaps_Type = TimeTicks
_DsucsuDiagDteBertTimeElaps_Object = MibTableColumn
dsucsuDiagDteBertTimeElaps = _DsucsuDiagDteBertTimeElaps_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 16, 1, 10),
    _DsucsuDiagDteBertTimeElaps_Type()
)
dsucsuDiagDteBertTimeElaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsucsuDiagDteBertTimeElaps.setStatus("mandatory")
_DsucsuDiagDteBertErrors_Type = Counter32
_DsucsuDiagDteBertErrors_Object = MibTableColumn
dsucsuDiagDteBertErrors = _DsucsuDiagDteBertErrors_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 16, 1, 11),
    _DsucsuDiagDteBertErrors_Type()
)
dsucsuDiagDteBertErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsucsuDiagDteBertErrors.setStatus("mandatory")
_DsucsuDiagFrmTable_Object = MibTable
dsucsuDiagFrmTable = _DsucsuDiagFrmTable_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 17)
)
if mibBuilder.loadTexts:
    dsucsuDiagFrmTable.setStatus("mandatory")
_DsucsuDiagFrmEntry_Object = MibTableRow
dsucsuDiagFrmEntry = _DsucsuDiagFrmEntry_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 17, 1)
)
dsucsuDiagFrmEntry.setIndexNames(
    (0, "NETEXEC-MIB", "dsucsuDiagFrmSlot"),
    (0, "NETEXEC-MIB", "dsucsuDiagFrmNode"),
    (0, "NETEXEC-MIB", "dsucsuDiagFrmIndex"),
)
if mibBuilder.loadTexts:
    dsucsuDiagFrmEntry.setStatus("mandatory")


class _DsucsuDiagFrmSlot_Type(Integer32):
    """Custom type dsucsuDiagFrmSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_DsucsuDiagFrmSlot_Type.__name__ = "Integer32"
_DsucsuDiagFrmSlot_Object = MibTableColumn
dsucsuDiagFrmSlot = _DsucsuDiagFrmSlot_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 17, 1, 1),
    _DsucsuDiagFrmSlot_Type()
)
dsucsuDiagFrmSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsucsuDiagFrmSlot.setStatus("mandatory")


class _DsucsuDiagFrmNode_Type(Integer32):
    """Custom type dsucsuDiagFrmNode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_DsucsuDiagFrmNode_Type.__name__ = "Integer32"
_DsucsuDiagFrmNode_Object = MibTableColumn
dsucsuDiagFrmNode = _DsucsuDiagFrmNode_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 17, 1, 2),
    _DsucsuDiagFrmNode_Type()
)
dsucsuDiagFrmNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsucsuDiagFrmNode.setStatus("mandatory")


class _DsucsuDiagFrmIndex_Type(Integer32):
    """Custom type dsucsuDiagFrmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_DsucsuDiagFrmIndex_Type.__name__ = "Integer32"
_DsucsuDiagFrmIndex_Object = MibTableColumn
dsucsuDiagFrmIndex = _DsucsuDiagFrmIndex_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 17, 1, 3),
    _DsucsuDiagFrmIndex_Type()
)
dsucsuDiagFrmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsucsuDiagFrmIndex.setStatus("mandatory")


class _DsucsuDiagFrmLclLpbk_Type(Integer32):
    """Custom type dsucsuDiagFrmLclLpbk based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disableLoopbackMode", 2),
          ("enableLoopbackMode", 1),
          ("notApplicable", 3))
    )


_DsucsuDiagFrmLclLpbk_Type.__name__ = "Integer32"
_DsucsuDiagFrmLclLpbk_Object = MibTableColumn
dsucsuDiagFrmLclLpbk = _DsucsuDiagFrmLclLpbk_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 17, 1, 4),
    _DsucsuDiagFrmLclLpbk_Type()
)
dsucsuDiagFrmLclLpbk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsucsuDiagFrmLclLpbk.setStatus("mandatory")


class _DsucsuDiagFrmLclPayload_Type(Integer32):
    """Custom type dsucsuDiagFrmLclPayload based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disableLoopbackMode", 2),
          ("enableLoopbackMode", 1),
          ("notApplicable", 3))
    )


_DsucsuDiagFrmLclPayload_Type.__name__ = "Integer32"
_DsucsuDiagFrmLclPayload_Object = MibTableColumn
dsucsuDiagFrmLclPayload = _DsucsuDiagFrmLclPayload_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 17, 1, 5),
    _DsucsuDiagFrmLclPayload_Type()
)
dsucsuDiagFrmLclPayload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsucsuDiagFrmLclPayload.setStatus("mandatory")


class _DsucsuDiagFrmLclBiDir_Type(Integer32):
    """Custom type dsucsuDiagFrmLclBiDir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disableLoopbackMode", 2),
          ("enableLoopbackMode", 1),
          ("notApplicable", 3))
    )


_DsucsuDiagFrmLclBiDir_Type.__name__ = "Integer32"
_DsucsuDiagFrmLclBiDir_Object = MibTableColumn
dsucsuDiagFrmLclBiDir = _DsucsuDiagFrmLclBiDir_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 17, 1, 6),
    _DsucsuDiagFrmLclBiDir_Type()
)
dsucsuDiagFrmLclBiDir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsucsuDiagFrmLclBiDir.setStatus("mandatory")


class _DsucsuDiagFrmRemLpbk_Type(Integer32):
    """Custom type dsucsuDiagFrmRemLpbk based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 3),
          ("transmitLoopDownCode", 2),
          ("transmitLoopUpCode", 1))
    )


_DsucsuDiagFrmRemLpbk_Type.__name__ = "Integer32"
_DsucsuDiagFrmRemLpbk_Object = MibTableColumn
dsucsuDiagFrmRemLpbk = _DsucsuDiagFrmRemLpbk_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 17, 1, 7),
    _DsucsuDiagFrmRemLpbk_Type()
)
dsucsuDiagFrmRemLpbk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsucsuDiagFrmRemLpbk.setStatus("mandatory")


class _DsucsuDiagFrmLclDte_Type(Integer32):
    """Custom type dsucsuDiagFrmLclDte based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disableLoopbackMode", 2),
          ("enableLoopbackMode", 1),
          ("notApplicable", 3))
    )


_DsucsuDiagFrmLclDte_Type.__name__ = "Integer32"
_DsucsuDiagFrmLclDte_Object = MibTableColumn
dsucsuDiagFrmLclDte = _DsucsuDiagFrmLclDte_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 17, 1, 8),
    _DsucsuDiagFrmLclDte_Type()
)
dsucsuDiagFrmLclDte.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsucsuDiagFrmLclDte.setStatus("mandatory")


class _DsucsuDiagFrmLclDte2_Type(Integer32):
    """Custom type dsucsuDiagFrmLclDte2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disableLoopbackMode", 2),
          ("enableLoopbackMode", 1),
          ("notApplicable", 3))
    )


_DsucsuDiagFrmLclDte2_Type.__name__ = "Integer32"
_DsucsuDiagFrmLclDte2_Object = MibTableColumn
dsucsuDiagFrmLclDte2 = _DsucsuDiagFrmLclDte2_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 17, 1, 9),
    _DsucsuDiagFrmLclDte2_Type()
)
dsucsuDiagFrmLclDte2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsucsuDiagFrmLclDte2.setStatus("mandatory")


class _DsucsuDiagFrmBertTestAct_Type(Integer32):
    """Custom type dsucsuDiagFrmBertTestAct based on Integer32"""
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
        *(("clearErrorBertTest", 4),
          ("injectErrorBertTest", 3),
          ("startBertTest", 1),
          ("stopBertTest", 2))
    )


_DsucsuDiagFrmBertTestAct_Type.__name__ = "Integer32"
_DsucsuDiagFrmBertTestAct_Object = MibTableColumn
dsucsuDiagFrmBertTestAct = _DsucsuDiagFrmBertTestAct_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 17, 1, 10),
    _DsucsuDiagFrmBertTestAct_Type()
)
dsucsuDiagFrmBertTestAct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsucsuDiagFrmBertTestAct.setStatus("mandatory")
_DsucsuDiagFrmEvElapTime_Type = TimeTicks
_DsucsuDiagFrmEvElapTime_Object = MibTableColumn
dsucsuDiagFrmEvElapTime = _DsucsuDiagFrmEvElapTime_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 17, 1, 11),
    _DsucsuDiagFrmEvElapTime_Type()
)
dsucsuDiagFrmEvElapTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsucsuDiagFrmEvElapTime.setStatus("mandatory")
_DsucsuDiagFrmEvBpvErr_Type = Counter32
_DsucsuDiagFrmEvBpvErr_Object = MibTableColumn
dsucsuDiagFrmEvBpvErr = _DsucsuDiagFrmEvBpvErr_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 17, 1, 12),
    _DsucsuDiagFrmEvBpvErr_Type()
)
dsucsuDiagFrmEvBpvErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsucsuDiagFrmEvBpvErr.setStatus("mandatory")
_DsucsuDiagFrmEvOofErr_Type = Counter32
_DsucsuDiagFrmEvOofErr_Object = MibTableColumn
dsucsuDiagFrmEvOofErr = _DsucsuDiagFrmEvOofErr_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 17, 1, 13),
    _DsucsuDiagFrmEvOofErr_Type()
)
dsucsuDiagFrmEvOofErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsucsuDiagFrmEvOofErr.setStatus("mandatory")
_DsucsuDiagFrmFrameErr_Type = Counter32
_DsucsuDiagFrmFrameErr_Object = MibTableColumn
dsucsuDiagFrmFrameErr = _DsucsuDiagFrmFrameErr_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 17, 1, 14),
    _DsucsuDiagFrmFrameErr_Type()
)
dsucsuDiagFrmFrameErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsucsuDiagFrmFrameErr.setStatus("mandatory")


class _DsucsuDiagFrmClearEvReg_Type(Integer32):
    """Custom type dsucsuDiagFrmClearEvReg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clearRegister", 1)
    )


_DsucsuDiagFrmClearEvReg_Type.__name__ = "Integer32"
_DsucsuDiagFrmClearEvReg_Object = MibTableColumn
dsucsuDiagFrmClearEvReg = _DsucsuDiagFrmClearEvReg_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 17, 1, 15),
    _DsucsuDiagFrmClearEvReg_Type()
)
dsucsuDiagFrmClearEvReg.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    dsucsuDiagFrmClearEvReg.setStatus("mandatory")
_DsucsuDiagAuxTable_Object = MibTable
dsucsuDiagAuxTable = _DsucsuDiagAuxTable_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 18)
)
if mibBuilder.loadTexts:
    dsucsuDiagAuxTable.setStatus("mandatory")
_DsucsuDiagAuxEntry_Object = MibTableRow
dsucsuDiagAuxEntry = _DsucsuDiagAuxEntry_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 18, 1)
)
dsucsuDiagAuxEntry.setIndexNames(
    (0, "NETEXEC-MIB", "dsucsuDiagAuxSlot"),
    (0, "NETEXEC-MIB", "dsucsuDiagAuxNode"),
)
if mibBuilder.loadTexts:
    dsucsuDiagAuxEntry.setStatus("mandatory")


class _DsucsuDiagAuxSlot_Type(Integer32):
    """Custom type dsucsuDiagAuxSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_DsucsuDiagAuxSlot_Type.__name__ = "Integer32"
_DsucsuDiagAuxSlot_Object = MibTableColumn
dsucsuDiagAuxSlot = _DsucsuDiagAuxSlot_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 18, 1, 1),
    _DsucsuDiagAuxSlot_Type()
)
dsucsuDiagAuxSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsucsuDiagAuxSlot.setStatus("mandatory")


class _DsucsuDiagAuxNode_Type(Integer32):
    """Custom type dsucsuDiagAuxNode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_DsucsuDiagAuxNode_Type.__name__ = "Integer32"
_DsucsuDiagAuxNode_Object = MibTableColumn
dsucsuDiagAuxNode = _DsucsuDiagAuxNode_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 18, 1, 2),
    _DsucsuDiagAuxNode_Type()
)
dsucsuDiagAuxNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsucsuDiagAuxNode.setStatus("mandatory")


class _DsucsuDiagAuxChAStatus_Type(Integer32):
    """Custom type dsucsuDiagAuxChAStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("off", 3),
          ("sync", 2))
    )


_DsucsuDiagAuxChAStatus_Type.__name__ = "Integer32"
_DsucsuDiagAuxChAStatus_Object = MibTableColumn
dsucsuDiagAuxChAStatus = _DsucsuDiagAuxChAStatus_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 18, 1, 3),
    _DsucsuDiagAuxChAStatus_Type()
)
dsucsuDiagAuxChAStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsucsuDiagAuxChAStatus.setStatus("mandatory")


class _DsucsuDiagAuxChBStatus_Type(Integer32):
    """Custom type dsucsuDiagAuxChBStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("off", 3),
          ("sync", 2))
    )


_DsucsuDiagAuxChBStatus_Type.__name__ = "Integer32"
_DsucsuDiagAuxChBStatus_Object = MibTableColumn
dsucsuDiagAuxChBStatus = _DsucsuDiagAuxChBStatus_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 18, 1, 4),
    _DsucsuDiagAuxChBStatus_Type()
)
dsucsuDiagAuxChBStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsucsuDiagAuxChBStatus.setStatus("mandatory")


class _DsucsuDiagAuxFdlStatus_Type(Integer32):
    """Custom type dsucsuDiagAuxFdlStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("off", 3),
          ("sync", 2))
    )


_DsucsuDiagAuxFdlStatus_Type.__name__ = "Integer32"
_DsucsuDiagAuxFdlStatus_Object = MibTableColumn
dsucsuDiagAuxFdlStatus = _DsucsuDiagAuxFdlStatus_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 18, 1, 5),
    _DsucsuDiagAuxFdlStatus_Type()
)
dsucsuDiagAuxFdlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsucsuDiagAuxFdlStatus.setStatus("mandatory")


class _DsucsuDiagAuxFdl2Status_Type(Integer32):
    """Custom type dsucsuDiagAuxFdl2Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("off", 3),
          ("sync", 2))
    )


_DsucsuDiagAuxFdl2Status_Type.__name__ = "Integer32"
_DsucsuDiagAuxFdl2Status_Object = MibTableColumn
dsucsuDiagAuxFdl2Status = _DsucsuDiagAuxFdl2Status_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 18, 1, 6),
    _DsucsuDiagAuxFdl2Status_Type()
)
dsucsuDiagAuxFdl2Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsucsuDiagAuxFdl2Status.setStatus("mandatory")


class _DsucsuDiagAuxMaintStatus_Type(Integer32):
    """Custom type dsucsuDiagAuxMaintStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("off", 3),
          ("sync", 2))
    )


_DsucsuDiagAuxMaintStatus_Type.__name__ = "Integer32"
_DsucsuDiagAuxMaintStatus_Object = MibTableColumn
dsucsuDiagAuxMaintStatus = _DsucsuDiagAuxMaintStatus_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 18, 1, 7),
    _DsucsuDiagAuxMaintStatus_Type()
)
dsucsuDiagAuxMaintStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsucsuDiagAuxMaintStatus.setStatus("mandatory")


class _DsucsuDiagAuxCommStatus_Type(Integer32):
    """Custom type dsucsuDiagAuxCommStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("off", 3),
          ("sync", 2))
    )


_DsucsuDiagAuxCommStatus_Type.__name__ = "Integer32"
_DsucsuDiagAuxCommStatus_Object = MibTableColumn
dsucsuDiagAuxCommStatus = _DsucsuDiagAuxCommStatus_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 18, 1, 8),
    _DsucsuDiagAuxCommStatus_Type()
)
dsucsuDiagAuxCommStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsucsuDiagAuxCommStatus.setStatus("mandatory")
_DsucsuDiagPortTable_Object = MibTable
dsucsuDiagPortTable = _DsucsuDiagPortTable_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 19)
)
if mibBuilder.loadTexts:
    dsucsuDiagPortTable.setStatus("mandatory")
_DsucsuDiagPortEntry_Object = MibTableRow
dsucsuDiagPortEntry = _DsucsuDiagPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 19, 1)
)
dsucsuDiagPortEntry.setIndexNames(
    (0, "NETEXEC-MIB", "dsucsuDiagPortSlot"),
    (0, "NETEXEC-MIB", "dsucsuDiagPortNode"),
    (0, "NETEXEC-MIB", "dsucsuDiagPortIndex"),
)
if mibBuilder.loadTexts:
    dsucsuDiagPortEntry.setStatus("mandatory")


class _DsucsuDiagPortSlot_Type(Integer32):
    """Custom type dsucsuDiagPortSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_DsucsuDiagPortSlot_Type.__name__ = "Integer32"
_DsucsuDiagPortSlot_Object = MibTableColumn
dsucsuDiagPortSlot = _DsucsuDiagPortSlot_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 19, 1, 1),
    _DsucsuDiagPortSlot_Type()
)
dsucsuDiagPortSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsucsuDiagPortSlot.setStatus("mandatory")


class _DsucsuDiagPortNode_Type(Integer32):
    """Custom type dsucsuDiagPortNode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_DsucsuDiagPortNode_Type.__name__ = "Integer32"
_DsucsuDiagPortNode_Object = MibTableColumn
dsucsuDiagPortNode = _DsucsuDiagPortNode_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 19, 1, 2),
    _DsucsuDiagPortNode_Type()
)
dsucsuDiagPortNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsucsuDiagPortNode.setStatus("mandatory")


class _DsucsuDiagPortIndex_Type(Integer32):
    """Custom type dsucsuDiagPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_DsucsuDiagPortIndex_Type.__name__ = "Integer32"
_DsucsuDiagPortIndex_Object = MibTableColumn
dsucsuDiagPortIndex = _DsucsuDiagPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 19, 1, 3),
    _DsucsuDiagPortIndex_Type()
)
dsucsuDiagPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsucsuDiagPortIndex.setStatus("mandatory")


class _DsucsuDiagPortType_Type(Integer32):
    """Custom type dsucsuDiagPortType based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("dsx", 3),
          ("dte", 9),
          ("mil188", 7),
          ("network", 2),
          ("none", 1),
          ("pbx", 4),
          ("rs232", 6),
          ("rs449", 5),
          ("tdm", 10),
          ("v35", 8))
    )


_DsucsuDiagPortType_Type.__name__ = "Integer32"
_DsucsuDiagPortType_Object = MibTableColumn
dsucsuDiagPortType = _DsucsuDiagPortType_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 19, 1, 4),
    _DsucsuDiagPortType_Type()
)
dsucsuDiagPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsucsuDiagPortType.setStatus("mandatory")


class _DsucsuDiagPortStatus_Type(Integer32):
    """Custom type dsucsuDiagPortStatus based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("blueAlarm", 6),
          ("bpvAlarm", 5),
          ("clearOK", 1),
          ("notApplicable", 9),
          ("redAlarm", 2),
          ("syncLoss", 4),
          ("test", 7),
          ("timeout", 8),
          ("yellowAlarm", 3))
    )


_DsucsuDiagPortStatus_Type.__name__ = "Integer32"
_DsucsuDiagPortStatus_Object = MibTableColumn
dsucsuDiagPortStatus = _DsucsuDiagPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 19, 1, 5),
    _DsucsuDiagPortStatus_Type()
)
dsucsuDiagPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsucsuDiagPortStatus.setStatus("mandatory")
_DsucsuIntervalTable_Object = MibTable
dsucsuIntervalTable = _DsucsuIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 20)
)
if mibBuilder.loadTexts:
    dsucsuIntervalTable.setStatus("mandatory")
_DsucsuIntervalEntry_Object = MibTableRow
dsucsuIntervalEntry = _DsucsuIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 20, 1)
)
dsucsuIntervalEntry.setIndexNames(
    (0, "NETEXEC-MIB", "dsucsuIntervalSlot"),
    (0, "NETEXEC-MIB", "dsucsuIntervalNode"),
    (0, "NETEXEC-MIB", "dsucsuIntervalPort"),
    (0, "NETEXEC-MIB", "dsucsuIntervalNum"),
)
if mibBuilder.loadTexts:
    dsucsuIntervalEntry.setStatus("mandatory")


class _DsucsuIntervalSlot_Type(Integer32):
    """Custom type dsucsuIntervalSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_DsucsuIntervalSlot_Type.__name__ = "Integer32"
_DsucsuIntervalSlot_Object = MibTableColumn
dsucsuIntervalSlot = _DsucsuIntervalSlot_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 20, 1, 1),
    _DsucsuIntervalSlot_Type()
)
dsucsuIntervalSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsucsuIntervalSlot.setStatus("mandatory")


class _DsucsuIntervalNode_Type(Integer32):
    """Custom type dsucsuIntervalNode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_DsucsuIntervalNode_Type.__name__ = "Integer32"
_DsucsuIntervalNode_Object = MibTableColumn
dsucsuIntervalNode = _DsucsuIntervalNode_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 20, 1, 2),
    _DsucsuIntervalNode_Type()
)
dsucsuIntervalNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsucsuIntervalNode.setStatus("mandatory")


class _DsucsuIntervalPort_Type(Integer32):
    """Custom type dsucsuIntervalPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_DsucsuIntervalPort_Type.__name__ = "Integer32"
_DsucsuIntervalPort_Object = MibTableColumn
dsucsuIntervalPort = _DsucsuIntervalPort_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 20, 1, 3),
    _DsucsuIntervalPort_Type()
)
dsucsuIntervalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsucsuIntervalPort.setStatus("mandatory")


class _DsucsuIntervalNum_Type(Integer32):
    """Custom type dsucsuIntervalNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_DsucsuIntervalNum_Type.__name__ = "Integer32"
_DsucsuIntervalNum_Object = MibTableColumn
dsucsuIntervalNum = _DsucsuIntervalNum_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 20, 1, 4),
    _DsucsuIntervalNum_Type()
)
dsucsuIntervalNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsucsuIntervalNum.setStatus("mandatory")
_DsucsuIntervalESs_Type = Counter32
_DsucsuIntervalESs_Object = MibTableColumn
dsucsuIntervalESs = _DsucsuIntervalESs_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 20, 1, 5),
    _DsucsuIntervalESs_Type()
)
dsucsuIntervalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsucsuIntervalESs.setStatus("mandatory")
_DsucsuIntervalSESs_Type = Counter32
_DsucsuIntervalSESs_Object = MibTableColumn
dsucsuIntervalSESs = _DsucsuIntervalSESs_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 20, 1, 6),
    _DsucsuIntervalSESs_Type()
)
dsucsuIntervalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsucsuIntervalSESs.setStatus("mandatory")
_DsucsuIntervalBPVs_Type = Counter32
_DsucsuIntervalBPVs_Object = MibTableColumn
dsucsuIntervalBPVs = _DsucsuIntervalBPVs_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 20, 1, 7),
    _DsucsuIntervalBPVs_Type()
)
dsucsuIntervalBPVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsucsuIntervalBPVs.setStatus("mandatory")
_DsucsuIntervalFSs_Type = Counter32
_DsucsuIntervalFSs_Object = MibTableColumn
dsucsuIntervalFSs = _DsucsuIntervalFSs_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 20, 1, 8),
    _DsucsuIntervalFSs_Type()
)
dsucsuIntervalFSs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsucsuIntervalFSs.setStatus("mandatory")
_DsucsuCurrentTable_Object = MibTable
dsucsuCurrentTable = _DsucsuCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 22)
)
if mibBuilder.loadTexts:
    dsucsuCurrentTable.setStatus("mandatory")
_DsucsuCurrentEntry_Object = MibTableRow
dsucsuCurrentEntry = _DsucsuCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 22, 1)
)
dsucsuCurrentEntry.setIndexNames(
    (0, "NETEXEC-MIB", "dsucsuCurrentSlot"),
    (0, "NETEXEC-MIB", "dsucsuCurrentNode"),
    (0, "NETEXEC-MIB", "dsucsuCurrentPort"),
)
if mibBuilder.loadTexts:
    dsucsuCurrentEntry.setStatus("mandatory")


class _DsucsuCurrentSlot_Type(Integer32):
    """Custom type dsucsuCurrentSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_DsucsuCurrentSlot_Type.__name__ = "Integer32"
_DsucsuCurrentSlot_Object = MibTableColumn
dsucsuCurrentSlot = _DsucsuCurrentSlot_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 22, 1, 1),
    _DsucsuCurrentSlot_Type()
)
dsucsuCurrentSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsucsuCurrentSlot.setStatus("mandatory")


class _DsucsuCurrentNode_Type(Integer32):
    """Custom type dsucsuCurrentNode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_DsucsuCurrentNode_Type.__name__ = "Integer32"
_DsucsuCurrentNode_Object = MibTableColumn
dsucsuCurrentNode = _DsucsuCurrentNode_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 22, 1, 2),
    _DsucsuCurrentNode_Type()
)
dsucsuCurrentNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsucsuCurrentNode.setStatus("mandatory")


class _DsucsuCurrentPort_Type(Integer32):
    """Custom type dsucsuCurrentPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_DsucsuCurrentPort_Type.__name__ = "Integer32"
_DsucsuCurrentPort_Object = MibTableColumn
dsucsuCurrentPort = _DsucsuCurrentPort_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 22, 1, 3),
    _DsucsuCurrentPort_Type()
)
dsucsuCurrentPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsucsuCurrentPort.setStatus("mandatory")
_DsucsuCurrentESs_Type = Counter32
_DsucsuCurrentESs_Object = MibTableColumn
dsucsuCurrentESs = _DsucsuCurrentESs_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 22, 1, 4),
    _DsucsuCurrentESs_Type()
)
dsucsuCurrentESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsucsuCurrentESs.setStatus("mandatory")
_DsucsuCurrentSESs_Type = Counter32
_DsucsuCurrentSESs_Object = MibTableColumn
dsucsuCurrentSESs = _DsucsuCurrentSESs_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 22, 1, 5),
    _DsucsuCurrentSESs_Type()
)
dsucsuCurrentSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsucsuCurrentSESs.setStatus("mandatory")
_DsucsuCurrentBPVs_Type = Counter32
_DsucsuCurrentBPVs_Object = MibTableColumn
dsucsuCurrentBPVs = _DsucsuCurrentBPVs_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 22, 1, 6),
    _DsucsuCurrentBPVs_Type()
)
dsucsuCurrentBPVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsucsuCurrentBPVs.setStatus("mandatory")
_DsucsuCurrentSECs_Type = Counter32
_DsucsuCurrentSECs_Object = MibTableColumn
dsucsuCurrentSECs = _DsucsuCurrentSECs_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 22, 1, 7),
    _DsucsuCurrentSECs_Type()
)
dsucsuCurrentSECs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsucsuCurrentSECs.setStatus("mandatory")


class _DsucsuCurrentStatus_Type(Integer32):
    """Custom type dsucsuCurrentStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("frozen", 1),
          ("unfrozen", 2))
    )


_DsucsuCurrentStatus_Type.__name__ = "Integer32"
_DsucsuCurrentStatus_Object = MibTableColumn
dsucsuCurrentStatus = _DsucsuCurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 22, 1, 8),
    _DsucsuCurrentStatus_Type()
)
dsucsuCurrentStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsucsuCurrentStatus.setStatus("mandatory")
_DsucsuTotalTable_Object = MibTable
dsucsuTotalTable = _DsucsuTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 24)
)
if mibBuilder.loadTexts:
    dsucsuTotalTable.setStatus("mandatory")
_DsucsuTotalEntry_Object = MibTableRow
dsucsuTotalEntry = _DsucsuTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 24, 1)
)
dsucsuTotalEntry.setIndexNames(
    (0, "NETEXEC-MIB", "dsucsuTotalSlot"),
    (0, "NETEXEC-MIB", "dsucsuTotalNode"),
    (0, "NETEXEC-MIB", "dsucsuTotalPort"),
)
if mibBuilder.loadTexts:
    dsucsuTotalEntry.setStatus("mandatory")


class _DsucsuTotalSlot_Type(Integer32):
    """Custom type dsucsuTotalSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_DsucsuTotalSlot_Type.__name__ = "Integer32"
_DsucsuTotalSlot_Object = MibTableColumn
dsucsuTotalSlot = _DsucsuTotalSlot_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 24, 1, 1),
    _DsucsuTotalSlot_Type()
)
dsucsuTotalSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsucsuTotalSlot.setStatus("mandatory")


class _DsucsuTotalNode_Type(Integer32):
    """Custom type dsucsuTotalNode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_DsucsuTotalNode_Type.__name__ = "Integer32"
_DsucsuTotalNode_Object = MibTableColumn
dsucsuTotalNode = _DsucsuTotalNode_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 24, 1, 2),
    _DsucsuTotalNode_Type()
)
dsucsuTotalNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsucsuTotalNode.setStatus("mandatory")


class _DsucsuTotalPort_Type(Integer32):
    """Custom type dsucsuTotalPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_DsucsuTotalPort_Type.__name__ = "Integer32"
_DsucsuTotalPort_Object = MibTableColumn
dsucsuTotalPort = _DsucsuTotalPort_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 24, 1, 3),
    _DsucsuTotalPort_Type()
)
dsucsuTotalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsucsuTotalPort.setStatus("mandatory")
_DsucsuTotalESs_Type = Counter32
_DsucsuTotalESs_Object = MibTableColumn
dsucsuTotalESs = _DsucsuTotalESs_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 24, 1, 4),
    _DsucsuTotalESs_Type()
)
dsucsuTotalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsucsuTotalESs.setStatus("mandatory")
_DsucsuTotalSESs_Type = Counter32
_DsucsuTotalSESs_Object = MibTableColumn
dsucsuTotalSESs = _DsucsuTotalSESs_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 24, 1, 5),
    _DsucsuTotalSESs_Type()
)
dsucsuTotalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsucsuTotalSESs.setStatus("mandatory")
_DsucsuTotalBPVs_Type = Counter32
_DsucsuTotalBPVs_Object = MibTableColumn
dsucsuTotalBPVs = _DsucsuTotalBPVs_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 24, 1, 6),
    _DsucsuTotalBPVs_Type()
)
dsucsuTotalBPVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsucsuTotalBPVs.setStatus("mandatory")
_DsucsuTotalSECs_Type = Counter32
_DsucsuTotalSECs_Object = MibTableColumn
dsucsuTotalSECs = _DsucsuTotalSECs_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 24, 1, 7),
    _DsucsuTotalSECs_Type()
)
dsucsuTotalSECs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsucsuTotalSECs.setStatus("mandatory")


class _DsucsuTotalStatus_Type(Integer32):
    """Custom type dsucsuTotalStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("frozen", 1),
          ("unfrozen", 2))
    )


_DsucsuTotalStatus_Type.__name__ = "Integer32"
_DsucsuTotalStatus_Object = MibTableColumn
dsucsuTotalStatus = _DsucsuTotalStatus_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 24, 1, 8),
    _DsucsuTotalStatus_Type()
)
dsucsuTotalStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsucsuTotalStatus.setStatus("mandatory")


class _DsucsuAlarmType_Type(Integer32):
    """Custom type dsucsuAlarmType based on Integer32"""
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
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
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
              48,
              49,
              50,
              51,
              52,
              53,
              54)
        )
    )
    namedValues = NamedValues(
        *(("ais-Alarm", 13),
          ("ais-Alarm-Clear", 39),
          ("bpv-Alarm", 4),
          ("bpv-Alarm-Clear", 32),
          ("confg-Activated", 5),
          ("confg-Stored", 6),
          ("crc4-Error-Alarm", 21),
          ("crc4-Error-Alarm-Clear", 47),
          ("fan-one-Failure", 27),
          ("fan-one-Failure-Clear", 53),
          ("fan-two-Failure", 28),
          ("fan-two-Failure-Clear", 54),
          ("frame-Error-Alarm", 20),
          ("frame-Error-Alarm-Clear", 46),
          ("node-communications-lost", 14),
          ("node-communications-restored", 40),
          ("pbx1-Los-Alarm", 9),
          ("pbx1-Los-Alarm-Clear", 35),
          ("pbx1-Red-Alarm", 8),
          ("pbx1-Red-Alarm-Clear", 34),
          ("pbx1-Yellow-Alarm", 7),
          ("pbx1-Yellow-Alarm-Clear", 33),
          ("pbx3-Los-Alarm", 12),
          ("pbx3-Los-Alarm-Clear", 38),
          ("pbx3-Red-Alarm", 11),
          ("pbx3-Red-Alarm-Clear", 37),
          ("pbx3-Yellow-Alarm", 10),
          ("pbx3-Yellow-Alarm-Clear", 36),
          ("port2-Bpv-Alarm", 25),
          ("port2-Bpv-Alarm-Clear", 51),
          ("port2-Red-Alarm", 24),
          ("port2-Red-Alarm-Clear", 50),
          ("port2-Sync-Alarm", 23),
          ("port2-Sync-Alarm-Clear", 49),
          ("port2-Yellow-Alarm", 22),
          ("port2-Yellow-Alarm-Clear", 48),
          ("power-Supply-Alarm", 26),
          ("power-Supply-Alarm-Clear", 52),
          ("red-Alarm", 3),
          ("red-Alarm-Clear", 31),
          ("remote-Alarm", 18),
          ("remote-Alarm-Clear", 44),
          ("remote-ts16-Alarm", 19),
          ("remote-ts16-Alarm-Clear", 45),
          ("sync-Alarm", 2),
          ("sync-Alarm-Clear", 30),
          ("sync-ais-Alarm", 15),
          ("sync-ais-Alarm-Clear", 41),
          ("ts16-Los-Alarm", 17),
          ("ts16-Los-Alarm-Clear", 43),
          ("ts16-ais-Alarm", 16),
          ("ts16-ais-Alarm-Clear", 42),
          ("yellow-Alarm", 1),
          ("yellow-Alarm-Clear", 29))
    )


_DsucsuAlarmType_Type.__name__ = "Integer32"
_DsucsuAlarmType_Object = MibScalar
dsucsuAlarmType = _DsucsuAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 25),
    _DsucsuAlarmType_Type()
)
dsucsuAlarmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsucsuAlarmType.setStatus("mandatory")


class _DsucsuAlarmSlot_Type(Integer32):
    """Custom type dsucsuAlarmSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_DsucsuAlarmSlot_Type.__name__ = "Integer32"
_DsucsuAlarmSlot_Object = MibScalar
dsucsuAlarmSlot = _DsucsuAlarmSlot_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 26),
    _DsucsuAlarmSlot_Type()
)
dsucsuAlarmSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsucsuAlarmSlot.setStatus("mandatory")


class _DsucsuAlarmNode_Type(Integer32):
    """Custom type dsucsuAlarmNode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_DsucsuAlarmNode_Type.__name__ = "Integer32"
_DsucsuAlarmNode_Object = MibScalar
dsucsuAlarmNode = _DsucsuAlarmNode_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 27),
    _DsucsuAlarmNode_Type()
)
dsucsuAlarmNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsucsuAlarmNode.setStatus("mandatory")


class _DsucsuAlarmName_Type(DisplayString):
    """Custom type dsucsuAlarmName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_DsucsuAlarmName_Type.__name__ = "DisplayString"
_DsucsuAlarmName_Object = MibScalar
dsucsuAlarmName = _DsucsuAlarmName_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 28),
    _DsucsuAlarmName_Type()
)
dsucsuAlarmName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsucsuAlarmName.setStatus("mandatory")
_Tyview_ObjectIdentity = ObjectIdentity
tyview = _Tyview_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 466, 6, 2)
)
_TyviewSysTable_ObjectIdentity = ObjectIdentity
tyviewSysTable = _TyviewSysTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 466, 6, 2, 1)
)


class _TyviewSysRevSw_Type(DisplayString):
    """Custom type tyviewSysRevSw based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_TyviewSysRevSw_Type.__name__ = "DisplayString"
_TyviewSysRevSw_Object = MibScalar
tyviewSysRevSw = _TyviewSysRevSw_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 2, 1, 1),
    _TyviewSysRevSw_Type()
)
tyviewSysRevSw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tyviewSysRevSw.setStatus("mandatory")


class _TyviewSysName_Type(DisplayString):
    """Custom type tyviewSysName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_TyviewSysName_Type.__name__ = "DisplayString"
_TyviewSysName_Object = MibScalar
tyviewSysName = _TyviewSysName_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 2, 1, 2),
    _TyviewSysName_Type()
)
tyviewSysName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tyviewSysName.setStatus("mandatory")
_TyviewSysId_Type = Integer32
_TyviewSysId_Object = MibScalar
tyviewSysId = _TyviewSysId_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 2, 1, 3),
    _TyviewSysId_Type()
)
tyviewSysId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tyviewSysId.setStatus("mandatory")
_TyviewSysTimeOutFactor_Type = Integer32
_TyviewSysTimeOutFactor_Object = MibScalar
tyviewSysTimeOutFactor = _TyviewSysTimeOutFactor_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 2, 1, 4),
    _TyviewSysTimeOutFactor_Type()
)
tyviewSysTimeOutFactor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tyviewSysTimeOutFactor.setStatus("mandatory")


class _TyviewSysObjectId_Type(DisplayString):
    """Custom type tyviewSysObjectId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_TyviewSysObjectId_Type.__name__ = "DisplayString"
_TyviewSysObjectId_Object = MibScalar
tyviewSysObjectId = _TyviewSysObjectId_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 2, 1, 5),
    _TyviewSysObjectId_Type()
)
tyviewSysObjectId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tyviewSysObjectId.setStatus("mandatory")
_TyviewSysSlotNumber_Type = Integer32
_TyviewSysSlotNumber_Object = MibScalar
tyviewSysSlotNumber = _TyviewSysSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 2, 1, 6),
    _TyviewSysSlotNumber_Type()
)
tyviewSysSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tyviewSysSlotNumber.setStatus("mandatory")


class _TyviewSysClearDatabase_Type(Integer32):
    """Custom type tyviewSysClearDatabase based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clearDatabase", 1)
    )


_TyviewSysClearDatabase_Type.__name__ = "Integer32"
_TyviewSysClearDatabase_Object = MibScalar
tyviewSysClearDatabase = _TyviewSysClearDatabase_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 2, 1, 7),
    _TyviewSysClearDatabase_Type()
)
tyviewSysClearDatabase.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    tyviewSysClearDatabase.setStatus("mandatory")


class _TyviewSysGetCommName_Type(DisplayString):
    """Custom type tyviewSysGetCommName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TyviewSysGetCommName_Type.__name__ = "DisplayString"
_TyviewSysGetCommName_Object = MibScalar
tyviewSysGetCommName = _TyviewSysGetCommName_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 2, 1, 8),
    _TyviewSysGetCommName_Type()
)
tyviewSysGetCommName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tyviewSysGetCommName.setStatus("mandatory")


class _TyviewSysSetCommName_Type(DisplayString):
    """Custom type tyviewSysSetCommName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TyviewSysSetCommName_Type.__name__ = "DisplayString"
_TyviewSysSetCommName_Object = MibScalar
tyviewSysSetCommName = _TyviewSysSetCommName_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 2, 1, 9),
    _TyviewSysSetCommName_Type()
)
tyviewSysSetCommName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tyviewSysSetCommName.setStatus("mandatory")


class _TyviewSysTrapCommName_Type(DisplayString):
    """Custom type tyviewSysTrapCommName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TyviewSysTrapCommName_Type.__name__ = "DisplayString"
_TyviewSysTrapCommName_Object = MibScalar
tyviewSysTrapCommName = _TyviewSysTrapCommName_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 2, 1, 10),
    _TyviewSysTrapCommName_Type()
)
tyviewSysTrapCommName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tyviewSysTrapCommName.setStatus("mandatory")


class _TyviewSysN1TrapDest_Type(DisplayString):
    """Custom type tyviewSysN1TrapDest based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_TyviewSysN1TrapDest_Type.__name__ = "DisplayString"
_TyviewSysN1TrapDest_Object = MibScalar
tyviewSysN1TrapDest = _TyviewSysN1TrapDest_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 2, 1, 11),
    _TyviewSysN1TrapDest_Type()
)
tyviewSysN1TrapDest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tyviewSysN1TrapDest.setStatus("mandatory")


class _TyviewSysN2TrapDest_Type(DisplayString):
    """Custom type tyviewSysN2TrapDest based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_TyviewSysN2TrapDest_Type.__name__ = "DisplayString"
_TyviewSysN2TrapDest_Object = MibScalar
tyviewSysN2TrapDest = _TyviewSysN2TrapDest_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 2, 1, 12),
    _TyviewSysN2TrapDest_Type()
)
tyviewSysN2TrapDest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tyviewSysN2TrapDest.setStatus("mandatory")


class _TyviewSysDate_Type(DisplayString):
    """Custom type tyviewSysDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_TyviewSysDate_Type.__name__ = "DisplayString"
_TyviewSysDate_Object = MibScalar
tyviewSysDate = _TyviewSysDate_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 2, 1, 13),
    _TyviewSysDate_Type()
)
tyviewSysDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tyviewSysDate.setStatus("mandatory")


class _TyviewSysTime_Type(DisplayString):
    """Custom type tyviewSysTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_TyviewSysTime_Type.__name__ = "DisplayString"
_TyviewSysTime_Object = MibScalar
tyviewSysTime = _TyviewSysTime_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 2, 1, 14),
    _TyviewSysTime_Type()
)
tyviewSysTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tyviewSysTime.setStatus("mandatory")


class _TyviewSysMjrMnrLED_Type(Integer32):
    """Custom type tyviewSysMjrMnrLED based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("led-Green", 3),
          ("led-Off", 1),
          ("led-Red", 2),
          ("led-RedYellow", 5),
          ("led-Yellow", 4))
    )


_TyviewSysMjrMnrLED_Type.__name__ = "Integer32"
_TyviewSysMjrMnrLED_Object = MibScalar
tyviewSysMjrMnrLED = _TyviewSysMjrMnrLED_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 2, 1, 15),
    _TyviewSysMjrMnrLED_Type()
)
tyviewSysMjrMnrLED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tyviewSysMjrMnrLED.setStatus("mandatory")


class _TyviewSysFanPSLED_Type(Integer32):
    """Custom type tyviewSysFanPSLED based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("led-Green", 3),
          ("led-Off", 1),
          ("led-Red", 2),
          ("led-RedYellow", 5),
          ("led-Yellow", 4))
    )


_TyviewSysFanPSLED_Type.__name__ = "Integer32"
_TyviewSysFanPSLED_Object = MibScalar
tyviewSysFanPSLED = _TyviewSysFanPSLED_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 2, 1, 16),
    _TyviewSysFanPSLED_Type()
)
tyviewSysFanPSLED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tyviewSysFanPSLED.setStatus("mandatory")


class _TyviewSysCtlrLED_Type(Integer32):
    """Custom type tyviewSysCtlrLED based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("led-Green", 3),
          ("led-Off", 1),
          ("led-Red", 2),
          ("led-RedYellow", 5),
          ("led-Yellow", 4))
    )


_TyviewSysCtlrLED_Type.__name__ = "Integer32"
_TyviewSysCtlrLED_Object = MibScalar
tyviewSysCtlrLED = _TyviewSysCtlrLED_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 2, 1, 17),
    _TyviewSysCtlrLED_Type()
)
tyviewSysCtlrLED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tyviewSysCtlrLED.setStatus("mandatory")


class _TyviewSysSlipLED_Type(Integer32):
    """Custom type tyviewSysSlipLED based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("led-Green", 3),
          ("led-Off", 1),
          ("led-Red", 2),
          ("led-RedYellow", 5),
          ("led-Yellow", 4))
    )


_TyviewSysSlipLED_Type.__name__ = "Integer32"
_TyviewSysSlipLED_Object = MibScalar
tyviewSysSlipLED = _TyviewSysSlipLED_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 2, 1, 18),
    _TyviewSysSlipLED_Type()
)
tyviewSysSlipLED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tyviewSysSlipLED.setStatus("mandatory")


class _TyviewSysCtlChLED_Type(Integer32):
    """Custom type tyviewSysCtlChLED based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("led-Green", 3),
          ("led-Off", 1),
          ("led-Red", 2),
          ("led-RedYellow", 5),
          ("led-Yellow", 4))
    )


_TyviewSysCtlChLED_Type.__name__ = "Integer32"
_TyviewSysCtlChLED_Object = MibScalar
tyviewSysCtlChLED = _TyviewSysCtlChLED_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 2, 1, 19),
    _TyviewSysCtlChLED_Type()
)
tyviewSysCtlChLED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tyviewSysCtlChLED.setStatus("mandatory")


class _TyviewSysTDMLED_Type(Integer32):
    """Custom type tyviewSysTDMLED based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("led-Green", 3),
          ("led-Off", 1),
          ("led-Red", 2),
          ("led-RedYellow", 5),
          ("led-Yellow", 4))
    )


_TyviewSysTDMLED_Type.__name__ = "Integer32"
_TyviewSysTDMLED_Object = MibScalar
tyviewSysTDMLED = _TyviewSysTDMLED_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 2, 1, 20),
    _TyviewSysTDMLED_Type()
)
tyviewSysTDMLED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tyviewSysTDMLED.setStatus("mandatory")


class _TyviewSysMaintUseage_Type(Integer32):
    """Custom type tyviewSysMaintUseage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("command", 2),
          ("diagnostic", 5),
          ("none", 1),
          ("ppp", 6),
          ("slip", 3),
          ("tp-modem", 4))
    )


_TyviewSysMaintUseage_Type.__name__ = "Integer32"
_TyviewSysMaintUseage_Object = MibScalar
tyviewSysMaintUseage = _TyviewSysMaintUseage_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 2, 1, 21),
    _TyviewSysMaintUseage_Type()
)
tyviewSysMaintUseage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tyviewSysMaintUseage.setStatus("mandatory")


class _TyviewSysMaintDataBits_Type(Integer32):
    """Custom type tyviewSysMaintDataBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("databits-7", 1),
          ("databits-8", 2))
    )


_TyviewSysMaintDataBits_Type.__name__ = "Integer32"
_TyviewSysMaintDataBits_Object = MibScalar
tyviewSysMaintDataBits = _TyviewSysMaintDataBits_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 2, 1, 22),
    _TyviewSysMaintDataBits_Type()
)
tyviewSysMaintDataBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tyviewSysMaintDataBits.setStatus("mandatory")


class _TyviewSysMaintRate_Type(Integer32):
    """Custom type tyviewSysMaintRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("rate-1200", 1),
          ("rate-19200", 5),
          ("rate-2400", 2),
          ("rate-4800", 3),
          ("rate-9600", 4))
    )


_TyviewSysMaintRate_Type.__name__ = "Integer32"
_TyviewSysMaintRate_Object = MibScalar
tyviewSysMaintRate = _TyviewSysMaintRate_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 2, 1, 23),
    _TyviewSysMaintRate_Type()
)
tyviewSysMaintRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tyviewSysMaintRate.setStatus("mandatory")


class _TyviewSysMaintStopBits_Type(Integer32):
    """Custom type tyviewSysMaintStopBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("stopbits-1", 1),
          ("stopbits-2", 2))
    )


_TyviewSysMaintStopBits_Type.__name__ = "Integer32"
_TyviewSysMaintStopBits_Object = MibScalar
tyviewSysMaintStopBits = _TyviewSysMaintStopBits_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 2, 1, 24),
    _TyviewSysMaintStopBits_Type()
)
tyviewSysMaintStopBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tyviewSysMaintStopBits.setStatus("mandatory")


class _TyviewSysMaintParity_Type(Integer32):
    """Custom type tyviewSysMaintParity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("even", 3),
          ("none", 1),
          ("odd", 2))
    )


_TyviewSysMaintParity_Type.__name__ = "Integer32"
_TyviewSysMaintParity_Object = MibScalar
tyviewSysMaintParity = _TyviewSysMaintParity_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 2, 1, 25),
    _TyviewSysMaintParity_Type()
)
tyviewSysMaintParity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tyviewSysMaintParity.setStatus("mandatory")
_TyviewSysMaintMtu_Type = Integer32
_TyviewSysMaintMtu_Object = MibScalar
tyviewSysMaintMtu = _TyviewSysMaintMtu_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 2, 1, 26),
    _TyviewSysMaintMtu_Type()
)
tyviewSysMaintMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tyviewSysMaintMtu.setStatus("mandatory")


class _TyviewSysMaintCompression_Type(Integer32):
    """Custom type tyviewSysMaintCompression based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_TyviewSysMaintCompression_Type.__name__ = "Integer32"
_TyviewSysMaintCompression_Object = MibScalar
tyviewSysMaintCompression = _TyviewSysMaintCompression_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 2, 1, 27),
    _TyviewSysMaintCompression_Type()
)
tyviewSysMaintCompression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tyviewSysMaintCompression.setStatus("mandatory")


class _TyviewSysMaintSubnetMask_Type(DisplayString):
    """Custom type tyviewSysMaintSubnetMask based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_TyviewSysMaintSubnetMask_Type.__name__ = "DisplayString"
_TyviewSysMaintSubnetMask_Object = MibScalar
tyviewSysMaintSubnetMask = _TyviewSysMaintSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 2, 1, 28),
    _TyviewSysMaintSubnetMask_Type()
)
tyviewSysMaintSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tyviewSysMaintSubnetMask.setStatus("mandatory")


class _TyviewSysMaintLocalIP_Type(DisplayString):
    """Custom type tyviewSysMaintLocalIP based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_TyviewSysMaintLocalIP_Type.__name__ = "DisplayString"
_TyviewSysMaintLocalIP_Object = MibScalar
tyviewSysMaintLocalIP = _TyviewSysMaintLocalIP_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 2, 1, 29),
    _TyviewSysMaintLocalIP_Type()
)
tyviewSysMaintLocalIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tyviewSysMaintLocalIP.setStatus("mandatory")


class _TyviewSysMaintPeerIP_Type(DisplayString):
    """Custom type tyviewSysMaintPeerIP based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_TyviewSysMaintPeerIP_Type.__name__ = "DisplayString"
_TyviewSysMaintPeerIP_Object = MibScalar
tyviewSysMaintPeerIP = _TyviewSysMaintPeerIP_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 2, 1, 30),
    _TyviewSysMaintPeerIP_Type()
)
tyviewSysMaintPeerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tyviewSysMaintPeerIP.setStatus("mandatory")


class _TyviewSysComUseage_Type(Integer32):
    """Custom type tyviewSysComUseage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("command", 2),
          ("diagnostic", 5),
          ("none", 1),
          ("ppp", 6),
          ("slip", 3),
          ("tp-modem", 4))
    )


_TyviewSysComUseage_Type.__name__ = "Integer32"
_TyviewSysComUseage_Object = MibScalar
tyviewSysComUseage = _TyviewSysComUseage_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 2, 1, 31),
    _TyviewSysComUseage_Type()
)
tyviewSysComUseage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tyviewSysComUseage.setStatus("mandatory")


class _TyviewSysComDataBits_Type(Integer32):
    """Custom type tyviewSysComDataBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("databits-7", 1),
          ("databits-8", 2))
    )


_TyviewSysComDataBits_Type.__name__ = "Integer32"
_TyviewSysComDataBits_Object = MibScalar
tyviewSysComDataBits = _TyviewSysComDataBits_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 2, 1, 32),
    _TyviewSysComDataBits_Type()
)
tyviewSysComDataBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tyviewSysComDataBits.setStatus("mandatory")


class _TyviewSysComRate_Type(Integer32):
    """Custom type tyviewSysComRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("rate-1200", 1),
          ("rate-19200", 5),
          ("rate-2400", 2),
          ("rate-4800", 3),
          ("rate-9600", 4))
    )


_TyviewSysComRate_Type.__name__ = "Integer32"
_TyviewSysComRate_Object = MibScalar
tyviewSysComRate = _TyviewSysComRate_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 2, 1, 33),
    _TyviewSysComRate_Type()
)
tyviewSysComRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tyviewSysComRate.setStatus("mandatory")


class _TyviewSysComStopBits_Type(Integer32):
    """Custom type tyviewSysComStopBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("stopbits-1", 1),
          ("stopbits-2", 2))
    )


_TyviewSysComStopBits_Type.__name__ = "Integer32"
_TyviewSysComStopBits_Object = MibScalar
tyviewSysComStopBits = _TyviewSysComStopBits_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 2, 1, 34),
    _TyviewSysComStopBits_Type()
)
tyviewSysComStopBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tyviewSysComStopBits.setStatus("mandatory")


class _TyviewSysComParity_Type(Integer32):
    """Custom type tyviewSysComParity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("even", 3),
          ("none", 1),
          ("odd", 2))
    )


_TyviewSysComParity_Type.__name__ = "Integer32"
_TyviewSysComParity_Object = MibScalar
tyviewSysComParity = _TyviewSysComParity_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 2, 1, 35),
    _TyviewSysComParity_Type()
)
tyviewSysComParity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tyviewSysComParity.setStatus("mandatory")
_TyviewSysComMtu_Type = Integer32
_TyviewSysComMtu_Object = MibScalar
tyviewSysComMtu = _TyviewSysComMtu_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 2, 1, 36),
    _TyviewSysComMtu_Type()
)
tyviewSysComMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tyviewSysComMtu.setStatus("mandatory")


class _TyviewSysComCompression_Type(Integer32):
    """Custom type tyviewSysComCompression based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_TyviewSysComCompression_Type.__name__ = "Integer32"
_TyviewSysComCompression_Object = MibScalar
tyviewSysComCompression = _TyviewSysComCompression_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 2, 1, 37),
    _TyviewSysComCompression_Type()
)
tyviewSysComCompression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tyviewSysComCompression.setStatus("mandatory")


class _TyviewSysComSubnetMask_Type(DisplayString):
    """Custom type tyviewSysComSubnetMask based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_TyviewSysComSubnetMask_Type.__name__ = "DisplayString"
_TyviewSysComSubnetMask_Object = MibScalar
tyviewSysComSubnetMask = _TyviewSysComSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 2, 1, 38),
    _TyviewSysComSubnetMask_Type()
)
tyviewSysComSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tyviewSysComSubnetMask.setStatus("mandatory")


class _TyviewSysComLocalIP_Type(DisplayString):
    """Custom type tyviewSysComLocalIP based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_TyviewSysComLocalIP_Type.__name__ = "DisplayString"
_TyviewSysComLocalIP_Object = MibScalar
tyviewSysComLocalIP = _TyviewSysComLocalIP_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 2, 1, 39),
    _TyviewSysComLocalIP_Type()
)
tyviewSysComLocalIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tyviewSysComLocalIP.setStatus("mandatory")


class _TyviewSysComPeerIP_Type(DisplayString):
    """Custom type tyviewSysComPeerIP based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_TyviewSysComPeerIP_Type.__name__ = "DisplayString"
_TyviewSysComPeerIP_Object = MibScalar
tyviewSysComPeerIP = _TyviewSysComPeerIP_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 2, 1, 40),
    _TyviewSysComPeerIP_Type()
)
tyviewSysComPeerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tyviewSysComPeerIP.setStatus("mandatory")


class _TyviewSysTelnetEna_Type(Integer32):
    """Custom type tyviewSysTelnetEna based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_TyviewSysTelnetEna_Type.__name__ = "Integer32"
_TyviewSysTelnetEna_Object = MibScalar
tyviewSysTelnetEna = _TyviewSysTelnetEna_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 2, 1, 41),
    _TyviewSysTelnetEna_Type()
)
tyviewSysTelnetEna.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tyviewSysTelnetEna.setStatus("mandatory")
_TyviewSysTelnetTO_Type = Integer32
_TyviewSysTelnetTO_Object = MibScalar
tyviewSysTelnetTO = _TyviewSysTelnetTO_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 2, 1, 42),
    _TyviewSysTelnetTO_Type()
)
tyviewSysTelnetTO.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tyviewSysTelnetTO.setStatus("mandatory")


class _TyviewSysClrMjrMin_Type(Integer32):
    """Custom type tyviewSysClrMjrMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clearMajorMinor", 1)
    )


_TyviewSysClrMjrMin_Type.__name__ = "Integer32"
_TyviewSysClrMjrMin_Object = MibScalar
tyviewSysClrMjrMin = _TyviewSysClrMjrMin_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 2, 1, 43),
    _TyviewSysClrMjrMin_Type()
)
tyviewSysClrMjrMin.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    tyviewSysClrMjrMin.setStatus("mandatory")
_TyviewDatabaseTable_Object = MibTable
tyviewDatabaseTable = _TyviewDatabaseTable_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 2, 2)
)
if mibBuilder.loadTexts:
    tyviewDatabaseTable.setStatus("mandatory")
_TyviewDatabaseEntry_Object = MibTableRow
tyviewDatabaseEntry = _TyviewDatabaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 2, 2, 1)
)
tyviewDatabaseEntry.setIndexNames(
    (0, "NETEXEC-MIB", "tyviewDatabaseSlot"),
    (0, "NETEXEC-MIB", "tyviewDatabaseNode"),
)
if mibBuilder.loadTexts:
    tyviewDatabaseEntry.setStatus("mandatory")


class _TyviewDatabaseSlot_Type(Integer32):
    """Custom type tyviewDatabaseSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_TyviewDatabaseSlot_Type.__name__ = "Integer32"
_TyviewDatabaseSlot_Object = MibTableColumn
tyviewDatabaseSlot = _TyviewDatabaseSlot_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 2, 2, 1, 1),
    _TyviewDatabaseSlot_Type()
)
tyviewDatabaseSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tyviewDatabaseSlot.setStatus("mandatory")


class _TyviewDatabaseNode_Type(Integer32):
    """Custom type tyviewDatabaseNode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TyviewDatabaseNode_Type.__name__ = "Integer32"
_TyviewDatabaseNode_Object = MibTableColumn
tyviewDatabaseNode = _TyviewDatabaseNode_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 2, 2, 1, 2),
    _TyviewDatabaseNode_Type()
)
tyviewDatabaseNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tyviewDatabaseNode.setStatus("mandatory")


class _TyviewDatabaseName_Type(DisplayString):
    """Custom type tyviewDatabaseName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_TyviewDatabaseName_Type.__name__ = "DisplayString"
_TyviewDatabaseName_Object = MibTableColumn
tyviewDatabaseName = _TyviewDatabaseName_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 2, 2, 1, 3),
    _TyviewDatabaseName_Type()
)
tyviewDatabaseName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tyviewDatabaseName.setStatus("mandatory")


class _TyviewDatabaseStatus_Type(Integer32):
    """Custom type tyviewDatabaseStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("error", 3),
          ("ok", 1),
          ("timeout", 2))
    )


_TyviewDatabaseStatus_Type.__name__ = "Integer32"
_TyviewDatabaseStatus_Object = MibTableColumn
tyviewDatabaseStatus = _TyviewDatabaseStatus_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 2, 2, 1, 4),
    _TyviewDatabaseStatus_Type()
)
tyviewDatabaseStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tyviewDatabaseStatus.setStatus("mandatory")
_TyviewBroadcastTable_ObjectIdentity = ObjectIdentity
tyviewBroadcastTable = _TyviewBroadcastTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 466, 6, 2, 3)
)


class _TyviewBroadcastSetTime_Type(Integer32):
    """Custom type tyviewBroadcastSetTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("setTime", 1)
    )


_TyviewBroadcastSetTime_Type.__name__ = "Integer32"
_TyviewBroadcastSetTime_Object = MibScalar
tyviewBroadcastSetTime = _TyviewBroadcastSetTime_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 2, 3, 1),
    _TyviewBroadcastSetTime_Type()
)
tyviewBroadcastSetTime.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    tyviewBroadcastSetTime.setStatus("mandatory")


class _TyviewBroadcastForwardAlarms_Type(Integer32):
    """Custom type tyviewBroadcastForwardAlarms based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("forwardAlarms", 1)
    )


_TyviewBroadcastForwardAlarms_Type.__name__ = "Integer32"
_TyviewBroadcastForwardAlarms_Object = MibScalar
tyviewBroadcastForwardAlarms = _TyviewBroadcastForwardAlarms_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 2, 3, 2),
    _TyviewBroadcastForwardAlarms_Type()
)
tyviewBroadcastForwardAlarms.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    tyviewBroadcastForwardAlarms.setStatus("mandatory")


class _TyviewBroadcastClearLoopbacks_Type(Integer32):
    """Custom type tyviewBroadcastClearLoopbacks based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clearChanLoopbacks", 2),
          ("clearNetLoopbacks", 1))
    )


_TyviewBroadcastClearLoopbacks_Type.__name__ = "Integer32"
_TyviewBroadcastClearLoopbacks_Object = MibScalar
tyviewBroadcastClearLoopbacks = _TyviewBroadcastClearLoopbacks_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 2, 3, 3),
    _TyviewBroadcastClearLoopbacks_Type()
)
tyviewBroadcastClearLoopbacks.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    tyviewBroadcastClearLoopbacks.setStatus("mandatory")
_TyviewTPTable_Object = MibTable
tyviewTPTable = _TyviewTPTable_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 2, 4)
)
if mibBuilder.loadTexts:
    tyviewTPTable.setStatus("mandatory")
_TyviewTPEntry_Object = MibTableRow
tyviewTPEntry = _TyviewTPEntry_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 2, 4, 1)
)
tyviewTPEntry.setIndexNames(
    (0, "NETEXEC-MIB", "tyviewTPRecord"),
)
if mibBuilder.loadTexts:
    tyviewTPEntry.setStatus("mandatory")


class _TyviewTPRecord_Type(Integer32):
    """Custom type tyviewTPRecord based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 25),
    )


_TyviewTPRecord_Type.__name__ = "Integer32"
_TyviewTPRecord_Object = MibTableColumn
tyviewTPRecord = _TyviewTPRecord_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 2, 4, 1, 1),
    _TyviewTPRecord_Type()
)
tyviewTPRecord.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tyviewTPRecord.setStatus("mandatory")


class _TyviewTPMonNodeMode_Type(Integer32):
    """Custom type tyviewTPMonNodeMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("all-nodes", 2),
          ("node-specific", 3),
          ("none", 1))
    )


_TyviewTPMonNodeMode_Type.__name__ = "Integer32"
_TyviewTPMonNodeMode_Object = MibTableColumn
tyviewTPMonNodeMode = _TyviewTPMonNodeMode_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 2, 4, 1, 2),
    _TyviewTPMonNodeMode_Type()
)
tyviewTPMonNodeMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tyviewTPMonNodeMode.setStatus("mandatory")


class _TyviewTPNode_Type(DisplayString):
    """Custom type tyviewTPNode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_TyviewTPNode_Type.__name__ = "DisplayString"
_TyviewTPNode_Object = MibTableColumn
tyviewTPNode = _TyviewTPNode_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 2, 4, 1, 3),
    _TyviewTPNode_Type()
)
tyviewTPNode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tyviewTPNode.setStatus("mandatory")


class _TyviewTPAlarmType_Type(Integer32):
    """Custom type tyviewTPAlarmType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("all", 3),
          ("major", 1),
          ("minor", 2))
    )


_TyviewTPAlarmType_Type.__name__ = "Integer32"
_TyviewTPAlarmType_Object = MibTableColumn
tyviewTPAlarmType = _TyviewTPAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 2, 4, 1, 4),
    _TyviewTPAlarmType_Type()
)
tyviewTPAlarmType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tyviewTPAlarmType.setStatus("mandatory")


class _TyviewTPTriggerEvent_Type(Integer32):
    """Custom type tyviewTPTriggerEvent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alarm-instance", 2),
          ("alarm-on", 1))
    )


_TyviewTPTriggerEvent_Type.__name__ = "Integer32"
_TyviewTPTriggerEvent_Object = MibTableColumn
tyviewTPTriggerEvent = _TyviewTPTriggerEvent_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 2, 4, 1, 5),
    _TyviewTPTriggerEvent_Type()
)
tyviewTPTriggerEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tyviewTPTriggerEvent.setStatus("mandatory")
_TyviewTPInstance_Type = Integer32
_TyviewTPInstance_Object = MibTableColumn
tyviewTPInstance = _TyviewTPInstance_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 2, 4, 1, 6),
    _TyviewTPInstance_Type()
)
tyviewTPInstance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tyviewTPInstance.setStatus("mandatory")
_TyviewTPInterval_Type = Integer32
_TyviewTPInterval_Object = MibTableColumn
tyviewTPInterval = _TyviewTPInterval_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 2, 4, 1, 7),
    _TyviewTPInterval_Type()
)
tyviewTPInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tyviewTPInterval.setStatus("mandatory")


class _TyviewTPEventAction_Type(DisplayString):
    """Custom type tyviewTPEventAction based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TyviewTPEventAction_Type.__name__ = "DisplayString"
_TyviewTPEventAction_Object = MibTableColumn
tyviewTPEventAction = _TyviewTPEventAction_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 2, 4, 1, 8),
    _TyviewTPEventAction_Type()
)
tyviewTPEventAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tyviewTPEventAction.setStatus("mandatory")


class _TyviewTPDryContact_Type(Integer32):
    """Custom type tyviewTPDryContact based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dry-contact-major", 2),
          ("dry-contact-minor", 3),
          ("dry-contact-off", 1))
    )


_TyviewTPDryContact_Type.__name__ = "Integer32"
_TyviewTPDryContact_Object = MibTableColumn
tyviewTPDryContact = _TyviewTPDryContact_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 2, 4, 1, 9),
    _TyviewTPDryContact_Type()
)
tyviewTPDryContact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tyviewTPDryContact.setStatus("mandatory")


class _TyviewTPClearDryContact_Type(Integer32):
    """Custom type tyviewTPClearDryContact based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear-major", 1),
          ("clear-minor", 2))
    )


_TyviewTPClearDryContact_Type.__name__ = "Integer32"
_TyviewTPClearDryContact_Object = MibTableColumn
tyviewTPClearDryContact = _TyviewTPClearDryContact_Object(
    (1, 3, 6, 1, 4, 1, 466, 6, 2, 4, 1, 10),
    _TyviewTPClearDryContact_Type()
)
tyviewTPClearDryContact.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    tyviewTPClearDryContact.setStatus("mandatory")

# Managed Objects groups


# Notification objects

dsucsuTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 466, 6, 1, 0, 0)
)
dsucsuTrap.setObjects(
      *(("NETEXEC-MIB", "dsucsuAlarmType"),
        ("NETEXEC-MIB", "dsucsuAlarmSlot"),
        ("NETEXEC-MIB", "dsucsuAlarmNode"),
        ("NETEXEC-MIB", "dsucsuAlarmName"))
)
if mibBuilder.loadTexts:
    dsucsuTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NETEXEC-MIB",
    **{"internet": internet,
       "private": private,
       "enterprises": enterprises,
       "tylink": tylink,
       "netexec": netexec,
       "dsucsu": dsucsu,
       "dsucsuTrap": dsucsuTrap,
       "dsucsuSysTable": dsucsuSysTable,
       "dsucsuSysEntry": dsucsuSysEntry,
       "dsucsuSysSlot": dsucsuSysSlot,
       "dsucsuSysNode": dsucsuSysNode,
       "dsucsuSysName": dsucsuSysName,
       "dsucsuSysType": dsucsuSysType,
       "dsucsuSysSoftRev": dsucsuSysSoftRev,
       "dsucsuSysHardRev": dsucsuSysHardRev,
       "dsucsuSysNumChan": dsucsuSysNumChan,
       "dsucsuCfgNetTable": dsucsuCfgNetTable,
       "dsucsuCfgNetEntry": dsucsuCfgNetEntry,
       "dsucsuCfgNetSlot": dsucsuCfgNetSlot,
       "dsucsuCfgNetNode": dsucsuCfgNetNode,
       "dsucsuCfgNetIndex": dsucsuCfgNetIndex,
       "dsucsuCfgNetInterface": dsucsuCfgNetInterface,
       "dsucsuCfgNetType": dsucsuCfgNetType,
       "dsucsuCfgNetCoding": dsucsuCfgNetCoding,
       "dsucsuCfgNetClockSource": dsucsuCfgNetClockSource,
       "dsucsuCfgNetCsuEnable": dsucsuCfgNetCsuEnable,
       "dsucsuCfgNetCsuLBO": dsucsuCfgNetCsuLBO,
       "dsucsuCfgNetCsuDensity": dsucsuCfgNetCsuDensity,
       "dsucsuCfgNetRateMultiples": dsucsuCfgNetRateMultiples,
       "dsucsuCfgNetOutputPulse": dsucsuCfgNetOutputPulse,
       "dsucsuCfgNetTs0": dsucsuCfgNetTs0,
       "dsucsuCfgNetTs16": dsucsuCfgNetTs16,
       "dsucsuCfgDteChanTable": dsucsuCfgDteChanTable,
       "dsucsuCfgDteChanEntry": dsucsuCfgDteChanEntry,
       "dsucsuCfgDteChanSlot": dsucsuCfgDteChanSlot,
       "dsucsuCfgDteChanNode": dsucsuCfgDteChanNode,
       "dsucsuCfgDteChanIndex": dsucsuCfgDteChanIndex,
       "dsucsuCfgDteChanType": dsucsuCfgDteChanType,
       "dsucsuCfgDteChanRate": dsucsuCfgDteChanRate,
       "dsucsuCfgDteChanEncoding": dsucsuCfgDteChanEncoding,
       "dsucsuCfgDteChanStartDs0": dsucsuCfgDteChanStartDs0,
       "dsucsuCfgDteChanCtrlSignal": dsucsuCfgDteChanCtrlSignal,
       "dsucsuCfgDteChanTiming": dsucsuCfgDteChanTiming,
       "dsucsuCfgDteChanClockInvert": dsucsuCfgDteChanClockInvert,
       "dsucsuCfgDteChanDataInvert": dsucsuCfgDteChanDataInvert,
       "dsucsuCfgFrmChanTable": dsucsuCfgFrmChanTable,
       "dsucsuCfgFrmChanEntry": dsucsuCfgFrmChanEntry,
       "dsucsuCfgFrmChanSlot": dsucsuCfgFrmChanSlot,
       "dsucsuCfgFrmChanNode": dsucsuCfgFrmChanNode,
       "dsucsuCfgFrmChanIndex": dsucsuCfgFrmChanIndex,
       "dsucsuCfgFrmChanType": dsucsuCfgFrmChanType,
       "dsucsuCfgFrmChanNumDs0": dsucsuCfgFrmChanNumDs0,
       "dsucsuCfgFrmChanEncoding": dsucsuCfgFrmChanEncoding,
       "dsucsuCfgFrmChanStartDs0": dsucsuCfgFrmChanStartDs0,
       "dsucsuCfgFrmChanDteStartDs0": dsucsuCfgFrmChanDteStartDs0,
       "dsucsuCfgFrmChanMapping": dsucsuCfgFrmChanMapping,
       "dsucsuCfgFrmChanDs0Type": dsucsuCfgFrmChanDs0Type,
       "dsucsuCfgFrmChanFrameType": dsucsuCfgFrmChanFrameType,
       "dsucsuCfgFrmChanOutputPulse": dsucsuCfgFrmChanOutputPulse,
       "dsucsuCfgFrmChanNetMapping": dsucsuCfgFrmChanNetMapping,
       "dsucsuConfigSupTable": dsucsuConfigSupTable,
       "dsucsuConfigSupEntry": dsucsuConfigSupEntry,
       "dsucsuConfigSupSlot": dsucsuConfigSupSlot,
       "dsucsuConfigSupNode": dsucsuConfigSupNode,
       "dsucsuConfigSupIndex": dsucsuConfigSupIndex,
       "dsucsuConfigSupDs0": dsucsuConfigSupDs0,
       "dsucsuCfgSupAuxTable": dsucsuCfgSupAuxTable,
       "dsucsuCfgSupAuxEntry": dsucsuCfgSupAuxEntry,
       "dsucsuCfgSupAuxSlot": dsucsuCfgSupAuxSlot,
       "dsucsuCfgSupAuxNode": dsucsuCfgSupAuxNode,
       "dsucsuCfgSupAuxIndex": dsucsuCfgSupAuxIndex,
       "dsucsuCfgSupAuxFdl": dsucsuCfgSupAuxFdl,
       "dsucsuActvConfTable": dsucsuActvConfTable,
       "dsucsuActvConfEntry": dsucsuActvConfEntry,
       "dsucsuActvConfSlot": dsucsuActvConfSlot,
       "dsucsuActvConfNode": dsucsuActvConfNode,
       "dsucsuActvConfIndex": dsucsuActvConfIndex,
       "dsucsuEventDesTable": dsucsuEventDesTable,
       "dsucsuEventDesEntry": dsucsuEventDesEntry,
       "dsucsuEventDesSlot": dsucsuEventDesSlot,
       "dsucsuEventDesNode": dsucsuEventDesNode,
       "dsucsuEventNameIndx": dsucsuEventNameIndx,
       "dsucsuEventDesName1": dsucsuEventDesName1,
       "dsucsuEventDesName2": dsucsuEventDesName2,
       "dsucsuEventClrDest": dsucsuEventClrDest,
       "dsucsuCfgMaintTable": dsucsuCfgMaintTable,
       "dsucsuCfgMaintEntry": dsucsuCfgMaintEntry,
       "dsucsuCfgMaintSlot": dsucsuCfgMaintSlot,
       "dsucsuCfgMaintNode": dsucsuCfgMaintNode,
       "dsucsuCfgMaintChanType": dsucsuCfgMaintChanType,
       "dsucsuCfgMaintFlowCtrl": dsucsuCfgMaintFlowCtrl,
       "dsucsuCfgMaintStopBits": dsucsuCfgMaintStopBits,
       "dsucsuCfgMaintParity": dsucsuCfgMaintParity,
       "dsucsuCfgMaintDataBits": dsucsuCfgMaintDataBits,
       "dsucsuCfgMaintBaud": dsucsuCfgMaintBaud,
       "dsucsuCfgCommTable": dsucsuCfgCommTable,
       "dsucsuCfgCommEntry": dsucsuCfgCommEntry,
       "dsucsuCfgCommSlot": dsucsuCfgCommSlot,
       "dsucsuCfgCommNode": dsucsuCfgCommNode,
       "dsucsuCfgCommChanType": dsucsuCfgCommChanType,
       "dsucsuCfgCommFlowCtrl": dsucsuCfgCommFlowCtrl,
       "dsucsuCfgCommStopBits": dsucsuCfgCommStopBits,
       "dsucsuCfgCommParity": dsucsuCfgCommParity,
       "dsucsuCfgCommDataBits": dsucsuCfgCommDataBits,
       "dsucsuCfgCommBaud": dsucsuCfgCommBaud,
       "dsucsuCfgBrdTable": dsucsuCfgBrdTable,
       "dsucsuCfgBrdEntry": dsucsuCfgBrdEntry,
       "dsucsuCfgBrdSlot": dsucsuCfgBrdSlot,
       "dsucsuCfgBrdNode": dsucsuCfgBrdNode,
       "dsucsuCfgBrdTiming": dsucsuCfgBrdTiming,
       "dsucsuCfgDacsTable": dsucsuCfgDacsTable,
       "dsucsuCfgAutoAssignTable": dsucsuCfgAutoAssignTable,
       "dsucsuCfgAutoAssignEntry": dsucsuCfgAutoAssignEntry,
       "dsucsuConnAutoSlot": dsucsuConnAutoSlot,
       "dsucsuConnAutoNode": dsucsuConnAutoNode,
       "dsucsuConnAutoSrcPort": dsucsuConnAutoSrcPort,
       "dsucsuConnAutoStartDS0": dsucsuConnAutoStartDS0,
       "dsucsuConnAutoDestPort": dsucsuConnAutoDestPort,
       "dsucsuConnAutoType": dsucsuConnAutoType,
       "dsucsuConnDteRate": dsucsuConnDteRate,
       "dsucsuConnDteDensity": dsucsuConnDteDensity,
       "dsucsuConnDs0Required": dsucsuConnDs0Required,
       "dsucsuConnAutoStatus": dsucsuConnAutoStatus,
       "dsucsuConnAutoUpdateCmd": dsucsuConnAutoUpdateCmd,
       "dsucsuCfgCurrentConnTable": dsucsuCfgCurrentConnTable,
       "dsucsuCfgCurrentConnections": dsucsuCfgCurrentConnections,
       "dsucsuSlot": dsucsuSlot,
       "dsucsuNode": dsucsuNode,
       "dsucsuT1Index": dsucsuT1Index,
       "dsucsuDs0": dsucsuDs0,
       "dsucsuDtePort": dsucsuDtePort,
       "dsucsuType": dsucsuType,
       "dsucsuCfgEditConnTable": dsucsuCfgEditConnTable,
       "dsucsuCfgEditConnEntry": dsucsuCfgEditConnEntry,
       "dsucsuConnSlot": dsucsuConnSlot,
       "dsucsuConnNode": dsucsuConnNode,
       "dsucsuConnSrcPort": dsucsuConnSrcPort,
       "dsucsuConnSrcDs0": dsucsuConnSrcDs0,
       "dsucsuConnDestPort": dsucsuConnDestPort,
       "dsucsuConnDestDs0": dsucsuConnDestDs0,
       "dsucsuConnType": dsucsuConnType,
       "dsucsuConnNumDs0s": dsucsuConnNumDs0s,
       "dsucsuConnSetStatus": dsucsuConnSetStatus,
       "dsucsuConnConnect": dsucsuConnConnect,
       "dsucsuConnUpdateRequired": dsucsuConnUpdateRequired,
       "dsucsuConnUpdateCmd": dsucsuConnUpdateCmd,
       "dsucsuConnClearEditBuff": dsucsuConnClearEditBuff,
       "dsucsuDiagNetTable": dsucsuDiagNetTable,
       "dsucsuDiagNetEntry": dsucsuDiagNetEntry,
       "dsucsuDiagNetSlot": dsucsuDiagNetSlot,
       "dsucsuDiagNetNode": dsucsuDiagNetNode,
       "dsucsuDiagNetIndex": dsucsuDiagNetIndex,
       "dsucsuDiagNetLclNetAggLpbk": dsucsuDiagNetLclNetAggLpbk,
       "dsucsuDiagNetLclNetLpbk": dsucsuDiagNetLclNetLpbk,
       "dsucsuDiagNetLclNetPayload": dsucsuDiagNetLclNetPayload,
       "dsucsuDiagNetLclNetBiDir": dsucsuDiagNetLclNetBiDir,
       "dsucsuDiagNetRemCsuLpbk": dsucsuDiagNetRemCsuLpbk,
       "dsucsuDiagNetRemDsuLpbk": dsucsuDiagNetRemDsuLpbk,
       "dsucsuDiagNetEvElapTime": dsucsuDiagNetEvElapTime,
       "dsucsuDiagNetEvCRC6Err": dsucsuDiagNetEvCRC6Err,
       "dsucsuDiagNetEvOofErr": dsucsuDiagNetEvOofErr,
       "dsucsuDiagNetErrEvents": dsucsuDiagNetErrEvents,
       "dsucsuDiagNetClearEvReg": dsucsuDiagNetClearEvReg,
       "dsucsuDiagDteTable": dsucsuDiagDteTable,
       "dsucsuDiagDteEntry": dsucsuDiagDteEntry,
       "dsucsuDiagDteSlot": dsucsuDiagDteSlot,
       "dsucsuDiagDteNode": dsucsuDiagDteNode,
       "dsucsuDiagDteIndex": dsucsuDiagDteIndex,
       "dsucsuDiagDteLocalBiDir": dsucsuDiagDteLocalBiDir,
       "dsucsuDiagDteLocalPayload": dsucsuDiagDteLocalPayload,
       "dsucsuDiagDteRemLpbk": dsucsuDiagDteRemLpbk,
       "dsucsuDiagDteBertTestAct": dsucsuDiagDteBertTestAct,
       "dsucsuDiagDteBertHourStrt": dsucsuDiagDteBertHourStrt,
       "dsucsuDiagDteBertMinStrt": dsucsuDiagDteBertMinStrt,
       "dsucsuDiagDteBertTimeElaps": dsucsuDiagDteBertTimeElaps,
       "dsucsuDiagDteBertErrors": dsucsuDiagDteBertErrors,
       "dsucsuDiagFrmTable": dsucsuDiagFrmTable,
       "dsucsuDiagFrmEntry": dsucsuDiagFrmEntry,
       "dsucsuDiagFrmSlot": dsucsuDiagFrmSlot,
       "dsucsuDiagFrmNode": dsucsuDiagFrmNode,
       "dsucsuDiagFrmIndex": dsucsuDiagFrmIndex,
       "dsucsuDiagFrmLclLpbk": dsucsuDiagFrmLclLpbk,
       "dsucsuDiagFrmLclPayload": dsucsuDiagFrmLclPayload,
       "dsucsuDiagFrmLclBiDir": dsucsuDiagFrmLclBiDir,
       "dsucsuDiagFrmRemLpbk": dsucsuDiagFrmRemLpbk,
       "dsucsuDiagFrmLclDte": dsucsuDiagFrmLclDte,
       "dsucsuDiagFrmLclDte2": dsucsuDiagFrmLclDte2,
       "dsucsuDiagFrmBertTestAct": dsucsuDiagFrmBertTestAct,
       "dsucsuDiagFrmEvElapTime": dsucsuDiagFrmEvElapTime,
       "dsucsuDiagFrmEvBpvErr": dsucsuDiagFrmEvBpvErr,
       "dsucsuDiagFrmEvOofErr": dsucsuDiagFrmEvOofErr,
       "dsucsuDiagFrmFrameErr": dsucsuDiagFrmFrameErr,
       "dsucsuDiagFrmClearEvReg": dsucsuDiagFrmClearEvReg,
       "dsucsuDiagAuxTable": dsucsuDiagAuxTable,
       "dsucsuDiagAuxEntry": dsucsuDiagAuxEntry,
       "dsucsuDiagAuxSlot": dsucsuDiagAuxSlot,
       "dsucsuDiagAuxNode": dsucsuDiagAuxNode,
       "dsucsuDiagAuxChAStatus": dsucsuDiagAuxChAStatus,
       "dsucsuDiagAuxChBStatus": dsucsuDiagAuxChBStatus,
       "dsucsuDiagAuxFdlStatus": dsucsuDiagAuxFdlStatus,
       "dsucsuDiagAuxFdl2Status": dsucsuDiagAuxFdl2Status,
       "dsucsuDiagAuxMaintStatus": dsucsuDiagAuxMaintStatus,
       "dsucsuDiagAuxCommStatus": dsucsuDiagAuxCommStatus,
       "dsucsuDiagPortTable": dsucsuDiagPortTable,
       "dsucsuDiagPortEntry": dsucsuDiagPortEntry,
       "dsucsuDiagPortSlot": dsucsuDiagPortSlot,
       "dsucsuDiagPortNode": dsucsuDiagPortNode,
       "dsucsuDiagPortIndex": dsucsuDiagPortIndex,
       "dsucsuDiagPortType": dsucsuDiagPortType,
       "dsucsuDiagPortStatus": dsucsuDiagPortStatus,
       "dsucsuIntervalTable": dsucsuIntervalTable,
       "dsucsuIntervalEntry": dsucsuIntervalEntry,
       "dsucsuIntervalSlot": dsucsuIntervalSlot,
       "dsucsuIntervalNode": dsucsuIntervalNode,
       "dsucsuIntervalPort": dsucsuIntervalPort,
       "dsucsuIntervalNum": dsucsuIntervalNum,
       "dsucsuIntervalESs": dsucsuIntervalESs,
       "dsucsuIntervalSESs": dsucsuIntervalSESs,
       "dsucsuIntervalBPVs": dsucsuIntervalBPVs,
       "dsucsuIntervalFSs": dsucsuIntervalFSs,
       "dsucsuCurrentTable": dsucsuCurrentTable,
       "dsucsuCurrentEntry": dsucsuCurrentEntry,
       "dsucsuCurrentSlot": dsucsuCurrentSlot,
       "dsucsuCurrentNode": dsucsuCurrentNode,
       "dsucsuCurrentPort": dsucsuCurrentPort,
       "dsucsuCurrentESs": dsucsuCurrentESs,
       "dsucsuCurrentSESs": dsucsuCurrentSESs,
       "dsucsuCurrentBPVs": dsucsuCurrentBPVs,
       "dsucsuCurrentSECs": dsucsuCurrentSECs,
       "dsucsuCurrentStatus": dsucsuCurrentStatus,
       "dsucsuTotalTable": dsucsuTotalTable,
       "dsucsuTotalEntry": dsucsuTotalEntry,
       "dsucsuTotalSlot": dsucsuTotalSlot,
       "dsucsuTotalNode": dsucsuTotalNode,
       "dsucsuTotalPort": dsucsuTotalPort,
       "dsucsuTotalESs": dsucsuTotalESs,
       "dsucsuTotalSESs": dsucsuTotalSESs,
       "dsucsuTotalBPVs": dsucsuTotalBPVs,
       "dsucsuTotalSECs": dsucsuTotalSECs,
       "dsucsuTotalStatus": dsucsuTotalStatus,
       "dsucsuAlarmType": dsucsuAlarmType,
       "dsucsuAlarmSlot": dsucsuAlarmSlot,
       "dsucsuAlarmNode": dsucsuAlarmNode,
       "dsucsuAlarmName": dsucsuAlarmName,
       "tyview": tyview,
       "tyviewSysTable": tyviewSysTable,
       "tyviewSysRevSw": tyviewSysRevSw,
       "tyviewSysName": tyviewSysName,
       "tyviewSysId": tyviewSysId,
       "tyviewSysTimeOutFactor": tyviewSysTimeOutFactor,
       "tyviewSysObjectId": tyviewSysObjectId,
       "tyviewSysSlotNumber": tyviewSysSlotNumber,
       "tyviewSysClearDatabase": tyviewSysClearDatabase,
       "tyviewSysGetCommName": tyviewSysGetCommName,
       "tyviewSysSetCommName": tyviewSysSetCommName,
       "tyviewSysTrapCommName": tyviewSysTrapCommName,
       "tyviewSysN1TrapDest": tyviewSysN1TrapDest,
       "tyviewSysN2TrapDest": tyviewSysN2TrapDest,
       "tyviewSysDate": tyviewSysDate,
       "tyviewSysTime": tyviewSysTime,
       "tyviewSysMjrMnrLED": tyviewSysMjrMnrLED,
       "tyviewSysFanPSLED": tyviewSysFanPSLED,
       "tyviewSysCtlrLED": tyviewSysCtlrLED,
       "tyviewSysSlipLED": tyviewSysSlipLED,
       "tyviewSysCtlChLED": tyviewSysCtlChLED,
       "tyviewSysTDMLED": tyviewSysTDMLED,
       "tyviewSysMaintUseage": tyviewSysMaintUseage,
       "tyviewSysMaintDataBits": tyviewSysMaintDataBits,
       "tyviewSysMaintRate": tyviewSysMaintRate,
       "tyviewSysMaintStopBits": tyviewSysMaintStopBits,
       "tyviewSysMaintParity": tyviewSysMaintParity,
       "tyviewSysMaintMtu": tyviewSysMaintMtu,
       "tyviewSysMaintCompression": tyviewSysMaintCompression,
       "tyviewSysMaintSubnetMask": tyviewSysMaintSubnetMask,
       "tyviewSysMaintLocalIP": tyviewSysMaintLocalIP,
       "tyviewSysMaintPeerIP": tyviewSysMaintPeerIP,
       "tyviewSysComUseage": tyviewSysComUseage,
       "tyviewSysComDataBits": tyviewSysComDataBits,
       "tyviewSysComRate": tyviewSysComRate,
       "tyviewSysComStopBits": tyviewSysComStopBits,
       "tyviewSysComParity": tyviewSysComParity,
       "tyviewSysComMtu": tyviewSysComMtu,
       "tyviewSysComCompression": tyviewSysComCompression,
       "tyviewSysComSubnetMask": tyviewSysComSubnetMask,
       "tyviewSysComLocalIP": tyviewSysComLocalIP,
       "tyviewSysComPeerIP": tyviewSysComPeerIP,
       "tyviewSysTelnetEna": tyviewSysTelnetEna,
       "tyviewSysTelnetTO": tyviewSysTelnetTO,
       "tyviewSysClrMjrMin": tyviewSysClrMjrMin,
       "tyviewDatabaseTable": tyviewDatabaseTable,
       "tyviewDatabaseEntry": tyviewDatabaseEntry,
       "tyviewDatabaseSlot": tyviewDatabaseSlot,
       "tyviewDatabaseNode": tyviewDatabaseNode,
       "tyviewDatabaseName": tyviewDatabaseName,
       "tyviewDatabaseStatus": tyviewDatabaseStatus,
       "tyviewBroadcastTable": tyviewBroadcastTable,
       "tyviewBroadcastSetTime": tyviewBroadcastSetTime,
       "tyviewBroadcastForwardAlarms": tyviewBroadcastForwardAlarms,
       "tyviewBroadcastClearLoopbacks": tyviewBroadcastClearLoopbacks,
       "tyviewTPTable": tyviewTPTable,
       "tyviewTPEntry": tyviewTPEntry,
       "tyviewTPRecord": tyviewTPRecord,
       "tyviewTPMonNodeMode": tyviewTPMonNodeMode,
       "tyviewTPNode": tyviewTPNode,
       "tyviewTPAlarmType": tyviewTPAlarmType,
       "tyviewTPTriggerEvent": tyviewTPTriggerEvent,
       "tyviewTPInstance": tyviewTPInstance,
       "tyviewTPInterval": tyviewTPInterval,
       "tyviewTPEventAction": tyviewTPEventAction,
       "tyviewTPDryContact": tyviewTPDryContact,
       "tyviewTPClearDryContact": tyviewTPClearDryContact}
)
