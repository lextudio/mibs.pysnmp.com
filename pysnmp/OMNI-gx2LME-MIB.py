# SNMP MIB module (OMNI-gx2LME-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/OMNI-gx2LME-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:34:25 2024
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

(gx2LmE,) = mibBuilder.importSymbols(
    "GX2HFC-MIB",
    "gx2LmE")

(gi,
 motproxies) = mibBuilder.importSymbols(
    "NLS-BBNIDENT-MIB",
    "gi",
    "motproxies")

(trapChangedObjectId,
 trapChangedValueDisplayString,
 trapChangedValueInteger,
 trapIdentifier,
 trapNETrapLastTrapTimeStamp,
 trapNetworkElemAdminState,
 trapNetworkElemAlarmStatus,
 trapNetworkElemAvailStatus,
 trapNetworkElemModelNumber,
 trapNetworkElemOperState,
 trapNetworkElemSerialNum,
 trapPerceivedSeverity,
 trapText) = mibBuilder.importSymbols(
    "NLSBBN-TRAPS-MIB",
    "trapChangedObjectId",
    "trapChangedValueDisplayString",
    "trapChangedValueInteger",
    "trapIdentifier",
    "trapNETrapLastTrapTimeStamp",
    "trapNetworkElemAdminState",
    "trapNetworkElemAlarmStatus",
    "trapNetworkElemAvailStatus",
    "trapNetworkElemModelNumber",
    "trapNetworkElemOperState",
    "trapNetworkElemSerialNum",
    "trapPerceivedSeverity",
    "trapText")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(sysUpTime,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysUpTime")

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



class Float(Counter32):
    """Custom type Float based on Counter32"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Gx2lmeDescriptor_ObjectIdentity = ObjectIdentity
gx2lmeDescriptor = _Gx2lmeDescriptor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 1)
)
_Gx2lmeAnalogTable_Object = MibTable
gx2lmeAnalogTable = _Gx2lmeAnalogTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 2)
)
if mibBuilder.loadTexts:
    gx2lmeAnalogTable.setStatus("mandatory")
_Gx2lmeAnalogEntry_Object = MibTableRow
gx2lmeAnalogEntry = _Gx2lmeAnalogEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 2, 1)
)
gx2lmeAnalogEntry.setIndexNames(
    (0, "OMNI-gx2LME-MIB", "gx2lmeAnalogTableIndex"),
)
if mibBuilder.loadTexts:
    gx2lmeAnalogEntry.setStatus("mandatory")


class _Gx2lmeAnalogTableIndex_Type(Integer32):
    """Custom type gx2lmeAnalogTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Gx2lmeAnalogTableIndex_Type.__name__ = "Integer32"
_Gx2lmeAnalogTableIndex_Object = MibTableColumn
gx2lmeAnalogTableIndex = _Gx2lmeAnalogTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 2, 1, 1),
    _Gx2lmeAnalogTableIndex_Type()
)
gx2lmeAnalogTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gx2lmeAnalogTableIndex.setStatus("mandatory")


class _LmelabelOffsetNomMonitor_Type(DisplayString):
    """Custom type lmelabelOffsetNomMonitor based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_LmelabelOffsetNomMonitor_Type.__name__ = "DisplayString"
_LmelabelOffsetNomMonitor_Object = MibTableColumn
lmelabelOffsetNomMonitor = _LmelabelOffsetNomMonitor_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 2, 1, 2),
    _LmelabelOffsetNomMonitor_Type()
)
lmelabelOffsetNomMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmelabelOffsetNomMonitor.setStatus("optional")


class _LmeuomOffsetNomMonitor_Type(DisplayString):
    """Custom type lmeuomOffsetNomMonitor based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_LmeuomOffsetNomMonitor_Type.__name__ = "DisplayString"
_LmeuomOffsetNomMonitor_Object = MibTableColumn
lmeuomOffsetNomMonitor = _LmeuomOffsetNomMonitor_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 2, 1, 3),
    _LmeuomOffsetNomMonitor_Type()
)
lmeuomOffsetNomMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmeuomOffsetNomMonitor.setStatus("optional")
_LmemajorHighOffsetNomMonitor_Type = Float
_LmemajorHighOffsetNomMonitor_Object = MibTableColumn
lmemajorHighOffsetNomMonitor = _LmemajorHighOffsetNomMonitor_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 2, 1, 4),
    _LmemajorHighOffsetNomMonitor_Type()
)
lmemajorHighOffsetNomMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmemajorHighOffsetNomMonitor.setStatus("mandatory")
_LmemajorLowOffsetNomMonitor_Type = Float
_LmemajorLowOffsetNomMonitor_Object = MibTableColumn
lmemajorLowOffsetNomMonitor = _LmemajorLowOffsetNomMonitor_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 2, 1, 5),
    _LmemajorLowOffsetNomMonitor_Type()
)
lmemajorLowOffsetNomMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmemajorLowOffsetNomMonitor.setStatus("mandatory")
_LmeminorHighOffsetNomMonitor_Type = Float
_LmeminorHighOffsetNomMonitor_Object = MibTableColumn
lmeminorHighOffsetNomMonitor = _LmeminorHighOffsetNomMonitor_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 2, 1, 6),
    _LmeminorHighOffsetNomMonitor_Type()
)
lmeminorHighOffsetNomMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmeminorHighOffsetNomMonitor.setStatus("mandatory")
_LmeminorLowOffsetNomMonitor_Type = Float
_LmeminorLowOffsetNomMonitor_Object = MibTableColumn
lmeminorLowOffsetNomMonitor = _LmeminorLowOffsetNomMonitor_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 2, 1, 7),
    _LmeminorLowOffsetNomMonitor_Type()
)
lmeminorLowOffsetNomMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmeminorLowOffsetNomMonitor.setStatus("mandatory")
_LmecurrentValueOffsetNomMonitor_Type = Float
_LmecurrentValueOffsetNomMonitor_Object = MibTableColumn
lmecurrentValueOffsetNomMonitor = _LmecurrentValueOffsetNomMonitor_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 2, 1, 8),
    _LmecurrentValueOffsetNomMonitor_Type()
)
lmecurrentValueOffsetNomMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmecurrentValueOffsetNomMonitor.setStatus("mandatory")


class _LmestateFlagOffsetNomMonitor_Type(Integer32):
    """Custom type lmestateFlagOffsetNomMonitor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hidden", 1),
          ("read-only", 2),
          ("updateable", 3))
    )


_LmestateFlagOffsetNomMonitor_Type.__name__ = "Integer32"
_LmestateFlagOffsetNomMonitor_Object = MibTableColumn
lmestateFlagOffsetNomMonitor = _LmestateFlagOffsetNomMonitor_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 2, 1, 9),
    _LmestateFlagOffsetNomMonitor_Type()
)
lmestateFlagOffsetNomMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmestateFlagOffsetNomMonitor.setStatus("mandatory")
_LmeminValueOffsetNomMonitor_Type = Float
_LmeminValueOffsetNomMonitor_Object = MibTableColumn
lmeminValueOffsetNomMonitor = _LmeminValueOffsetNomMonitor_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 2, 1, 10),
    _LmeminValueOffsetNomMonitor_Type()
)
lmeminValueOffsetNomMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmeminValueOffsetNomMonitor.setStatus("mandatory")
_LmemaxValueOffsetNomMonitor_Type = Float
_LmemaxValueOffsetNomMonitor_Object = MibTableColumn
lmemaxValueOffsetNomMonitor = _LmemaxValueOffsetNomMonitor_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 2, 1, 11),
    _LmemaxValueOffsetNomMonitor_Type()
)
lmemaxValueOffsetNomMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmemaxValueOffsetNomMonitor.setStatus("mandatory")


class _LmealarmStateOffsetNomMonitor_Type(Integer32):
    """Custom type lmealarmStateOffsetNomMonitor based on Integer32"""
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
        *(("informational", 6),
          ("majorHighAlarm", 5),
          ("majorLowAlarm", 2),
          ("minorHighAlarm", 4),
          ("minorLowAlarm", 3),
          ("noAlarm", 1))
    )


_LmealarmStateOffsetNomMonitor_Type.__name__ = "Integer32"
_LmealarmStateOffsetNomMonitor_Object = MibTableColumn
lmealarmStateOffsetNomMonitor = _LmealarmStateOffsetNomMonitor_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 2, 1, 12),
    _LmealarmStateOffsetNomMonitor_Type()
)
lmealarmStateOffsetNomMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmealarmStateOffsetNomMonitor.setStatus("mandatory")


class _LmelabelOffsetNomCnt_Type(DisplayString):
    """Custom type lmelabelOffsetNomCnt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_LmelabelOffsetNomCnt_Type.__name__ = "DisplayString"
_LmelabelOffsetNomCnt_Object = MibTableColumn
lmelabelOffsetNomCnt = _LmelabelOffsetNomCnt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 2, 1, 13),
    _LmelabelOffsetNomCnt_Type()
)
lmelabelOffsetNomCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmelabelOffsetNomCnt.setStatus("optional")


class _LmeuomOffsetNomCnt_Type(DisplayString):
    """Custom type lmeuomOffsetNomCnt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_LmeuomOffsetNomCnt_Type.__name__ = "DisplayString"
_LmeuomOffsetNomCnt_Object = MibTableColumn
lmeuomOffsetNomCnt = _LmeuomOffsetNomCnt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 2, 1, 14),
    _LmeuomOffsetNomCnt_Type()
)
lmeuomOffsetNomCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmeuomOffsetNomCnt.setStatus("optional")
_LmemajorHighOffsetNomCnt_Type = Float
_LmemajorHighOffsetNomCnt_Object = MibTableColumn
lmemajorHighOffsetNomCnt = _LmemajorHighOffsetNomCnt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 2, 1, 15),
    _LmemajorHighOffsetNomCnt_Type()
)
lmemajorHighOffsetNomCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmemajorHighOffsetNomCnt.setStatus("mandatory")
_LmemajorLowOffsetNomCnt_Type = Float
_LmemajorLowOffsetNomCnt_Object = MibTableColumn
lmemajorLowOffsetNomCnt = _LmemajorLowOffsetNomCnt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 2, 1, 16),
    _LmemajorLowOffsetNomCnt_Type()
)
lmemajorLowOffsetNomCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmemajorLowOffsetNomCnt.setStatus("mandatory")
_LmeminorHighOffsetNomCnt_Type = Float
_LmeminorHighOffsetNomCnt_Object = MibTableColumn
lmeminorHighOffsetNomCnt = _LmeminorHighOffsetNomCnt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 2, 1, 17),
    _LmeminorHighOffsetNomCnt_Type()
)
lmeminorHighOffsetNomCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmeminorHighOffsetNomCnt.setStatus("mandatory")
_LmeminorLowOffsetNomCnt_Type = Float
_LmeminorLowOffsetNomCnt_Object = MibTableColumn
lmeminorLowOffsetNomCnt = _LmeminorLowOffsetNomCnt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 2, 1, 18),
    _LmeminorLowOffsetNomCnt_Type()
)
lmeminorLowOffsetNomCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmeminorLowOffsetNomCnt.setStatus("mandatory")
_LmecurrentValueOffsetNomCnt_Type = Float
_LmecurrentValueOffsetNomCnt_Object = MibTableColumn
lmecurrentValueOffsetNomCnt = _LmecurrentValueOffsetNomCnt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 2, 1, 19),
    _LmecurrentValueOffsetNomCnt_Type()
)
lmecurrentValueOffsetNomCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lmecurrentValueOffsetNomCnt.setStatus("mandatory")


class _LmestateFlagOffsetNomCnt_Type(Integer32):
    """Custom type lmestateFlagOffsetNomCnt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hidden", 1),
          ("read-only", 2),
          ("updateable", 3))
    )


_LmestateFlagOffsetNomCnt_Type.__name__ = "Integer32"
_LmestateFlagOffsetNomCnt_Object = MibTableColumn
lmestateFlagOffsetNomCnt = _LmestateFlagOffsetNomCnt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 2, 1, 20),
    _LmestateFlagOffsetNomCnt_Type()
)
lmestateFlagOffsetNomCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmestateFlagOffsetNomCnt.setStatus("mandatory")
_LmeminValueOffsetNomCnt_Type = Float
_LmeminValueOffsetNomCnt_Object = MibTableColumn
lmeminValueOffsetNomCnt = _LmeminValueOffsetNomCnt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 2, 1, 21),
    _LmeminValueOffsetNomCnt_Type()
)
lmeminValueOffsetNomCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmeminValueOffsetNomCnt.setStatus("mandatory")
_LmemaxValueOffsetNomCnt_Type = Float
_LmemaxValueOffsetNomCnt_Object = MibTableColumn
lmemaxValueOffsetNomCnt = _LmemaxValueOffsetNomCnt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 2, 1, 22),
    _LmemaxValueOffsetNomCnt_Type()
)
lmemaxValueOffsetNomCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmemaxValueOffsetNomCnt.setStatus("mandatory")


class _LmealarmStateOffsetNomCnt_Type(Integer32):
    """Custom type lmealarmStateOffsetNomCnt based on Integer32"""
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
        *(("informational", 6),
          ("majorHighAlarm", 5),
          ("majorLowAlarm", 2),
          ("minorHighAlarm", 4),
          ("minorLowAlarm", 3),
          ("noAlarm", 1))
    )


_LmealarmStateOffsetNomCnt_Type.__name__ = "Integer32"
_LmealarmStateOffsetNomCnt_Object = MibTableColumn
lmealarmStateOffsetNomCnt = _LmealarmStateOffsetNomCnt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 2, 1, 23),
    _LmealarmStateOffsetNomCnt_Type()
)
lmealarmStateOffsetNomCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmealarmStateOffsetNomCnt.setStatus("mandatory")


class _LmelabelRelAttenSetting_Type(DisplayString):
    """Custom type lmelabelRelAttenSetting based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_LmelabelRelAttenSetting_Type.__name__ = "DisplayString"
_LmelabelRelAttenSetting_Object = MibTableColumn
lmelabelRelAttenSetting = _LmelabelRelAttenSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 2, 1, 24),
    _LmelabelRelAttenSetting_Type()
)
lmelabelRelAttenSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmelabelRelAttenSetting.setStatus("optional")


class _LmeuomRelAttenSetting_Type(DisplayString):
    """Custom type lmeuomRelAttenSetting based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_LmeuomRelAttenSetting_Type.__name__ = "DisplayString"
_LmeuomRelAttenSetting_Object = MibTableColumn
lmeuomRelAttenSetting = _LmeuomRelAttenSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 2, 1, 25),
    _LmeuomRelAttenSetting_Type()
)
lmeuomRelAttenSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmeuomRelAttenSetting.setStatus("optional")
_LmemajorHighRelAttenSetting_Type = Float
_LmemajorHighRelAttenSetting_Object = MibTableColumn
lmemajorHighRelAttenSetting = _LmemajorHighRelAttenSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 2, 1, 26),
    _LmemajorHighRelAttenSetting_Type()
)
lmemajorHighRelAttenSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmemajorHighRelAttenSetting.setStatus("mandatory")
_LmemajorLowRelAttenSetting_Type = Float
_LmemajorLowRelAttenSetting_Object = MibTableColumn
lmemajorLowRelAttenSetting = _LmemajorLowRelAttenSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 2, 1, 27),
    _LmemajorLowRelAttenSetting_Type()
)
lmemajorLowRelAttenSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmemajorLowRelAttenSetting.setStatus("mandatory")
_LmeminorHighRelAttenSetting_Type = Float
_LmeminorHighRelAttenSetting_Object = MibTableColumn
lmeminorHighRelAttenSetting = _LmeminorHighRelAttenSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 2, 1, 28),
    _LmeminorHighRelAttenSetting_Type()
)
lmeminorHighRelAttenSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmeminorHighRelAttenSetting.setStatus("mandatory")
_LmeminorLowRelAttenSetting_Type = Float
_LmeminorLowRelAttenSetting_Object = MibTableColumn
lmeminorLowRelAttenSetting = _LmeminorLowRelAttenSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 2, 1, 29),
    _LmeminorLowRelAttenSetting_Type()
)
lmeminorLowRelAttenSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmeminorLowRelAttenSetting.setStatus("mandatory")
_LmecurrentValueRelAttenSetting_Type = Float
_LmecurrentValueRelAttenSetting_Object = MibTableColumn
lmecurrentValueRelAttenSetting = _LmecurrentValueRelAttenSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 2, 1, 30),
    _LmecurrentValueRelAttenSetting_Type()
)
lmecurrentValueRelAttenSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lmecurrentValueRelAttenSetting.setStatus("mandatory")


