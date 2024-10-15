# SNMP MIB module (RADLAN-PHY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RADLAN-PHY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:42:53 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

rlPhy = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 89, 90)
)
rlPhy.setRevisions(
        ("2002-09-30 00:24",
         "2003-09-21 00:24")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class RlPhyTestType(Integer32, TextualConvention):
    status = "current"
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
              24)
        )
    )
    namedValues = NamedValues(
        *(("rlPhyTestTableCableChannel1", 13),
          ("rlPhyTestTableCableChannel2", 14),
          ("rlPhyTestTableCableChannel3", 15),
          ("rlPhyTestTableCableChannel4", 16),
          ("rlPhyTestTableCableFault", 3),
          ("rlPhyTestTableCableLength", 4),
          ("rlPhyTestTableCablePairSkew1", 21),
          ("rlPhyTestTableCablePairSkew2", 22),
          ("rlPhyTestTableCablePairSkew3", 23),
          ("rlPhyTestTableCablePairSkew4", 24),
          ("rlPhyTestTableCablePolarity1", 17),
          ("rlPhyTestTableCablePolarity2", 18),
          ("rlPhyTestTableCablePolarity3", 19),
          ("rlPhyTestTableCablePolarity4", 20),
          ("rlPhyTestTableCableStatus", 2),
          ("rlPhyTestTableDataReady", 10),
          ("rlPhyTestTableLOS", 11),
          ("rlPhyTestTableNoTest", 1),
          ("rlPhyTestTableRxOpticalPower", 9),
          ("rlPhyTestTableTransceiverSupply", 6),
          ("rlPhyTestTableTransceiverTemp", 5),
          ("rlPhyTestTableTxBias", 7),
          ("rlPhyTestTableTxFault", 12),
          ("rlPhyTestTableTxOutput", 8))
    )



# MIB Managed Objects in the order of their OIDs

_RlPhyTest_ObjectIdentity = ObjectIdentity
rlPhyTest = _RlPhyTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 90, 1)
)
_RlPhyTestSetTable_Object = MibTable
rlPhyTestSetTable = _RlPhyTestSetTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 90, 1, 1)
)
if mibBuilder.loadTexts:
    rlPhyTestSetTable.setStatus("current")
_RlPhyTestSetEntry_Object = MibTableRow
rlPhyTestSetEntry = _RlPhyTestSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 90, 1, 1, 1)
)
rlPhyTestSetEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    rlPhyTestSetEntry.setStatus("current")
_RlPhyTestSetType_Type = RlPhyTestType
_RlPhyTestSetType_Object = MibTableColumn
rlPhyTestSetType = _RlPhyTestSetType_Object(
    (1, 3, 6, 1, 4, 1, 89, 90, 1, 1, 1, 1),
    _RlPhyTestSetType_Type()
)
rlPhyTestSetType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPhyTestSetType.setStatus("current")
_RlPhyTestGetTable_Object = MibTable
rlPhyTestGetTable = _RlPhyTestGetTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 90, 1, 2)
)
if mibBuilder.loadTexts:
    rlPhyTestGetTable.setStatus("current")
_RlPhyTestGetEntry_Object = MibTableRow
rlPhyTestGetEntry = _RlPhyTestGetEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 90, 1, 2, 1)
)
rlPhyTestGetEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "RADLAN-PHY-MIB", "rlPhyTestGetType"),
)
if mibBuilder.loadTexts:
    rlPhyTestGetEntry.setStatus("current")
_RlPhyTestGetType_Type = RlPhyTestType
_RlPhyTestGetType_Object = MibTableColumn
rlPhyTestGetType = _RlPhyTestGetType_Object(
    (1, 3, 6, 1, 4, 1, 89, 90, 1, 2, 1, 1),
    _RlPhyTestGetType_Type()
)
rlPhyTestGetType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPhyTestGetType.setStatus("current")


