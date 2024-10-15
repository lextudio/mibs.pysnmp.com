# SNMP MIB module (ASCEND-MIBTRANSACTION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-MIBTRANSACTION-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:42:28 2024
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

(configuration,) = mibBuilder.importSymbols(
    "ASCEND-MIB",
    "configuration")

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



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MibtransactionProfile_ObjectIdentity = ObjectIdentity
mibtransactionProfile = _MibtransactionProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 131)
)
_MibtransactionProfileTable_Object = MibTable
mibtransactionProfileTable = _MibtransactionProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 131, 1)
)
if mibBuilder.loadTexts:
    mibtransactionProfileTable.setStatus("mandatory")
_MibtransactionProfileEntry_Object = MibTableRow
mibtransactionProfileEntry = _MibtransactionProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 131, 1, 1)
)
mibtransactionProfileEntry.setIndexNames(
    (0, "ASCEND-MIBTRANSACTION-MIB", "transactionProfile-Index-o"),
)
if mibBuilder.loadTexts:
    mibtransactionProfileEntry.setStatus("mandatory")
_TransactionProfile_Index_o_Type = Integer32
_TransactionProfile_Index_o_Object = MibScalar
transactionProfile_Index_o = _TransactionProfile_Index_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 131, 1, 1, 1),
    _TransactionProfile_Index_o_Type()
)
transactionProfile_Index_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transactionProfile_Index_o.setStatus("mandatory")
_TransactionProfile_SelectionTimeout_Type = Integer32
_TransactionProfile_SelectionTimeout_Object = MibScalar
transactionProfile_SelectionTimeout = _TransactionProfile_SelectionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 131, 1, 1, 2),
    _TransactionProfile_SelectionTimeout_Type()
)
transactionProfile_SelectionTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    transactionProfile_SelectionTimeout.setStatus("mandatory")
_TransactionProfile_DataAckTimeout_Type = Integer32
_TransactionProfile_DataAckTimeout_Object = MibScalar
transactionProfile_DataAckTimeout = _TransactionProfile_DataAckTimeout_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 131, 1, 1, 3),
    _TransactionProfile_DataAckTimeout_Type()
)
transactionProfile_DataAckTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    transactionProfile_DataAckTimeout.setStatus("mandatory")
_TransactionProfile_KeepAliveTimeout_Type = Integer32
_TransactionProfile_KeepAliveTimeout_Object = MibScalar
transactionProfile_KeepAliveTimeout = _TransactionProfile_KeepAliveTimeout_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 131, 1, 1, 4),
    _TransactionProfile_KeepAliveTimeout_Type()
)
transactionProfile_KeepAliveTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    transactionProfile_KeepAliveTimeout.setStatus("mandatory")
_TransactionProfile_QtpPort_Type = Integer32
_TransactionProfile_QtpPort_Object = MibScalar
transactionProfile_QtpPort = _TransactionProfile_QtpPort_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 131, 1, 1, 5),
    _TransactionProfile_QtpPort_Type()
)
transactionProfile_QtpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    transactionProfile_QtpPort.setStatus("mandatory")
_TransactionProfile_MetricMax_Type = Integer32
_TransactionProfile_MetricMax_Object = MibScalar
transactionProfile_MetricMax = _TransactionProfile_MetricMax_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 131, 1, 1, 6),
    _TransactionProfile_MetricMax_Type()
)
transactionProfile_MetricMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    transactionProfile_MetricMax.setStatus("mandatory")
_TransactionProfile_NoConnAckIncrement_Type = Integer32
_TransactionProfile_NoConnAckIncrement_Object = MibScalar
transactionProfile_NoConnAckIncrement = _TransactionProfile_NoConnAckIncrement_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 131, 1, 1, 7),
    _TransactionProfile_NoConnAckIncrement_Type()
)
transactionProfile_NoConnAckIncrement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    transactionProfile_NoConnAckIncrement.setStatus("mandatory")
_TransactionProfile_CallRejectIncrement_Type = Integer32
_TransactionProfile_CallRejectIncrement_Object = MibScalar
transactionProfile_CallRejectIncrement = _TransactionProfile_CallRejectIncrement_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 131, 1, 1, 8),
    _TransactionProfile_CallRejectIncrement_Type()
)
transactionProfile_CallRejectIncrement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    transactionProfile_CallRejectIncrement.setStatus("mandatory")
_TransactionProfile_CallAckDecrement_Type = Integer32
_TransactionProfile_CallAckDecrement_Object = MibScalar
transactionProfile_CallAckDecrement = _TransactionProfile_CallAckDecrement_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 131, 1, 1, 9),
    _TransactionProfile_CallAckDecrement_Type()
)
transactionProfile_CallAckDecrement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    transactionProfile_CallAckDecrement.setStatus("mandatory")
_TransactionProfile_AvailableMetric_Type = Integer32
_TransactionProfile_AvailableMetric_Object = MibScalar
transactionProfile_AvailableMetric = _TransactionProfile_AvailableMetric_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 131, 1, 1, 10),
    _TransactionProfile_AvailableMetric_Type()
)
transactionProfile_AvailableMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    transactionProfile_AvailableMetric.setStatus("mandatory")
_TransactionProfile_PartlyCongestedMetric_Type = Integer32
_TransactionProfile_PartlyCongestedMetric_Object = MibScalar
transactionProfile_PartlyCongestedMetric = _TransactionProfile_PartlyCongestedMetric_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 131, 1, 1, 11),
    _TransactionProfile_PartlyCongestedMetric_Type()
)
transactionProfile_PartlyCongestedMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    transactionProfile_PartlyCongestedMetric.setStatus("mandatory")
_TransactionProfile_CongestedMetric_Type = Integer32
_TransactionProfile_CongestedMetric_Object = MibScalar
transactionProfile_CongestedMetric = _TransactionProfile_CongestedMetric_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 131, 1, 1, 12),
    _TransactionProfile_CongestedMetric_Type()
)
transactionProfile_CongestedMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    transactionProfile_CongestedMetric.setStatus("mandatory")
_TransactionProfile_ShutdownMetric_Type = Integer32
_TransactionProfile_ShutdownMetric_Object = MibScalar
transactionProfile_ShutdownMetric = _TransactionProfile_ShutdownMetric_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 131, 1, 1, 13),
    _TransactionProfile_ShutdownMetric_Type()
)
transactionProfile_ShutdownMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    transactionProfile_ShutdownMetric.setStatus("mandatory")
_TransactionProfile_NoFirstStatusMetric_Type = Integer32
_TransactionProfile_NoFirstStatusMetric_Object = MibScalar
transactionProfile_NoFirstStatusMetric = _TransactionProfile_NoFirstStatusMetric_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 131, 1, 1, 14),
    _TransactionProfile_NoFirstStatusMetric_Type()
)
transactionProfile_NoFirstStatusMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    transactionProfile_NoFirstStatusMetric.setStatus("mandatory")
_TransactionProfile_NoSecondStatusMetric_Type = Integer32
_TransactionProfile_NoSecondStatusMetric_Object = MibScalar
transactionProfile_NoSecondStatusMetric = _TransactionProfile_NoSecondStatusMetric_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 131, 1, 1, 15),
    _TransactionProfile_NoSecondStatusMetric_Type()
)
transactionProfile_NoSecondStatusMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    transactionProfile_NoSecondStatusMetric.setStatus("mandatory")
_TransactionProfile_MaxQtpPduSize_Type = Integer32
_TransactionProfile_MaxQtpPduSize_Object = MibScalar
transactionProfile_MaxQtpPduSize = _TransactionProfile_MaxQtpPduSize_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 131, 1, 1, 16),
    _TransactionProfile_MaxQtpPduSize_Type()
)
transactionProfile_MaxQtpPduSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    transactionProfile_MaxQtpPduSize.setStatus("mandatory")


