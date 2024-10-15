# SNMP MIB module (TPLINK-STACK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TPLINK-STACK-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:06:43 2024
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

tplinkStackMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 34)
)
tplinkStackMIB.setRevisions(
        ("2012-11-29 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TplinkStackMIBObjects_ObjectIdentity = ObjectIdentity
tplinkStackMIBObjects = _TplinkStackMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 34, 1)
)
_TpStackGlobal_ObjectIdentity = ObjectIdentity
tpStackGlobal = _TpStackGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 34, 1, 1)
)


class _TpStackName_Type(DisplayString):
    """Custom type tpStackName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TpStackName_Type.__name__ = "DisplayString"
_TpStackName_Object = MibScalar
tpStackName = _TpStackName_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 34, 1, 1, 1),
    _TpStackName_Type()
)
tpStackName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpStackName.setStatus("current")


class _TpStackMacAddress_Type(DisplayString):
    """Custom type tpStackMacAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TpStackMacAddress_Type.__name__ = "DisplayString"
_TpStackMacAddress_Object = MibScalar
tpStackMacAddress = _TpStackMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 34, 1, 1, 2),
    _TpStackMacAddress_Type()
)
tpStackMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpStackMacAddress.setStatus("current")


class _TpStackTopo_Type(Integer32):
    """Custom type tpStackTopo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("line", 0),
          ("ring", 1))
    )


_TpStackTopo_Type.__name__ = "Integer32"
_TpStackTopo_Object = MibScalar
tpStackTopo = _TpStackTopo_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 34, 1, 1, 3),
    _TpStackTopo_Type()
)
tpStackTopo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpStackTopo.setStatus("current")


class _TpStackAuthMode_Type(Integer32):
    """Custom type tpStackAuthMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("md5", 2),
          ("none", 0),
          ("simple", 1))
    )


_TpStackAuthMode_Type.__name__ = "Integer32"
_TpStackAuthMode_Object = MibScalar
tpStackAuthMode = _TpStackAuthMode_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 34, 1, 1, 4),
    _TpStackAuthMode_Type()
)
tpStackAuthMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpStackAuthMode.setStatus("current")


class _TpStackAuthKey_Type(DisplayString):
    """Custom type tpStackAuthKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TpStackAuthKey_Type.__name__ = "DisplayString"
_TpStackAuthKey_Object = MibScalar
tpStackAuthKey = _TpStackAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 34, 1, 1, 5),
    _TpStackAuthKey_Type()
)
tpStackAuthKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpStackAuthKey.setStatus("current")
_TpStackInfo_ObjectIdentity = ObjectIdentity
tpStackInfo = _TpStackInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 34, 1, 2)
)
_TpSwitchInfoTable_Object = MibTable
tpSwitchInfoTable = _TpSwitchInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 34, 1, 2, 1)
)
if mibBuilder.loadTexts:
    tpSwitchInfoTable.setStatus("current")
_TpSwitchInfoEntry_Object = MibTableRow
tpSwitchInfoEntry = _TpSwitchInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 34, 1, 2, 1, 1)
)
tpSwitchInfoEntry.setIndexNames(
    (0, "TPLINK-STACK-MIB", "tpSwitchCurrentUnit"),
)
if mibBuilder.loadTexts:
    tpSwitchInfoEntry.setStatus("current")


class _TpSwitchCurrentUnit_Type(Integer32):
    """Custom type tpSwitchCurrentUnit based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("unit-1", 1),
          ("unit-2", 2),
          ("unit-3", 3),
          ("unit-4", 4),
          ("unit-5", 5),
          ("unit-6", 6),
          ("unit-7", 7),
          ("unit-8", 8))
    )


_TpSwitchCurrentUnit_Type.__name__ = "Integer32"
_TpSwitchCurrentUnit_Object = MibTableColumn
tpSwitchCurrentUnit = _TpSwitchCurrentUnit_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 34, 1, 2, 1, 1, 1),
    _TpSwitchCurrentUnit_Type()
)
tpSwitchCurrentUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpSwitchCurrentUnit.setStatus("current")


class _TpSwitchDesignatedUnit_Type(Integer32):
    """Custom type tpSwitchDesignatedUnit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("auto", -1),
          ("unit-1", 1),
          ("unit-2", 2),
          ("unit-3", 3),
          ("unit-4", 4),
          ("unit-5", 5),
          ("unit-6", 6),
          ("unit-7", 7),
          ("unit-8", 8))
    )


_TpSwitchDesignatedUnit_Type.__name__ = "Integer32"
_TpSwitchDesignatedUnit_Object = MibTableColumn
tpSwitchDesignatedUnit = _TpSwitchDesignatedUnit_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 34, 1, 2, 1, 1, 3),
    _TpSwitchDesignatedUnit_Type()
)
tpSwitchDesignatedUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpSwitchDesignatedUnit.setStatus("current")


class _TpSwitchRole_Type(Integer32):
    """Custom type tpSwitchRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("master", 1),
          ("slave", 0))
    )


_TpSwitchRole_Type.__name__ = "Integer32"
_TpSwitchRole_Object = MibTableColumn
tpSwitchRole = _TpSwitchRole_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 34, 1, 2, 1, 1, 4),
    _TpSwitchRole_Type()
)
tpSwitchRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpSwitchRole.setStatus("current")


