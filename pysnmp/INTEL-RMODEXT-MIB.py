# SNMP MIB module (INTEL-RMODEXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/INTEL-RMODEXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:09:57 2024
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

(modulesext,) = mibBuilder.importSymbols(
    "INTEL-GEN-MIB",
    "modulesext")

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

_Rmodext_ObjectIdentity = ObjectIdentity
rmodext = _Rmodext_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 7, 13, 1)
)
_RmodextGeneral_ObjectIdentity = ObjectIdentity
rmodextGeneral = _RmodextGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 7, 13, 1, 1)
)
_RmodextGModuleTable_Object = MibTable
rmodextGModuleTable = _RmodextGModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 7, 13, 1, 1, 1)
)
if mibBuilder.loadTexts:
    rmodextGModuleTable.setStatus("mandatory")
_RmodextGModuleEntry_Object = MibTableRow
rmodextGModuleEntry = _RmodextGModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 7, 13, 1, 1, 1, 1)
)
rmodextGModuleEntry.setIndexNames(
    (0, "INTEL-RMODEXT-MIB", "rmodextGModuleChassisIndex"),
    (0, "INTEL-RMODEXT-MIB", "rmodextGModuleIndex"),
)
if mibBuilder.loadTexts:
    rmodextGModuleEntry.setStatus("mandatory")
_RmodextGModuleChassisIndex_Type = Integer32
_RmodextGModuleChassisIndex_Object = MibTableColumn
rmodextGModuleChassisIndex = _RmodextGModuleChassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 7, 13, 1, 1, 1, 1, 1),
    _RmodextGModuleChassisIndex_Type()
)
rmodextGModuleChassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmodextGModuleChassisIndex.setStatus("mandatory")
_RmodextGModuleIndex_Type = Integer32
_RmodextGModuleIndex_Object = MibTableColumn
rmodextGModuleIndex = _RmodextGModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 7, 13, 1, 1, 1, 1, 2),
    _RmodextGModuleIndex_Type()
)
rmodextGModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmodextGModuleIndex.setStatus("mandatory")


class _RmodextGModuleHwEncryption_Type(Integer32):
    """Custom type rmodextGModuleHwEncryption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_RmodextGModuleHwEncryption_Type.__name__ = "Integer32"
_RmodextGModuleHwEncryption_Object = MibTableColumn
rmodextGModuleHwEncryption = _RmodextGModuleHwEncryption_Object(
    (1, 3, 6, 1, 4, 1, 343, 7, 13, 1, 1, 1, 1, 3),
    _RmodextGModuleHwEncryption_Type()
)
rmodextGModuleHwEncryption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmodextGModuleHwEncryption.setStatus("mandatory")


class _RmodextGModuleSwEncryption_Type(Integer32):
    """Custom type rmodextGModuleSwEncryption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_RmodextGModuleSwEncryption_Type.__name__ = "Integer32"
_RmodextGModuleSwEncryption_Object = MibTableColumn
rmodextGModuleSwEncryption = _RmodextGModuleSwEncryption_Object(
    (1, 3, 6, 1, 4, 1, 343, 7, 13, 1, 1, 1, 1, 4),
    _RmodextGModuleSwEncryption_Type()
)
rmodextGModuleSwEncryption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmodextGModuleSwEncryption.setStatus("mandatory")


