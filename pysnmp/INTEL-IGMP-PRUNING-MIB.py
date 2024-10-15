# SNMP MIB module (INTEL-IGMP-PRUNING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/INTEL-IGMP-PRUNING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:09:46 2024
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

(mib2ext,) = mibBuilder.importSymbols(
    "INTEL-GEN-MIB",
    "mib2ext")

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

_Igmppru_ObjectIdentity = ObjectIdentity
igmppru = _Igmppru_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 35)
)
_Conf_ObjectIdentity = ObjectIdentity
conf = _Conf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 35, 1)
)


class _ConfIgmpPruEnabled_Type(Integer32):
    """Custom type confIgmpPruEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_ConfIgmpPruEnabled_Type.__name__ = "Integer32"
_ConfIgmpPruEnabled_Object = MibScalar
confIgmpPruEnabled = _ConfIgmpPruEnabled_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 35, 1, 1),
    _ConfIgmpPruEnabled_Type()
)
confIgmpPruEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    confIgmpPruEnabled.setStatus("mandatory")


class _ConfIgmpPruTimer_Type(Integer32):
    """Custom type confIgmpPruTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_ConfIgmpPruTimer_Type.__name__ = "Integer32"
_ConfIgmpPruTimer_Object = MibScalar
confIgmpPruTimer = _ConfIgmpPruTimer_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 35, 1, 2),
    _ConfIgmpPruTimer_Type()
)
confIgmpPruTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    confIgmpPruTimer.setStatus("mandatory")
_ConfIgmpPruPortTable_Object = MibTable
confIgmpPruPortTable = _ConfIgmpPruPortTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 35, 1, 3)
)
if mibBuilder.loadTexts:
    confIgmpPruPortTable.setStatus("mandatory")
_ConfIgmpPruPortEntry_Object = MibTableRow
confIgmpPruPortEntry = _ConfIgmpPruPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 35, 1, 3, 1)
)
confIgmpPruPortEntry.setIndexNames(
    (0, "INTEL-IGMP-PRUNING-MIB", "confIgmpPruPortIndex"),
)
if mibBuilder.loadTexts:
    confIgmpPruPortEntry.setStatus("mandatory")
_ConfIgmpPruPortIndex_Type = Integer32
_ConfIgmpPruPortIndex_Object = MibTableColumn
confIgmpPruPortIndex = _ConfIgmpPruPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 35, 1, 3, 1, 1),
    _ConfIgmpPruPortIndex_Type()
)
confIgmpPruPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    confIgmpPruPortIndex.setStatus("mandatory")


class _ConfIgmpPruPortEnabled_Type(Integer32):
    """Custom type confIgmpPruPortEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_ConfIgmpPruPortEnabled_Type.__name__ = "Integer32"
_ConfIgmpPruPortEnabled_Object = MibTableColumn
confIgmpPruPortEnabled = _ConfIgmpPruPortEnabled_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 35, 1, 3, 1, 2),
    _ConfIgmpPruPortEnabled_Type()
)
confIgmpPruPortEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    confIgmpPruPortEnabled.setStatus("mandatory")


class _ConfIgmpPruAllowAsQuerier_Type(Integer32):
    """Custom type confIgmpPruAllowAsQuerier based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_ConfIgmpPruAllowAsQuerier_Type.__name__ = "Integer32"
_ConfIgmpPruAllowAsQuerier_Object = MibScalar
confIgmpPruAllowAsQuerier = _ConfIgmpPruAllowAsQuerier_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 35, 1, 4),
    _ConfIgmpPruAllowAsQuerier_Type()
)
confIgmpPruAllowAsQuerier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    confIgmpPruAllowAsQuerier.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INTEL-IGMP-PRUNING-MIB",
    **{"igmppru": igmppru,
       "conf": conf,
       "confIgmpPruEnabled": confIgmpPruEnabled,
       "confIgmpPruTimer": confIgmpPruTimer,
       "confIgmpPruPortTable": confIgmpPruPortTable,
       "confIgmpPruPortEntry": confIgmpPruPortEntry,
       "confIgmpPruPortIndex": confIgmpPruPortIndex,
       "confIgmpPruPortEnabled": confIgmpPruPortEnabled,
       "confIgmpPruAllowAsQuerier": confIgmpPruAllowAsQuerier}
)
