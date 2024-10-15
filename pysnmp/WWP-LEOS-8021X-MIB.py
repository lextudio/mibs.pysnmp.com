# SNMP MIB module (WWP-LEOS-8021X-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WWP-LEOS-8021X-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:14:44 2024
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")

(wwpModulesLeos,) = mibBuilder.importSymbols(
    "WWP-SMI",
    "wwpModulesLeos")


# MODULE-IDENTITY

wwpLeos8021xMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 401)
)
wwpLeos8021xMibModule.setRevisions(
        ("2005-08-28 19:35",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WwpLeos8021xMIB_ObjectIdentity = ObjectIdentity
wwpLeos8021xMIB = _WwpLeos8021xMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 401, 1)
)
_WwpLeos8021xConf_ObjectIdentity = ObjectIdentity
wwpLeos8021xConf = _WwpLeos8021xConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 401, 1, 1)
)
_WwpLeos8021xGroups_ObjectIdentity = ObjectIdentity
wwpLeos8021xGroups = _WwpLeos8021xGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 401, 1, 1, 1)
)
_WwpLeos8021xCompls_ObjectIdentity = ObjectIdentity
wwpLeos8021xCompls = _WwpLeos8021xCompls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 401, 1, 1, 2)
)
_WwpLeos8021xObjs_ObjectIdentity = ObjectIdentity
wwpLeos8021xObjs = _WwpLeos8021xObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 401, 1, 2)
)
_WwpLeos8021xPortTable_Object = MibTable
wwpLeos8021xPortTable = _WwpLeos8021xPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 401, 1, 2, 1)
)
if mibBuilder.loadTexts:
    wwpLeos8021xPortTable.setStatus("current")
_WwpLeos8021xPortEntry_Object = MibTableRow
wwpLeos8021xPortEntry = _WwpLeos8021xPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 401, 1, 2, 1, 1)
)
wwpLeos8021xPortEntry.setIndexNames(
    (0, "WWP-LEOS-8021X-MIB", "wwpLeos8021xPort"),
)
if mibBuilder.loadTexts:
    wwpLeos8021xPortEntry.setStatus("current")


class _WwpLeos8021xPort_Type(Integer32):
    """Custom type wwpLeos8021xPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_WwpLeos8021xPort_Type.__name__ = "Integer32"
_WwpLeos8021xPort_Object = MibTableColumn
wwpLeos8021xPort = _WwpLeos8021xPort_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 401, 1, 2, 1, 1, 1),
    _WwpLeos8021xPort_Type()
)
wwpLeos8021xPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeos8021xPort.setStatus("current")


class _WwpLeos8021xRole_Type(Integer32):
    """Custom type wwpLeos8021xRole based on Integer32"""
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
        *(("authenticator", 3),
          ("both", 4),
          ("none", 1),
          ("supplicant", 2))
    )


_WwpLeos8021xRole_Type.__name__ = "Integer32"
_WwpLeos8021xRole_Object = MibTableColumn
wwpLeos8021xRole = _WwpLeos8021xRole_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 401, 1, 2, 1, 1, 2),
    _WwpLeos8021xRole_Type()
)
wwpLeos8021xRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeos8021xRole.setStatus("current")
_WwpLeos8021xAuthPortStatsClear_Type = TruthValue
_WwpLeos8021xAuthPortStatsClear_Object = MibTableColumn
wwpLeos8021xAuthPortStatsClear = _WwpLeos8021xAuthPortStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 401, 1, 2, 1, 1, 3),
    _WwpLeos8021xAuthPortStatsClear_Type()
)
wwpLeos8021xAuthPortStatsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeos8021xAuthPortStatsClear.setStatus("current")
_WwpLeos8021xSuppTable_Object = MibTable
wwpLeos8021xSuppTable = _WwpLeos8021xSuppTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 401, 1, 2, 2)
)
if mibBuilder.loadTexts:
    wwpLeos8021xSuppTable.setStatus("current")
_WwpLeos8021xSuppEntry_Object = MibTableRow
wwpLeos8021xSuppEntry = _WwpLeos8021xSuppEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 401, 1, 2, 2, 1)
)
wwpLeos8021xSuppEntry.setIndexNames(
    (0, "WWP-LEOS-8021X-MIB", "wwpLeos8021xSuppPort"),
)
if mibBuilder.loadTexts:
    wwpLeos8021xSuppEntry.setStatus("current")


class _WwpLeos8021xSuppPort_Type(Integer32):
    """Custom type wwpLeos8021xSuppPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_WwpLeos8021xSuppPort_Type.__name__ = "Integer32"
_WwpLeos8021xSuppPort_Object = MibTableColumn
wwpLeos8021xSuppPort = _WwpLeos8021xSuppPort_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 401, 1, 2, 2, 1, 1),
    _WwpLeos8021xSuppPort_Type()
)
wwpLeos8021xSuppPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeos8021xSuppPort.setStatus("current")