class _RmodextGModuleSwState_Type(Integer32):
    """Custom type rmodextGModuleSwState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("error", 3),
          ("noError", 2),
          ("testing", 1))
    )


_RmodextGModuleSwState_Type.__name__ = "Integer32"
_RmodextGModuleSwState_Object = MibTableColumn
rmodextGModuleSwState = _RmodextGModuleSwState_Object(
    (1, 3, 6, 1, 4, 1, 343, 7, 13, 1, 1, 1, 1, 5),
    _RmodextGModuleSwState_Type()
)
rmodextGModuleSwState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmodextGModuleSwState.setStatus("mandatory")
_RmodextGModuleRamFree_Type = Integer32
_RmodextGModuleRamFree_Object = MibTableColumn
rmodextGModuleRamFree = _RmodextGModuleRamFree_Object(
    (1, 3, 6, 1, 4, 1, 343, 7, 13, 1, 1, 1, 1, 6),
    _RmodextGModuleRamFree_Type()
)
rmodextGModuleRamFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmodextGModuleRamFree.setStatus("mandatory")
_RmodextGModuleSwVersion_Type = OctetString
_RmodextGModuleSwVersion_Object = MibTableColumn
rmodextGModuleSwVersion = _RmodextGModuleSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 343, 7, 13, 1, 1, 1, 1, 7),
    _RmodextGModuleSwVersion_Type()
)
rmodextGModuleSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmodextGModuleSwVersion.setStatus("mandatory")
_RmodextGModulePbaNo_Type = OctetString
_RmodextGModulePbaNo_Object = MibTableColumn
rmodextGModulePbaNo = _RmodextGModulePbaNo_Object(
    (1, 3, 6, 1, 4, 1, 343, 7, 13, 1, 1, 1, 1, 8),
    _RmodextGModulePbaNo_Type()
)
rmodextGModulePbaNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmodextGModulePbaNo.setStatus("mandatory")
_RmodextGModuleBootSectionVersion_Type = OctetString
_RmodextGModuleBootSectionVersion_Object = MibTableColumn
rmodextGModuleBootSectionVersion = _RmodextGModuleBootSectionVersion_Object(
    (1, 3, 6, 1, 4, 1, 343, 7, 13, 1, 1, 1, 1, 9),
    _RmodextGModuleBootSectionVersion_Type()
)
rmodextGModuleBootSectionVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmodextGModuleBootSectionVersion.setStatus("mandatory")


class _RmodextGModuleMulti1_Type(OctetString):
    """Custom type rmodextGModuleMulti1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(250, 250),
    )


_RmodextGModuleMulti1_Type.__name__ = "OctetString"
_RmodextGModuleMulti1_Object = MibTableColumn
rmodextGModuleMulti1 = _RmodextGModuleMulti1_Object(
    (1, 3, 6, 1, 4, 1, 343, 7, 13, 1, 1, 1, 1, 10),
    _RmodextGModuleMulti1_Type()
)
rmodextGModuleMulti1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmodextGModuleMulti1.setStatus("mandatory")


class _RmodextGModuleMulti2_Type(OctetString):
    """Custom type rmodextGModuleMulti2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(250, 250),
    )


_RmodextGModuleMulti2_Type.__name__ = "OctetString"
_RmodextGModuleMulti2_Object = MibTableColumn
rmodextGModuleMulti2 = _RmodextGModuleMulti2_Object(
    (1, 3, 6, 1, 4, 1, 343, 7, 13, 1, 1, 1, 1, 11),
    _RmodextGModuleMulti2_Type()
)
rmodextGModuleMulti2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmodextGModuleMulti2.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INTEL-RMODEXT-MIB",
    **{"rmodext": rmodext,
       "rmodextGeneral": rmodextGeneral,
       "rmodextGModuleTable": rmodextGModuleTable,
       "rmodextGModuleEntry": rmodextGModuleEntry,
       "rmodextGModuleChassisIndex": rmodextGModuleChassisIndex,
       "rmodextGModuleIndex": rmodextGModuleIndex,
       "rmodextGModuleHwEncryption": rmodextGModuleHwEncryption,
       "rmodextGModuleSwEncryption": rmodextGModuleSwEncryption,
       "rmodextGModuleSwState": rmodextGModuleSwState,
       "rmodextGModuleRamFree": rmodextGModuleRamFree,
       "rmodextGModuleSwVersion": rmodextGModuleSwVersion,
       "rmodextGModulePbaNo": rmodextGModulePbaNo,
       "rmodextGModuleBootSectionVersion": rmodextGModuleBootSectionVersion,
       "rmodextGModuleMulti1": rmodextGModuleMulti1,
       "rmodextGModuleMulti2": rmodextGModuleMulti2}
)