class _TpSwitchPriority_Type(Integer32):
    """Custom type tpSwitchPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_TpSwitchPriority_Type.__name__ = "Integer32"
_TpSwitchPriority_Object = MibTableColumn
tpSwitchPriority = _TpSwitchPriority_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 34, 1, 2, 1, 1, 5),
    _TpSwitchPriority_Type()
)
tpSwitchPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpSwitchPriority.setStatus("current")


class _TpSwitchMacAddress_Type(DisplayString):
    """Custom type tpSwitchMacAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TpSwitchMacAddress_Type.__name__ = "DisplayString"
_TpSwitchMacAddress_Object = MibTableColumn
tpSwitchMacAddress = _TpSwitchMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 34, 1, 2, 1, 1, 6),
    _TpSwitchMacAddress_Type()
)
tpSwitchMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpSwitchMacAddress.setStatus("current")


class _TpSwitchVersion_Type(DisplayString):
    """Custom type tpSwitchVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TpSwitchVersion_Type.__name__ = "DisplayString"
_TpSwitchVersion_Object = MibTableColumn
tpSwitchVersion = _TpSwitchVersion_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 34, 1, 2, 1, 1, 7),
    _TpSwitchVersion_Type()
)
tpSwitchVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpSwitchVersion.setStatus("current")


class _TpSwitchState_Type(Integer32):
    """Custom type tpSwitchState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("disc", 2),
          ("init", 1),
          ("ready", 4),
          ("sync", 3),
          ("verMismatch", 5))
    )


_TpSwitchState_Type.__name__ = "Integer32"
_TpSwitchState_Object = MibTableColumn
tpSwitchState = _TpSwitchState_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 34, 1, 2, 1, 1, 8),
    _TpSwitchState_Type()
)
tpSwitchState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpSwitchState.setStatus("current")
_TpStackPortInfoTable_Object = MibTable
tpStackPortInfoTable = _TpStackPortInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 34, 1, 2, 2)
)
if mibBuilder.loadTexts:
    tpStackPortInfoTable.setStatus("current")
_TpStackPortInfoEntry_Object = MibTableRow
tpStackPortInfoEntry = _TpStackPortInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 34, 1, 2, 2, 1)
)
tpStackPortInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tpStackPortInfoEntry.setStatus("current")


class _TpStackPortEnable_Type(Integer32):
    """Custom type tpStackPortEnable based on Integer32"""
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


_TpStackPortEnable_Type.__name__ = "Integer32"
_TpStackPortEnable_Object = MibTableColumn
tpStackPortEnable = _TpStackPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 34, 1, 2, 2, 1, 1),
    _TpStackPortEnable_Type()
)
tpStackPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpStackPortEnable.setStatus("current")


class _TpStackPortStatus_Type(Integer32):
    """Custom type tpStackPortStatus based on Integer32"""
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
        *(("authFail", 3),
          ("down", 2),
          ("ethernet", 4),
          ("ok", 1))
    )


_TpStackPortStatus_Type.__name__ = "Integer32"
_TpStackPortStatus_Object = MibTableColumn
tpStackPortStatus = _TpStackPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 34, 1, 2, 2, 1, 2),
    _TpStackPortStatus_Type()
)
tpStackPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpStackPortStatus.setStatus("current")


class _TpStackPortNeighbor_Type(DisplayString):
    """Custom type tpStackPortNeighbor based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TpStackPortNeighbor_Type.__name__ = "DisplayString"
_TpStackPortNeighbor_Object = MibTableColumn
tpStackPortNeighbor = _TpStackPortNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 34, 1, 2, 2, 1, 3),
    _TpStackPortNeighbor_Type()
)
tpStackPortNeighbor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpStackPortNeighbor.setStatus("current")
_TplinkStackNotifications_ObjectIdentity = ObjectIdentity
tplinkStackNotifications = _TplinkStackNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 34, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPLINK-STACK-MIB",
    **{"tplinkStackMIB": tplinkStackMIB,
       "tplinkStackMIBObjects": tplinkStackMIBObjects,
       "tpStackGlobal": tpStackGlobal,
       "tpStackName": tpStackName,
       "tpStackMacAddress": tpStackMacAddress,
       "tpStackTopo": tpStackTopo,
       "tpStackAuthMode": tpStackAuthMode,
       "tpStackAuthKey": tpStackAuthKey,
       "tpStackInfo": tpStackInfo,
       "tpSwitchInfoTable": tpSwitchInfoTable,
       "tpSwitchInfoEntry": tpSwitchInfoEntry,
       "tpSwitchCurrentUnit": tpSwitchCurrentUnit,
       "tpSwitchDesignatedUnit": tpSwitchDesignatedUnit,
       "tpSwitchRole": tpSwitchRole,
       "tpSwitchPriority": tpSwitchPriority,
       "tpSwitchMacAddress": tpSwitchMacAddress,
       "tpSwitchVersion": tpSwitchVersion,
       "tpSwitchState": tpSwitchState,
       "tpStackPortInfoTable": tpStackPortInfoTable,
       "tpStackPortInfoEntry": tpStackPortInfoEntry,
       "tpStackPortEnable": tpStackPortEnable,
       "tpStackPortStatus": tpStackPortStatus,
       "tpStackPortNeighbor": tpStackPortNeighbor,
       "tplinkStackNotifications": tplinkStackNotifications}
)
