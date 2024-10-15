# SNMP MIB module (LANOPTICS-ETHERNET-OPTION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/LANOPTICS-ETHERNET-OPTION-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:17:14 2024
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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_LanOptics_ObjectIdentity = ObjectIdentity
lanOptics = _LanOptics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 224)
)
_LanOpticsDot3Monitor_ObjectIdentity = ObjectIdentity
lanOpticsDot3Monitor = _LanOpticsDot3Monitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 224, 3)
)
_EtAlertsLevel_Type = OctetString
_EtAlertsLevel_Object = MibScalar
etAlertsLevel = _EtAlertsLevel_Object(
    (1, 3, 6, 1, 4, 1, 224, 3, 1),
    _EtAlertsLevel_Type()
)
etAlertsLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etAlertsLevel.setStatus("mandatory")
_EtAlertsBuffer_Type = OctetString
_EtAlertsBuffer_Object = MibScalar
etAlertsBuffer = _EtAlertsBuffer_Object(
    (1, 3, 6, 1, 4, 1, 224, 3, 2),
    _EtAlertsBuffer_Type()
)
etAlertsBuffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etAlertsBuffer.setStatus("mandatory")
_EtFullStatisticsBuffer_Type = OctetString
_EtFullStatisticsBuffer_Object = MibScalar
etFullStatisticsBuffer = _EtFullStatisticsBuffer_Object(
    (1, 3, 6, 1, 4, 1, 224, 3, 3),
    _EtFullStatisticsBuffer_Type()
)
etFullStatisticsBuffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etFullStatisticsBuffer.setStatus("mandatory")


class _EtResetBuffers_Type(Integer32):
    """Custom type etResetBuffers based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_EtResetBuffers_Type.__name__ = "Integer32"
_EtResetBuffers_Object = MibScalar
etResetBuffers = _EtResetBuffers_Object(
    (1, 3, 6, 1, 4, 1, 224, 3, 4),
    _EtResetBuffers_Type()
)
etResetBuffers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etResetBuffers.setStatus("mandatory")
_EtSlotsTable_Object = MibTable
etSlotsTable = _EtSlotsTable_Object(
    (1, 3, 6, 1, 4, 1, 224, 3, 5)
)
if mibBuilder.loadTexts:
    etSlotsTable.setStatus("mandatory")
_EtSlotsEntry_Object = MibTableRow
etSlotsEntry = _EtSlotsEntry_Object(
    (1, 3, 6, 1, 4, 1, 224, 3, 5, 1)
)
etSlotsEntry.setIndexNames(
    (0, "LANOPTICS-ETHERNET-OPTION-MIB", "pysmiFakeCol1"),
)
if mibBuilder.loadTexts:
    etSlotsEntry.setStatus("mandatory")
_EtSlotPollStruct_Type = OctetString
_EtSlotPollStruct_Object = MibTableColumn
etSlotPollStruct = _EtSlotPollStruct_Object(
    (1, 3, 6, 1, 4, 1, 224, 3, 5, 1, 1),
    _EtSlotPollStruct_Type()
)
etSlotPollStruct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etSlotPollStruct.setStatus("mandatory")
_PysmiFakeCol1_Type = Integer32
_PysmiFakeCol1_Object = MibTableColumn
pysmiFakeCol1 = _PysmiFakeCol1_Object(
    (1, 3, 6, 1, 4, 1, 224, 3, 5, 1, 4294967295),
    _PysmiFakeCol1_Type()
)
pysmiFakeCol1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pysmiFakeCol1.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LANOPTICS-ETHERNET-OPTION-MIB",
    **{"lanOptics": lanOptics,
       "lanOpticsDot3Monitor": lanOpticsDot3Monitor,
       "etAlertsLevel": etAlertsLevel,
       "etAlertsBuffer": etAlertsBuffer,
       "etFullStatisticsBuffer": etFullStatisticsBuffer,
       "etResetBuffers": etResetBuffers,
       "etSlotsTable": etSlotsTable,
       "etSlotsEntry": etSlotsEntry,
       "etSlotPollStruct": etSlotPollStruct,
       "pysmiFakeCol1": pysmiFakeCol1}
)
