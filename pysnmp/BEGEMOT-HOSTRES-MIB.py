# SNMP MIB module (BEGEMOT-HOSTRES-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BEGEMOT-HOSTRES-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:46:43 2024
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

(begemot,) = mibBuilder.importSymbols(
    "BEGEMOT-MIB",
    "begemot")

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


# MODULE-IDENTITY

begemotHostres = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 12325, 1, 202)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BegemotHostresObjects_ObjectIdentity = ObjectIdentity
begemotHostresObjects = _BegemotHostresObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12325, 1, 202, 1)
)


class _BegemotHrStorageUpdate_Type(TimeTicks):
    """Custom type begemotHrStorageUpdate based on TimeTicks"""
    defaultValue = 700


_BegemotHrStorageUpdate_Object = MibScalar
begemotHrStorageUpdate = _BegemotHrStorageUpdate_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 202, 1, 1),
    _BegemotHrStorageUpdate_Type()
)
begemotHrStorageUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    begemotHrStorageUpdate.setStatus("current")


class _BegemotHrFSUpdate_Type(TimeTicks):
    """Custom type begemotHrFSUpdate based on TimeTicks"""
    defaultValue = 700


_BegemotHrFSUpdate_Object = MibScalar
begemotHrFSUpdate = _BegemotHrFSUpdate_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 202, 1, 2),
    _BegemotHrFSUpdate_Type()
)
begemotHrFSUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    begemotHrFSUpdate.setStatus("current")


class _BegemotHrDiskStorageUpdate_Type(TimeTicks):
    """Custom type begemotHrDiskStorageUpdate based on TimeTicks"""
    defaultValue = 300


_BegemotHrDiskStorageUpdate_Object = MibScalar
begemotHrDiskStorageUpdate = _BegemotHrDiskStorageUpdate_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 202, 1, 3),
    _BegemotHrDiskStorageUpdate_Type()
)
begemotHrDiskStorageUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    begemotHrDiskStorageUpdate.setStatus("current")


class _BegemotHrNetworkUpdate_Type(TimeTicks):
    """Custom type begemotHrNetworkUpdate based on TimeTicks"""
    defaultValue = 700


_BegemotHrNetworkUpdate_Object = MibScalar
begemotHrNetworkUpdate = _BegemotHrNetworkUpdate_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 202, 1, 4),
    _BegemotHrNetworkUpdate_Type()
)
begemotHrNetworkUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    begemotHrNetworkUpdate.setStatus("current")


class _BegemotHrSWInstalledUpdate_Type(TimeTicks):
    """Custom type begemotHrSWInstalledUpdate based on TimeTicks"""
    defaultValue = 1200


_BegemotHrSWInstalledUpdate_Object = MibScalar
begemotHrSWInstalledUpdate = _BegemotHrSWInstalledUpdate_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 202, 1, 5),
    _BegemotHrSWInstalledUpdate_Type()
)
begemotHrSWInstalledUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    begemotHrSWInstalledUpdate.setStatus("current")


class _BegemotHrSWRunUpdate_Type(TimeTicks):
    """Custom type begemotHrSWRunUpdate based on TimeTicks"""
    defaultValue = 300


_BegemotHrSWRunUpdate_Object = MibScalar
begemotHrSWRunUpdate = _BegemotHrSWRunUpdate_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 202, 1, 6),
    _BegemotHrSWRunUpdate_Type()
)
begemotHrSWRunUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    begemotHrSWRunUpdate.setStatus("current")


class _BegemotHrPkgDir_Type(OctetString):
    """Custom type begemotHrPkgDir based on OctetString"""
    defaultValue = OctetString("/var/db/pkg")


_BegemotHrPkgDir_Object = MibScalar
begemotHrPkgDir = _BegemotHrPkgDir_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 202, 1, 7),
    _BegemotHrPkgDir_Type()
)
begemotHrPkgDir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    begemotHrPkgDir.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BEGEMOT-HOSTRES-MIB",
    **{"begemotHostres": begemotHostres,
       "begemotHostresObjects": begemotHostresObjects,
       "begemotHrStorageUpdate": begemotHrStorageUpdate,
       "begemotHrFSUpdate": begemotHrFSUpdate,
       "begemotHrDiskStorageUpdate": begemotHrDiskStorageUpdate,
       "begemotHrNetworkUpdate": begemotHrNetworkUpdate,
       "begemotHrSWInstalledUpdate": begemotHrSWInstalledUpdate,
       "begemotHrSWRunUpdate": begemotHrSWRunUpdate,
       "begemotHrPkgDir": begemotHrPkgDir}
)
