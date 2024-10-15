# SNMP MIB module (NBS-TUNABLE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NBS-TUNABLE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:25:05 2024
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

(InterfaceIndex,
 nbs) = mibBuilder.importSymbols(
    "NBS-CMMC-MIB",
    "InterfaceIndex",
    "nbs")

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

nbsTunableMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 629, 203)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NbsTunableGrp_ObjectIdentity = ObjectIdentity
nbsTunableGrp = _NbsTunableGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 203, 1)
)
if mibBuilder.loadTexts:
    nbsTunableGrp.setStatus("current")
_NbsTunableChannelTableSize_Type = Unsigned32
_NbsTunableChannelTableSize_Object = MibScalar
nbsTunableChannelTableSize = _NbsTunableChannelTableSize_Object(
    (1, 3, 6, 1, 4, 1, 629, 203, 1, 1),
    _NbsTunableChannelTableSize_Type()
)
nbsTunableChannelTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsTunableChannelTableSize.setStatus("current")
_NbsTunableChannelTable_Object = MibTable
nbsTunableChannelTable = _NbsTunableChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 203, 1, 2)
)
if mibBuilder.loadTexts:
    nbsTunableChannelTable.setStatus("current")
_NbsTunableChannelEntry_Object = MibTableRow
nbsTunableChannelEntry = _NbsTunableChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 203, 1, 2, 1)
)
nbsTunableChannelEntry.setIndexNames(
    (0, "NBS-TUNABLE-MIB", "nbsTunableChannelIfIndex"),
)
if mibBuilder.loadTexts:
    nbsTunableChannelEntry.setStatus("current")
_NbsTunableChannelIfIndex_Type = InterfaceIndex
_NbsTunableChannelIfIndex_Object = MibTableColumn
nbsTunableChannelIfIndex = _NbsTunableChannelIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 203, 1, 2, 1, 1),
    _NbsTunableChannelIfIndex_Type()
)
nbsTunableChannelIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsTunableChannelIfIndex.setStatus("current")


class _NbsTunableChannelFreqStart_Type(Integer32):
    """Custom type nbsTunableChannelFreqStart based on Integer32"""
    defaultValue = 190100


_NbsTunableChannelFreqStart_Object = MibTableColumn
nbsTunableChannelFreqStart = _NbsTunableChannelFreqStart_Object(
    (1, 3, 6, 1, 4, 1, 629, 203, 1, 2, 1, 2),
    _NbsTunableChannelFreqStart_Type()
)
nbsTunableChannelFreqStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsTunableChannelFreqStart.setStatus("current")


class _NbsTunableChannelFreqEnd_Type(Integer32):
    """Custom type nbsTunableChannelFreqEnd based on Integer32"""
    defaultValue = 197200


_NbsTunableChannelFreqEnd_Object = MibTableColumn
nbsTunableChannelFreqEnd = _NbsTunableChannelFreqEnd_Object(
    (1, 3, 6, 1, 4, 1, 629, 203, 1, 2, 1, 3),
    _NbsTunableChannelFreqEnd_Type()
)
nbsTunableChannelFreqEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsTunableChannelFreqEnd.setStatus("current")


class _NbsTunableChannelFreqStep_Type(Integer32):
    """Custom type nbsTunableChannelFreqStep based on Integer32"""
    defaultValue = 100


_NbsTunableChannelFreqStep_Object = MibTableColumn
nbsTunableChannelFreqStep = _NbsTunableChannelFreqStep_Object(
    (1, 3, 6, 1, 4, 1, 629, 203, 1, 2, 1, 4),
    _NbsTunableChannelFreqStep_Type()
)
nbsTunableChannelFreqStep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsTunableChannelFreqStep.setStatus("current")


class _NbsTunableChannelFreqExponent_Type(Integer32):
    """Custom type nbsTunableChannelFreqExponent based on Integer32"""
    defaultValue = 9


_NbsTunableChannelFreqExponent_Object = MibTableColumn
nbsTunableChannelFreqExponent = _NbsTunableChannelFreqExponent_Object(
    (1, 3, 6, 1, 4, 1, 629, 203, 1, 2, 1, 5),
    _NbsTunableChannelFreqExponent_Type()
)
nbsTunableChannelFreqExponent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsTunableChannelFreqExponent.setStatus("current")
_NbsTunableChannelFreqAdmin_Type = Integer32
_NbsTunableChannelFreqAdmin_Object = MibTableColumn
nbsTunableChannelFreqAdmin = _NbsTunableChannelFreqAdmin_Object(
    (1, 3, 6, 1, 4, 1, 629, 203, 1, 2, 1, 6),
    _NbsTunableChannelFreqAdmin_Type()
)
nbsTunableChannelFreqAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsTunableChannelFreqAdmin.setStatus("current")
_NbsTunableChannelFreqOper_Type = Integer32
_NbsTunableChannelFreqOper_Object = MibTableColumn
nbsTunableChannelFreqOper = _NbsTunableChannelFreqOper_Object(
    (1, 3, 6, 1, 4, 1, 629, 203, 1, 2, 1, 7),
    _NbsTunableChannelFreqOper_Type()
)
nbsTunableChannelFreqOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsTunableChannelFreqOper.setStatus("current")
_NbsTunableChannelFreqDefault_Type = Integer32
_NbsTunableChannelFreqDefault_Object = MibTableColumn
nbsTunableChannelFreqDefault = _NbsTunableChannelFreqDefault_Object(
    (1, 3, 6, 1, 4, 1, 629, 203, 1, 2, 1, 8),
    _NbsTunableChannelFreqDefault_Type()
)
nbsTunableChannelFreqDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsTunableChannelFreqDefault.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NBS-TUNABLE-MIB",
    **{"nbsTunableMib": nbsTunableMib,
       "nbsTunableGrp": nbsTunableGrp,
       "nbsTunableChannelTableSize": nbsTunableChannelTableSize,
       "nbsTunableChannelTable": nbsTunableChannelTable,
       "nbsTunableChannelEntry": nbsTunableChannelEntry,
       "nbsTunableChannelIfIndex": nbsTunableChannelIfIndex,
       "nbsTunableChannelFreqStart": nbsTunableChannelFreqStart,
       "nbsTunableChannelFreqEnd": nbsTunableChannelFreqEnd,
       "nbsTunableChannelFreqStep": nbsTunableChannelFreqStep,
       "nbsTunableChannelFreqExponent": nbsTunableChannelFreqExponent,
       "nbsTunableChannelFreqAdmin": nbsTunableChannelFreqAdmin,
       "nbsTunableChannelFreqOper": nbsTunableChannelFreqOper,
       "nbsTunableChannelFreqDefault": nbsTunableChannelFreqDefault}
)
