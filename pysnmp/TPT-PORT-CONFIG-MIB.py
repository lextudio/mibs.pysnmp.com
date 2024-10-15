# SNMP MIB module (TPT-PORT-CONFIG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TPT-PORT-CONFIG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:06:56 2024
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

(tpt_tpa_objs,) = mibBuilder.importSymbols(
    "TPT-TPAMIBS-MIB",
    "tpt-tpa-objs")


# MODULE-IDENTITY

tpt_port_config_objs = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 4)
)
tpt_port_config_objs.setRevisions(
        ("2016-05-25 18:54",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class LineSpeed(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("fourty-gigabit", 5),
          ("gigabit", 1),
          ("hundred-megabit", 2),
          ("ten-gigabit", 4),
          ("ten-megabit", 3))
    )



class DuplexSetting(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("full", 2),
          ("half", 1))
    )



class AutoNegotiation(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("off", 2),
          ("on", 1))
    )



class EnabledOrNot(Integer32, TextualConvention):
    status = "current"
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



class FailoverAction(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("block", 0),
          ("permit", 1))
    )



class LinkDownMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("breaker", 1),
          ("hub", 0),
          ("wire", 2))
    )



# MIB Managed Objects in the order of their OIDs

_PortConfigTable_Object = MibTable
portConfigTable = _PortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 4, 1)
)
if mibBuilder.loadTexts:
    portConfigTable.setStatus("current")
_PortConfigEntry_Object = MibTableRow
portConfigEntry = _PortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 4, 1, 1)
)
portConfigEntry.setIndexNames(
    (0, "TPT-PORT-CONFIG-MIB", "portConfigSlot"),
    (0, "TPT-PORT-CONFIG-MIB", "portConfigPort"),
)
if mibBuilder.loadTexts:
    portConfigEntry.setStatus("current")
_PortConfigSlot_Type = Unsigned32
_PortConfigSlot_Object = MibTableColumn
portConfigSlot = _PortConfigSlot_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 4, 1, 1, 1),
    _PortConfigSlot_Type()
)
portConfigSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portConfigSlot.setStatus("current")
_PortConfigPort_Type = Unsigned32
_PortConfigPort_Object = MibTableColumn
portConfigPort = _PortConfigPort_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 4, 1, 1, 2),
    _PortConfigPort_Type()
)
portConfigPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portConfigPort.setStatus("current")
_PortConfigLineSpeed_Type = LineSpeed
_PortConfigLineSpeed_Object = MibTableColumn
portConfigLineSpeed = _PortConfigLineSpeed_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 4, 1, 1, 3),
    _PortConfigLineSpeed_Type()
)
portConfigLineSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portConfigLineSpeed.setStatus("current")
_PortConfigDuplex_Type = DuplexSetting
_PortConfigDuplex_Object = MibTableColumn
portConfigDuplex = _PortConfigDuplex_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 4, 1, 1, 4),
    _PortConfigDuplex_Type()
)
portConfigDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portConfigDuplex.setStatus("current")
_PortConfigAutoNeg_Type = AutoNegotiation
_PortConfigAutoNeg_Object = MibTableColumn
portConfigAutoNeg = _PortConfigAutoNeg_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 4, 1, 1, 5),
    _PortConfigAutoNeg_Type()
)
portConfigAutoNeg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portConfigAutoNeg.setStatus("current")
_PortConfigShutdown_Type = EnabledOrNot
_PortConfigShutdown_Object = MibTableColumn
portConfigShutdown = _PortConfigShutdown_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 4, 1, 1, 6),
    _PortConfigShutdown_Type()
)
portConfigShutdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portConfigShutdown.setStatus("current")
_PortConfigLoopback_Type = EnabledOrNot
_PortConfigLoopback_Object = MibTableColumn
portConfigLoopback = _PortConfigLoopback_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 4, 1, 1, 7),
    _PortConfigLoopback_Type()
)
portConfigLoopback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portConfigLoopback.setStatus("current")
_PortConfigFailover_Type = FailoverAction
_PortConfigFailover_Object = MibTableColumn
portConfigFailover = _PortConfigFailover_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 4, 1, 1, 8),
    _PortConfigFailover_Type()
)
portConfigFailover.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portConfigFailover.setStatus("current")
_PortConfigLDSMode_Type = LinkDownMode
_PortConfigLDSMode_Object = MibTableColumn
portConfigLDSMode = _PortConfigLDSMode_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 4, 1, 1, 9),
    _PortConfigLDSMode_Type()
)
portConfigLDSMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portConfigLDSMode.setStatus("current")
_PortConfigLDSTimeout_Type = Unsigned32
_PortConfigLDSTimeout_Object = MibTableColumn
portConfigLDSTimeout = _PortConfigLDSTimeout_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 4, 1, 1, 10),
    _PortConfigLDSTimeout_Type()
)
portConfigLDSTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portConfigLDSTimeout.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPT-PORT-CONFIG-MIB",
    **{"LineSpeed": LineSpeed,
       "DuplexSetting": DuplexSetting,
       "AutoNegotiation": AutoNegotiation,
       "EnabledOrNot": EnabledOrNot,
       "FailoverAction": FailoverAction,
       "LinkDownMode": LinkDownMode,
       "tpt-port-config-objs": tpt_port_config_objs,
       "portConfigTable": portConfigTable,
       "portConfigEntry": portConfigEntry,
       "portConfigSlot": portConfigSlot,
       "portConfigPort": portConfigPort,
       "portConfigLineSpeed": portConfigLineSpeed,
       "portConfigDuplex": portConfigDuplex,
       "portConfigAutoNeg": portConfigAutoNeg,
       "portConfigShutdown": portConfigShutdown,
       "portConfigLoopback": portConfigLoopback,
       "portConfigFailover": portConfigFailover,
       "portConfigLDSMode": portConfigLDSMode,
       "portConfigLDSTimeout": portConfigLDSTimeout}
)