class _TransactionProfile_Action_o_Type(Integer32):
    """Custom type transactionProfile_Action_o based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("createProfile", 2),
          ("deleteProfile", 3),
          ("noAction", 1))
    )


_TransactionProfile_Action_o_Type.__name__ = "Integer32"
_TransactionProfile_Action_o_Object = MibScalar
transactionProfile_Action_o = _TransactionProfile_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 131, 1, 1, 17),
    _TransactionProfile_Action_o_Type()
)
transactionProfile_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    transactionProfile_Action_o.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-MIBTRANSACTION-MIB",
    **{"DisplayString": DisplayString,
       "mibtransactionProfile": mibtransactionProfile,
       "mibtransactionProfileTable": mibtransactionProfileTable,
       "mibtransactionProfileEntry": mibtransactionProfileEntry,
       "transactionProfile-Index-o": transactionProfile_Index_o,
       "transactionProfile-SelectionTimeout": transactionProfile_SelectionTimeout,
       "transactionProfile-DataAckTimeout": transactionProfile_DataAckTimeout,
       "transactionProfile-KeepAliveTimeout": transactionProfile_KeepAliveTimeout,
       "transactionProfile-QtpPort": transactionProfile_QtpPort,
       "transactionProfile-MetricMax": transactionProfile_MetricMax,
       "transactionProfile-NoConnAckIncrement": transactionProfile_NoConnAckIncrement,
       "transactionProfile-CallRejectIncrement": transactionProfile_CallRejectIncrement,
       "transactionProfile-CallAckDecrement": transactionProfile_CallAckDecrement,
       "transactionProfile-AvailableMetric": transactionProfile_AvailableMetric,
       "transactionProfile-PartlyCongestedMetric": transactionProfile_PartlyCongestedMetric,
       "transactionProfile-CongestedMetric": transactionProfile_CongestedMetric,
       "transactionProfile-ShutdownMetric": transactionProfile_ShutdownMetric,
       "transactionProfile-NoFirstStatusMetric": transactionProfile_NoFirstStatusMetric,
       "transactionProfile-NoSecondStatusMetric": transactionProfile_NoSecondStatusMetric,
       "transactionProfile-MaxQtpPduSize": transactionProfile_MaxQtpPduSize,
       "transactionProfile-Action-o": transactionProfile_Action_o}
)