class _LmestateFlagRelAttenSetting_Type(Integer32):
    """Custom type lmestateFlagRelAttenSetting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hidden", 1),
          ("read-only", 2),
          ("updateable", 3))
    )


_LmestateFlagRelAttenSetting_Type.__name__ = "Integer32"
_LmestateFlagRelAttenSetting_Object = MibTableColumn
lmestateFlagRelAttenSetting = _LmestateFlagRelAttenSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 2, 1, 31),
    _LmestateFlagRelAttenSetting_Type()
)
lmestateFlagRelAttenSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmestateFlagRelAttenSetting.setStatus("mandatory")
_LmeminValueRelAttenSetting_Type = Float
_LmeminValueRelAttenSetting_Object = MibTableColumn
lmeminValueRelAttenSetting = _LmeminValueRelAttenSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 2, 1, 32),
    _LmeminValueRelAttenSetting_Type()
)
lmeminValueRelAttenSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmeminValueRelAttenSetting.setStatus("mandatory")
_LmemaxValueRelAttenSetting_Type = Float
_LmemaxValueRelAttenSetting_Object = MibTableColumn
lmemaxValueRelAttenSetting = _LmemaxValueRelAttenSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 2, 1, 33),
    _LmemaxValueRelAttenSetting_Type()
)
lmemaxValueRelAttenSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmemaxValueRelAttenSetting.setStatus("mandatory")


class _LmealarmStateRelAttenSetting_Type(Integer32):
    """Custom type lmealarmStateRelAttenSetting based on Integer32"""
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
        *(("informational", 6),
          ("majorHighAlarm", 5),
          ("majorLowAlarm", 2),
          ("minorHighAlarm", 4),
          ("minorLowAlarm", 3),
          ("noAlarm", 1))
    )


_LmealarmStateRelAttenSetting_Type.__name__ = "Integer32"
_LmealarmStateRelAttenSetting_Object = MibTableColumn
lmealarmStateRelAttenSetting = _LmealarmStateRelAttenSetting_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 2, 1, 34),
    _LmealarmStateRelAttenSetting_Type()
)
lmealarmStateRelAttenSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmealarmStateRelAttenSetting.setStatus("mandatory")


class _LmelabelOptPower_Type(DisplayString):
    """Custom type lmelabelOptPower based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_LmelabelOptPower_Type.__name__ = "DisplayString"
_LmelabelOptPower_Object = MibTableColumn
lmelabelOptPower = _LmelabelOptPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 2, 1, 35),
    _LmelabelOptPower_Type()
)
lmelabelOptPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmelabelOptPower.setStatus("optional")


class _LmeuomOptPower_Type(DisplayString):
    """Custom type lmeuomOptPower based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_LmeuomOptPower_Type.__name__ = "DisplayString"
_LmeuomOptPower_Object = MibTableColumn
lmeuomOptPower = _LmeuomOptPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 2, 1, 36),
    _LmeuomOptPower_Type()
)
lmeuomOptPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmeuomOptPower.setStatus("optional")
_LmemajorHighOptPower_Type = Float
_LmemajorHighOptPower_Object = MibTableColumn
lmemajorHighOptPower = _LmemajorHighOptPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 2, 1, 37),
    _LmemajorHighOptPower_Type()
)
lmemajorHighOptPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmemajorHighOptPower.setStatus("mandatory")
_LmemajorLowOptPower_Type = Float
_LmemajorLowOptPower_Object = MibTableColumn
lmemajorLowOptPower = _LmemajorLowOptPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 2, 1, 38),
    _LmemajorLowOptPower_Type()
)
lmemajorLowOptPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmemajorLowOptPower.setStatus("mandatory")
_LmeminorHighOptPower_Type = Float
_LmeminorHighOptPower_Object = MibTableColumn
lmeminorHighOptPower = _LmeminorHighOptPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 2, 1, 39),
    _LmeminorHighOptPower_Type()
)
lmeminorHighOptPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmeminorHighOptPower.setStatus("mandatory")
_LmeminorLowOptPower_Type = Float
_LmeminorLowOptPower_Object = MibTableColumn
lmeminorLowOptPower = _LmeminorLowOptPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 2, 1, 40),
    _LmeminorLowOptPower_Type()
)
lmeminorLowOptPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmeminorLowOptPower.setStatus("mandatory")
_LmecurrentValueOptPower_Type = Float
_LmecurrentValueOptPower_Object = MibTableColumn
lmecurrentValueOptPower = _LmecurrentValueOptPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 2, 1, 41),
    _LmecurrentValueOptPower_Type()
)
lmecurrentValueOptPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmecurrentValueOptPower.setStatus("mandatory")


class _LmestateFlagOptPower_Type(Integer32):
    """Custom type lmestateFlagOptPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hidden", 1),
          ("read-only", 2),
          ("updateable", 3))
    )


_LmestateFlagOptPower_Type.__name__ = "Integer32"
_LmestateFlagOptPower_Object = MibTableColumn
lmestateFlagOptPower = _LmestateFlagOptPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 2, 1, 42),
    _LmestateFlagOptPower_Type()
)
lmestateFlagOptPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmestateFlagOptPower.setStatus("mandatory")
_LmeminValueOptPower_Type = Float
_LmeminValueOptPower_Object = MibTableColumn
lmeminValueOptPower = _LmeminValueOptPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 2, 1, 43),
    _LmeminValueOptPower_Type()
)
lmeminValueOptPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmeminValueOptPower.setStatus("mandatory")
_LmemaxValueOptPower_Type = Float
_LmemaxValueOptPower_Object = MibTableColumn
lmemaxValueOptPower = _LmemaxValueOptPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 2, 1, 44),
    _LmemaxValueOptPower_Type()
)
lmemaxValueOptPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmemaxValueOptPower.setStatus("mandatory")


class _LmealarmStateOptPower_Type(Integer32):
    """Custom type lmealarmStateOptPower based on Integer32"""
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
        *(("informational", 6),
          ("majorHighAlarm", 5),
          ("majorLowAlarm", 2),
          ("minorHighAlarm", 4),
          ("minorLowAlarm", 3),
          ("noAlarm", 1))
    )


_LmealarmStateOptPower_Type.__name__ = "Integer32"
_LmealarmStateOptPower_Object = MibTableColumn
lmealarmStateOptPower = _LmealarmStateOptPower_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 2, 1, 45),
    _LmealarmStateOptPower_Type()
)
lmealarmStateOptPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmealarmStateOptPower.setStatus("mandatory")


class _LmelabelLaserBias_Type(DisplayString):
    """Custom type lmelabelLaserBias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_LmelabelLaserBias_Type.__name__ = "DisplayString"
_LmelabelLaserBias_Object = MibTableColumn
lmelabelLaserBias = _LmelabelLaserBias_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 2, 1, 46),
    _LmelabelLaserBias_Type()
)
lmelabelLaserBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmelabelLaserBias.setStatus("optional")


class _LmeuomLaserBias_Type(DisplayString):
    """Custom type lmeuomLaserBias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_LmeuomLaserBias_Type.__name__ = "DisplayString"
_LmeuomLaserBias_Object = MibTableColumn
lmeuomLaserBias = _LmeuomLaserBias_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 2, 1, 47),
    _LmeuomLaserBias_Type()
)
lmeuomLaserBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmeuomLaserBias.setStatus("optional")
_LmemajorHighLaserBias_Type = Float
_LmemajorHighLaserBias_Object = MibTableColumn
lmemajorHighLaserBias = _LmemajorHighLaserBias_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 2, 1, 48),
    _LmemajorHighLaserBias_Type()
)
lmemajorHighLaserBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmemajorHighLaserBias.setStatus("mandatory")
_LmemajorLowLaserBias_Type = Float
_LmemajorLowLaserBias_Object = MibTableColumn
lmemajorLowLaserBias = _LmemajorLowLaserBias_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 2, 1, 49),
    _LmemajorLowLaserBias_Type()
)
lmemajorLowLaserBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmemajorLowLaserBias.setStatus("mandatory")
_LmeminorHighLaserBias_Type = Float
_LmeminorHighLaserBias_Object = MibTableColumn
lmeminorHighLaserBias = _LmeminorHighLaserBias_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 2, 1, 50),
    _LmeminorHighLaserBias_Type()
)
lmeminorHighLaserBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmeminorHighLaserBias.setStatus("mandatory")
_LmeminorLowLaserBias_Type = Float
_LmeminorLowLaserBias_Object = MibTableColumn
lmeminorLowLaserBias = _LmeminorLowLaserBias_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 2, 1, 51),
    _LmeminorLowLaserBias_Type()
)
lmeminorLowLaserBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmeminorLowLaserBias.setStatus("mandatory")
_LmecurrentValueLaserBias_Type = Float
_LmecurrentValueLaserBias_Object = MibTableColumn
lmecurrentValueLaserBias = _LmecurrentValueLaserBias_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 2, 1, 52),
    _LmecurrentValueLaserBias_Type()
)
lmecurrentValueLaserBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmecurrentValueLaserBias.setStatus("mandatory")


class _LmestateFlagLaserBias_Type(Integer32):
    """Custom type lmestateFlagLaserBias based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hidden", 1),
          ("read-only", 2),
          ("updateable", 3))
    )


_LmestateFlagLaserBias_Type.__name__ = "Integer32"
_LmestateFlagLaserBias_Object = MibTableColumn
lmestateFlagLaserBias = _LmestateFlagLaserBias_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 2, 1, 53),
    _LmestateFlagLaserBias_Type()
)
lmestateFlagLaserBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmestateFlagLaserBias.setStatus("mandatory")
_LmeminValueLaserBias_Type = Float
_LmeminValueLaserBias_Object = MibTableColumn
lmeminValueLaserBias = _LmeminValueLaserBias_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 2, 1, 54),
    _LmeminValueLaserBias_Type()
)
lmeminValueLaserBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmeminValueLaserBias.setStatus("mandatory")
_LmemaxValueLaserBias_Type = Float
_LmemaxValueLaserBias_Object = MibTableColumn
lmemaxValueLaserBias = _LmemaxValueLaserBias_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 2, 1, 55),
    _LmemaxValueLaserBias_Type()
)
lmemaxValueLaserBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmemaxValueLaserBias.setStatus("mandatory")


class _LmealarmStateLaserBias_Type(Integer32):
    """Custom type lmealarmStateLaserBias based on Integer32"""
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
        *(("informational", 6),
          ("majorHighAlarm", 5),
          ("majorLowAlarm", 2),
          ("minorHighAlarm", 4),
          ("minorLowAlarm", 3),
          ("noAlarm", 1))
    )


_LmealarmStateLaserBias_Type.__name__ = "Integer32"
_LmealarmStateLaserBias_Object = MibTableColumn
lmealarmStateLaserBias = _LmealarmStateLaserBias_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 2, 1, 56),
    _LmealarmStateLaserBias_Type()
)
lmealarmStateLaserBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmealarmStateLaserBias.setStatus("mandatory")


class _LmelabelTecCurrent_Type(DisplayString):
    """Custom type lmelabelTecCurrent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_LmelabelTecCurrent_Type.__name__ = "DisplayString"
_LmelabelTecCurrent_Object = MibTableColumn
lmelabelTecCurrent = _LmelabelTecCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 2, 1, 57),
    _LmelabelTecCurrent_Type()
)
lmelabelTecCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmelabelTecCurrent.setStatus("optional")


class _LmeuomTecCurrent_Type(DisplayString):
    """Custom type lmeuomTecCurrent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_LmeuomTecCurrent_Type.__name__ = "DisplayString"
_LmeuomTecCurrent_Object = MibTableColumn
lmeuomTecCurrent = _LmeuomTecCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 2, 1, 58),
    _LmeuomTecCurrent_Type()
)
lmeuomTecCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmeuomTecCurrent.setStatus("optional")
_LmemajorHighTecCurrent_Type = Float
_LmemajorHighTecCurrent_Object = MibTableColumn
lmemajorHighTecCurrent = _LmemajorHighTecCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 2, 1, 59),
    _LmemajorHighTecCurrent_Type()
)
lmemajorHighTecCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmemajorHighTecCurrent.setStatus("mandatory")
_LmemajorLowTecCurrent_Type = Float
_LmemajorLowTecCurrent_Object = MibTableColumn
lmemajorLowTecCurrent = _LmemajorLowTecCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 2, 1, 60),
    _LmemajorLowTecCurrent_Type()
)
lmemajorLowTecCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmemajorLowTecCurrent.setStatus("mandatory")
_LmeminorHighTecCurrent_Type = Float
_LmeminorHighTecCurrent_Object = MibTableColumn
lmeminorHighTecCurrent = _LmeminorHighTecCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 2, 1, 61),
    _LmeminorHighTecCurrent_Type()
)
lmeminorHighTecCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmeminorHighTecCurrent.setStatus("mandatory")
_LmeminorLowTecCurrent_Type = Float
_LmeminorLowTecCurrent_Object = MibTableColumn
lmeminorLowTecCurrent = _LmeminorLowTecCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 2, 1, 62),
    _LmeminorLowTecCurrent_Type()
)
lmeminorLowTecCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmeminorLowTecCurrent.setStatus("mandatory")
_LmecurrentValueTecCurrent_Type = Float
_LmecurrentValueTecCurrent_Object = MibTableColumn
lmecurrentValueTecCurrent = _LmecurrentValueTecCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 2, 1, 63),
    _LmecurrentValueTecCurrent_Type()
)
lmecurrentValueTecCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmecurrentValueTecCurrent.setStatus("mandatory")


class _LmestateFlagTecCurrent_Type(Integer32):
    """Custom type lmestateFlagTecCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hidden", 1),
          ("read-only", 2),
          ("updateable", 3))
    )


_LmestateFlagTecCurrent_Type.__name__ = "Integer32"
_LmestateFlagTecCurrent_Object = MibTableColumn
lmestateFlagTecCurrent = _LmestateFlagTecCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 2, 1, 64),
    _LmestateFlagTecCurrent_Type()
)
lmestateFlagTecCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmestateFlagTecCurrent.setStatus("mandatory")
_LmeminValueTecCurrent_Type = Float
_LmeminValueTecCurrent_Object = MibTableColumn
lmeminValueTecCurrent = _LmeminValueTecCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 2, 1, 65),
    _LmeminValueTecCurrent_Type()
)
lmeminValueTecCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmeminValueTecCurrent.setStatus("mandatory")
_LmemaxValueTecCurrent_Type = Float
_LmemaxValueTecCurrent_Object = MibTableColumn
lmemaxValueTecCurrent = _LmemaxValueTecCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 2, 1, 66),
    _LmemaxValueTecCurrent_Type()
)
lmemaxValueTecCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmemaxValueTecCurrent.setStatus("mandatory")


class _LmealarmStateTecCurrent_Type(Integer32):
    """Custom type lmealarmStateTecCurrent based on Integer32"""
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
        *(("informational", 6),
          ("majorHighAlarm", 5),
          ("majorLowAlarm", 2),
          ("minorHighAlarm", 4),
          ("minorLowAlarm", 3),
          ("noAlarm", 1))
    )


