# SNMP MIB module (PDN-RADIUS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PDN-RADIUS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:38:03 2024
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

(pdn_radius,) = mibBuilder.importSymbols(
    "PDN-HEADER-MIB",
    "pdn-radius")

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

_SysDevRadiusMIBObjects_ObjectIdentity = ObjectIdentity
sysDevRadiusMIBObjects = _SysDevRadiusMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 25, 1)
)


class _SysDevRadiusAuthEnable_Type(Integer32):
    """Custom type sysDevRadiusAuthEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_SysDevRadiusAuthEnable_Type.__name__ = "Integer32"
_SysDevRadiusAuthEnable_Object = MibScalar
sysDevRadiusAuthEnable = _SysDevRadiusAuthEnable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 25, 1, 1),
    _SysDevRadiusAuthEnable_Type()
)
sysDevRadiusAuthEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDevRadiusAuthEnable.setStatus("mandatory")


class _SysDevRadiusAuthTimeout_Type(Integer32):
    """Custom type sysDevRadiusAuthTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 30),
    )


_SysDevRadiusAuthTimeout_Type.__name__ = "Integer32"
_SysDevRadiusAuthTimeout_Object = MibScalar
sysDevRadiusAuthTimeout = _SysDevRadiusAuthTimeout_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 25, 1, 2),
    _SysDevRadiusAuthTimeout_Type()
)
sysDevRadiusAuthTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDevRadiusAuthTimeout.setStatus("mandatory")


class _SysDevRadiusAuthAttempts_Type(Integer32):
    """Custom type sysDevRadiusAuthAttempts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_SysDevRadiusAuthAttempts_Type.__name__ = "Integer32"
_SysDevRadiusAuthAttempts_Object = MibScalar
sysDevRadiusAuthAttempts = _SysDevRadiusAuthAttempts_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 25, 1, 3),
    _SysDevRadiusAuthAttempts_Type()
)
sysDevRadiusAuthAttempts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDevRadiusAuthAttempts.setStatus("mandatory")
_SysDevRadiusAuthConfigTable_Object = MibTable
sysDevRadiusAuthConfigTable = _SysDevRadiusAuthConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 25, 1, 4)
)
if mibBuilder.loadTexts:
    sysDevRadiusAuthConfigTable.setStatus("mandatory")
_SysDevRadiusAuthConfigEntry_Object = MibTableRow
sysDevRadiusAuthConfigEntry = _SysDevRadiusAuthConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 25, 1, 4, 1)
)
sysDevRadiusAuthConfigEntry.setIndexNames(
    (0, "PDN-RADIUS-MIB", "sysDevRadiusAuthServerIndex"),
)
if mibBuilder.loadTexts:
    sysDevRadiusAuthConfigEntry.setStatus("mandatory")
_SysDevRadiusAuthServerIndex_Type = Integer32
_SysDevRadiusAuthServerIndex_Object = MibTableColumn
sysDevRadiusAuthServerIndex = _SysDevRadiusAuthServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 25, 1, 4, 1, 1),
    _SysDevRadiusAuthServerIndex_Type()
)
sysDevRadiusAuthServerIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDevRadiusAuthServerIndex.setStatus("mandatory")
_SysDevRadiusAuthServerAddress_Type = IpAddress
_SysDevRadiusAuthServerAddress_Object = MibTableColumn
sysDevRadiusAuthServerAddress = _SysDevRadiusAuthServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 25, 1, 4, 1, 2),
    _SysDevRadiusAuthServerAddress_Type()
)
sysDevRadiusAuthServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDevRadiusAuthServerAddress.setStatus("mandatory")


class _SysDevRadiusAuthServerPort_Type(Integer32):
    """Custom type sysDevRadiusAuthServerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SysDevRadiusAuthServerPort_Type.__name__ = "Integer32"
_SysDevRadiusAuthServerPort_Object = MibTableColumn
sysDevRadiusAuthServerPort = _SysDevRadiusAuthServerPort_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 25, 1, 4, 1, 3),
    _SysDevRadiusAuthServerPort_Type()
)
sysDevRadiusAuthServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDevRadiusAuthServerPort.setStatus("mandatory")


class _SysDevRadiusAuthSecret_Type(DisplayString):
    """Custom type sysDevRadiusAuthSecret based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 32),
    )


_SysDevRadiusAuthSecret_Type.__name__ = "DisplayString"
_SysDevRadiusAuthSecret_Object = MibTableColumn
sysDevRadiusAuthSecret = _SysDevRadiusAuthSecret_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 25, 1, 4, 1, 4),
    _SysDevRadiusAuthSecret_Type()
)
sysDevRadiusAuthSecret.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysDevRadiusAuthSecret.setStatus("mandatory")
_SysDevRadiusMIBTraps_ObjectIdentity = ObjectIdentity
sysDevRadiusMIBTraps = _SysDevRadiusMIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 25, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PDN-RADIUS-MIB",
    **{"sysDevRadiusMIBObjects": sysDevRadiusMIBObjects,
       "sysDevRadiusAuthEnable": sysDevRadiusAuthEnable,
       "sysDevRadiusAuthTimeout": sysDevRadiusAuthTimeout,
       "sysDevRadiusAuthAttempts": sysDevRadiusAuthAttempts,
       "sysDevRadiusAuthConfigTable": sysDevRadiusAuthConfigTable,
       "sysDevRadiusAuthConfigEntry": sysDevRadiusAuthConfigEntry,
       "sysDevRadiusAuthServerIndex": sysDevRadiusAuthServerIndex,
       "sysDevRadiusAuthServerAddress": sysDevRadiusAuthServerAddress,
       "sysDevRadiusAuthServerPort": sysDevRadiusAuthServerPort,
       "sysDevRadiusAuthSecret": sysDevRadiusAuthSecret,
       "sysDevRadiusMIBTraps": sysDevRadiusMIBTraps}
)
