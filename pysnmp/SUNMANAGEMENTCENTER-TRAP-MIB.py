# SNMP MIB module (SUNMANAGEMENTCENTER-TRAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SUNMANAGEMENTCENTER-TRAP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:58:39 2024
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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

traps = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 0)
)
traps.setRevisions(
        ("1999-07-20 15:05",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Sun_ObjectIdentity = ObjectIdentity
sun = _Sun_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42)
)
_Prod_ObjectIdentity = ObjectIdentity
prod = _Prod_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2)
)
_Sunsymon_ObjectIdentity = ObjectIdentity
sunsymon = _Sunsymon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12)
)
_Agent_ObjectIdentity = ObjectIdentity
agent = _Agent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2)
)
_Base_ObjectIdentity = ObjectIdentity
base = _Base_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 1)
)
_StatusOID_Type = ObjectIdentifier
_StatusOID_Object = MibScalar
statusOID = _StatusOID_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 1, 3, 1),
    _StatusOID_Type()
)
statusOID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    statusOID.setStatus("current")
_RefreshOID_Type = ObjectIdentifier
_RefreshOID_Object = MibScalar
refreshOID = _RefreshOID_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 1, 3, 2),
    _RefreshOID_Type()
)
refreshOID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    refreshOID.setStatus("current")
_ModuleInfo_Type = OctetString
_ModuleInfo_Object = MibScalar
moduleInfo = _ModuleInfo_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 1, 3, 5),
    _ModuleInfo_Type()
)
moduleInfo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    moduleInfo.setStatus("current")

# Managed Objects groups

trapInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 1, 3)
)
trapInfoGroup.setObjects(
      *(("SUNMANAGEMENTCENTER-TRAP-MIB", "statusOID"),
        ("SUNMANAGEMENTCENTER-TRAP-MIB", "refreshOID"),
        ("SUNMANAGEMENTCENTER-TRAP-MIB", "moduleInfo"))
)
if mibBuilder.loadTexts:
    trapInfoGroup.setStatus("current")


# Notification objects

statusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 0, 1)
)
statusChange.setObjects(
    ("SUNMANAGEMENTCENTER-TRAP-MIB", "statusOID")
)
if mibBuilder.loadTexts:
    statusChange.setStatus(
        "current"
    )

valueRefresh = NotificationType(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 0, 2)
)
valueRefresh.setObjects(
    ("SUNMANAGEMENTCENTER-TRAP-MIB", "refreshOID")
)
if mibBuilder.loadTexts:
    valueRefresh.setStatus(
        "current"
    )

moduleLoaded = NotificationType(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 0, 4)
)
moduleLoaded.setObjects(
    ("SUNMANAGEMENTCENTER-TRAP-MIB", "moduleInfo")
)
if mibBuilder.loadTexts:
    moduleLoaded.setStatus(
        "current"
    )

moduleUnloaded = NotificationType(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 0, 5)
)
moduleUnloaded.setObjects(
    ("SUNMANAGEMENTCENTER-TRAP-MIB", "moduleInfo")
)
if mibBuilder.loadTexts:
    moduleUnloaded.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SUNMANAGEMENTCENTER-TRAP-MIB",
    **{"sun": sun,
       "prod": prod,
       "sunsymon": sunsymon,
       "agent": agent,
       "traps": traps,
       "statusChange": statusChange,
       "valueRefresh": valueRefresh,
       "moduleLoaded": moduleLoaded,
       "moduleUnloaded": moduleUnloaded,
       "base": base,
       "trapInfoGroup": trapInfoGroup,
       "statusOID": statusOID,
       "refreshOID": refreshOID,
       "moduleInfo": moduleInfo}
)