class _WwpLeos8021xSuppUserName_Type(DisplayString):
    """Custom type wwpLeos8021xSuppUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_WwpLeos8021xSuppUserName_Type.__name__ = "DisplayString"
_WwpLeos8021xSuppUserName_Object = MibTableColumn
wwpLeos8021xSuppUserName = _WwpLeos8021xSuppUserName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 401, 1, 2, 2, 1, 2),
    _WwpLeos8021xSuppUserName_Type()
)
wwpLeos8021xSuppUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeos8021xSuppUserName.setStatus("current")


class _WwpLeos8021xSuppPassword_Type(DisplayString):
    """Custom type wwpLeos8021xSuppPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_WwpLeos8021xSuppPassword_Type.__name__ = "DisplayString"
_WwpLeos8021xSuppPassword_Object = MibTableColumn
wwpLeos8021xSuppPassword = _WwpLeos8021xSuppPassword_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 401, 1, 2, 2, 1, 3),
    _WwpLeos8021xSuppPassword_Type()
)
wwpLeos8021xSuppPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeos8021xSuppPassword.setStatus("current")
_WwpLeos8021xSuppPortStatsClear_Type = TruthValue
_WwpLeos8021xSuppPortStatsClear_Object = MibTableColumn
wwpLeos8021xSuppPortStatsClear = _WwpLeos8021xSuppPortStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 401, 1, 2, 2, 1, 5),
    _WwpLeos8021xSuppPortStatsClear_Type()
)
wwpLeos8021xSuppPortStatsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeos8021xSuppPortStatsClear.setStatus("current")


class _WwpLeos8021xSuppEAPMethod_Type(Integer32):
    """Custom type wwpLeos8021xSuppEAPMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("eapMd5", 1)
    )


_WwpLeos8021xSuppEAPMethod_Type.__name__ = "Integer32"
_WwpLeos8021xSuppEAPMethod_Object = MibTableColumn
wwpLeos8021xSuppEAPMethod = _WwpLeos8021xSuppEAPMethod_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 401, 1, 2, 2, 1, 10),
    _WwpLeos8021xSuppEAPMethod_Type()
)
wwpLeos8021xSuppEAPMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeos8021xSuppEAPMethod.setStatus("current")
_WwpLeos8021xGlobalAttrs_ObjectIdentity = ObjectIdentity
wwpLeos8021xGlobalAttrs = _WwpLeos8021xGlobalAttrs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 401, 1, 2, 3)
)
_WwpLeos8021xAuthStatsClear_Type = TruthValue
_WwpLeos8021xAuthStatsClear_Object = MibScalar
wwpLeos8021xAuthStatsClear = _WwpLeos8021xAuthStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 401, 1, 2, 3, 1),
    _WwpLeos8021xAuthStatsClear_Type()
)
wwpLeos8021xAuthStatsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeos8021xAuthStatsClear.setStatus("current")
_WwpLeos8021xSuppStatsClear_Type = TruthValue
_WwpLeos8021xSuppStatsClear_Object = MibScalar
wwpLeos8021xSuppStatsClear = _WwpLeos8021xSuppStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 401, 1, 2, 3, 2),
    _WwpLeos8021xSuppStatsClear_Type()
)
wwpLeos8021xSuppStatsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeos8021xSuppStatsClear.setStatus("current")
_WwpLeos8021xEvents_ObjectIdentity = ObjectIdentity
wwpLeos8021xEvents = _WwpLeos8021xEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 401, 1, 3)
)
_WwpLeos8021xEventsV2_ObjectIdentity = ObjectIdentity
wwpLeos8021xEventsV2 = _WwpLeos8021xEventsV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 401, 1, 3, 0)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WWP-LEOS-8021X-MIB",
    **{"wwpLeos8021xMibModule": wwpLeos8021xMibModule,
       "wwpLeos8021xMIB": wwpLeos8021xMIB,
       "wwpLeos8021xConf": wwpLeos8021xConf,
       "wwpLeos8021xGroups": wwpLeos8021xGroups,
       "wwpLeos8021xCompls": wwpLeos8021xCompls,
       "wwpLeos8021xObjs": wwpLeos8021xObjs,
       "wwpLeos8021xPortTable": wwpLeos8021xPortTable,
       "wwpLeos8021xPortEntry": wwpLeos8021xPortEntry,
       "wwpLeos8021xPort": wwpLeos8021xPort,
       "wwpLeos8021xRole": wwpLeos8021xRole,
       "wwpLeos8021xAuthPortStatsClear": wwpLeos8021xAuthPortStatsClear,
       "wwpLeos8021xSuppTable": wwpLeos8021xSuppTable,
       "wwpLeos8021xSuppEntry": wwpLeos8021xSuppEntry,
       "wwpLeos8021xSuppPort": wwpLeos8021xSuppPort,
       "wwpLeos8021xSuppUserName": wwpLeos8021xSuppUserName,
       "wwpLeos8021xSuppPassword": wwpLeos8021xSuppPassword,
       "wwpLeos8021xSuppPortStatsClear": wwpLeos8021xSuppPortStatsClear,
       "wwpLeos8021xSuppEAPMethod": wwpLeos8021xSuppEAPMethod,
       "wwpLeos8021xGlobalAttrs": wwpLeos8021xGlobalAttrs,
       "wwpLeos8021xAuthStatsClear": wwpLeos8021xAuthStatsClear,
       "wwpLeos8021xSuppStatsClear": wwpLeos8021xSuppStatsClear,
       "wwpLeos8021xEvents": wwpLeos8021xEvents,
       "wwpLeos8021xEventsV2": wwpLeos8021xEventsV2}
)