class _RlPhyTestGetStatus_Type(Integer32):
    """Custom type rlPhyTestGetStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("aborted", 6),
          ("failed", 7),
          ("inProgress", 3),
          ("none", 1),
          ("notSupported", 4),
          ("success", 2),
          ("unAbleToRun", 5))
    )


_RlPhyTestGetStatus_Type.__name__ = "Integer32"
_RlPhyTestGetStatus_Object = MibTableColumn
rlPhyTestGetStatus = _RlPhyTestGetStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 90, 1, 2, 1, 2),
    _RlPhyTestGetStatus_Type()
)
rlPhyTestGetStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPhyTestGetStatus.setStatus("current")
_RlPhyTestGetResult_Type = Integer32
_RlPhyTestGetResult_Object = MibTableColumn
rlPhyTestGetResult = _RlPhyTestGetResult_Object(
    (1, 3, 6, 1, 4, 1, 89, 90, 1, 2, 1, 3),
    _RlPhyTestGetResult_Type()
)
rlPhyTestGetResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPhyTestGetResult.setStatus("current")


class _RlPhyTestGetUnits_Type(Integer32):
    """Custom type rlPhyTestGetUnits based on Integer32"""
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
        *(("abcd", 18),
          ("alaskaPhyLength", 13),
          ("alaskaPhyStatus", 14),
          ("boolean", 2),
          ("dbm", 15),
          ("decidbm", 16),
          ("degree", 7),
          ("downUP", 3),
          ("integer", 1),
          ("mdiMdix", 5),
          ("meter", 6),
          ("microAmper", 10),
          ("microOham", 9),
          ("microVolt", 8),
          ("microWatt", 11),
          ("milidbm", 17),
          ("millisecond", 12),
          ("nanosecond", 19),
          ("reverseNormal", 4))
    )


_RlPhyTestGetUnits_Type.__name__ = "Integer32"
_RlPhyTestGetUnits_Object = MibTableColumn
rlPhyTestGetUnits = _RlPhyTestGetUnits_Object(
    (1, 3, 6, 1, 4, 1, 89, 90, 1, 2, 1, 4),
    _RlPhyTestGetUnits_Type()
)
rlPhyTestGetUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPhyTestGetUnits.setStatus("current")


class _RlPhyTestGetAlarm_Type(Integer32):
    """Custom type rlPhyTestGetAlarm based on Integer32"""
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
        *(("highAlarm", 6),
          ("highWarning", 4),
          ("lowAlarm", 5),
          ("lowWarning", 3),
          ("noAlarmSet", 2),
          ("notRelevant", 1))
    )


_RlPhyTestGetAlarm_Type.__name__ = "Integer32"
_RlPhyTestGetAlarm_Object = MibTableColumn
rlPhyTestGetAlarm = _RlPhyTestGetAlarm_Object(
    (1, 3, 6, 1, 4, 1, 89, 90, 1, 2, 1, 5),
    _RlPhyTestGetAlarm_Type()
)
rlPhyTestGetAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPhyTestGetAlarm.setStatus("current")


class _RlPhyTestGetTimeStamp_Type(DisplayString):
    """Custom type rlPhyTestGetTimeStamp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RlPhyTestGetTimeStamp_Type.__name__ = "DisplayString"
_RlPhyTestGetTimeStamp_Object = MibTableColumn
rlPhyTestGetTimeStamp = _RlPhyTestGetTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 89, 90, 1, 2, 1, 6),
    _RlPhyTestGetTimeStamp_Type()
)
rlPhyTestGetTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPhyTestGetTimeStamp.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RADLAN-PHY-MIB",
    **{"RlPhyTestType": RlPhyTestType,
       "rlPhy": rlPhy,
       "rlPhyTest": rlPhyTest,
       "rlPhyTestSetTable": rlPhyTestSetTable,
       "rlPhyTestSetEntry": rlPhyTestSetEntry,
       "rlPhyTestSetType": rlPhyTestSetType,
       "rlPhyTestGetTable": rlPhyTestGetTable,
       "rlPhyTestGetEntry": rlPhyTestGetEntry,
       "rlPhyTestGetType": rlPhyTestGetType,
       "rlPhyTestGetStatus": rlPhyTestGetStatus,
       "rlPhyTestGetResult": rlPhyTestGetResult,
       "rlPhyTestGetUnits": rlPhyTestGetUnits,
       "rlPhyTestGetAlarm": rlPhyTestGetAlarm,
       "rlPhyTestGetTimeStamp": rlPhyTestGetTimeStamp}
)