_LmealarmStateTecCurrent_Type.__name__ = "Integer32"
_LmealarmStateTecCurrent_Object = MibTableColumn
lmealarmStateTecCurrent = _LmealarmStateTecCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 2, 1, 67),
    _LmealarmStateTecCurrent_Type()
)
lmealarmStateTecCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmealarmStateTecCurrent.setStatus("mandatory")


class _LmelabelLaserTemp_Type(DisplayString):
    """Custom type lmelabelLaserTemp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_LmelabelLaserTemp_Type.__name__ = "DisplayString"
_LmelabelLaserTemp_Object = MibTableColumn
lmelabelLaserTemp = _LmelabelLaserTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 2, 1, 68),
    _LmelabelLaserTemp_Type()
)
lmelabelLaserTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmelabelLaserTemp.setStatus("optional")


class _LmeuomLaserTemp_Type(DisplayString):
    """Custom type lmeuomLaserTemp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_LmeuomLaserTemp_Type.__name__ = "DisplayString"
_LmeuomLaserTemp_Object = MibTableColumn
lmeuomLaserTemp = _LmeuomLaserTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 2, 1, 69),
    _LmeuomLaserTemp_Type()
)
lmeuomLaserTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmeuomLaserTemp.setStatus("optional")
_LmemajorHighLaserTemp_Type = Float
_LmemajorHighLaserTemp_Object = MibTableColumn
lmemajorHighLaserTemp = _LmemajorHighLaserTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 2, 1, 70),
    _LmemajorHighLaserTemp_Type()
)
lmemajorHighLaserTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmemajorHighLaserTemp.setStatus("mandatory")
_LmemajorLowLaserTemp_Type = Float
_LmemajorLowLaserTemp_Object = MibTableColumn
lmemajorLowLaserTemp = _LmemajorLowLaserTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 2, 1, 71),
    _LmemajorLowLaserTemp_Type()
)
lmemajorLowLaserTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmemajorLowLaserTemp.setStatus("mandatory")
_LmeminorHighLaserTemp_Type = Float
_LmeminorHighLaserTemp_Object = MibTableColumn
lmeminorHighLaserTemp = _LmeminorHighLaserTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 2, 1, 72),
    _LmeminorHighLaserTemp_Type()
)
lmeminorHighLaserTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmeminorHighLaserTemp.setStatus("mandatory")
_LmeminorLowLaserTemp_Type = Float
_LmeminorLowLaserTemp_Object = MibTableColumn
lmeminorLowLaserTemp = _LmeminorLowLaserTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 2, 1, 73),
    _LmeminorLowLaserTemp_Type()
)
lmeminorLowLaserTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmeminorLowLaserTemp.setStatus("mandatory")
_LmecurrentValueLaserTemp_Type = Float
_LmecurrentValueLaserTemp_Object = MibTableColumn
lmecurrentValueLaserTemp = _LmecurrentValueLaserTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 2, 1, 74),
    _LmecurrentValueLaserTemp_Type()
)
lmecurrentValueLaserTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmecurrentValueLaserTemp.setStatus("mandatory")


class _LmestateFlagLaserTemp_Type(Integer32):
    """Custom type lmestateFlagLaserTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hidden", 1),
          ("read-only", 2),
          ("updateable", 3))
    )


_LmestateFlagLaserTemp_Type.__name__ = "Integer32"
_LmestateFlagLaserTemp_Object = MibTableColumn
lmestateFlagLaserTemp = _LmestateFlagLaserTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 2, 1, 75),
    _LmestateFlagLaserTemp_Type()
)
lmestateFlagLaserTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmestateFlagLaserTemp.setStatus("mandatory")
_LmeminValueLaserTemp_Type = Float
_LmeminValueLaserTemp_Object = MibTableColumn
lmeminValueLaserTemp = _LmeminValueLaserTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 2, 1, 76),
    _LmeminValueLaserTemp_Type()
)
lmeminValueLaserTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmeminValueLaserTemp.setStatus("mandatory")
_LmemaxValueLaserTemp_Type = Float
_LmemaxValueLaserTemp_Object = MibTableColumn
lmemaxValueLaserTemp = _LmemaxValueLaserTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 2, 1, 77),
    _LmemaxValueLaserTemp_Type()
)
lmemaxValueLaserTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmemaxValueLaserTemp.setStatus("mandatory")


class _LmealarmStateLaserTemp_Type(Integer32):
    """Custom type lmealarmStateLaserTemp based on Integer32"""
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
        *(("informational", 6),
          ("majorHighAlarm", 5),
          ("majorLowAlarm", 2),
          ("minorHighAlarm", 4),
          ("minorLowAlarm", 3),
          ("noAlarm", 1))
    )


_LmealarmStateLaserTemp_Type.__name__ = "Integer32"
_LmealarmStateLaserTemp_Object = MibTableColumn
lmealarmStateLaserTemp = _LmealarmStateLaserTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 2, 1, 78),
    _LmealarmStateLaserTemp_Type()
)
lmealarmStateLaserTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmealarmStateLaserTemp.setStatus("mandatory")


class _LmelabelModuleTemp_Type(DisplayString):
    """Custom type lmelabelModuleTemp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_LmelabelModuleTemp_Type.__name__ = "DisplayString"
_LmelabelModuleTemp_Object = MibTableColumn
lmelabelModuleTemp = _LmelabelModuleTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 2, 1, 79),
    _LmelabelModuleTemp_Type()
)
lmelabelModuleTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmelabelModuleTemp.setStatus("optional")


class _LmeuomModuleTemp_Type(DisplayString):
    """Custom type lmeuomModuleTemp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_LmeuomModuleTemp_Type.__name__ = "DisplayString"
_LmeuomModuleTemp_Object = MibTableColumn
lmeuomModuleTemp = _LmeuomModuleTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 2, 1, 80),
    _LmeuomModuleTemp_Type()
)
lmeuomModuleTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmeuomModuleTemp.setStatus("optional")
_LmemajorHighModuleTemp_Type = Float
_LmemajorHighModuleTemp_Object = MibTableColumn
lmemajorHighModuleTemp = _LmemajorHighModuleTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 2, 1, 81),
    _LmemajorHighModuleTemp_Type()
)
lmemajorHighModuleTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmemajorHighModuleTemp.setStatus("mandatory")
_LmemajorLowModuleTemp_Type = Float
_LmemajorLowModuleTemp_Object = MibTableColumn
lmemajorLowModuleTemp = _LmemajorLowModuleTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 2, 1, 82),
    _LmemajorLowModuleTemp_Type()
)
lmemajorLowModuleTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmemajorLowModuleTemp.setStatus("mandatory")
_LmeminorHighModuleTemp_Type = Float
_LmeminorHighModuleTemp_Object = MibTableColumn
lmeminorHighModuleTemp = _LmeminorHighModuleTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 2, 1, 83),
    _LmeminorHighModuleTemp_Type()
)
lmeminorHighModuleTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmeminorHighModuleTemp.setStatus("mandatory")
_LmeminorLowModuleTemp_Type = Float
_LmeminorLowModuleTemp_Object = MibTableColumn
lmeminorLowModuleTemp = _LmeminorLowModuleTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 2, 1, 84),
    _LmeminorLowModuleTemp_Type()
)
lmeminorLowModuleTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmeminorLowModuleTemp.setStatus("mandatory")
_LmecurrentValueModuleTemp_Type = Float
_LmecurrentValueModuleTemp_Object = MibTableColumn
lmecurrentValueModuleTemp = _LmecurrentValueModuleTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 2, 1, 85),
    _LmecurrentValueModuleTemp_Type()
)
lmecurrentValueModuleTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmecurrentValueModuleTemp.setStatus("mandatory")


class _LmestateFlagModuleTemp_Type(Integer32):
    """Custom type lmestateFlagModuleTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hidden", 1),
          ("read-only", 2),
          ("updateable", 3))
    )


_LmestateFlagModuleTemp_Type.__name__ = "Integer32"
_LmestateFlagModuleTemp_Object = MibTableColumn
lmestateFlagModuleTemp = _LmestateFlagModuleTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 2, 1, 86),
    _LmestateFlagModuleTemp_Type()
)
lmestateFlagModuleTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmestateFlagModuleTemp.setStatus("mandatory")
_LmeminValueModuleTemp_Type = Float
_LmeminValueModuleTemp_Object = MibTableColumn
lmeminValueModuleTemp = _LmeminValueModuleTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 2, 1, 87),
    _LmeminValueModuleTemp_Type()
)
lmeminValueModuleTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmeminValueModuleTemp.setStatus("mandatory")
_LmemaxValueModuleTemp_Type = Float
_LmemaxValueModuleTemp_Object = MibTableColumn
lmemaxValueModuleTemp = _LmemaxValueModuleTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 2, 1, 88),
    _LmemaxValueModuleTemp_Type()
)
lmemaxValueModuleTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmemaxValueModuleTemp.setStatus("mandatory")


class _LmealarmStateModuleTemp_Type(Integer32):
    """Custom type lmealarmStateModuleTemp based on Integer32"""
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
        *(("informational", 6),
          ("majorHighAlarm", 5),
          ("majorLowAlarm", 2),
          ("minorHighAlarm", 4),
          ("minorLowAlarm", 3),
          ("noAlarm", 1))
    )


_LmealarmStateModuleTemp_Type.__name__ = "Integer32"
_LmealarmStateModuleTemp_Object = MibTableColumn
lmealarmStateModuleTemp = _LmealarmStateModuleTemp_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 2, 1, 89),
    _LmealarmStateModuleTemp_Type()
)
lmealarmStateModuleTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmealarmStateModuleTemp.setStatus("mandatory")


class _LmelabelFanCurrent_Type(DisplayString):
    """Custom type lmelabelFanCurrent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_LmelabelFanCurrent_Type.__name__ = "DisplayString"
_LmelabelFanCurrent_Object = MibTableColumn
lmelabelFanCurrent = _LmelabelFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 2, 1, 90),
    _LmelabelFanCurrent_Type()
)
lmelabelFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmelabelFanCurrent.setStatus("optional")


class _LmeuomFanCurrent_Type(DisplayString):
    """Custom type lmeuomFanCurrent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_LmeuomFanCurrent_Type.__name__ = "DisplayString"
_LmeuomFanCurrent_Object = MibTableColumn
lmeuomFanCurrent = _LmeuomFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 2, 1, 91),
    _LmeuomFanCurrent_Type()
)
lmeuomFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmeuomFanCurrent.setStatus("optional")
_LmemajorHighFanCurrent_Type = Float
_LmemajorHighFanCurrent_Object = MibTableColumn
lmemajorHighFanCurrent = _LmemajorHighFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 2, 1, 92),
    _LmemajorHighFanCurrent_Type()
)
lmemajorHighFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmemajorHighFanCurrent.setStatus("mandatory")
_LmemajorLowFanCurrent_Type = Float
_LmemajorLowFanCurrent_Object = MibTableColumn
lmemajorLowFanCurrent = _LmemajorLowFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 2, 1, 93),
    _LmemajorLowFanCurrent_Type()
)
lmemajorLowFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmemajorLowFanCurrent.setStatus("mandatory")
_LmeminorHighFanCurrent_Type = Float
_LmeminorHighFanCurrent_Object = MibTableColumn
lmeminorHighFanCurrent = _LmeminorHighFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 2, 1, 94),
    _LmeminorHighFanCurrent_Type()
)
lmeminorHighFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmeminorHighFanCurrent.setStatus("mandatory")
_LmeminorLowFanCurrent_Type = Float
_LmeminorLowFanCurrent_Object = MibTableColumn
lmeminorLowFanCurrent = _LmeminorLowFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 2, 1, 95),
    _LmeminorLowFanCurrent_Type()
)
lmeminorLowFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmeminorLowFanCurrent.setStatus("mandatory")
_LmecurrentValueFanCurrent_Type = Float
_LmecurrentValueFanCurrent_Object = MibTableColumn
lmecurrentValueFanCurrent = _LmecurrentValueFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 2, 1, 96),
    _LmecurrentValueFanCurrent_Type()
)
lmecurrentValueFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmecurrentValueFanCurrent.setStatus("mandatory")


class _LmestateFlagFanCurrent_Type(Integer32):
    """Custom type lmestateFlagFanCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hidden", 1),
          ("read-only", 2),
          ("updateable", 3))
    )


_LmestateFlagFanCurrent_Type.__name__ = "Integer32"
_LmestateFlagFanCurrent_Object = MibTableColumn
lmestateFlagFanCurrent = _LmestateFlagFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 2, 1, 97),
    _LmestateFlagFanCurrent_Type()
)
lmestateFlagFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmestateFlagFanCurrent.setStatus("mandatory")
_LmeminValueFanCurrent_Type = Float
_LmeminValueFanCurrent_Object = MibTableColumn
lmeminValueFanCurrent = _LmeminValueFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 2, 1, 98),
    _LmeminValueFanCurrent_Type()
)
lmeminValueFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmeminValueFanCurrent.setStatus("mandatory")
_LmemaxValueFanCurrent_Type = Float
_LmemaxValueFanCurrent_Object = MibTableColumn
lmemaxValueFanCurrent = _LmemaxValueFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 2, 1, 99),
    _LmemaxValueFanCurrent_Type()
)
lmemaxValueFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmemaxValueFanCurrent.setStatus("mandatory")


class _LmealarmStateFanCurrent_Type(Integer32):
    """Custom type lmealarmStateFanCurrent based on Integer32"""
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
        *(("informational", 6),
          ("majorHighAlarm", 5),
          ("majorLowAlarm", 2),
          ("minorHighAlarm", 4),
          ("minorLowAlarm", 3),
          ("noAlarm", 1))
    )


_LmealarmStateFanCurrent_Type.__name__ = "Integer32"
_LmealarmStateFanCurrent_Object = MibTableColumn
lmealarmStateFanCurrent = _LmealarmStateFanCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 2, 1, 100),
    _LmealarmStateFanCurrent_Type()
)
lmealarmStateFanCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmealarmStateFanCurrent.setStatus("mandatory")


class _Lmelabel12Volt_Type(DisplayString):
    """Custom type lmelabel12Volt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Lmelabel12Volt_Type.__name__ = "DisplayString"
_Lmelabel12Volt_Object = MibTableColumn
lmelabel12Volt = _Lmelabel12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 2, 1, 101),
    _Lmelabel12Volt_Type()
)
lmelabel12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmelabel12Volt.setStatus("optional")


class _Lmeuom12Volt_Type(DisplayString):
    """Custom type lmeuom12Volt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Lmeuom12Volt_Type.__name__ = "DisplayString"
_Lmeuom12Volt_Object = MibTableColumn
lmeuom12Volt = _Lmeuom12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 2, 1, 102),
    _Lmeuom12Volt_Type()
)
lmeuom12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmeuom12Volt.setStatus("optional")
_LmemajorHigh12Volt_Type = Float
_LmemajorHigh12Volt_Object = MibTableColumn
lmemajorHigh12Volt = _LmemajorHigh12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 2, 1, 103),
    _LmemajorHigh12Volt_Type()
)
lmemajorHigh12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmemajorHigh12Volt.setStatus("mandatory")
_LmemajorLow12Volt_Type = Float
_LmemajorLow12Volt_Object = MibTableColumn
lmemajorLow12Volt = _LmemajorLow12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 2, 1, 104),
    _LmemajorLow12Volt_Type()
)
lmemajorLow12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmemajorLow12Volt.setStatus("mandatory")
_LmeminorHigh12Volt_Type = Float
_LmeminorHigh12Volt_Object = MibTableColumn
lmeminorHigh12Volt = _LmeminorHigh12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 2, 1, 105),
    _LmeminorHigh12Volt_Type()
)
lmeminorHigh12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmeminorHigh12Volt.setStatus("mandatory")
_LmeminorLow12Volt_Type = Float
_LmeminorLow12Volt_Object = MibTableColumn
lmeminorLow12Volt = _LmeminorLow12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 2, 1, 106),
    _LmeminorLow12Volt_Type()
)
lmeminorLow12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmeminorLow12Volt.setStatus("mandatory")
_LmecurrentValue12Volt_Type = Float
_LmecurrentValue12Volt_Object = MibTableColumn
lmecurrentValue12Volt = _LmecurrentValue12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 2, 1, 107),
    _LmecurrentValue12Volt_Type()
)
lmecurrentValue12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmecurrentValue12Volt.setStatus("mandatory")


class _LmestateFlag12Volt_Type(Integer32):
    """Custom type lmestateFlag12Volt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hidden", 1),
          ("read-only", 2),
          ("updateable", 3))
    )


