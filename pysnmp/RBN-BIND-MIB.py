# SNMP MIB module (RBN-BIND-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RBN-BIND-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:44:57 2024
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

(rbnMgmt,) = mibBuilder.importSymbols(
    "RBN-SMI",
    "rbnMgmt")

(RbnCircuitHandle,
 RbnPort,
 RbnSlot) = mibBuilder.importSymbols(
    "RBN-TC",
    "RbnCircuitHandle",
    "RbnPort",
    "RbnSlot")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

rbnBindMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 17)
)
rbnBindMib.setRevisions(
        ("2003-10-13 17:00",
         "2003-03-07 17:00",
         "2002-11-13 00:00",
         "2002-07-25 17:00",
         "2002-01-07 17:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class RbnBindType(Integer32, TextualConvention):
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("authBind", 2),
          ("bypassBind", 3),
          ("dot1qBind", 8),
          ("interfaceBind", 4),
          ("l2tptunnelBind", 6),
          ("multiClipsBind", 11),
          ("multiIntfBind", 9),
          ("multiSubBind", 10),
          ("sessionBind", 7),
          ("subscriberBind", 5),
          ("unbound", 1))
    )



# MIB Managed Objects in the order of their OIDs

_RbnBindMIBObjects_ObjectIdentity = ObjectIdentity
rbnBindMIBObjects = _RbnBindMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 17, 1)
)
_RbnBindTable_Object = MibTable
rbnBindTable = _RbnBindTable_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 17, 1, 1)
)
if mibBuilder.loadTexts:
    rbnBindTable.setStatus("current")
_RbnBindEntry_Object = MibTableRow
rbnBindEntry = _RbnBindEntry_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 17, 1, 1, 1)
)
rbnBindEntry.setIndexNames(
    (0, "RBN-BIND-MIB", "rbnBindCircuit"),
)
if mibBuilder.loadTexts:
    rbnBindEntry.setStatus("current")
_RbnBindCircuit_Type = RbnCircuitHandle
_RbnBindCircuit_Object = MibTableColumn
rbnBindCircuit = _RbnBindCircuit_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 17, 1, 1, 1, 1),
    _RbnBindCircuit_Type()
)
rbnBindCircuit.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbnBindCircuit.setStatus("current")
_RbnBindType_Type = RbnBindType
_RbnBindType_Object = MibTableColumn
rbnBindType = _RbnBindType_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 17, 1, 1, 1, 2),
    _RbnBindType_Type()
)
rbnBindType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnBindType.setStatus("current")


class _RbnBindName_Type(SnmpAdminString):
    """Custom type rbnBindName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 192),
    )


_RbnBindName_Type.__name__ = "SnmpAdminString"
_RbnBindName_Object = MibTableColumn
rbnBindName = _RbnBindName_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 17, 1, 1, 1, 3),
    _RbnBindName_Type()
)
rbnBindName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnBindName.setStatus("current")


class _RbnBindPassword_Type(SnmpAdminString):
    """Custom type rbnBindPassword based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_RbnBindPassword_Type.__name__ = "SnmpAdminString"
_RbnBindPassword_Object = MibTableColumn
rbnBindPassword = _RbnBindPassword_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 17, 1, 1, 1, 4),
    _RbnBindPassword_Type()
)
rbnBindPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnBindPassword.setStatus("current")


class _RbnBindContext_Type(SnmpAdminString):
    """Custom type rbnBindContext based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_RbnBindContext_Type.__name__ = "SnmpAdminString"
_RbnBindContext_Object = MibTableColumn
rbnBindContext = _RbnBindContext_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 17, 1, 1, 1, 5),
    _RbnBindContext_Type()
)
rbnBindContext.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnBindContext.setStatus("current")


class _RbnBindAuthContext_Type(SnmpAdminString):
    """Custom type rbnBindAuthContext based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_RbnBindAuthContext_Type.__name__ = "SnmpAdminString"
_RbnBindAuthContext_Object = MibTableColumn
rbnBindAuthContext = _RbnBindAuthContext_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 17, 1, 1, 1, 6),
    _RbnBindAuthContext_Type()
)
rbnBindAuthContext.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnBindAuthContext.setStatus("current")


class _RbnBindServiceGrp_Type(SnmpAdminString):
    """Custom type rbnBindServiceGrp based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_RbnBindServiceGrp_Type.__name__ = "SnmpAdminString"
_RbnBindServiceGrp_Object = MibTableColumn
rbnBindServiceGrp = _RbnBindServiceGrp_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 17, 1, 1, 1, 7),
    _RbnBindServiceGrp_Type()
)
rbnBindServiceGrp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnBindServiceGrp.setStatus("current")


class _RbnBindAcl_Type(SnmpAdminString):
    """Custom type rbnBindAcl based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_RbnBindAcl_Type.__name__ = "SnmpAdminString"
