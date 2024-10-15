# SNMP MIB module (TPLINK-PORTISOLATION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TPLINK-PORTISOLATION-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:06:28 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(tplinkMgmt,) = mibBuilder.importSymbols(
    "TPLINK-MIB",
    "tplinkMgmt")


# MODULE-IDENTITY

tplinkPortIsolationMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 13)
)
tplinkPortIsolationMIB.setRevisions(
        ("2012-12-13 09:30",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TplinkPortIsolationMIBObjects_ObjectIdentity = ObjectIdentity
tplinkPortIsolationMIBObjects = _TplinkPortIsolationMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 13, 1)
)
_PortIsolationCtrlTable_Object = MibTable
portIsolationCtrlTable = _PortIsolationCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 13, 1, 1)
)
if mibBuilder.loadTexts:
    portIsolationCtrlTable.setStatus("current")
_PortIsolationCtrlEntry_Object = MibTableRow
portIsolationCtrlEntry = _PortIsolationCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 13, 1, 1, 1)
)
portIsolationCtrlEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    portIsolationCtrlEntry.setStatus("current")


class _PortIsolationPortId_Type(OctetString):
    """Custom type portIsolationPortId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_PortIsolationPortId_Type.__name__ = "OctetString"
_PortIsolationPortId_Object = MibTableColumn
portIsolationPortId = _PortIsolationPortId_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 13, 1, 1, 1, 1),
    _PortIsolationPortId_Type()
)
portIsolationPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portIsolationPortId.setStatus("current")


class _PortIsolationForList_Type(OctetString):
    """Custom type portIsolationForList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PortIsolationForList_Type.__name__ = "OctetString"
_PortIsolationForList_Object = MibTableColumn
portIsolationForList = _PortIsolationForList_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 13, 1, 1, 1, 2),
    _PortIsolationForList_Type()
)
portIsolationForList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portIsolationForList.setStatus("current")


class _PortIsolationLagId_Type(OctetString):
    """Custom type portIsolationLagId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_PortIsolationLagId_Type.__name__ = "OctetString"
_PortIsolationLagId_Object = MibTableColumn
portIsolationLagId = _PortIsolationLagId_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 13, 1, 1, 1, 3),
    _PortIsolationLagId_Type()
)
portIsolationLagId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portIsolationLagId.setStatus("current")
_TplinkPortIsolationMIBNotifications_ObjectIdentity = ObjectIdentity
tplinkPortIsolationMIBNotifications = _TplinkPortIsolationMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 13, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPLINK-PORTISOLATION-MIB",
    **{"tplinkPortIsolationMIB": tplinkPortIsolationMIB,
       "tplinkPortIsolationMIBObjects": tplinkPortIsolationMIBObjects,
       "portIsolationCtrlTable": portIsolationCtrlTable,
       "portIsolationCtrlEntry": portIsolationCtrlEntry,
       "portIsolationPortId": portIsolationPortId,
       "portIsolationForList": portIsolationForList,
       "portIsolationLagId": portIsolationLagId,
       "tplinkPortIsolationMIBNotifications": tplinkPortIsolationMIBNotifications}
)
