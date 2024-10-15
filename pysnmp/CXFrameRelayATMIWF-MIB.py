# SNMP MIB module (CXFrameRelayATMIWF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CXFrameRelayATMIWF-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:20:27 2024
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

(SapIndex,
 cxFrameRelay) = mibBuilder.importSymbols(
    "CXProduct-SMI",
    "SapIndex",
    "cxFrameRelay")

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



class _FrpAtmIWFMibLevel_Type(Integer32):
    """Custom type frpAtmIWFMibLevel based on Integer32"""
    defaultValue = 0


_FrpAtmIWFMibLevel_Object = MibScalar
frpAtmIWFMibLevel = _FrpAtmIWFMibLevel_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 50),
    _FrpAtmIWFMibLevel_Type()
)
frpAtmIWFMibLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpAtmIWFMibLevel.setStatus("mandatory")


class _FrpAtmConnectTimer_Type(Integer32):
    """Custom type frpAtmConnectTimer based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 600),
    )


_FrpAtmConnectTimer_Type.__name__ = "Integer32"
_FrpAtmConnectTimer_Object = MibScalar
frpAtmConnectTimer = _FrpAtmConnectTimer_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 51),
    _FrpAtmConnectTimer_Type()
)
frpAtmConnectTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frpAtmConnectTimer.setStatus("mandatory")
_FrpAtmNISapTable_Object = MibTable
frpAtmNISapTable = _FrpAtmNISapTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 52)
)
if mibBuilder.loadTexts:
    frpAtmNISapTable.setStatus("mandatory")
_FrpAtmNISapEntry_Object = MibTableRow
frpAtmNISapEntry = _FrpAtmNISapEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 52, 1)
)
frpAtmNISapEntry.setIndexNames(
    (0, "CXFrameRelayATMIWF-MIB", "frpAtmNISapNumber"),
)
if mibBuilder.loadTexts:
    frpAtmNISapEntry.setStatus("mandatory")
_FrpAtmNISapNumber_Type = SapIndex
_FrpAtmNISapNumber_Object = MibTableColumn
frpAtmNISapNumber = _FrpAtmNISapNumber_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 52, 1, 1),
    _FrpAtmNISapNumber_Type()
)
frpAtmNISapNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpAtmNISapNumber.setStatus("mandatory")


class _FrpAtmNISapState_Type(Integer32):
    """Custom type frpAtmNISapState based on Integer32"""
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
        *(("connectFlowOff", 5),
          ("connected", 4),
          ("inProgress", 3),
          ("notConnected", 2),
          ("offLine", 1))
    )


_FrpAtmNISapState_Type.__name__ = "Integer32"
_FrpAtmNISapState_Object = MibTableColumn
frpAtmNISapState = _FrpAtmNISapState_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 52, 1, 2),
    _FrpAtmNISapState_Type()
)
frpAtmNISapState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpAtmNISapState.setStatus("mandatory")


class _FrpAtmNIFailureReason_Type(Integer32):
    """Custom type frpAtmNIFailureReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              8,
              10,
              11,
              12,
              13,
              15,
              16,
              18)
        )
    )
    namedValues = NamedValues(
        *(("internalError", 2),
          ("localAllocFailure", 3),
          ("localDsnFailure", 13),
          ("localFcnFailure", 11),
          ("localNoAccess", 5),
          ("noFailure", 1),
          ("remoteAliasNotFound", 15),
          ("remoteAllocFailure", 4),
          ("remoteFcnFailure", 12),
          ("remoteNoAccess", 6),
          ("remoteNoPvcService", 16),
          ("remotePvcBusy", 10),
          ("remotePvcDown", 8),
          ("routeStalled", 18))
    )


_FrpAtmNIFailureReason_Type.__name__ = "Integer32"
_FrpAtmNIFailureReason_Object = MibTableColumn
frpAtmNIFailureReason = _FrpAtmNIFailureReason_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 52, 1, 3),
    _FrpAtmNIFailureReason_Type()
)
frpAtmNIFailureReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frpAtmNIFailureReason.setStatus("mandatory")


class _FrpAtmNISapDEtoCLPMapping_Type(Integer32):
    """Custom type frpAtmNISapDEtoCLPMapping based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mode1", 1),
          ("mode2", 2))
    )


_FrpAtmNISapDEtoCLPMapping_Type.__name__ = "Integer32"
_FrpAtmNISapDEtoCLPMapping_Object = MibTableColumn
frpAtmNISapDEtoCLPMapping = _FrpAtmNISapDEtoCLPMapping_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 52, 1, 4),
    _FrpAtmNISapDEtoCLPMapping_Type()
)
frpAtmNISapDEtoCLPMapping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frpAtmNISapDEtoCLPMapping.setStatus("mandatory")


class _FrpAtmNISapCLPtoDEMapping_Type(Integer32):
    """Custom type frpAtmNISapCLPtoDEMapping based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mode1", 1),
          ("mode2", 2))
    )


_FrpAtmNISapCLPtoDEMapping_Type.__name__ = "Integer32"
_FrpAtmNISapCLPtoDEMapping_Object = MibTableColumn
frpAtmNISapCLPtoDEMapping = _FrpAtmNISapCLPtoDEMapping_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 52, 1, 5),
    _FrpAtmNISapCLPtoDEMapping_Type()
)
frpAtmNISapCLPtoDEMapping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frpAtmNISapCLPtoDEMapping.setStatus("mandatory")


class _FrpAtmNISapCLPBit_Type(Integer32):
    """Custom type frpAtmNISapCLPBit based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("one", 2),
          ("zero", 1))
    )


_FrpAtmNISapCLPBit_Type.__name__ = "Integer32"
_FrpAtmNISapCLPBit_Object = MibTableColumn
frpAtmNISapCLPBit = _FrpAtmNISapCLPBit_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 3, 52, 1, 6),
    _FrpAtmNISapCLPBit_Type()
)
frpAtmNISapCLPBit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frpAtmNISapCLPBit.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CXFrameRelayATMIWF-MIB",
    **{"frpAtmIWFMibLevel": frpAtmIWFMibLevel,
       "frpAtmConnectTimer": frpAtmConnectTimer,
       "frpAtmNISapTable": frpAtmNISapTable,
       "frpAtmNISapEntry": frpAtmNISapEntry,
       "frpAtmNISapNumber": frpAtmNISapNumber,
       "frpAtmNISapState": frpAtmNISapState,
       "frpAtmNIFailureReason": frpAtmNIFailureReason,
       "frpAtmNISapDEtoCLPMapping": frpAtmNISapDEtoCLPMapping,
       "frpAtmNISapCLPtoDEMapping": frpAtmNISapCLPtoDEMapping,
       "frpAtmNISapCLPBit": frpAtmNISapCLPBit}
)
