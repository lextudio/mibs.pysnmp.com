# SNMP MIB module (CLAVISTER-TRAPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CLAVISTER-TRAPS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:15:44 2024
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

(clavisterOSTrap,
 clavisterOSTrapInfo) = mibBuilder.importSymbols(
    "CLAVISTER-SMI",
    "clavisterOSTrap",
    "clavisterOSTrapInfo")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

clavisterOSTrapMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5089, 1, 1, 0)
)
clavisterOSTrapMibModule.setRevisions(
        ("2006-05-19 09:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _ClavisterOSTrapVarSeverity_Type(Integer32):
    """Custom type clavisterOSTrapVarSeverity based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("alert", 1),
          ("critical", 2),
          ("debug", 7),
          ("emergency", 0),
          ("error", 3),
          ("info", 6),
          ("notice", 5),
          ("warning", 4))
    )


_ClavisterOSTrapVarSeverity_Type.__name__ = "Integer32"
_ClavisterOSTrapVarSeverity_Object = MibScalar
clavisterOSTrapVarSeverity = _ClavisterOSTrapVarSeverity_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 1, 4),
    _ClavisterOSTrapVarSeverity_Type()
)
clavisterOSTrapVarSeverity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    clavisterOSTrapVarSeverity.setStatus("current")
_ClavisterOSTrapVarCategory_Type = DisplayString
_ClavisterOSTrapVarCategory_Object = MibScalar
clavisterOSTrapVarCategory = _ClavisterOSTrapVarCategory_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 1, 5),
    _ClavisterOSTrapVarCategory_Type()
)
clavisterOSTrapVarCategory.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    clavisterOSTrapVarCategory.setStatus("current")
_ClavisterOSTrapVarID_Type = DisplayString
_ClavisterOSTrapVarID_Object = MibScalar
clavisterOSTrapVarID = _ClavisterOSTrapVarID_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 1, 6),
    _ClavisterOSTrapVarID_Type()
)
clavisterOSTrapVarID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    clavisterOSTrapVarID.setStatus("current")
_ClavisterOSTrapVarEvent_Type = DisplayString
_ClavisterOSTrapVarEvent_Object = MibScalar
clavisterOSTrapVarEvent = _ClavisterOSTrapVarEvent_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 1, 7),
    _ClavisterOSTrapVarEvent_Type()
)
clavisterOSTrapVarEvent.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    clavisterOSTrapVarEvent.setStatus("current")
_ClavisterOSTrapVarAction_Type = DisplayString
_ClavisterOSTrapVarAction_Object = MibScalar
clavisterOSTrapVarAction = _ClavisterOSTrapVarAction_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 1, 8),
    _ClavisterOSTrapVarAction_Type()
)
clavisterOSTrapVarAction.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    clavisterOSTrapVarAction.setStatus("current")
_ClavisterOSTrapVarTime_Type = DisplayString
_ClavisterOSTrapVarTime_Object = MibScalar
clavisterOSTrapVarTime = _ClavisterOSTrapVarTime_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 1, 9),
    _ClavisterOSTrapVarTime_Type()
)
clavisterOSTrapVarTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    clavisterOSTrapVarTime.setStatus("current")
_ClavisterOSTrapVarMessage_Type = DisplayString
_ClavisterOSTrapVarMessage_Object = MibScalar
clavisterOSTrapVarMessage = _ClavisterOSTrapVarMessage_Object(
    (1, 3, 6, 1, 4, 1, 5089, 1, 1, 10),
    _ClavisterOSTrapVarMessage_Type()
)
clavisterOSTrapVarMessage.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    clavisterOSTrapVarMessage.setStatus("current")

# Managed Objects groups

clavisterOSTrapGroupVar = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5089, 1, 1, 2)
)
clavisterOSTrapGroupVar.setObjects(
      *(("CLAVISTER-TRAPS-MIB", "clavisterOSTrapVarSeverity"),
        ("CLAVISTER-TRAPS-MIB", "clavisterOSTrapVarCategory"),
        ("CLAVISTER-TRAPS-MIB", "clavisterOSTrapVarID"),
        ("CLAVISTER-TRAPS-MIB", "clavisterOSTrapVarEvent"),
        ("CLAVISTER-TRAPS-MIB", "clavisterOSTrapVarAction"),
        ("CLAVISTER-TRAPS-MIB", "clavisterOSTrapVarTime"),
        ("CLAVISTER-TRAPS-MIB", "clavisterOSTrapVarMessage"))
)
if mibBuilder.loadTexts:
    clavisterOSTrapGroupVar.setStatus("current")


# Notification objects

clavisterOSGenericTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5089, 1, 0, 1)
)
clavisterOSGenericTrap.setObjects(
      *(("CLAVISTER-TRAPS-MIB", "clavisterOSTrapVarSeverity"),
        ("CLAVISTER-TRAPS-MIB", "clavisterOSTrapVarCategory"),
        ("CLAVISTER-TRAPS-MIB", "clavisterOSTrapVarID"),
        ("CLAVISTER-TRAPS-MIB", "clavisterOSTrapVarEvent"),
        ("CLAVISTER-TRAPS-MIB", "clavisterOSTrapVarAction"),
        ("CLAVISTER-TRAPS-MIB", "clavisterOSTrapVarTime"),
        ("CLAVISTER-TRAPS-MIB", "clavisterOSTrapVarMessage"))
)
if mibBuilder.loadTexts:
    clavisterOSGenericTrap.setStatus(
        "current"
    )


# Notifications groups

clavisterOSTrapGroupTrap = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 5089, 1, 1, 1)
)
clavisterOSTrapGroupTrap.setObjects(
    ("CLAVISTER-TRAPS-MIB", "clavisterOSGenericTrap")
)
if mibBuilder.loadTexts:
    clavisterOSTrapGroupTrap.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

clavisterOSTrapCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5089, 1, 1, 3)
)
if mibBuilder.loadTexts:
    clavisterOSTrapCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CLAVISTER-TRAPS-MIB",
    **{"clavisterOSGenericTrap": clavisterOSGenericTrap,
       "clavisterOSTrapMibModule": clavisterOSTrapMibModule,
       "clavisterOSTrapGroupTrap": clavisterOSTrapGroupTrap,
       "clavisterOSTrapGroupVar": clavisterOSTrapGroupVar,
       "clavisterOSTrapCompliance": clavisterOSTrapCompliance,
       "clavisterOSTrapVarSeverity": clavisterOSTrapVarSeverity,
       "clavisterOSTrapVarCategory": clavisterOSTrapVarCategory,
       "clavisterOSTrapVarID": clavisterOSTrapVarID,
       "clavisterOSTrapVarEvent": clavisterOSTrapVarEvent,
       "clavisterOSTrapVarAction": clavisterOSTrapVarAction,
       "clavisterOSTrapVarTime": clavisterOSTrapVarTime,
       "clavisterOSTrapVarMessage": clavisterOSTrapVarMessage}
)
