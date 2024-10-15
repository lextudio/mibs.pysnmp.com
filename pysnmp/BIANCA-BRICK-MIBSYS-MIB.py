# SNMP MIB module (BIANCA-BRICK-MIBSYS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BIANCA-BRICK-MIBSYS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:47:34 2024
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


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Org_ObjectIdentity = ObjectIdentity
org = _Org_ObjectIdentity(
    (1, 3)
)
_Dod_ObjectIdentity = ObjectIdentity
dod = _Dod_ObjectIdentity(
    (1, 3, 6)
)
_Internet_ObjectIdentity = ObjectIdentity
internet = _Internet_ObjectIdentity(
    (1, 3, 6, 1)
)
_Private_ObjectIdentity = ObjectIdentity
private = _Private_ObjectIdentity(
    (1, 3, 6, 1, 4)
)
_Enterprises_ObjectIdentity = ObjectIdentity
enterprises = _Enterprises_ObjectIdentity(
    (1, 3, 6, 1, 4, 1)
)
_Bintec_ObjectIdentity = ObjectIdentity
bintec = _Bintec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272)
)
_Bibo_ObjectIdentity = ObjectIdentity
bibo = _Bibo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272, 4)
)
_Sys_ObjectIdentity = ObjectIdentity
sys = _Sys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272, 4, 17)
)
_SysPCMTable_Object = MibTable
sysPCMTable = _SysPCMTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 17, 1)
)
if mibBuilder.loadTexts:
    sysPCMTable.setStatus("mandatory")
_SysPCMEntry_Object = MibTableRow
sysPCMEntry = _SysPCMEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 17, 1, 1)
)
sysPCMEntry.setIndexNames(
    (0, "BIANCA-BRICK-MIBSYS-MIB", "sysPCMSlot"),
    (0, "BIANCA-BRICK-MIBSYS-MIB", "sysPCMUnit"),
)
if mibBuilder.loadTexts:
    sysPCMEntry.setStatus("mandatory")


class _SysPCMSlot_Type(Integer32):
    """Custom type sysPCMSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_SysPCMSlot_Type.__name__ = "Integer32"
_SysPCMSlot_Object = MibTableColumn
sysPCMSlot = _SysPCMSlot_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 17, 1, 1, 1),
    _SysPCMSlot_Type()
)
sysPCMSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysPCMSlot.setStatus("mandatory")


class _SysPCMUnit_Type(Integer32):
    """Custom type sysPCMUnit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 31),
    )


_SysPCMUnit_Type.__name__ = "Integer32"
_SysPCMUnit_Object = MibTableColumn
sysPCMUnit = _SysPCMUnit_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 17, 1, 1, 2),
    _SysPCMUnit_Type()
)
sysPCMUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysPCMUnit.setStatus("mandatory")


class _SysPCMClockStatus_Type(Integer32):
    """Custom type sysPCMClockStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-ready", 2),
          ("ready", 1))
    )


_SysPCMClockStatus_Type.__name__ = "Integer32"
_SysPCMClockStatus_Object = MibTableColumn
sysPCMClockStatus = _SysPCMClockStatus_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 17, 1, 1, 3),
    _SysPCMClockStatus_Type()
)
sysPCMClockStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysPCMClockStatus.setStatus("mandatory")


class _SysPCMClockMaster_Type(Integer32):
    """Custom type sysPCMClockMaster based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("candidate", 1),
          ("master", 2))
    )


_SysPCMClockMaster_Type.__name__ = "Integer32"
_SysPCMClockMaster_Object = MibTableColumn
sysPCMClockMaster = _SysPCMClockMaster_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 17, 1, 1, 4),
    _SysPCMClockMaster_Type()
)
sysPCMClockMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysPCMClockMaster.setStatus("mandatory")


class _SysPCMMasterPrio_Type(Integer32):
    """Custom type sysPCMMasterPrio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_SysPCMMasterPrio_Type.__name__ = "Integer32"
_SysPCMMasterPrio_Object = MibTableColumn
sysPCMMasterPrio = _SysPCMMasterPrio_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 17, 1, 1, 5),
    _SysPCMMasterPrio_Type()
)
sysPCMMasterPrio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysPCMMasterPrio.setStatus("mandatory")
_SysPCMChanges_Type = Counter32
_SysPCMChanges_Object = MibTableColumn
sysPCMChanges = _SysPCMChanges_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 17, 1, 1, 10),
    _SysPCMChanges_Type()
)
sysPCMChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysPCMChanges.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BIANCA-BRICK-MIBSYS-MIB",
    **{"org": org,
       "dod": dod,
       "internet": internet,
       "private": private,
       "enterprises": enterprises,
       "bintec": bintec,
       "bibo": bibo,
       "sys": sys,
       "sysPCMTable": sysPCMTable,
       "sysPCMEntry": sysPCMEntry,
       "sysPCMSlot": sysPCMSlot,
       "sysPCMUnit": sysPCMUnit,
       "sysPCMClockStatus": sysPCMClockStatus,
       "sysPCMClockMaster": sysPCMClockMaster,
       "sysPCMMasterPrio": sysPCMMasterPrio,
       "sysPCMChanges": sysPCMChanges}
)
