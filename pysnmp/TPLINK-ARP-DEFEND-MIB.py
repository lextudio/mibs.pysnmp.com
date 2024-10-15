# SNMP MIB module (TPLINK-ARP-DEFEND-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TPLINK-ARP-DEFEND-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:05:47 2024
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

(tplinkArpInspectionMIBObjects,) = mibBuilder.importSymbols(
    "TPLINK-ARP-INSPECTION-MIB",
    "tplinkArpInspectionMIBObjects")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TpArpDefend_ObjectIdentity = ObjectIdentity
tpArpDefend = _TpArpDefend_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 28, 1, 2)
)
_TpArpDefendConfig_ObjectIdentity = ObjectIdentity
tpArpDefendConfig = _TpArpDefendConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 28, 1, 2, 1)
)
_TpArpDefendConfigTable_Object = MibTable
tpArpDefendConfigTable = _TpArpDefendConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 28, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    tpArpDefendConfigTable.setStatus("current")
_TpArpDefendConfigEntry_Object = MibTableRow
tpArpDefendConfigEntry = _TpArpDefendConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 28, 1, 2, 1, 1, 1)
)
tpArpDefendConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tpArpDefendConfigEntry.setStatus("current")
_TpArpDefendConfigPort_Type = OctetString
_TpArpDefendConfigPort_Object = MibTableColumn
tpArpDefendConfigPort = _TpArpDefendConfigPort_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 28, 1, 2, 1, 1, 1, 1),
    _TpArpDefendConfigPort_Type()
)
tpArpDefendConfigPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpArpDefendConfigPort.setStatus("current")


class _TpArpDefendConfigEnable_Type(Integer32):
    """Custom type tpArpDefendConfigEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_TpArpDefendConfigEnable_Type.__name__ = "Integer32"
_TpArpDefendConfigEnable_Object = MibTableColumn
tpArpDefendConfigEnable = _TpArpDefendConfigEnable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 28, 1, 2, 1, 1, 1, 2),
    _TpArpDefendConfigEnable_Type()
)
tpArpDefendConfigEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpArpDefendConfigEnable.setStatus("current")
_TpArpDefendConfigRate_Type = Integer32
_TpArpDefendConfigRate_Object = MibTableColumn
tpArpDefendConfigRate = _TpArpDefendConfigRate_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 28, 1, 2, 1, 1, 1, 3),
    _TpArpDefendConfigRate_Type()
)
tpArpDefendConfigRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpArpDefendConfigRate.setStatus("current")
_TpArpDefendConfigState_Type = OctetString
_TpArpDefendConfigState_Object = MibTableColumn
tpArpDefendConfigState = _TpArpDefendConfigState_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 28, 1, 2, 1, 1, 1, 4),
    _TpArpDefendConfigState_Type()
)
tpArpDefendConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpArpDefendConfigState.setStatus("current")
_TpArpDefendConfigPortLag_Type = OctetString
_TpArpDefendConfigPortLag_Object = MibTableColumn
tpArpDefendConfigPortLag = _TpArpDefendConfigPortLag_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 28, 1, 2, 1, 1, 1, 5),
    _TpArpDefendConfigPortLag_Type()
)
tpArpDefendConfigPortLag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpArpDefendConfigPortLag.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPLINK-ARP-DEFEND-MIB",
    **{"tpArpDefend": tpArpDefend,
       "tpArpDefendConfig": tpArpDefendConfig,
       "tpArpDefendConfigTable": tpArpDefendConfigTable,
       "tpArpDefendConfigEntry": tpArpDefendConfigEntry,
       "tpArpDefendConfigPort": tpArpDefendConfigPort,
       "tpArpDefendConfigEnable": tpArpDefendConfigEnable,
       "tpArpDefendConfigRate": tpArpDefendConfigRate,
       "tpArpDefendConfigState": tpArpDefendConfigState,
       "tpArpDefendConfigPortLag": tpArpDefendConfigPortLag}
)