_LmestateFlag12Volt_Type.__name__ = "Integer32"
_LmestateFlag12Volt_Object = MibTableColumn
lmestateFlag12Volt = _LmestateFlag12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 2, 1, 108),
    _LmestateFlag12Volt_Type()
)
lmestateFlag12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmestateFlag12Volt.setStatus("mandatory")
_LmeminValue12Volt_Type = Float
_LmeminValue12Volt_Object = MibTableColumn
lmeminValue12Volt = _LmeminValue12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 2, 1, 109),
    _LmeminValue12Volt_Type()
)
lmeminValue12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmeminValue12Volt.setStatus("mandatory")
_LmemaxValue12Volt_Type = Float
_LmemaxValue12Volt_Object = MibTableColumn
lmemaxValue12Volt = _LmemaxValue12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 2, 1, 110),
    _LmemaxValue12Volt_Type()
)
lmemaxValue12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmemaxValue12Volt.setStatus("mandatory")


class _LmealarmState12Volt_Type(Integer32):
    """Custom type lmealarmState12Volt based on Integer32"""
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
        *(("informational", 6),
          ("majorHighAlarm", 5),
          ("majorLowAlarm", 2),
          ("minorHighAlarm", 4),
          ("minorLowAlarm", 3),
          ("noAlarm", 1))
    )


_LmealarmState12Volt_Type.__name__ = "Integer32"
_LmealarmState12Volt_Object = MibTableColumn
lmealarmState12Volt = _LmealarmState12Volt_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 2, 1, 111),
    _LmealarmState12Volt_Type()
)
lmealarmState12Volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmealarmState12Volt.setStatus("mandatory")
_Gx2lmeDigitalTable_Object = MibTable
gx2lmeDigitalTable = _Gx2lmeDigitalTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 3)
)
if mibBuilder.loadTexts:
    gx2lmeDigitalTable.setStatus("mandatory")
_Gx2lmeDigitalEntry_Object = MibTableRow
gx2lmeDigitalEntry = _Gx2lmeDigitalEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 3, 2)
)
gx2lmeDigitalEntry.setIndexNames(
    (0, "OMNI-gx2LME-MIB", "gx2lmeDigitalTableIndex"),
)
if mibBuilder.loadTexts:
    gx2lmeDigitalEntry.setStatus("mandatory")


class _Gx2lmeDigitalTableIndex_Type(Integer32):
    """Custom type gx2lmeDigitalTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Gx2lmeDigitalTableIndex_Type.__name__ = "Integer32"
_Gx2lmeDigitalTableIndex_Object = MibTableColumn
gx2lmeDigitalTableIndex = _Gx2lmeDigitalTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 3, 2, 1),
    _Gx2lmeDigitalTableIndex_Type()
)
gx2lmeDigitalTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gx2lmeDigitalTableIndex.setStatus("mandatory")


class _LmelabelRfInput_Type(DisplayString):
    """Custom type lmelabelRfInput based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_LmelabelRfInput_Type.__name__ = "DisplayString"
_LmelabelRfInput_Object = MibTableColumn
lmelabelRfInput = _LmelabelRfInput_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 3, 2, 2),
    _LmelabelRfInput_Type()
)
lmelabelRfInput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmelabelRfInput.setStatus("optional")


class _LmeenumRfInput_Type(DisplayString):
    """Custom type lmeenumRfInput based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_LmeenumRfInput_Type.__name__ = "DisplayString"
_LmeenumRfInput_Object = MibTableColumn
lmeenumRfInput = _LmeenumRfInput_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 3, 2, 3),
    _LmeenumRfInput_Type()
)
lmeenumRfInput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmeenumRfInput.setStatus("optional")


class _LmevalueRfInput_Type(Integer32):
    """Custom type lmevalueRfInput based on Integer32"""
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


_LmevalueRfInput_Type.__name__ = "Integer32"
_LmevalueRfInput_Object = MibTableColumn
lmevalueRfInput = _LmevalueRfInput_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 3, 2, 4),
    _LmevalueRfInput_Type()
)
lmevalueRfInput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lmevalueRfInput.setStatus("mandatory")


class _LmestateflagRfInput_Type(Integer32):
    """Custom type lmestateflagRfInput based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hidden", 1),
          ("read-only", 2),
          ("updateable", 3))
    )


_LmestateflagRfInput_Type.__name__ = "Integer32"
_LmestateflagRfInput_Object = MibTableColumn
lmestateflagRfInput = _LmestateflagRfInput_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 3, 2, 5),
    _LmestateflagRfInput_Type()
)
lmestateflagRfInput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmestateflagRfInput.setStatus("mandatory")


class _LmelabelOptOutput_Type(DisplayString):
    """Custom type lmelabelOptOutput based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_LmelabelOptOutput_Type.__name__ = "DisplayString"
_LmelabelOptOutput_Object = MibTableColumn
lmelabelOptOutput = _LmelabelOptOutput_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 3, 2, 6),
    _LmelabelOptOutput_Type()
)
lmelabelOptOutput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmelabelOptOutput.setStatus("optional")


class _LmeenumOptOutput_Type(DisplayString):
    """Custom type lmeenumOptOutput based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_LmeenumOptOutput_Type.__name__ = "DisplayString"
_LmeenumOptOutput_Object = MibTableColumn
lmeenumOptOutput = _LmeenumOptOutput_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 3, 2, 7),
    _LmeenumOptOutput_Type()
)
lmeenumOptOutput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmeenumOptOutput.setStatus("optional")


class _LmevalueOptOutput_Type(Integer32):
    """Custom type lmevalueOptOutput based on Integer32"""
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


_LmevalueOptOutput_Type.__name__ = "Integer32"
_LmevalueOptOutput_Object = MibTableColumn
lmevalueOptOutput = _LmevalueOptOutput_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 3, 2, 8),
    _LmevalueOptOutput_Type()
)
lmevalueOptOutput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lmevalueOptOutput.setStatus("mandatory")


class _LmestateflagOptOutput_Type(Integer32):
    """Custom type lmestateflagOptOutput based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hidden", 1),
          ("read-only", 2),
          ("updateable", 3))
    )


_LmestateflagOptOutput_Type.__name__ = "Integer32"
_LmestateflagOptOutput_Object = MibTableColumn
lmestateflagOptOutput = _LmestateflagOptOutput_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 3, 2, 9),
    _LmestateflagOptOutput_Type()
)
lmestateflagOptOutput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmestateflagOptOutput.setStatus("mandatory")


class _LmelabelLaserMode_Type(DisplayString):
    """Custom type lmelabelLaserMode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_LmelabelLaserMode_Type.__name__ = "DisplayString"
_LmelabelLaserMode_Object = MibTableColumn
lmelabelLaserMode = _LmelabelLaserMode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 3, 2, 10),
    _LmelabelLaserMode_Type()
)
lmelabelLaserMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmelabelLaserMode.setStatus("optional")


class _LmeenumLaserMode_Type(DisplayString):
    """Custom type lmeenumLaserMode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_LmeenumLaserMode_Type.__name__ = "DisplayString"
_LmeenumLaserMode_Object = MibTableColumn
lmeenumLaserMode = _LmeenumLaserMode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 3, 2, 11),
    _LmeenumLaserMode_Type()
)
lmeenumLaserMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmeenumLaserMode.setStatus("optional")


class _LmevalueLaserMode_Type(Integer32):
    """Custom type lmevalueLaserMode based on Integer32"""
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
        *(("manual", 4),
          ("manualEquate", 5),
          ("preset", 1),
          ("set", 2),
          ("setEquate", 3))
    )


_LmevalueLaserMode_Type.__name__ = "Integer32"
_LmevalueLaserMode_Object = MibTableColumn
lmevalueLaserMode = _LmevalueLaserMode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 3, 2, 12),
    _LmevalueLaserMode_Type()
)
lmevalueLaserMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lmevalueLaserMode.setStatus("mandatory")


class _LmestateflagLaserMode_Type(Integer32):
    """Custom type lmestateflagLaserMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hidden", 1),
          ("read-only", 2),
          ("updateable", 3))
    )


_LmestateflagLaserMode_Type.__name__ = "Integer32"
_LmestateflagLaserMode_Object = MibTableColumn
lmestateflagLaserMode = _LmestateflagLaserMode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 3, 2, 13),
    _LmestateflagLaserMode_Type()
)
lmestateflagLaserMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmestateflagLaserMode.setStatus("mandatory")


class _LmelabelLaserSecMode_Type(DisplayString):
    """Custom type lmelabelLaserSecMode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_LmelabelLaserSecMode_Type.__name__ = "DisplayString"
_LmelabelLaserSecMode_Object = MibTableColumn
lmelabelLaserSecMode = _LmelabelLaserSecMode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 3, 2, 14),
    _LmelabelLaserSecMode_Type()
)
lmelabelLaserSecMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmelabelLaserSecMode.setStatus("optional")


class _LmeenumLaserSecMode_Type(DisplayString):
    """Custom type lmeenumLaserSecMode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_LmeenumLaserSecMode_Type.__name__ = "DisplayString"
_LmeenumLaserSecMode_Object = MibTableColumn
lmeenumLaserSecMode = _LmeenumLaserSecMode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 3, 2, 15),
    _LmeenumLaserSecMode_Type()
)
lmeenumLaserSecMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmeenumLaserSecMode.setStatus("optional")


class _LmevalueLaserSecMode_Type(Integer32):
    """Custom type lmevalueLaserSecMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cw", 1),
          ("video", 2))
    )


_LmevalueLaserSecMode_Type.__name__ = "Integer32"
_LmevalueLaserSecMode_Object = MibTableColumn
lmevalueLaserSecMode = _LmevalueLaserSecMode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 3, 2, 16),
    _LmevalueLaserSecMode_Type()
)
lmevalueLaserSecMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lmevalueLaserSecMode.setStatus("mandatory")


class _LmestateflagLaserSecMode_Type(Integer32):
    """Custom type lmestateflagLaserSecMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hidden", 1),
          ("read-only", 2),
          ("updateable", 3))
    )


_LmestateflagLaserSecMode_Type.__name__ = "Integer32"
_LmestateflagLaserSecMode_Object = MibTableColumn
lmestateflagLaserSecMode = _LmestateflagLaserSecMode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 3, 2, 17),
    _LmestateflagLaserSecMode_Type()
)
lmestateflagLaserSecMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmestateflagLaserSecMode.setStatus("mandatory")


class _LmelabelVideoOffset_Type(DisplayString):
    """Custom type lmelabelVideoOffset based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_LmelabelVideoOffset_Type.__name__ = "DisplayString"
_LmelabelVideoOffset_Object = MibTableColumn
lmelabelVideoOffset = _LmelabelVideoOffset_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 3, 2, 18),
    _LmelabelVideoOffset_Type()
)
lmelabelVideoOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmelabelVideoOffset.setStatus("optional")


class _LmeenumVideoOffset_Type(DisplayString):
    """Custom type lmeenumVideoOffset based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_LmeenumVideoOffset_Type.__name__ = "DisplayString"
_LmeenumVideoOffset_Object = MibTableColumn
lmeenumVideoOffset = _LmeenumVideoOffset_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 3, 2, 19),
    _LmeenumVideoOffset_Type()
)
lmeenumVideoOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmeenumVideoOffset.setStatus("optional")


class _LmevalueVideoOffset_Type(Integer32):
    """Custom type lmevalueVideoOffset based on Integer32"""
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
        *(("minus2dB", 1),
          ("minus3dB", 2),
          ("minus4dB", 3),
          ("minus5dB", 4))
    )


_LmevalueVideoOffset_Type.__name__ = "Integer32"
_LmevalueVideoOffset_Object = MibTableColumn
lmevalueVideoOffset = _LmevalueVideoOffset_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 3, 2, 20),
    _LmevalueVideoOffset_Type()
)
lmevalueVideoOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lmevalueVideoOffset.setStatus("mandatory")


class _LmestateflagVideoOffset_Type(Integer32):
    """Custom type lmestateflagVideoOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hidden", 1),
          ("read-only", 2),
          ("updateable", 3))
    )


_LmestateflagVideoOffset_Type.__name__ = "Integer32"
_LmestateflagVideoOffset_Object = MibTableColumn
lmestateflagVideoOffset = _LmestateflagVideoOffset_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 3, 2, 21),
    _LmestateflagVideoOffset_Type()
)
lmestateflagVideoOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmestateflagVideoOffset.setStatus("mandatory")


class _LmelabelFactoryDefault_Type(DisplayString):
    """Custom type lmelabelFactoryDefault based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_LmelabelFactoryDefault_Type.__name__ = "DisplayString"
_LmelabelFactoryDefault_Object = MibTableColumn
lmelabelFactoryDefault = _LmelabelFactoryDefault_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 3, 2, 22),
    _LmelabelFactoryDefault_Type()
)
lmelabelFactoryDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmelabelFactoryDefault.setStatus("optional")


class _LmeenumFactoryDefault_Type(DisplayString):
    """Custom type lmeenumFactoryDefault based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_LmeenumFactoryDefault_Type.__name__ = "DisplayString"
_LmeenumFactoryDefault_Object = MibTableColumn
lmeenumFactoryDefault = _LmeenumFactoryDefault_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 3, 2, 23),
    _LmeenumFactoryDefault_Type()
)
lmeenumFactoryDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmeenumFactoryDefault.setStatus("optional")


class _LmevalueFactoryDefault_Type(Integer32):
    """Custom type lmevalueFactoryDefault based on Integer32"""
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


_LmevalueFactoryDefault_Type.__name__ = "Integer32"
_LmevalueFactoryDefault_Object = MibTableColumn
lmevalueFactoryDefault = _LmevalueFactoryDefault_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 3, 2, 24),
    _LmevalueFactoryDefault_Type()
)
lmevalueFactoryDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lmevalueFactoryDefault.setStatus("mandatory")


class _LmestateflagFactoryDefault_Type(Integer32):
    """Custom type lmestateflagFactoryDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hidden", 1),
          ("read-only", 2),
          ("updateable", 3))
    )


_LmestateflagFactoryDefault_Type.__name__ = "Integer32"
_LmestateflagFactoryDefault_Object = MibTableColumn
lmestateflagFactoryDefault = _LmestateflagFactoryDefault_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 3, 2, 25),
    _LmestateflagFactoryDefault_Type()
)
lmestateflagFactoryDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmestateflagFactoryDefault.setStatus("mandatory")


class _LmelabelFiberLength_Type(DisplayString):
    """Custom type lmelabelFiberLength based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_LmelabelFiberLength_Type.__name__ = "DisplayString"
_LmelabelFiberLength_Object = MibTableColumn
lmelabelFiberLength = _LmelabelFiberLength_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 3, 2, 26),
    _LmelabelFiberLength_Type()
)
lmelabelFiberLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmelabelFiberLength.setStatus("optional")


class _LmeenumFiberLength_Type(DisplayString):
    """Custom type lmeenumFiberLength based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_LmeenumFiberLength_Type.__name__ = "DisplayString"