_RbnBindAcl_Object = MibTableColumn
rbnBindAcl = _RbnBindAcl_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 17, 1, 1, 1, 8),
    _RbnBindAcl_Type()
)
rbnBindAcl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnBindAcl.setStatus("current")
_RbnBindAuthChap_Type = TruthValue
_RbnBindAuthChap_Object = MibTableColumn
rbnBindAuthChap = _RbnBindAuthChap_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 17, 1, 1, 1, 9),
    _RbnBindAuthChap_Type()
)
rbnBindAuthChap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnBindAuthChap.setStatus("current")
_RbnBindAuthPap_Type = TruthValue
_RbnBindAuthPap_Object = MibTableColumn
rbnBindAuthPap = _RbnBindAuthPap_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 17, 1, 1, 1, 10),
    _RbnBindAuthPap_Type()
)
rbnBindAuthPap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnBindAuthPap.setStatus("current")
_RbnBindAuthWait_Type = TruthValue
_RbnBindAuthWait_Object = MibTableColumn
rbnBindAuthWait = _RbnBindAuthWait_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 17, 1, 1, 1, 11),
    _RbnBindAuthWait_Type()
)
rbnBindAuthWait.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnBindAuthWait.setStatus("current")
_RbnBindAuthPapFirst_Type = TruthValue
_RbnBindAuthPapFirst_Object = MibTableColumn
rbnBindAuthPapFirst = _RbnBindAuthPapFirst_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 17, 1, 1, 1, 12),
    _RbnBindAuthPapFirst_Type()
)
rbnBindAuthPapFirst.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnBindAuthPapFirst.setStatus("current")


class _RbnBindMaxSessions_Type(Unsigned32):
    """Custom type rbnBindMaxSessions based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RbnBindMaxSessions_Type.__name__ = "Unsigned32"
_RbnBindMaxSessions_Object = MibTableColumn
rbnBindMaxSessions = _RbnBindMaxSessions_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 17, 1, 1, 1, 13),
    _RbnBindMaxSessions_Type()
)
rbnBindMaxSessions.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnBindMaxSessions.setStatus("current")
_RbnBindPvcSlot_Type = RbnSlot
_RbnBindPvcSlot_Object = MibTableColumn
rbnBindPvcSlot = _RbnBindPvcSlot_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 17, 1, 1, 1, 14),
    _RbnBindPvcSlot_Type()
)
rbnBindPvcSlot.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnBindPvcSlot.setStatus("current")
_RbnBindPvcPort_Type = RbnPort
_RbnBindPvcPort_Object = MibTableColumn
rbnBindPvcPort = _RbnBindPvcPort_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 17, 1, 1, 1, 15),
    _RbnBindPvcPort_Type()
)
rbnBindPvcPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnBindPvcPort.setStatus("current")


class _RbnBindVpn_Type(Unsigned32):
    """Custom type rbnBindVpn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 4094),
    )


_RbnBindVpn_Type.__name__ = "Unsigned32"
_RbnBindVpn_Object = MibTableColumn
rbnBindVpn = _RbnBindVpn_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 17, 1, 1, 1, 16),
    _RbnBindVpn_Type()
)
rbnBindVpn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnBindVpn.setStatus("current")
_RbnBindAuthDhcp_Type = TruthValue
_RbnBindAuthDhcp_Object = MibTableColumn
rbnBindAuthDhcp = _RbnBindAuthDhcp_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 17, 1, 1, 1, 17),
    _RbnBindAuthDhcp_Type()
)
rbnBindAuthDhcp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnBindAuthDhcp.setStatus("current")
_RbnBindMIBConformance_ObjectIdentity = ObjectIdentity
rbnBindMIBConformance = _RbnBindMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 17, 2)
)
_RbnBindCompliances_ObjectIdentity = ObjectIdentity
rbnBindCompliances = _RbnBindCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 17, 2, 1)
)
_RbnBindGroups_ObjectIdentity = ObjectIdentity
rbnBindGroups = _RbnBindGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 17, 2, 2)
)
_RbnBindMIBNotifications_ObjectIdentity = ObjectIdentity
rbnBindMIBNotifications = _RbnBindMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 17, 3)
)

# Managed Objects groups

rbnBindConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 17, 2, 2, 1)
)
rbnBindConfigGroup.setObjects(
      *(("RBN-BIND-MIB", "rbnBindType"),
        ("RBN-BIND-MIB", "rbnBindName"),
        ("RBN-BIND-MIB", "rbnBindContext"),
        ("RBN-BIND-MIB", "rbnBindPassword"),
        ("RBN-BIND-MIB", "rbnBindAuthContext"),
        ("RBN-BIND-MIB", "rbnBindServiceGrp"),
        ("RBN-BIND-MIB", "rbnBindAcl"),
        ("RBN-BIND-MIB", "rbnBindAuthChap"),
        ("RBN-BIND-MIB", "rbnBindAuthPap"),
        ("RBN-BIND-MIB", "rbnBindAuthWait"),
        ("RBN-BIND-MIB", "rbnBindAuthPapFirst"),
        ("RBN-BIND-MIB", "rbnBindMaxSessions"),
        ("RBN-BIND-MIB", "rbnBindPvcSlot"),
        ("RBN-BIND-MIB", "rbnBindPvcPort"),
        ("RBN-BIND-MIB", "rbnBindVpn"))
)
if mibBuilder.loadTexts:
    rbnBindConfigGroup.setStatus("deprecated")

rbnBindConfigGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 17, 2, 2, 2)
)
rbnBindConfigGroup2.setObjects(
      *(("RBN-BIND-MIB", "rbnBindType"),
        ("RBN-BIND-MIB", "rbnBindName"),
        ("RBN-BIND-MIB", "rbnBindContext"),
        ("RBN-BIND-MIB", "rbnBindPassword"),
        ("RBN-BIND-MIB", "rbnBindAuthContext"),
        ("RBN-BIND-MIB", "rbnBindServiceGrp"),
        ("RBN-BIND-MIB", "rbnBindAcl"),
        ("RBN-BIND-MIB", "rbnBindAuthChap"),
        ("RBN-BIND-MIB", "rbnBindAuthPap"),
        ("RBN-BIND-MIB", "rbnBindAuthWait"),
        ("RBN-BIND-MIB", "rbnBindAuthPapFirst"),
        ("RBN-BIND-MIB", "rbnBindMaxSessions"),
        ("RBN-BIND-MIB", "rbnBindPvcSlot"),
        ("RBN-BIND-MIB", "rbnBindPvcPort"),
        ("RBN-BIND-MIB", "rbnBindVpn"),
        ("RBN-BIND-MIB", "rbnBindAuthDhcp"))
)
if mibBuilder.loadTexts:
    rbnBindConfigGroup2.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

rbnBindCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2352, 2, 17, 2, 1, 1)
)
if mibBuilder.loadTexts:
    rbnBindCompliance.setStatus(
        "deprecated"
    )

rbnBindCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2352, 2, 17, 2, 1, 2)
)
if mibBuilder.loadTexts:
    rbnBindCompliance2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RBN-BIND-MIB",
    **{"RbnBindType": RbnBindType,
       "rbnBindMib": rbnBindMib,
       "rbnBindMIBObjects": rbnBindMIBObjects,
       "rbnBindTable": rbnBindTable,
       "rbnBindEntry": rbnBindEntry,
       "rbnBindCircuit": rbnBindCircuit,
       "rbnBindType": rbnBindType,
       "rbnBindName": rbnBindName,
       "rbnBindPassword": rbnBindPassword,
       "rbnBindContext": rbnBindContext,
       "rbnBindAuthContext": rbnBindAuthContext,
       "rbnBindServiceGrp": rbnBindServiceGrp,
       "rbnBindAcl": rbnBindAcl,
       "rbnBindAuthChap": rbnBindAuthChap,
       "rbnBindAuthPap": rbnBindAuthPap,
       "rbnBindAuthWait": rbnBindAuthWait,
       "rbnBindAuthPapFirst": rbnBindAuthPapFirst,
       "rbnBindMaxSessions": rbnBindMaxSessions,
       "rbnBindPvcSlot": rbnBindPvcSlot,
       "rbnBindPvcPort": rbnBindPvcPort,
       "rbnBindVpn": rbnBindVpn,
       "rbnBindAuthDhcp": rbnBindAuthDhcp,
       "rbnBindMIBConformance": rbnBindMIBConformance,
       "rbnBindCompliances": rbnBindCompliances,
       "rbnBindCompliance": rbnBindCompliance,
       "rbnBindCompliance2": rbnBindCompliance2,
       "rbnBindGroups": rbnBindGroups,
       "rbnBindConfigGroup": rbnBindConfigGroup,
       "rbnBindConfigGroup2": rbnBindConfigGroup2,
       "rbnBindMIBNotifications": rbnBindMIBNotifications}
)
