# SNMP MIB module (CT-PRIORITY-CLASSIFY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CT-PRIORITY-CLASSIFY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:18:20 2024
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

(ctPriorityExt,) = mibBuilder.importSymbols(
    "CTRON-MIB-NAMES",
    "ctPriorityExt")

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

_CtPriorityExtClassifyConfig_ObjectIdentity = ObjectIdentity
ctPriorityExtClassifyConfig = _CtPriorityExtClassifyConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 5)
)
_PClassifyRTP_ObjectIdentity = ObjectIdentity
pClassifyRTP = _PClassifyRTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 5, 1)
)


class _PClassifyRTPLowDelayQueuePreference_Type(Integer32):
    """Custom type pClassifyRTPLowDelayQueuePreference based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_PClassifyRTPLowDelayQueuePreference_Type.__name__ = "Integer32"
_PClassifyRTPLowDelayQueuePreference_Object = MibScalar
pClassifyRTPLowDelayQueuePreference = _PClassifyRTPLowDelayQueuePreference_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 5, 1, 1),
    _PClassifyRTPLowDelayQueuePreference_Type()
)
pClassifyRTPLowDelayQueuePreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pClassifyRTPLowDelayQueuePreference.setStatus("mandatory")


class _PClassifyRTCPParsing_Type(Integer32):
    """Custom type pClassifyRTCPParsing based on Integer32"""
    defaultValue = 1

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


_PClassifyRTCPParsing_Type.__name__ = "Integer32"
_PClassifyRTCPParsing_Object = MibScalar
pClassifyRTCPParsing = _PClassifyRTCPParsing_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 5, 1, 2),
    _PClassifyRTCPParsing_Type()
)
pClassifyRTCPParsing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pClassifyRTCPParsing.setStatus("mandatory")
_PClassifyRTPTable_Object = MibTable
pClassifyRTPTable = _PClassifyRTPTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 5, 1, 3)
)
if mibBuilder.loadTexts:
    pClassifyRTPTable.setStatus("mandatory")
_PClassifyRTPEntry_Object = MibTableRow
pClassifyRTPEntry = _PClassifyRTPEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 5, 1, 3, 1)
)
pClassifyRTPEntry.setIndexNames(
    (0, "CT-PRIORITY-CLASSIFY-MIB", "pClassifyRTPInterfaceNumber"),
)
if mibBuilder.loadTexts:
    pClassifyRTPEntry.setStatus("mandatory")
_PClassifyRTPInterfaceNumber_Type = Integer32
_PClassifyRTPInterfaceNumber_Object = MibTableColumn
pClassifyRTPInterfaceNumber = _PClassifyRTPInterfaceNumber_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 5, 1, 3, 1, 1),
    _PClassifyRTPInterfaceNumber_Type()
)
pClassifyRTPInterfaceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pClassifyRTPInterfaceNumber.setStatus("mandatory")


class _PClassifyRTPState_Type(Integer32):
    """Custom type pClassifyRTPState based on Integer32"""
    defaultValue = 1

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
        *(("noModification", 1),
          ("onlyQTOS", 3),
          ("onlyQTag", 2),
          ("qTagAndQTOS", 4))
    )


_PClassifyRTPState_Type.__name__ = "Integer32"
_PClassifyRTPState_Object = MibTableColumn
pClassifyRTPState = _PClassifyRTPState_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 5, 1, 3, 1, 2),
    _PClassifyRTPState_Type()
)
pClassifyRTPState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pClassifyRTPState.setStatus("mandatory")


class _PClassifyRTPTOSPrecedence_Type(Integer32):
    """Custom type pClassifyRTPTOSPrecedence based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_PClassifyRTPTOSPrecedence_Type.__name__ = "Integer32"
_PClassifyRTPTOSPrecedence_Object = MibTableColumn
pClassifyRTPTOSPrecedence = _PClassifyRTPTOSPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 5, 1, 3, 1, 3),
    _PClassifyRTPTOSPrecedence_Type()
)
pClassifyRTPTOSPrecedence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pClassifyRTPTOSPrecedence.setStatus("mandatory")