_LmeenumFiberLength_Object = MibTableColumn
lmeenumFiberLength = _LmeenumFiberLength_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 3, 2, 27),
    _LmeenumFiberLength_Type()
)
lmeenumFiberLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmeenumFiberLength.setStatus("optional")


class _LmevalueFiberLength_Type(Integer32):
    """Custom type lmevalueFiberLength based on Integer32"""
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
              20)
        )
    )
    namedValues = NamedValues(
        *(("fl10km", 5),
          ("fl11km", 6),
          ("fl12km", 7),
          ("fl13km", 8),
          ("fl14km", 9),
          ("fl15km", 10),
          ("fl16km", 11),
          ("fl17km", 12),
          ("fl18km", 13),
          ("fl19km", 14),
          ("fl20km", 15),
          ("fl21km", 16),
          ("fl22km", 17),
          ("fl23km", 18),
          ("fl24km", 19),
          ("fl25km", 20),
          ("fl6km", 1),
          ("fl7km", 2),
          ("fl8km", 3),
          ("fl9km", 4))
    )


_LmevalueFiberLength_Type.__name__ = "Integer32"
_LmevalueFiberLength_Object = MibTableColumn
lmevalueFiberLength = _LmevalueFiberLength_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 3, 2, 28),
    _LmevalueFiberLength_Type()
)
lmevalueFiberLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lmevalueFiberLength.setStatus("mandatory")


class _LmestateflagFiberLength_Type(Integer32):
    """Custom type lmestateflagFiberLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hidden", 1),
          ("read-only", 2),
          ("updateable", 3))
    )


_LmestateflagFiberLength_Type.__name__ = "Integer32"
_LmestateflagFiberLength_Object = MibTableColumn
lmestateflagFiberLength = _LmestateflagFiberLength_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 3, 2, 29),
    _LmestateflagFiberLength_Type()
)
lmestateflagFiberLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmestateflagFiberLength.setStatus("mandatory")


class _LmelabelConditioningUnit_Type(DisplayString):
    """Custom type lmelabelConditioningUnit based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_LmelabelConditioningUnit_Type.__name__ = "DisplayString"
_LmelabelConditioningUnit_Object = MibTableColumn
lmelabelConditioningUnit = _LmelabelConditioningUnit_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 3, 2, 30),
    _LmelabelConditioningUnit_Type()
)
lmelabelConditioningUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmelabelConditioningUnit.setStatus("optional")


class _LmeenumConditioningUnit_Type(DisplayString):
    """Custom type lmeenumConditioningUnit based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_LmeenumConditioningUnit_Type.__name__ = "DisplayString"
_LmeenumConditioningUnit_Object = MibTableColumn
lmeenumConditioningUnit = _LmeenumConditioningUnit_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 3, 2, 31),
    _LmeenumConditioningUnit_Type()
)
lmeenumConditioningUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmeenumConditioningUnit.setStatus("optional")


class _LmevalueConditioningUnit_Type(Integer32):
    """Custom type lmevalueConditioningUnit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_LmevalueConditioningUnit_Type.__name__ = "Integer32"
_LmevalueConditioningUnit_Object = MibTableColumn
lmevalueConditioningUnit = _LmevalueConditioningUnit_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 3, 2, 32),
    _LmevalueConditioningUnit_Type()
)
lmevalueConditioningUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lmevalueConditioningUnit.setStatus("mandatory")


class _LmestateflagConditioningUnit_Type(Integer32):
    """Custom type lmestateflagConditioningUnit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hidden", 1),
          ("read-only", 2),
          ("updateable", 3))
    )


_LmestateflagConditioningUnit_Type.__name__ = "Integer32"
_LmestateflagConditioningUnit_Object = MibTableColumn
lmestateflagConditioningUnit = _LmestateflagConditioningUnit_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 3, 2, 33),
    _LmestateflagConditioningUnit_Type()
)
lmestateflagConditioningUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmestateflagConditioningUnit.setStatus("mandatory")
_Gx2lmeStatusTable_Object = MibTable
gx2lmeStatusTable = _Gx2lmeStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 4)
)
if mibBuilder.loadTexts:
    gx2lmeStatusTable.setStatus("mandatory")
_Gx2lmeStatusEntry_Object = MibTableRow
gx2lmeStatusEntry = _Gx2lmeStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 4, 3)
)
gx2lmeStatusEntry.setIndexNames(
    (0, "OMNI-gx2LME-MIB", "gx2lmeStatusTableIndex"),
)
if mibBuilder.loadTexts:
    gx2lmeStatusEntry.setStatus("mandatory")


class _Gx2lmeStatusTableIndex_Type(Integer32):
    """Custom type gx2lmeStatusTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Gx2lmeStatusTableIndex_Type.__name__ = "Integer32"
_Gx2lmeStatusTableIndex_Object = MibTableColumn
gx2lmeStatusTableIndex = _Gx2lmeStatusTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 4, 3, 1),
    _Gx2lmeStatusTableIndex_Type()
)
gx2lmeStatusTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gx2lmeStatusTableIndex.setStatus("mandatory")


class _LmelabelBoot_Type(DisplayString):
    """Custom type lmelabelBoot based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_LmelabelBoot_Type.__name__ = "DisplayString"
_LmelabelBoot_Object = MibTableColumn
lmelabelBoot = _LmelabelBoot_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 4, 3, 2),
    _LmelabelBoot_Type()
)
lmelabelBoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmelabelBoot.setStatus("optional")


class _LmevalueBoot_Type(Integer32):
    """Custom type lmevalueBoot based on Integer32"""
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
        *(("critical", 6),
          ("major", 5),
          ("minor", 4),
          ("ok", 1),
          ("undetermined", 2),
          ("warning", 3))
    )


_LmevalueBoot_Type.__name__ = "Integer32"
_LmevalueBoot_Object = MibTableColumn
lmevalueBoot = _LmevalueBoot_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 4, 3, 3),
    _LmevalueBoot_Type()
)
lmevalueBoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmevalueBoot.setStatus("mandatory")


class _LmestateflagBoot_Type(Integer32):
    """Custom type lmestateflagBoot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hidden", 1),
          ("read-only", 2),
          ("updateable", 3))
    )


_LmestateflagBoot_Type.__name__ = "Integer32"
_LmestateflagBoot_Object = MibTableColumn
lmestateflagBoot = _LmestateflagBoot_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 4, 3, 4),
    _LmestateflagBoot_Type()
)
lmestateflagBoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmestateflagBoot.setStatus("mandatory")


class _LmelabelFlash_Type(DisplayString):
    """Custom type lmelabelFlash based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_LmelabelFlash_Type.__name__ = "DisplayString"
_LmelabelFlash_Object = MibTableColumn
lmelabelFlash = _LmelabelFlash_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 4, 3, 5),
    _LmelabelFlash_Type()
)
lmelabelFlash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmelabelFlash.setStatus("optional")


class _LmevalueFlash_Type(Integer32):
    """Custom type lmevalueFlash based on Integer32"""
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
        *(("critical", 6),
          ("major", 5),
          ("minor", 4),
          ("ok", 1),
          ("undetermined", 2),
          ("warning", 3))
    )


_LmevalueFlash_Type.__name__ = "Integer32"
_LmevalueFlash_Object = MibTableColumn
lmevalueFlash = _LmevalueFlash_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 4, 3, 6),
    _LmevalueFlash_Type()
)
lmevalueFlash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmevalueFlash.setStatus("mandatory")


class _LmestateflagFlash_Type(Integer32):
    """Custom type lmestateflagFlash based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hidden", 1),
          ("read-only", 2),
          ("updateable", 3))
    )


_LmestateflagFlash_Type.__name__ = "Integer32"
_LmestateflagFlash_Object = MibTableColumn
lmestateflagFlash = _LmestateflagFlash_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 4, 3, 7),
    _LmestateflagFlash_Type()
)
lmestateflagFlash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmestateflagFlash.setStatus("mandatory")


class _LmelabelFactoryDataCRC_Type(DisplayString):
    """Custom type lmelabelFactoryDataCRC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_LmelabelFactoryDataCRC_Type.__name__ = "DisplayString"
_LmelabelFactoryDataCRC_Object = MibTableColumn
lmelabelFactoryDataCRC = _LmelabelFactoryDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 4, 3, 8),
    _LmelabelFactoryDataCRC_Type()
)
lmelabelFactoryDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmelabelFactoryDataCRC.setStatus("optional")


class _LmevalueFactoryDataCRC_Type(Integer32):
    """Custom type lmevalueFactoryDataCRC based on Integer32"""
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
        *(("critical", 6),
          ("major", 5),
          ("minor", 4),
          ("ok", 1),
          ("undetermined", 2),
          ("warning", 3))
    )


_LmevalueFactoryDataCRC_Type.__name__ = "Integer32"
_LmevalueFactoryDataCRC_Object = MibTableColumn
lmevalueFactoryDataCRC = _LmevalueFactoryDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 4, 3, 9),
    _LmevalueFactoryDataCRC_Type()
)
lmevalueFactoryDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmevalueFactoryDataCRC.setStatus("mandatory")


class _LmestateflagFactoryDataCRC_Type(Integer32):
    """Custom type lmestateflagFactoryDataCRC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hidden", 1),
          ("read-only", 2),
          ("updateable", 3))
    )


_LmestateflagFactoryDataCRC_Type.__name__ = "Integer32"
_LmestateflagFactoryDataCRC_Object = MibTableColumn
lmestateflagFactoryDataCRC = _LmestateflagFactoryDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 4, 3, 10),
    _LmestateflagFactoryDataCRC_Type()
)
lmestateflagFactoryDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmestateflagFactoryDataCRC.setStatus("mandatory")


class _LmelabelLaserDataCRC_Type(DisplayString):
    """Custom type lmelabelLaserDataCRC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_LmelabelLaserDataCRC_Type.__name__ = "DisplayString"
_LmelabelLaserDataCRC_Object = MibTableColumn
lmelabelLaserDataCRC = _LmelabelLaserDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 4, 3, 11),
    _LmelabelLaserDataCRC_Type()
)
lmelabelLaserDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmelabelLaserDataCRC.setStatus("optional")


class _LmevalueLaserDataCRC_Type(Integer32):
    """Custom type lmevalueLaserDataCRC based on Integer32"""
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
        *(("critical", 6),
          ("major", 5),
          ("minor", 4),
          ("ok", 1),
          ("undetermined", 2),
          ("warning", 3))
    )


_LmevalueLaserDataCRC_Type.__name__ = "Integer32"
_LmevalueLaserDataCRC_Object = MibTableColumn
lmevalueLaserDataCRC = _LmevalueLaserDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 4, 3, 12),
    _LmevalueLaserDataCRC_Type()
)
lmevalueLaserDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmevalueLaserDataCRC.setStatus("mandatory")


class _LmestateflagLaserDataCRC_Type(Integer32):
    """Custom type lmestateflagLaserDataCRC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hidden", 1),
          ("read-only", 2),
          ("updateable", 3))
    )


_LmestateflagLaserDataCRC_Type.__name__ = "Integer32"
_LmestateflagLaserDataCRC_Object = MibTableColumn
lmestateflagLaserDataCRC = _LmestateflagLaserDataCRC_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 4, 3, 13),
    _LmestateflagLaserDataCRC_Type()
)
lmestateflagLaserDataCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmestateflagLaserDataCRC.setStatus("mandatory")


class _LmelabelAlarmDataCrc_Type(DisplayString):
    """Custom type lmelabelAlarmDataCrc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_LmelabelAlarmDataCrc_Type.__name__ = "DisplayString"
_LmelabelAlarmDataCrc_Object = MibTableColumn
lmelabelAlarmDataCrc = _LmelabelAlarmDataCrc_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 4, 3, 14),
    _LmelabelAlarmDataCrc_Type()
)
lmelabelAlarmDataCrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmelabelAlarmDataCrc.setStatus("optional")


class _LmevalueAlarmDataCrc_Type(Integer32):
    """Custom type lmevalueAlarmDataCrc based on Integer32"""
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
        *(("critical", 6),
          ("major", 5),
          ("minor", 4),
          ("ok", 1),
          ("undetermined", 2),
          ("warning", 3))
    )


_LmevalueAlarmDataCrc_Type.__name__ = "Integer32"
_LmevalueAlarmDataCrc_Object = MibTableColumn
lmevalueAlarmDataCrc = _LmevalueAlarmDataCrc_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 4, 3, 15),
    _LmevalueAlarmDataCrc_Type()
)
lmevalueAlarmDataCrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmevalueAlarmDataCrc.setStatus("mandatory")


class _LmestateflagAlarmDataCrc_Type(Integer32):
    """Custom type lmestateflagAlarmDataCrc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hidden", 1),
          ("read-only", 2),
          ("updateable", 3))
    )


_LmestateflagAlarmDataCrc_Type.__name__ = "Integer32"
_LmestateflagAlarmDataCrc_Object = MibTableColumn
lmestateflagAlarmDataCrc = _LmestateflagAlarmDataCrc_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 4, 3, 16),
    _LmestateflagAlarmDataCrc_Type()
)
lmestateflagAlarmDataCrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmestateflagAlarmDataCrc.setStatus("mandatory")


class _LmelabelHWStatus_Type(DisplayString):
    """Custom type lmelabelHWStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_LmelabelHWStatus_Type.__name__ = "DisplayString"
_LmelabelHWStatus_Object = MibTableColumn
lmelabelHWStatus = _LmelabelHWStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 4, 3, 17),
    _LmelabelHWStatus_Type()
)
lmelabelHWStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmelabelHWStatus.setStatus("optional")


class _LmevalueHWStatus_Type(Integer32):
    """Custom type lmevalueHWStatus based on Integer32"""
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
        *(("critical", 6),
          ("major", 5),
          ("minor", 4),
          ("ok", 1),
          ("undetermined", 2),
          ("warning", 3))
    )


_LmevalueHWStatus_Type.__name__ = "Integer32"
_LmevalueHWStatus_Object = MibTableColumn
lmevalueHWStatus = _LmevalueHWStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 4, 3, 18),
    _LmevalueHWStatus_Type()
)
lmevalueHWStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmevalueHWStatus.setStatus("mandatory")


class _LmestateflagHWStatus_Type(Integer32):
    """Custom type lmestateflagHWStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hidden", 1),
          ("read-only", 2),
          ("updateable", 3))
    )


_LmestateflagHWStatus_Type.__name__ = "Integer32"
_LmestateflagHWStatus_Object = MibTableColumn
lmestateflagHWStatus = _LmestateflagHWStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 4, 3, 19),
    _LmestateflagHWStatus_Type()
)
lmestateflagHWStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmestateflagHWStatus.setStatus("mandatory")


class _LmelabelRFInputStatus_Type(DisplayString):
    """Custom type lmelabelRFInputStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_LmelabelRFInputStatus_Type.__name__ = "DisplayString"
_LmelabelRFInputStatus_Object = MibTableColumn
lmelabelRFInputStatus = _LmelabelRFInputStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 4, 3, 20),
    _LmelabelRFInputStatus_Type()
)
lmelabelRFInputStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmelabelRFInputStatus.setStatus("optional")


class _LmevalueRFInputStatus_Type(Integer32):
    """Custom type lmevalueRFInputStatus based on Integer32"""
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
        *(("critical", 6),
          ("major", 5),
          ("minor", 4),
          ("ok", 1),
          ("undetermined", 2),
          ("warning", 3))
    )


_LmevalueRFInputStatus_Type.__name__ = "Integer32"
_LmevalueRFInputStatus_Object = MibTableColumn
lmevalueRFInputStatus = _LmevalueRFInputStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 4, 3, 21),
    _LmevalueRFInputStatus_Type()
)
lmevalueRFInputStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmevalueRFInputStatus.setStatus("mandatory")


class _LmestateflagRFInputStatus_Type(Integer32):
    """Custom type lmestateflagRFInputStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hidden", 1),
          ("read-only", 2),
          ("updateable", 3))
    )


