# SNMP MIB module (DNMSALARM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DNMSALARM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:31:47 2024
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

(dynaCommGeneral,) = mibBuilder.importSymbols(
    "DYNATECHCOMMUNICATIONS-MIB",
    "dynaCommGeneral")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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

_DnmsAlarm_ObjectIdentity = ObjectIdentity
dnmsAlarm = _DnmsAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 384, 2, 1)
)


class _DnmsAlarmEnable_Type(Integer32):
    """Custom type dnmsAlarmEnable based on Integer32"""
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


_DnmsAlarmEnable_Type.__name__ = "Integer32"
_DnmsAlarmEnable_Object = MibScalar
dnmsAlarmEnable = _DnmsAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 384, 2, 1, 1),
    _DnmsAlarmEnable_Type()
)
dnmsAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dnmsAlarmEnable.setStatus("mandatory")
_DnmsAlarmTable_Object = MibTable
dnmsAlarmTable = _DnmsAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 384, 2, 1, 2)
)
if mibBuilder.loadTexts:
    dnmsAlarmTable.setStatus("mandatory")
_DnmsAlarmEntry_Object = MibTableRow
dnmsAlarmEntry = _DnmsAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 384, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    dnmsAlarmEntry.setStatus("mandatory")


class _DnmsAlarmEntryIndex_Type(Integer32):
    """Custom type dnmsAlarmEntryIndex based on Integer32"""
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
              33)
        )
    )
    namedValues = NamedValues(
        *(("almlost", 9),
          ("card-linecrd", 18),
          ("card-primem", 14),
          ("card-primstr", 16),
          ("card-secmem", 15),
          ("card-secmstr", 17),
          ("cdrlost", 8),
          ("dev-dn", 12),
          ("dev-up", 11),
          ("dllfail", 24),
          ("dllinit", 22),
          ("dllok", 23),
          ("fcs-err", 7),
          ("fr-invmsg", 28),
          ("fr-nn4count", 27),
          ("fr-nt1time", 25),
          ("fr-nt2imte", 26),
          ("psufail", 13),
          ("stalost", 10),
          ("tpad-CD-down", 32),
          ("tpad-CD-up", 33),
          ("tpad-nak-ex", 29),
          ("tpad-normPoll", 31),
          ("tpad-slowPoll", 30),
          ("x25-lev1-dn", 1),
          ("x25-lev1-up", 2),
          ("x25-lev2-dn", 3),
          ("x25-lev2-up", 4),
          ("x25-lev3-dn", 5),
          ("x25-lev3-up", 6),
          ("x28-inact", 21),
          ("x28-portPkt", 20),
          ("x28-portX28", 19))
    )


_DnmsAlarmEntryIndex_Type.__name__ = "Integer32"
_DnmsAlarmEntryIndex_Object = MibTableColumn
dnmsAlarmEntryIndex = _DnmsAlarmEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 384, 2, 1, 2, 1, 1),
    _DnmsAlarmEntryIndex_Type()
)
dnmsAlarmEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnmsAlarmEntryIndex.setStatus("mandatory")


class _DnmsAlarmEntryEnable_Type(Integer32):
    """Custom type dnmsAlarmEntryEnable based on Integer32"""
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


_DnmsAlarmEntryEnable_Type.__name__ = "Integer32"
_DnmsAlarmEntryEnable_Object = MibTableColumn
dnmsAlarmEntryEnable = _DnmsAlarmEntryEnable_Object(
    (1, 3, 6, 1, 4, 1, 384, 2, 1, 2, 1, 2),
    _DnmsAlarmEntryEnable_Type()
)
dnmsAlarmEntryEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dnmsAlarmEntryEnable.setStatus("mandatory")


class _DnmsAlarmEntryDescr_Type(DisplayString):
    """Custom type dnmsAlarmEntryDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DnmsAlarmEntryDescr_Type.__name__ = "DisplayString"
_DnmsAlarmEntryDescr_Object = MibTableColumn
dnmsAlarmEntryDescr = _DnmsAlarmEntryDescr_Object(
    (1, 3, 6, 1, 4, 1, 384, 2, 1, 2, 1, 3),
    _DnmsAlarmEntryDescr_Type()
)
dnmsAlarmEntryDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnmsAlarmEntryDescr.setStatus("mandatory")

# Managed Objects groups


# Notification objects

dnmsAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 384, 2, 1, 0, 1)
)
dnmsAlarmTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("DNMSALARM-MIB", "dnmsAlarmEntryIndex"),
        ("DNMSALARM-MIB", "dnmsAlarmEntryDescr"))
)
if mibBuilder.loadTexts:
    dnmsAlarmTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DNMSALARM-MIB",
    **{"dnmsAlarm": dnmsAlarm,
       "dnmsAlarmTrap": dnmsAlarmTrap,
       "dnmsAlarmEnable": dnmsAlarmEnable,
       "dnmsAlarmTable": dnmsAlarmTable,
       "dnmsAlarmEntry": dnmsAlarmEntry,
       "dnmsAlarmEntryIndex": dnmsAlarmEntryIndex,
       "dnmsAlarmEntryEnable": dnmsAlarmEntryEnable,
       "dnmsAlarmEntryDescr": dnmsAlarmEntryDescr}
)