class _PClassifyRTPTagPriority_Type(Integer32):
    """Custom type pClassifyRTPTagPriority based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_PClassifyRTPTagPriority_Type.__name__ = "Integer32"
_PClassifyRTPTagPriority_Object = MibTableColumn
pClassifyRTPTagPriority = _PClassifyRTPTagPriority_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 5, 1, 3, 1, 4),
    _PClassifyRTPTagPriority_Type()
)
pClassifyRTPTagPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pClassifyRTPTagPriority.setStatus("mandatory")


class _PClassifyRTPTagVID_Type(Integer32):
    """Custom type pClassifyRTPTagVID based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_PClassifyRTPTagVID_Type.__name__ = "Integer32"
_PClassifyRTPTagVID_Object = MibTableColumn
pClassifyRTPTagVID = _PClassifyRTPTagVID_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 5, 1, 3, 1, 5),
    _PClassifyRTPTagVID_Type()
)
pClassifyRTPTagVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pClassifyRTPTagVID.setStatus("mandatory")
_PClassifyUDP_ObjectIdentity = ObjectIdentity
pClassifyUDP = _PClassifyUDP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 5, 2)
)
_PClassifyUDPTable_Object = MibTable
pClassifyUDPTable = _PClassifyUDPTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 5, 2, 1)
)
if mibBuilder.loadTexts:
    pClassifyUDPTable.setStatus("mandatory")
_PClassifyUDPEntry_Object = MibTableRow
pClassifyUDPEntry = _PClassifyUDPEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 5, 2, 1, 1)
)
pClassifyUDPEntry.setIndexNames(
    (0, "CT-PRIORITY-CLASSIFY-MIB", "pClassifyUDPPortNumber"),
)
if mibBuilder.loadTexts:
    pClassifyUDPEntry.setStatus("mandatory")
_PClassifyUDPPortNumber_Type = Integer32
_PClassifyUDPPortNumber_Object = MibTableColumn
pClassifyUDPPortNumber = _PClassifyUDPPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 5, 2, 1, 1, 1),
    _PClassifyUDPPortNumber_Type()
)
pClassifyUDPPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pClassifyUDPPortNumber.setStatus("mandatory")


class _PClassifyUDPState_Type(Integer32):
    """Custom type pClassifyUDPState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2),
          ("remove", 3))
    )


_PClassifyUDPState_Type.__name__ = "Integer32"
_PClassifyUDPState_Object = MibTableColumn
pClassifyUDPState = _PClassifyUDPState_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 5, 2, 1, 1, 2),
    _PClassifyUDPState_Type()
)
pClassifyUDPState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pClassifyUDPState.setStatus("mandatory")


class _PClassifyUDPLowDelayQueuePreference_Type(Integer32):
    """Custom type pClassifyUDPLowDelayQueuePreference based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_PClassifyUDPLowDelayQueuePreference_Type.__name__ = "Integer32"
_PClassifyUDPLowDelayQueuePreference_Object = MibTableColumn
pClassifyUDPLowDelayQueuePreference = _PClassifyUDPLowDelayQueuePreference_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 5, 2, 1, 1, 3),
    _PClassifyUDPLowDelayQueuePreference_Type()
)
pClassifyUDPLowDelayQueuePreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pClassifyUDPLowDelayQueuePreference.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CT-PRIORITY-CLASSIFY-MIB",
    **{"ctPriorityExtClassifyConfig": ctPriorityExtClassifyConfig,
       "pClassifyRTP": pClassifyRTP,
       "pClassifyRTPLowDelayQueuePreference": pClassifyRTPLowDelayQueuePreference,
       "pClassifyRTCPParsing": pClassifyRTCPParsing,
       "pClassifyRTPTable": pClassifyRTPTable,
       "pClassifyRTPEntry": pClassifyRTPEntry,
       "pClassifyRTPInterfaceNumber": pClassifyRTPInterfaceNumber,
       "pClassifyRTPState": pClassifyRTPState,
       "pClassifyRTPTOSPrecedence": pClassifyRTPTOSPrecedence,
       "pClassifyRTPTagPriority": pClassifyRTPTagPriority,
       "pClassifyRTPTagVID": pClassifyRTPTagVID,
       "pClassifyUDP": pClassifyUDP,
       "pClassifyUDPTable": pClassifyUDPTable,
       "pClassifyUDPEntry": pClassifyUDPEntry,
       "pClassifyUDPPortNumber": pClassifyUDPPortNumber,
       "pClassifyUDPState": pClassifyUDPState,
       "pClassifyUDPLowDelayQueuePreference": pClassifyUDPLowDelayQueuePreference}
)