_LmestateflagRFInputStatus_Type.__name__ = "Integer32"
_LmestateflagRFInputStatus_Object = MibTableColumn
lmestateflagRFInputStatus = _LmestateflagRFInputStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 4, 3, 22),
    _LmestateflagRFInputStatus_Type()
)
lmestateflagRFInputStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmestateflagRFInputStatus.setStatus("mandatory")
_Gx2lmeFactoryTable_Object = MibTable
gx2lmeFactoryTable = _Gx2lmeFactoryTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 5)
)
if mibBuilder.loadTexts:
    gx2lmeFactoryTable.setStatus("mandatory")
_Gx2lmeFactoryEntry_Object = MibTableRow
gx2lmeFactoryEntry = _Gx2lmeFactoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 5, 4)
)
gx2lmeFactoryEntry.setIndexNames(
    (0, "OMNI-gx2LME-MIB", "gx2lmeFactoryTableIndex"),
)
if mibBuilder.loadTexts:
    gx2lmeFactoryEntry.setStatus("mandatory")


class _Gx2lmeFactoryTableIndex_Type(Integer32):
    """Custom type gx2lmeFactoryTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Gx2lmeFactoryTableIndex_Type.__name__ = "Integer32"
_Gx2lmeFactoryTableIndex_Object = MibTableColumn
gx2lmeFactoryTableIndex = _Gx2lmeFactoryTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 5, 4, 1),
    _Gx2lmeFactoryTableIndex_Type()
)
gx2lmeFactoryTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gx2lmeFactoryTableIndex.setStatus("mandatory")
_LmebootControlByteValue_Type = Integer32
_LmebootControlByteValue_Object = MibTableColumn
lmebootControlByteValue = _LmebootControlByteValue_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 5, 4, 2),
    _LmebootControlByteValue_Type()
)
lmebootControlByteValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmebootControlByteValue.setStatus("mandatory")
_LmebootStatusByteValue_Type = Integer32
_LmebootStatusByteValue_Object = MibTableColumn
lmebootStatusByteValue = _LmebootStatusByteValue_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 5, 4, 3),
    _LmebootStatusByteValue_Type()
)
lmebootStatusByteValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmebootStatusByteValue.setStatus("mandatory")
_Lmebank1CRCValue_Type = Integer32
_Lmebank1CRCValue_Object = MibTableColumn
lmebank1CRCValue = _Lmebank1CRCValue_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 5, 4, 4),
    _Lmebank1CRCValue_Type()
)
lmebank1CRCValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmebank1CRCValue.setStatus("mandatory")
_Lmebank2CRCValue_Type = Integer32
_Lmebank2CRCValue_Object = MibTableColumn
lmebank2CRCValue = _Lmebank2CRCValue_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 5, 4, 5),
    _Lmebank2CRCValue_Type()
)
lmebank2CRCValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmebank2CRCValue.setStatus("mandatory")
_LmeprgEEPROMByteValue_Type = Integer32
_LmeprgEEPROMByteValue_Object = MibTableColumn
lmeprgEEPROMByteValue = _LmeprgEEPROMByteValue_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 5, 4, 6),
    _LmeprgEEPROMByteValue_Type()
)
lmeprgEEPROMByteValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmeprgEEPROMByteValue.setStatus("mandatory")
_LmefactoryCRCValue_Type = Integer32
_LmefactoryCRCValue_Object = MibTableColumn
lmefactoryCRCValue = _LmefactoryCRCValue_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 5, 4, 7),
    _LmefactoryCRCValue_Type()
)
lmefactoryCRCValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmefactoryCRCValue.setStatus("mandatory")


class _LmecalculateCRCValue_Type(Integer32):
    """Custom type lmecalculateCRCValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 3),
          ("factory", 1),
          ("laserData", 2))
    )


_LmecalculateCRCValue_Type.__name__ = "Integer32"
_LmecalculateCRCValue_Object = MibTableColumn
lmecalculateCRCValue = _LmecalculateCRCValue_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 5, 4, 8),
    _LmecalculateCRCValue_Type()
)
lmecalculateCRCValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmecalculateCRCValue.setStatus("mandatory")
_LmehourMeterValue_Type = Integer32
_LmehourMeterValue_Object = MibTableColumn
lmehourMeterValue = _LmehourMeterValue_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 5, 4, 9),
    _LmehourMeterValue_Type()
)
lmehourMeterValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmehourMeterValue.setStatus("mandatory")
_LmeflashPrgCntAValue_Type = Integer32
_LmeflashPrgCntAValue_Object = MibTableColumn
lmeflashPrgCntAValue = _LmeflashPrgCntAValue_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 5, 4, 10),
    _LmeflashPrgCntAValue_Type()
)
lmeflashPrgCntAValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmeflashPrgCntAValue.setStatus("mandatory")
_LmeflashPrgCntBValue_Type = Integer32
_LmeflashPrgCntBValue_Object = MibTableColumn
lmeflashPrgCntBValue = _LmeflashPrgCntBValue_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 5, 4, 11),
    _LmeflashPrgCntBValue_Type()
)
lmeflashPrgCntBValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmeflashPrgCntBValue.setStatus("mandatory")


class _LmeflashBankARevValue_Type(DisplayString):
    """Custom type lmeflashBankARevValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_LmeflashBankARevValue_Type.__name__ = "DisplayString"
_LmeflashBankARevValue_Object = MibTableColumn
lmeflashBankARevValue = _LmeflashBankARevValue_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 5, 4, 12),
    _LmeflashBankARevValue_Type()
)
lmeflashBankARevValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmeflashBankARevValue.setStatus("mandatory")


class _LmeflashBankBRevValue_Type(DisplayString):
    """Custom type lmeflashBankBRevValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_LmeflashBankBRevValue_Type.__name__ = "DisplayString"
_LmeflashBankBRevValue_Object = MibTableColumn
lmeflashBankBRevValue = _LmeflashBankBRevValue_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 5, 4, 13),
    _LmeflashBankBRevValue_Type()
)
lmeflashBankBRevValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmeflashBankBRevValue.setStatus("mandatory")
_Gx2Lm1000EHoldTimeTable_Object = MibTable
gx2Lm1000EHoldTimeTable = _Gx2Lm1000EHoldTimeTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 6)
)
if mibBuilder.loadTexts:
    gx2Lm1000EHoldTimeTable.setStatus("mandatory")
_Gx2Lm1000EHoldTimeEntry_Object = MibTableRow
gx2Lm1000EHoldTimeEntry = _Gx2Lm1000EHoldTimeEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 6, 5)
)
gx2Lm1000EHoldTimeEntry.setIndexNames(
    (0, "OMNI-gx2LME-MIB", "gx2Lm1000EHoldTimeTableIndex"),
    (0, "OMNI-gx2LME-MIB", "gx2Lm1000EHoldTimeSpecIndex"),
)
if mibBuilder.loadTexts:
    gx2Lm1000EHoldTimeEntry.setStatus("mandatory")


class _Gx2Lm1000EHoldTimeTableIndex_Type(Integer32):
    """Custom type gx2Lm1000EHoldTimeTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Gx2Lm1000EHoldTimeTableIndex_Type.__name__ = "Integer32"
_Gx2Lm1000EHoldTimeTableIndex_Object = MibTableColumn
gx2Lm1000EHoldTimeTableIndex = _Gx2Lm1000EHoldTimeTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 6, 5, 1),
    _Gx2Lm1000EHoldTimeTableIndex_Type()
)
gx2Lm1000EHoldTimeTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gx2Lm1000EHoldTimeTableIndex.setStatus("mandatory")


class _Gx2Lm1000EHoldTimeSpecIndex_Type(Integer32):
    """Custom type gx2Lm1000EHoldTimeSpecIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Gx2Lm1000EHoldTimeSpecIndex_Type.__name__ = "Integer32"
_Gx2Lm1000EHoldTimeSpecIndex_Object = MibTableColumn
gx2Lm1000EHoldTimeSpecIndex = _Gx2Lm1000EHoldTimeSpecIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 6, 5, 2),
    _Gx2Lm1000EHoldTimeSpecIndex_Type()
)
gx2Lm1000EHoldTimeSpecIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gx2Lm1000EHoldTimeSpecIndex.setStatus("mandatory")
_Gx2Lm1000EHoldTimeData_Type = Integer32
_Gx2Lm1000EHoldTimeData_Object = MibTableColumn
gx2Lm1000EHoldTimeData = _Gx2Lm1000EHoldTimeData_Object(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 6, 5, 3),
    _Gx2Lm1000EHoldTimeData_Type()
)
gx2Lm1000EHoldTimeData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gx2Lm1000EHoldTimeData.setStatus("mandatory")

# Managed Objects groups


# Notification objects

trapLMEConfigChangeInteger = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 0, 1)
)
trapLMEConfigChangeInteger.setObjects(
      *(("NLSBBN-TRAPS-MIB", "trapIdentifier"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemModelNumber"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemSerialNum"),
        ("NLSBBN-TRAPS-MIB", "trapPerceivedSeverity"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemOperState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAlarmStatus"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAdminState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAvailStatus"),
        ("NLSBBN-TRAPS-MIB", "trapText"),
        ("NLSBBN-TRAPS-MIB", "trapChangedObjectId"),
        ("NLSBBN-TRAPS-MIB", "trapChangedValueInteger"),
        ("NLSBBN-TRAPS-MIB", "trapNETrapLastTrapTimeStamp"))
)
if mibBuilder.loadTexts:
    trapLMEConfigChangeInteger.setStatus(
        ""
    )

trapLMEConfigChangeDisplayString = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 0, 2)
)
trapLMEConfigChangeDisplayString.setObjects(
      *(("NLSBBN-TRAPS-MIB", "trapIdentifier"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemModelNumber"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemSerialNum"),
        ("NLSBBN-TRAPS-MIB", "trapPerceivedSeverity"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemOperState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAlarmStatus"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAdminState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAvailStatus"),
        ("NLSBBN-TRAPS-MIB", "trapText"),
        ("NLSBBN-TRAPS-MIB", "trapChangedObjectId"),
        ("NLSBBN-TRAPS-MIB", "trapChangedValueDisplayString"),
        ("NLSBBN-TRAPS-MIB", "trapNETrapLastTrapTimeStamp"))
)
if mibBuilder.loadTexts:
    trapLMEConfigChangeDisplayString.setStatus(
        ""
    )

trapLMERFInputAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 0, 3)
)
trapLMERFInputAlarm.setObjects(
      *(("NLSBBN-TRAPS-MIB", "trapIdentifier"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemModelNumber"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemSerialNum"),
        ("NLSBBN-TRAPS-MIB", "trapPerceivedSeverity"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemOperState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAlarmStatus"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAdminState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAvailStatus"),
        ("NLSBBN-TRAPS-MIB", "trapText"),
        ("NLSBBN-TRAPS-MIB", "trapChangedObjectId"),
        ("NLSBBN-TRAPS-MIB", "trapChangedValueInteger"),
        ("NLSBBN-TRAPS-MIB", "trapNETrapLastTrapTimeStamp"))
)
if mibBuilder.loadTexts:
    trapLMERFInputAlarm.setStatus(
        ""
    )

trapLMERFOverloadAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 0, 4)
)
trapLMERFOverloadAlarm.setObjects(
      *(("NLSBBN-TRAPS-MIB", "trapIdentifier"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemModelNumber"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemSerialNum"),
        ("NLSBBN-TRAPS-MIB", "trapPerceivedSeverity"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemOperState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAlarmStatus"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAdminState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAvailStatus"),
        ("NLSBBN-TRAPS-MIB", "trapText"),
        ("NLSBBN-TRAPS-MIB", "trapChangedObjectId"),
        ("NLSBBN-TRAPS-MIB", "trapChangedValueInteger"),
        ("NLSBBN-TRAPS-MIB", "trapNETrapLastTrapTimeStamp"))
)
if mibBuilder.loadTexts:
    trapLMERFOverloadAlarm.setStatus(
        ""
    )

trapLMERFOffsetAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 0, 5)
)
trapLMERFOffsetAlarm.setObjects(
      *(("NLSBBN-TRAPS-MIB", "trapIdentifier"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemModelNumber"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemSerialNum"),
        ("NLSBBN-TRAPS-MIB", "trapPerceivedSeverity"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemOperState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAlarmStatus"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAdminState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAvailStatus"),
        ("NLSBBN-TRAPS-MIB", "trapText"),
        ("NLSBBN-TRAPS-MIB", "trapChangedObjectId"),
        ("NLSBBN-TRAPS-MIB", "trapChangedValueInteger"),
        ("NLSBBN-TRAPS-MIB", "trapNETrapLastTrapTimeStamp"))
)
if mibBuilder.loadTexts:
    trapLMERFOffsetAlarm.setStatus(
        ""
    )

trapLMEOpticalPowerAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 0, 6)
)
trapLMEOpticalPowerAlarm.setObjects(
      *(("NLSBBN-TRAPS-MIB", "trapIdentifier"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemModelNumber"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemSerialNum"),
        ("NLSBBN-TRAPS-MIB", "trapPerceivedSeverity"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemOperState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAlarmStatus"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAdminState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAvailStatus"),
        ("NLSBBN-TRAPS-MIB", "trapText"),
        ("NLSBBN-TRAPS-MIB", "trapChangedObjectId"),
        ("NLSBBN-TRAPS-MIB", "trapChangedValueInteger"),
        ("NLSBBN-TRAPS-MIB", "trapNETrapLastTrapTimeStamp"))
)
if mibBuilder.loadTexts:
    trapLMEOpticalPowerAlarm.setStatus(
        ""
    )

trapLMELaserBiasAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 0, 7)
)
trapLMELaserBiasAlarm.setObjects(
      *(("NLSBBN-TRAPS-MIB", "trapIdentifier"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemModelNumber"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemSerialNum"),
        ("NLSBBN-TRAPS-MIB", "trapPerceivedSeverity"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemOperState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAlarmStatus"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAdminState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAvailStatus"),
        ("NLSBBN-TRAPS-MIB", "trapText"),
        ("NLSBBN-TRAPS-MIB", "trapChangedObjectId"),
        ("NLSBBN-TRAPS-MIB", "trapChangedValueInteger"),
        ("NLSBBN-TRAPS-MIB", "trapNETrapLastTrapTimeStamp"))
)
if mibBuilder.loadTexts:
    trapLMELaserBiasAlarm.setStatus(
        ""
    )

trapLMELaserTempAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 0, 8)
)
trapLMELaserTempAlarm.setObjects(
      *(("NLSBBN-TRAPS-MIB", "trapIdentifier"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemModelNumber"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemSerialNum"),
        ("NLSBBN-TRAPS-MIB", "trapPerceivedSeverity"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemOperState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAlarmStatus"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAdminState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAvailStatus"),
        ("NLSBBN-TRAPS-MIB", "trapText"),
        ("NLSBBN-TRAPS-MIB", "trapChangedObjectId"),
        ("NLSBBN-TRAPS-MIB", "trapChangedValueInteger"),
        ("NLSBBN-TRAPS-MIB", "trapNETrapLastTrapTimeStamp"))
)
if mibBuilder.loadTexts:
    trapLMELaserTempAlarm.setStatus(
        ""
    )

trapLMETECCurrentAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 0, 9)
)
trapLMETECCurrentAlarm.setObjects(
      *(("NLSBBN-TRAPS-MIB", "trapIdentifier"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemModelNumber"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemSerialNum"),
        ("NLSBBN-TRAPS-MIB", "trapPerceivedSeverity"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemOperState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAlarmStatus"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAdminState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAvailStatus"),
        ("NLSBBN-TRAPS-MIB", "trapText"),
        ("NLSBBN-TRAPS-MIB", "trapChangedObjectId"),
        ("NLSBBN-TRAPS-MIB", "trapChangedValueInteger"),
        ("NLSBBN-TRAPS-MIB", "trapNETrapLastTrapTimeStamp"))
)
if mibBuilder.loadTexts:
    trapLMETECCurrentAlarm.setStatus(
        ""
    )

trapLMEFanCurrentAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 0, 10)
)
trapLMEFanCurrentAlarm.setObjects(
      *(("NLSBBN-TRAPS-MIB", "trapIdentifier"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemModelNumber"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemSerialNum"),
        ("NLSBBN-TRAPS-MIB", "trapPerceivedSeverity"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemOperState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAlarmStatus"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAdminState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAvailStatus"),
        ("NLSBBN-TRAPS-MIB", "trapText"),
        ("NLSBBN-TRAPS-MIB", "trapChangedObjectId"),
        ("NLSBBN-TRAPS-MIB", "trapChangedValueInteger"),
        ("NLSBBN-TRAPS-MIB", "trapNETrapLastTrapTimeStamp"))
)
if mibBuilder.loadTexts:
    trapLMEFanCurrentAlarm.setStatus(
        ""
    )

trapLME12vAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 0, 11)
)
trapLME12vAlarm.setObjects(
      *(("NLSBBN-TRAPS-MIB", "trapIdentifier"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemModelNumber"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemSerialNum"),
        ("NLSBBN-TRAPS-MIB", "trapPerceivedSeverity"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemOperState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAlarmStatus"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAdminState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAvailStatus"),
        ("NLSBBN-TRAPS-MIB", "trapText"),
        ("NLSBBN-TRAPS-MIB", "trapChangedObjectId"),
        ("NLSBBN-TRAPS-MIB", "trapChangedValueInteger"),
        ("NLSBBN-TRAPS-MIB", "trapNETrapLastTrapTimeStamp"))
)
if mibBuilder.loadTexts:
    trapLME12vAlarm.setStatus(
        ""
    )

trapLMEModuleTempAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 0, 12)
)
trapLMEModuleTempAlarm.setObjects(
      *(("NLSBBN-TRAPS-MIB", "trapIdentifier"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemModelNumber"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemSerialNum"),
        ("NLSBBN-TRAPS-MIB", "trapPerceivedSeverity"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemOperState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAlarmStatus"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAdminState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAvailStatus"),
        ("NLSBBN-TRAPS-MIB", "trapText"),
        ("NLSBBN-TRAPS-MIB", "trapChangedObjectId"),
        ("NLSBBN-TRAPS-MIB", "trapChangedValueInteger"),
        ("NLSBBN-TRAPS-MIB", "trapNETrapLastTrapTimeStamp"))
)
if mibBuilder.loadTexts:
    trapLMEModuleTempAlarm.setStatus(
        ""
    )

trapLMEFlashAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 0, 13)
)
trapLMEFlashAlarm.setObjects(
      *(("NLSBBN-TRAPS-MIB", "trapIdentifier"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemModelNumber"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemSerialNum"),
        ("NLSBBN-TRAPS-MIB", "trapPerceivedSeverity"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemOperState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAlarmStatus"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAdminState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAvailStatus"),
        ("NLSBBN-TRAPS-MIB", "trapText"),
        ("NLSBBN-TRAPS-MIB", "trapChangedObjectId"),
        ("NLSBBN-TRAPS-MIB", "trapChangedValueInteger"),
        ("NLSBBN-TRAPS-MIB", "trapNETrapLastTrapTimeStamp"))
)
if mibBuilder.loadTexts:
    trapLMEFlashAlarm.setStatus(
        ""
    )

trapLMELaserBiasCntLoopAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 0, 14)
)
trapLMELaserBiasCntLoopAlarm.setObjects(
      *(("NLSBBN-TRAPS-MIB", "trapIdentifier"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemModelNumber"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemSerialNum"),
        ("NLSBBN-TRAPS-MIB", "trapPerceivedSeverity"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemOperState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAlarmStatus"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAdminState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAvailStatus"),
        ("NLSBBN-TRAPS-MIB", "trapText"),
        ("NLSBBN-TRAPS-MIB", "trapChangedObjectId"),
        ("NLSBBN-TRAPS-MIB", "trapChangedValueInteger"),
        ("NLSBBN-TRAPS-MIB", "trapNETrapLastTrapTimeStamp"))
)
if mibBuilder.loadTexts:
    trapLMELaserBiasCntLoopAlarm.setStatus(
        ""
    )

trapLMEBankBootAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 0, 15)
)
trapLMEBankBootAlarm.setObjects(
      *(("NLSBBN-TRAPS-MIB", "trapIdentifier"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemModelNumber"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemSerialNum"),
        ("NLSBBN-TRAPS-MIB", "trapPerceivedSeverity"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemOperState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAlarmStatus"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAdminState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAvailStatus"),
        ("NLSBBN-TRAPS-MIB", "trapText"),
        ("NLSBBN-TRAPS-MIB", "trapChangedObjectId"),
        ("NLSBBN-TRAPS-MIB", "trapChangedValueInteger"),
        ("NLSBBN-TRAPS-MIB", "trapNETrapLastTrapTimeStamp"))
)
if mibBuilder.loadTexts:
    trapLMEBankBootAlarm.setStatus(
        ""
    )

trapLMELaserBiasCntLoopInitAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 0, 16)
)
trapLMELaserBiasCntLoopInitAlarm.setObjects(
      *(("NLSBBN-TRAPS-MIB", "trapIdentifier"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemModelNumber"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemSerialNum"),
        ("NLSBBN-TRAPS-MIB", "trapPerceivedSeverity"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemOperState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAlarmStatus"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAdminState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAvailStatus"),
        ("NLSBBN-TRAPS-MIB", "trapText"),
        ("NLSBBN-TRAPS-MIB", "trapChangedObjectId"),
        ("NLSBBN-TRAPS-MIB", "trapChangedValueInteger"),
        ("NLSBBN-TRAPS-MIB", "trapNETrapLastTrapTimeStamp"))
)
if mibBuilder.loadTexts:
    trapLMELaserBiasCntLoopInitAlarm.setStatus(
        ""
    )

trapLMERFParamInitAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 0, 17)
)
trapLMERFParamInitAlarm.setObjects(
      *(("NLSBBN-TRAPS-MIB", "trapIdentifier"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemModelNumber"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemSerialNum"),
        ("NLSBBN-TRAPS-MIB", "trapPerceivedSeverity"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemOperState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAlarmStatus"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAdminState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAvailStatus"),
        ("NLSBBN-TRAPS-MIB", "trapText"),
        ("NLSBBN-TRAPS-MIB", "trapChangedObjectId"),
        ("NLSBBN-TRAPS-MIB", "trapChangedValueInteger"),
        ("NLSBBN-TRAPS-MIB", "trapNETrapLastTrapTimeStamp"))
)
if mibBuilder.loadTexts:
    trapLMERFParamInitAlarm.setStatus(
        ""
    )

trapLMETECParamInitAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 0, 18)
)
trapLMETECParamInitAlarm.setObjects(
      *(("NLSBBN-TRAPS-MIB", "trapIdentifier"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemModelNumber"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemSerialNum"),
        ("NLSBBN-TRAPS-MIB", "trapPerceivedSeverity"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemOperState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAlarmStatus"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAdminState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAvailStatus"),
        ("NLSBBN-TRAPS-MIB", "trapText"),
        ("NLSBBN-TRAPS-MIB", "trapChangedObjectId"),
        ("NLSBBN-TRAPS-MIB", "trapChangedValueInteger"),
        ("NLSBBN-TRAPS-MIB", "trapNETrapLastTrapTimeStamp"))
)
if mibBuilder.loadTexts:
    trapLMETECParamInitAlarm.setStatus(
        ""
    )

trapLMEAttnTableInitAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 0, 19)
)
trapLMEAttnTableInitAlarm.setObjects(
      *(("NLSBBN-TRAPS-MIB", "trapIdentifier"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemModelNumber"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemSerialNum"),
        ("NLSBBN-TRAPS-MIB", "trapPerceivedSeverity"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemOperState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAlarmStatus"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAdminState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAvailStatus"),
        ("NLSBBN-TRAPS-MIB", "trapText"),
        ("NLSBBN-TRAPS-MIB", "trapChangedObjectId"),
        ("NLSBBN-TRAPS-MIB", "trapChangedValueInteger"),
        ("NLSBBN-TRAPS-MIB", "trapNETrapLastTrapTimeStamp"))
)
if mibBuilder.loadTexts:
    trapLMEAttnTableInitAlarm.setStatus(
        ""
    )

trapLMEPowerMeterTableInitAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 0, 20)
)
trapLMEPowerMeterTableInitAlarm.setObjects(
      *(("NLSBBN-TRAPS-MIB", "trapIdentifier"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemModelNumber"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemSerialNum"),
        ("NLSBBN-TRAPS-MIB", "trapPerceivedSeverity"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemOperState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAlarmStatus"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAdminState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAvailStatus"),
        ("NLSBBN-TRAPS-MIB", "trapText"),
        ("NLSBBN-TRAPS-MIB", "trapChangedObjectId"),
        ("NLSBBN-TRAPS-MIB", "trapChangedValueInteger"),
        ("NLSBBN-TRAPS-MIB", "trapNETrapLastTrapTimeStamp"))
)
if mibBuilder.loadTexts:
    trapLMEPowerMeterTableInitAlarm.setStatus(
        ""
    )

trapLMELaserDataCRCAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 0, 21)
)
trapLMELaserDataCRCAlarm.setObjects(
      *(("NLSBBN-TRAPS-MIB", "trapIdentifier"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemModelNumber"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemSerialNum"),
        ("NLSBBN-TRAPS-MIB", "trapPerceivedSeverity"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemOperState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAlarmStatus"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAdminState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAvailStatus"),
        ("NLSBBN-TRAPS-MIB", "trapText"),
        ("NLSBBN-TRAPS-MIB", "trapChangedObjectId"),
        ("NLSBBN-TRAPS-MIB", "trapChangedValueInteger"),
        ("NLSBBN-TRAPS-MIB", "trapNETrapLastTrapTimeStamp"))
)
if mibBuilder.loadTexts:
    trapLMELaserDataCRCAlarm.setStatus(
        ""
    )

trapLMEAlarmDataCRCAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 0, 22)
)
trapLMEAlarmDataCRCAlarm.setObjects(
      *(("NLSBBN-TRAPS-MIB", "trapIdentifier"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemModelNumber"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemSerialNum"),
        ("NLSBBN-TRAPS-MIB", "trapPerceivedSeverity"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemOperState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAlarmStatus"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAdminState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAvailStatus"),
        ("NLSBBN-TRAPS-MIB", "trapText"),
        ("NLSBBN-TRAPS-MIB", "trapChangedObjectId"),
        ("NLSBBN-TRAPS-MIB", "trapChangedValueInteger"),
        ("NLSBBN-TRAPS-MIB", "trapNETrapLastTrapTimeStamp"))
)
if mibBuilder.loadTexts:
    trapLMEAlarmDataCRCAlarm.setStatus(
        ""
    )

trapLMEFactoryDataCRCAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 0, 23)
)
trapLMEFactoryDataCRCAlarm.setObjects(
      *(("NLSBBN-TRAPS-MIB", "trapIdentifier"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemModelNumber"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemSerialNum"),
        ("NLSBBN-TRAPS-MIB", "trapPerceivedSeverity"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemOperState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAlarmStatus"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAdminState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAvailStatus"),
        ("NLSBBN-TRAPS-MIB", "trapText"),
        ("NLSBBN-TRAPS-MIB", "trapChangedObjectId"),
        ("NLSBBN-TRAPS-MIB", "trapChangedValueInteger"),
        ("NLSBBN-TRAPS-MIB", "trapNETrapLastTrapTimeStamp"))
)
if mibBuilder.loadTexts:
    trapLMEFactoryDataCRCAlarm.setStatus(
        ""
    )

trapLMEUserRFOffAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 0, 24)
)
trapLMEUserRFOffAlarm.setObjects(
      *(("NLSBBN-TRAPS-MIB", "trapIdentifier"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemModelNumber"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemSerialNum"),
        ("NLSBBN-TRAPS-MIB", "trapPerceivedSeverity"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemOperState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAlarmStatus"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAdminState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAvailStatus"),
        ("NLSBBN-TRAPS-MIB", "trapText"),
        ("NLSBBN-TRAPS-MIB", "trapChangedObjectId"),
        ("NLSBBN-TRAPS-MIB", "trapChangedValueInteger"),
        ("NLSBBN-TRAPS-MIB", "trapNETrapLastTrapTimeStamp"))
)
if mibBuilder.loadTexts:
    trapLMEUserRFOffAlarm.setStatus(
        ""
    )

trapLMEUserOpticalOffAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 0, 25)
)
trapLMEUserOpticalOffAlarm.setObjects(
      *(("NLSBBN-TRAPS-MIB", "trapIdentifier"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemModelNumber"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemSerialNum"),
        ("NLSBBN-TRAPS-MIB", "trapPerceivedSeverity"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemOperState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAlarmStatus"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAdminState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAvailStatus"),
        ("NLSBBN-TRAPS-MIB", "trapText"),
        ("NLSBBN-TRAPS-MIB", "trapChangedObjectId"),
        ("NLSBBN-TRAPS-MIB", "trapChangedValueInteger"),
        ("NLSBBN-TRAPS-MIB", "trapNETrapLastTrapTimeStamp"))
)
if mibBuilder.loadTexts:
    trapLMEUserOpticalOffAlarm.setStatus(
        ""
    )

trapLMEResetFactoryDefaultAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1166, 6, 1, 2, 27, 0, 26)
)
trapLMEResetFactoryDefaultAlarm.setObjects(
      *(("NLSBBN-TRAPS-MIB", "trapIdentifier"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemModelNumber"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemSerialNum"),
        ("NLSBBN-TRAPS-MIB", "trapPerceivedSeverity"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemOperState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAlarmStatus"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAdminState"),
        ("NLSBBN-TRAPS-MIB", "trapNetworkElemAvailStatus"),
        ("NLSBBN-TRAPS-MIB", "trapText"),
        ("NLSBBN-TRAPS-MIB", "trapChangedObjectId"),
        ("NLSBBN-TRAPS-MIB", "trapChangedValueInteger"),
        ("NLSBBN-TRAPS-MIB", "trapNETrapLastTrapTimeStamp"))
)
if mibBuilder.loadTexts:
    trapLMEResetFactoryDefaultAlarm.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OMNI-gx2LME-MIB",
    **{"Float": Float,
       "trapLMEConfigChangeInteger": trapLMEConfigChangeInteger,
       "trapLMEConfigChangeDisplayString": trapLMEConfigChangeDisplayString,
       "trapLMERFInputAlarm": trapLMERFInputAlarm,
       "trapLMERFOverloadAlarm": trapLMERFOverloadAlarm,
       "trapLMERFOffsetAlarm": trapLMERFOffsetAlarm,
       "trapLMEOpticalPowerAlarm": trapLMEOpticalPowerAlarm,
       "trapLMELaserBiasAlarm": trapLMELaserBiasAlarm,
       "trapLMELaserTempAlarm": trapLMELaserTempAlarm,
       "trapLMETECCurrentAlarm": trapLMETECCurrentAlarm,
       "trapLMEFanCurrentAlarm": trapLMEFanCurrentAlarm,
       "trapLME12vAlarm": trapLME12vAlarm,
       "trapLMEModuleTempAlarm": trapLMEModuleTempAlarm,
       "trapLMEFlashAlarm": trapLMEFlashAlarm,
       "trapLMELaserBiasCntLoopAlarm": trapLMELaserBiasCntLoopAlarm,
       "trapLMEBankBootAlarm": trapLMEBankBootAlarm,
       "trapLMELaserBiasCntLoopInitAlarm": trapLMELaserBiasCntLoopInitAlarm,
       "trapLMERFParamInitAlarm": trapLMERFParamInitAlarm,
       "trapLMETECParamInitAlarm": trapLMETECParamInitAlarm,
       "trapLMEAttnTableInitAlarm": trapLMEAttnTableInitAlarm,
       "trapLMEPowerMeterTableInitAlarm": trapLMEPowerMeterTableInitAlarm,
       "trapLMELaserDataCRCAlarm": trapLMELaserDataCRCAlarm,
       "trapLMEAlarmDataCRCAlarm": trapLMEAlarmDataCRCAlarm,
       "trapLMEFactoryDataCRCAlarm": trapLMEFactoryDataCRCAlarm,
       "trapLMEUserRFOffAlarm": trapLMEUserRFOffAlarm,
       "trapLMEUserOpticalOffAlarm": trapLMEUserOpticalOffAlarm,
       "trapLMEResetFactoryDefaultAlarm": trapLMEResetFactoryDefaultAlarm,
       "gx2lmeDescriptor": gx2lmeDescriptor,
       "gx2lmeAnalogTable": gx2lmeAnalogTable,
       "gx2lmeAnalogEntry": gx2lmeAnalogEntry,
       "gx2lmeAnalogTableIndex": gx2lmeAnalogTableIndex,
       "lmelabelOffsetNomMonitor": lmelabelOffsetNomMonitor,
       "lmeuomOffsetNomMonitor": lmeuomOffsetNomMonitor,
       "lmemajorHighOffsetNomMonitor": lmemajorHighOffsetNomMonitor,
       "lmemajorLowOffsetNomMonitor": lmemajorLowOffsetNomMonitor,
       "lmeminorHighOffsetNomMonitor": lmeminorHighOffsetNomMonitor,
       "lmeminorLowOffsetNomMonitor": lmeminorLowOffsetNomMonitor,
       "lmecurrentValueOffsetNomMonitor": lmecurrentValueOffsetNomMonitor,
       "lmestateFlagOffsetNomMonitor": lmestateFlagOffsetNomMonitor,
       "lmeminValueOffsetNomMonitor": lmeminValueOffsetNomMonitor,
       "lmemaxValueOffsetNomMonitor": lmemaxValueOffsetNomMonitor,
       "lmealarmStateOffsetNomMonitor": lmealarmStateOffsetNomMonitor,
       "lmelabelOffsetNomCnt": lmelabelOffsetNomCnt,
       "lmeuomOffsetNomCnt": lmeuomOffsetNomCnt,
       "lmemajorHighOffsetNomCnt": lmemajorHighOffsetNomCnt,
       "lmemajorLowOffsetNomCnt": lmemajorLowOffsetNomCnt,
       "lmeminorHighOffsetNomCnt": lmeminorHighOffsetNomCnt,
       "lmeminorLowOffsetNomCnt": lmeminorLowOffsetNomCnt,
       "lmecurrentValueOffsetNomCnt": lmecurrentValueOffsetNomCnt,
       "lmestateFlagOffsetNomCnt": lmestateFlagOffsetNomCnt,
       "lmeminValueOffsetNomCnt": lmeminValueOffsetNomCnt,
       "lmemaxValueOffsetNomCnt": lmemaxValueOffsetNomCnt,
       "lmealarmStateOffsetNomCnt": lmealarmStateOffsetNomCnt,
       "lmelabelRelAttenSetting": lmelabelRelAttenSetting,
       "lmeuomRelAttenSetting": lmeuomRelAttenSetting,
       "lmemajorHighRelAttenSetting": lmemajorHighRelAttenSetting,
       "lmemajorLowRelAttenSetting": lmemajorLowRelAttenSetting,
       "lmeminorHighRelAttenSetting": lmeminorHighRelAttenSetting,
       "lmeminorLowRelAttenSetting": lmeminorLowRelAttenSetting,
       "lmecurrentValueRelAttenSetting": lmecurrentValueRelAttenSetting,
       "lmestateFlagRelAttenSetting": lmestateFlagRelAttenSetting,
       "lmeminValueRelAttenSetting": lmeminValueRelAttenSetting,
       "lmemaxValueRelAttenSetting": lmemaxValueRelAttenSetting,
       "lmealarmStateRelAttenSetting": lmealarmStateRelAttenSetting,
       "lmelabelOptPower": lmelabelOptPower,
       "lmeuomOptPower": lmeuomOptPower,
       "lmemajorHighOptPower": lmemajorHighOptPower,
       "lmemajorLowOptPower": lmemajorLowOptPower,
       "lmeminorHighOptPower": lmeminorHighOptPower,
       "lmeminorLowOptPower": lmeminorLowOptPower,
       "lmecurrentValueOptPower": lmecurrentValueOptPower,
       "lmestateFlagOptPower": lmestateFlagOptPower,
       "lmeminValueOptPower": lmeminValueOptPower,
       "lmemaxValueOptPower": lmemaxValueOptPower,
       "lmealarmStateOptPower": lmealarmStateOptPower,
       "lmelabelLaserBias": lmelabelLaserBias,
       "lmeuomLaserBias": lmeuomLaserBias,
       "lmemajorHighLaserBias": lmemajorHighLaserBias,
       "lmemajorLowLaserBias": lmemajorLowLaserBias,
       "lmeminorHighLaserBias": lmeminorHighLaserBias,
       "lmeminorLowLaserBias": lmeminorLowLaserBias,
       "lmecurrentValueLaserBias": lmecurrentValueLaserBias,
       "lmestateFlagLaserBias": lmestateFlagLaserBias,
       "lmeminValueLaserBias": lmeminValueLaserBias,
       "lmemaxValueLaserBias": lmemaxValueLaserBias,
       "lmealarmStateLaserBias": lmealarmStateLaserBias,
       "lmelabelTecCurrent": lmelabelTecCurrent,
       "lmeuomTecCurrent": lmeuomTecCurrent,
       "lmemajorHighTecCurrent": lmemajorHighTecCurrent,
       "lmemajorLowTecCurrent": lmemajorLowTecCurrent,
       "lmeminorHighTecCurrent": lmeminorHighTecCurrent,
       "lmeminorLowTecCurrent": lmeminorLowTecCurrent,
       "lmecurrentValueTecCurrent": lmecurrentValueTecCurrent,
       "lmestateFlagTecCurrent": lmestateFlagTecCurrent,
       "lmeminValueTecCurrent": lmeminValueTecCurrent,
       "lmemaxValueTecCurrent": lmemaxValueTecCurrent,
       "lmealarmStateTecCurrent": lmealarmStateTecCurrent,
       "lmelabelLaserTemp": lmelabelLaserTemp,
       "lmeuomLaserTemp": lmeuomLaserTemp,
       "lmemajorHighLaserTemp": lmemajorHighLaserTemp,
       "lmemajorLowLaserTemp": lmemajorLowLaserTemp,
       "lmeminorHighLaserTemp": lmeminorHighLaserTemp,
       "lmeminorLowLaserTemp": lmeminorLowLaserTemp,
       "lmecurrentValueLaserTemp": lmecurrentValueLaserTemp,
       "lmestateFlagLaserTemp": lmestateFlagLaserTemp,
       "lmeminValueLaserTemp": lmeminValueLaserTemp,
       "lmemaxValueLaserTemp": lmemaxValueLaserTemp,
       "lmealarmStateLaserTemp": lmealarmStateLaserTemp,
       "lmelabelModuleTemp": lmelabelModuleTemp,
       "lmeuomModuleTemp": lmeuomModuleTemp,
       "lmemajorHighModuleTemp": lmemajorHighModuleTemp,
       "lmemajorLowModuleTemp": lmemajorLowModuleTemp,
       "lmeminorHighModuleTemp": lmeminorHighModuleTemp,
       "lmeminorLowModuleTemp": lmeminorLowModuleTemp,
       "lmecurrentValueModuleTemp": lmecurrentValueModuleTemp,
       "lmestateFlagModuleTemp": lmestateFlagModuleTemp,
       "lmeminValueModuleTemp": lmeminValueModuleTemp,
       "lmemaxValueModuleTemp": lmemaxValueModuleTemp,
       "lmealarmStateModuleTemp": lmealarmStateModuleTemp,
       "lmelabelFanCurrent": lmelabelFanCurrent,
       "lmeuomFanCurrent": lmeuomFanCurrent,
       "lmemajorHighFanCurrent": lmemajorHighFanCurrent,
       "lmemajorLowFanCurrent": lmemajorLowFanCurrent,
       "lmeminorHighFanCurrent": lmeminorHighFanCurrent,
       "lmeminorLowFanCurrent": lmeminorLowFanCurrent,
       "lmecurrentValueFanCurrent": lmecurrentValueFanCurrent,
       "lmestateFlagFanCurrent": lmestateFlagFanCurrent,
       "lmeminValueFanCurrent": lmeminValueFanCurrent,
       "lmemaxValueFanCurrent": lmemaxValueFanCurrent,
       "lmealarmStateFanCurrent": lmealarmStateFanCurrent,
       "lmelabel12Volt": lmelabel12Volt,
       "lmeuom12Volt": lmeuom12Volt,
       "lmemajorHigh12Volt": lmemajorHigh12Volt,
       "lmemajorLow12Volt": lmemajorLow12Volt,
       "lmeminorHigh12Volt": lmeminorHigh12Volt,
       "lmeminorLow12Volt": lmeminorLow12Volt,
       "lmecurrentValue12Volt": lmecurrentValue12Volt,
       "lmestateFlag12Volt": lmestateFlag12Volt,
       "lmeminValue12Volt": lmeminValue12Volt,
       "lmemaxValue12Volt": lmemaxValue12Volt,
       "lmealarmState12Volt": lmealarmState12Volt,
       "gx2lmeDigitalTable": gx2lmeDigitalTable,
       "gx2lmeDigitalEntry": gx2lmeDigitalEntry,
       "gx2lmeDigitalTableIndex": gx2lmeDigitalTableIndex,
       "lmelabelRfInput": lmelabelRfInput,
       "lmeenumRfInput": lmeenumRfInput,
       "lmevalueRfInput": lmevalueRfInput,
       "lmestateflagRfInput": lmestateflagRfInput,
       "lmelabelOptOutput": lmelabelOptOutput,
       "lmeenumOptOutput": lmeenumOptOutput,
       "lmevalueOptOutput": lmevalueOptOutput,
       "lmestateflagOptOutput": lmestateflagOptOutput,
       "lmelabelLaserMode": lmelabelLaserMode,
       "lmeenumLaserMode": lmeenumLaserMode,
       "lmevalueLaserMode": lmevalueLaserMode,
       "lmestateflagLaserMode": lmestateflagLaserMode,
       "lmelabelLaserSecMode": lmelabelLaserSecMode,
       "lmeenumLaserSecMode": lmeenumLaserSecMode,
       "lmevalueLaserSecMode": lmevalueLaserSecMode,
       "lmestateflagLaserSecMode": lmestateflagLaserSecMode,
       "lmelabelVideoOffset": lmelabelVideoOffset,
       "lmeenumVideoOffset": lmeenumVideoOffset,
       "lmevalueVideoOffset": lmevalueVideoOffset,
       "lmestateflagVideoOffset": lmestateflagVideoOffset,
       "lmelabelFactoryDefault": lmelabelFactoryDefault,
       "lmeenumFactoryDefault": lmeenumFactoryDefault,
       "lmevalueFactoryDefault": lmevalueFactoryDefault,
       "lmestateflagFactoryDefault": lmestateflagFactoryDefault,
       "lmelabelFiberLength": lmelabelFiberLength,
       "lmeenumFiberLength": lmeenumFiberLength,
       "lmevalueFiberLength": lmevalueFiberLength,
       "lmestateflagFiberLength": lmestateflagFiberLength,
       "lmelabelConditioningUnit": lmelabelConditioningUnit,
       "lmeenumConditioningUnit": lmeenumConditioningUnit,
       "lmevalueConditioningUnit": lmevalueConditioningUnit,
       "lmestateflagConditioningUnit": lmestateflagConditioningUnit,
       "gx2lmeStatusTable": gx2lmeStatusTable,
       "gx2lmeStatusEntry": gx2lmeStatusEntry,
       "gx2lmeStatusTableIndex": gx2lmeStatusTableIndex,
       "lmelabelBoot": lmelabelBoot,
       "lmevalueBoot": lmevalueBoot,
       "lmestateflagBoot": lmestateflagBoot,
       "lmelabelFlash": lmelabelFlash,
       "lmevalueFlash": lmevalueFlash,
       "lmestateflagFlash": lmestateflagFlash,
       "lmelabelFactoryDataCRC": lmelabelFactoryDataCRC,
       "lmevalueFactoryDataCRC": lmevalueFactoryDataCRC,
       "lmestateflagFactoryDataCRC": lmestateflagFactoryDataCRC,
       "lmelabelLaserDataCRC": lmelabelLaserDataCRC,
       "lmevalueLaserDataCRC": lmevalueLaserDataCRC,
       "lmestateflagLaserDataCRC": lmestateflagLaserDataCRC,
       "lmelabelAlarmDataCrc": lmelabelAlarmDataCrc,
       "lmevalueAlarmDataCrc": lmevalueAlarmDataCrc,
       "lmestateflagAlarmDataCrc": lmestateflagAlarmDataCrc,
       "lmelabelHWStatus": lmelabelHWStatus,
       "lmevalueHWStatus": lmevalueHWStatus,
       "lmestateflagHWStatus": lmestateflagHWStatus,
       "lmelabelRFInputStatus": lmelabelRFInputStatus,
       "lmevalueRFInputStatus": lmevalueRFInputStatus,
       "lmestateflagRFInputStatus": lmestateflagRFInputStatus,
       "gx2lmeFactoryTable": gx2lmeFactoryTable,
       "gx2lmeFactoryEntry": gx2lmeFactoryEntry,
       "gx2lmeFactoryTableIndex": gx2lmeFactoryTableIndex,
       "lmebootControlByteValue": lmebootControlByteValue,
       "lmebootStatusByteValue": lmebootStatusByteValue,
       "lmebank1CRCValue": lmebank1CRCValue,
       "lmebank2CRCValue": lmebank2CRCValue,
       "lmeprgEEPROMByteValue": lmeprgEEPROMByteValue,
       "lmefactoryCRCValue": lmefactoryCRCValue,
       "lmecalculateCRCValue": lmecalculateCRCValue,
       "lmehourMeterValue": lmehourMeterValue,
       "lmeflashPrgCntAValue": lmeflashPrgCntAValue,
       "lmeflashPrgCntBValue": lmeflashPrgCntBValue,
       "lmeflashBankARevValue": lmeflashBankARevValue,
       "lmeflashBankBRevValue": lmeflashBankBRevValue,
       "gx2Lm1000EHoldTimeTable": gx2Lm1000EHoldTimeTable,
       "gx2Lm1000EHoldTimeEntry": gx2Lm1000EHoldTimeEntry,
       "gx2Lm1000EHoldTimeTableIndex": gx2Lm1000EHoldTimeTableIndex,
       "gx2Lm1000EHoldTimeSpecIndex": gx2Lm1000EHoldTimeSpecIndex,
       "gx2Lm1000EHoldTimeData": gx2Lm1000EHoldTimeData}
)
