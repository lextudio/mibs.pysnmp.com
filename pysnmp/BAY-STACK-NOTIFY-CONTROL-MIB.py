# SNMP MIB module (BAY-STACK-NOTIFY-CONTROL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BAY-STACK-NOTIFY-CONTROL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:46:16 2024
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

(PortList,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(bayStackMibs,) = mibBuilder.importSymbols(
    "SYNOPTICS-ROOT-MIB",
    "bayStackMibs")


# MODULE-IDENTITY

bayStackNotifyControlMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 31)
)
bayStackNotifyControlMib.setRevisions(
        ("2010-09-08 00:00",
         "2008-10-17 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BsncObjects_ObjectIdentity = ObjectIdentity
bsncObjects = _BsncObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 31, 1)
)
_BsncNotifyControlTable_Object = MibTable
bsncNotifyControlTable = _BsncNotifyControlTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 31, 1, 1)
)
if mibBuilder.loadTexts:
    bsncNotifyControlTable.setStatus("current")
_BsncNotifyControlEntry_Object = MibTableRow
bsncNotifyControlEntry = _BsncNotifyControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 31, 1, 1, 1)
)
bsncNotifyControlEntry.setIndexNames(
    (0, "BAY-STACK-NOTIFY-CONTROL-MIB", "bsncNotifyControlType"),
)
if mibBuilder.loadTexts:
    bsncNotifyControlEntry.setStatus("current")
_BsncNotifyControlType_Type = ObjectIdentifier
_BsncNotifyControlType_Object = MibTableColumn
bsncNotifyControlType = _BsncNotifyControlType_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 31, 1, 1, 1, 1),
    _BsncNotifyControlType_Type()
)
bsncNotifyControlType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bsncNotifyControlType.setStatus("current")


class _BsncNotifyControlEnabled_Type(TruthValue):
    """Custom type bsncNotifyControlEnabled based on TruthValue"""


_BsncNotifyControlEnabled_Object = MibTableColumn
bsncNotifyControlEnabled = _BsncNotifyControlEnabled_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 31, 1, 1, 1, 2),
    _BsncNotifyControlEnabled_Type()
)
bsncNotifyControlEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsncNotifyControlEnabled.setStatus("current")
_BsncNotifyControlRowStatus_Type = RowStatus
_BsncNotifyControlRowStatus_Object = MibTableColumn
bsncNotifyControlRowStatus = _BsncNotifyControlRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 31, 1, 1, 1, 3),
    _BsncNotifyControlRowStatus_Type()
)
bsncNotifyControlRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsncNotifyControlRowStatus.setStatus("current")
_BsncNotifyControlPortListEnabled_Type = PortList
_BsncNotifyControlPortListEnabled_Object = MibTableColumn
bsncNotifyControlPortListEnabled = _BsncNotifyControlPortListEnabled_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 31, 1, 1, 1, 4),
    _BsncNotifyControlPortListEnabled_Type()
)
bsncNotifyControlPortListEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsncNotifyControlPortListEnabled.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BAY-STACK-NOTIFY-CONTROL-MIB",
    **{"bayStackNotifyControlMib": bayStackNotifyControlMib,
       "bsncObjects": bsncObjects,
       "bsncNotifyControlTable": bsncNotifyControlTable,
       "bsncNotifyControlEntry": bsncNotifyControlEntry,
       "bsncNotifyControlType": bsncNotifyControlType,
       "bsncNotifyControlEnabled": bsncNotifyControlEnabled,
       "bsncNotifyControlRowStatus": bsncNotifyControlRowStatus,
       "bsncNotifyControlPortListEnabled": bsncNotifyControlPortListEnabled}
)
