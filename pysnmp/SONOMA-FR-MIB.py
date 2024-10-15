# SNMP MIB module (SONOMA-FR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SONOMA-FR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:56:38 2024
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

(sonomaSeries,) = mibBuilder.importSymbols(
    "SONOMASYSTEMS-SONOMA-MIB",
    "sonomaSeries")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SonomaFR_ObjectIdentity = ObjectIdentity
sonomaFR = _SonomaFR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2926, 25, 9)
)
_SonomaFracTable_Object = MibTable
sonomaFracTable = _SonomaFracTable_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 9, 1)
)
if mibBuilder.loadTexts:
    sonomaFracTable.setStatus("mandatory")
_SonomaFracEntry_Object = MibTableRow
sonomaFracEntry = _SonomaFracEntry_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 9, 1, 1)
)
sonomaFracEntry.setIndexNames(
    (0, "SONOMA-FR-MIB", "sonomaFracIndex"),
)
if mibBuilder.loadTexts:
    sonomaFracEntry.setStatus("mandatory")
_SonomaFracIndex_Type = Integer32
_SonomaFracIndex_Object = MibTableColumn
sonomaFracIndex = _SonomaFracIndex_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 9, 1, 1, 1),
    _SonomaFracIndex_Type()
)
sonomaFracIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonomaFracIndex.setStatus("mandatory")
_SonomaFracCount_Type = Integer32
_SonomaFracCount_Object = MibTableColumn
sonomaFracCount = _SonomaFracCount_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 9, 1, 1, 2),
    _SonomaFracCount_Type()
)
sonomaFracCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonomaFracCount.setStatus("mandatory")
_CcT5Table_Object = MibTable
ccT5Table = _CcT5Table_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 9, 3)
)
if mibBuilder.loadTexts:
    ccT5Table.setStatus("mandatory")
_CcT5Entry_Object = MibTableRow
ccT5Entry = _CcT5Entry_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 9, 3, 1)
)
ccT5Entry.setIndexNames(
    (0, "SONOMA-FR-MIB", "ccT5EndPointA"),
    (0, "SONOMA-FR-MIB", "ccT5EndPointB"),
)
if mibBuilder.loadTexts:
    ccT5Entry.setStatus("mandatory")


class _CcT5EndPointA_Type(Integer32):
    """Custom type ccT5EndPointA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_CcT5EndPointA_Type.__name__ = "Integer32"
_CcT5EndPointA_Object = MibTableColumn
ccT5EndPointA = _CcT5EndPointA_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 9, 3, 1, 1),
    _CcT5EndPointA_Type()
)
ccT5EndPointA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccT5EndPointA.setStatus("mandatory")


class _CcT5EndPointB_Type(Integer32):
    """Custom type ccT5EndPointB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_CcT5EndPointB_Type.__name__ = "Integer32"
_CcT5EndPointB_Object = MibTableColumn
ccT5EndPointB = _CcT5EndPointB_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 9, 3, 1, 2),
    _CcT5EndPointB_Type()
)
ccT5EndPointB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccT5EndPointB.setStatus("mandatory")
_CcT5FRSSCSDLCI_Type = Integer32
_CcT5FRSSCSDLCI_Object = MibTableColumn
ccT5FRSSCSDLCI = _CcT5FRSSCSDLCI_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 9, 3, 1, 3),
    _CcT5FRSSCSDLCI_Type()
)
ccT5FRSSCSDLCI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccT5FRSSCSDLCI.setStatus("mandatory")


class _CcT5DEtoCLPMapping_Type(Integer32):
    """Custom type ccT5DEtoCLPMapping based on Integer32"""
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
        *(("frandclp", 1),
          ("fronlyclp0", 2),
          ("fronlyclp1", 3))
    )


_CcT5DEtoCLPMapping_Type.__name__ = "Integer32"
_CcT5DEtoCLPMapping_Object = MibTableColumn
ccT5DEtoCLPMapping = _CcT5DEtoCLPMapping_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 9, 3, 1, 4),
    _CcT5DEtoCLPMapping_Type()
)
ccT5DEtoCLPMapping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccT5DEtoCLPMapping.setStatus("mandatory")


class _CcT5CLPtoDEMapping_Type(Integer32):
    """Custom type ccT5CLPtoDEMapping based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("either", 2),
          ("fronly", 1))
    )


_CcT5CLPtoDEMapping_Type.__name__ = "Integer32"
_CcT5CLPtoDEMapping_Object = MibTableColumn
ccT5CLPtoDEMapping = _CcT5CLPtoDEMapping_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 9, 3, 1, 5),
    _CcT5CLPtoDEMapping_Type()
)
ccT5CLPtoDEMapping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccT5CLPtoDEMapping.setStatus("mandatory")


class _CcT5SSCSManagement_Type(Integer32):
    """Custom type ccT5SSCSManagement based on Integer32"""
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


_CcT5SSCSManagement_Type.__name__ = "Integer32"
_CcT5SSCSManagement_Object = MibTableColumn
ccT5SSCSManagement = _CcT5SSCSManagement_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 9, 3, 1, 6),
    _CcT5SSCSManagement_Type()
)
ccT5SSCSManagement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccT5SSCSManagement.setStatus("mandatory")


class _CcT5RowStatus_Type(Integer32):
    """Custom type ccT5RowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )


_CcT5RowStatus_Type.__name__ = "Integer32"
_CcT5RowStatus_Object = MibTableColumn
ccT5RowStatus = _CcT5RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 9, 3, 1, 7),
    _CcT5RowStatus_Type()
)
ccT5RowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccT5RowStatus.setStatus("mandatory")
_SonomaFRDcePortTable_Object = MibTable
sonomaFRDcePortTable = _SonomaFRDcePortTable_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 9, 4)
)
if mibBuilder.loadTexts:
    sonomaFRDcePortTable.setStatus("mandatory")
_SonomaFRDcePortEntry_Object = MibTableRow
sonomaFRDcePortEntry = _SonomaFRDcePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 9, 4, 1)
)
sonomaFRDcePortEntry.setIndexNames(
    (0, "SONOMA-FR-MIB", "sonomaFRDcePort"),
)
if mibBuilder.loadTexts:
    sonomaFRDcePortEntry.setStatus("mandatory")


class _SonomaFRDcePort_Type(Integer32):
    """Custom type sonomaFRDcePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_SonomaFRDcePort_Type.__name__ = "Integer32"
_SonomaFRDcePort_Object = MibTableColumn
sonomaFRDcePort = _SonomaFRDcePort_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 9, 4, 1, 1),
    _SonomaFRDcePort_Type()
)
sonomaFRDcePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonomaFRDcePort.setStatus("mandatory")


class _SonomaFRDcePortType_Type(Integer32):
    """Custom type sonomaFRDcePortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dce", 1),
          ("dte", 2))
    )


_SonomaFRDcePortType_Type.__name__ = "Integer32"
_SonomaFRDcePortType_Object = MibTableColumn
sonomaFRDcePortType = _SonomaFRDcePortType_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 9, 4, 1, 2),
    _SonomaFRDcePortType_Type()
)
sonomaFRDcePortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonomaFRDcePortType.setStatus("mandatory")


class _SonomaFRDcePortIncomingRateControl_Type(Integer32):
    """Custom type sonomaFRDcePortIncomingRateControl based on Integer32"""
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


_SonomaFRDcePortIncomingRateControl_Type.__name__ = "Integer32"
_SonomaFRDcePortIncomingRateControl_Object = MibTableColumn
sonomaFRDcePortIncomingRateControl = _SonomaFRDcePortIncomingRateControl_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 9, 4, 1, 3),
    _SonomaFRDcePortIncomingRateControl_Type()
)
sonomaFRDcePortIncomingRateControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonomaFRDcePortIncomingRateControl.setStatus("mandatory")


class _SonomaFRDcePortOutgoingRateControl_Type(Integer32):
    """Custom type sonomaFRDcePortOutgoingRateControl based on Integer32"""
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


_SonomaFRDcePortOutgoingRateControl_Type.__name__ = "Integer32"
_SonomaFRDcePortOutgoingRateControl_Object = MibTableColumn
sonomaFRDcePortOutgoingRateControl = _SonomaFRDcePortOutgoingRateControl_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 9, 4, 1, 4),
    _SonomaFRDcePortOutgoingRateControl_Type()
)
sonomaFRDcePortOutgoingRateControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonomaFRDcePortOutgoingRateControl.setStatus("mandatory")
_SonomaFRDlciTable_Object = MibTable
sonomaFRDlciTable = _SonomaFRDlciTable_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 9, 5)
)
if mibBuilder.loadTexts:
    sonomaFRDlciTable.setStatus("mandatory")
_SonomaFRDlciEntry_Object = MibTableRow
sonomaFRDlciEntry = _SonomaFRDlciEntry_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 9, 5, 1)
)
sonomaFRDlciEntry.setIndexNames(
    (0, "SONOMA-FR-MIB", "sonomaFRDlciPort"),
    (0, "SONOMA-FR-MIB", "sonomaFRDlci"),
)
if mibBuilder.loadTexts:
    sonomaFRDlciEntry.setStatus("mandatory")


class _SonomaFRDlciPort_Type(Integer32):
    """Custom type sonomaFRDlciPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_SonomaFRDlciPort_Type.__name__ = "Integer32"
_SonomaFRDlciPort_Object = MibTableColumn
sonomaFRDlciPort = _SonomaFRDlciPort_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 9, 5, 1, 1),
    _SonomaFRDlciPort_Type()
)
sonomaFRDlciPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonomaFRDlciPort.setStatus("mandatory")


class _SonomaFRDlci_Type(Integer32):
    """Custom type sonomaFRDlci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_SonomaFRDlci_Type.__name__ = "Integer32"
_SonomaFRDlci_Object = MibTableColumn
sonomaFRDlci = _SonomaFRDlci_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 9, 5, 1, 2),
    _SonomaFRDlci_Type()
)
sonomaFRDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonomaFRDlci.setStatus("mandatory")
_SonomaFrDlcmiTable_Object = MibTable
sonomaFrDlcmiTable = _SonomaFrDlcmiTable_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 9, 6)
)
if mibBuilder.loadTexts:
    sonomaFrDlcmiTable.setStatus("mandatory")
_SonomaFrDlcmiEntry_Object = MibTableRow
sonomaFrDlcmiEntry = _SonomaFrDlcmiEntry_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 9, 6, 1)
)
sonomaFrDlcmiEntry.setIndexNames(
    (0, "SONOMA-FR-MIB", "sonomaFrDlcmiIfIndex"),
)
if mibBuilder.loadTexts:
    sonomaFrDlcmiEntry.setStatus("mandatory")
_SonomaFrDlcmiIfIndex_Type = Integer32
_SonomaFrDlcmiIfIndex_Object = MibTableColumn
sonomaFrDlcmiIfIndex = _SonomaFrDlcmiIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 9, 6, 1, 1),
    _SonomaFrDlcmiIfIndex_Type()
)
sonomaFrDlcmiIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonomaFrDlcmiIfIndex.setStatus("mandatory")


class _SonomaFrDlcmiState_Type(Integer32):
    """Custom type sonomaFrDlcmiState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              5)
        )
    )
    namedValues = NamedValues(
        *(("ansiT1617D", 3),
          ("itut933A", 5),
          ("lmiRev1", 2),
          ("noLmiConfigured", 1))
    )


_SonomaFrDlcmiState_Type.__name__ = "Integer32"
_SonomaFrDlcmiState_Object = MibTableColumn
sonomaFrDlcmiState = _SonomaFrDlcmiState_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 9, 6, 1, 2),
    _SonomaFrDlcmiState_Type()
)
sonomaFrDlcmiState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonomaFrDlcmiState.setStatus("mandatory")


class _SonomaFrDlcmiPollingInterval_Type(Integer32):
    """Custom type sonomaFrDlcmiPollingInterval based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 30),
    )


_SonomaFrDlcmiPollingInterval_Type.__name__ = "Integer32"
_SonomaFrDlcmiPollingInterval_Object = MibTableColumn
sonomaFrDlcmiPollingInterval = _SonomaFrDlcmiPollingInterval_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 9, 6, 1, 5),
    _SonomaFrDlcmiPollingInterval_Type()
)
sonomaFrDlcmiPollingInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonomaFrDlcmiPollingInterval.setStatus("mandatory")


class _SonomaFrDlcmiFullEnquiryInterval_Type(Integer32):
    """Custom type sonomaFrDlcmiFullEnquiryInterval based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SonomaFrDlcmiFullEnquiryInterval_Type.__name__ = "Integer32"
_SonomaFrDlcmiFullEnquiryInterval_Object = MibTableColumn
sonomaFrDlcmiFullEnquiryInterval = _SonomaFrDlcmiFullEnquiryInterval_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 9, 6, 1, 6),
    _SonomaFrDlcmiFullEnquiryInterval_Type()
)
sonomaFrDlcmiFullEnquiryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonomaFrDlcmiFullEnquiryInterval.setStatus("mandatory")


class _SonomaFrDlcmiErrorThreshold_Type(Integer32):
    """Custom type sonomaFrDlcmiErrorThreshold based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_SonomaFrDlcmiErrorThreshold_Type.__name__ = "Integer32"
_SonomaFrDlcmiErrorThreshold_Object = MibTableColumn
sonomaFrDlcmiErrorThreshold = _SonomaFrDlcmiErrorThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 9, 6, 1, 7),
    _SonomaFrDlcmiErrorThreshold_Type()
)
sonomaFrDlcmiErrorThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonomaFrDlcmiErrorThreshold.setStatus("mandatory")


class _SonomaFrDlcmiMonitoredEvents_Type(Integer32):
    """Custom type sonomaFrDlcmiMonitoredEvents based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_SonomaFrDlcmiMonitoredEvents_Type.__name__ = "Integer32"
_SonomaFrDlcmiMonitoredEvents_Object = MibTableColumn
sonomaFrDlcmiMonitoredEvents = _SonomaFrDlcmiMonitoredEvents_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 9, 6, 1, 8),
    _SonomaFrDlcmiMonitoredEvents_Type()
)
sonomaFrDlcmiMonitoredEvents.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonomaFrDlcmiMonitoredEvents.setStatus("mandatory")


class _SonomaFrDlcmiStatus_Type(Integer32):
    """Custom type sonomaFrDlcmiStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fault", 2),
          ("initializing", 3),
          ("running", 1))
    )


_SonomaFrDlcmiStatus_Type.__name__ = "Integer32"
_SonomaFrDlcmiStatus_Object = MibTableColumn
sonomaFrDlcmiStatus = _SonomaFrDlcmiStatus_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 9, 6, 1, 11),
    _SonomaFrDlcmiStatus_Type()
)
sonomaFrDlcmiStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonomaFrDlcmiStatus.setStatus("mandatory")
_SonomaFRDtePortTable_Object = MibTable
sonomaFRDtePortTable = _SonomaFRDtePortTable_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 9, 7)
)
if mibBuilder.loadTexts:
    sonomaFRDtePortTable.setStatus("mandatory")
_SonomaFRDtePortEntry_Object = MibTableRow
sonomaFRDtePortEntry = _SonomaFRDtePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 9, 7, 1)
)
sonomaFRDtePortEntry.setIndexNames(
    (0, "SONOMA-FR-MIB", "sonomaFRDtePort"),
)
if mibBuilder.loadTexts:
    sonomaFRDtePortEntry.setStatus("mandatory")


class _SonomaFRDtePort_Type(Integer32):
    """Custom type sonomaFRDtePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_SonomaFRDtePort_Type.__name__ = "Integer32"
_SonomaFRDtePort_Object = MibTableColumn
sonomaFRDtePort = _SonomaFRDtePort_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 9, 7, 1, 1),
    _SonomaFRDtePort_Type()
)
sonomaFRDtePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonomaFRDtePort.setStatus("mandatory")


class _SonomaFRDtePortType_Type(Integer32):
    """Custom type sonomaFRDtePortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dce", 1),
          ("dte", 2))
    )


_SonomaFRDtePortType_Type.__name__ = "Integer32"
_SonomaFRDtePortType_Object = MibTableColumn
sonomaFRDtePortType = _SonomaFRDtePortType_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 9, 7, 1, 2),
    _SonomaFRDtePortType_Type()
)
sonomaFRDtePortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonomaFRDtePortType.setStatus("mandatory")
_CcT8Table_Object = MibTable
ccT8Table = _CcT8Table_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 9, 8)
)
if mibBuilder.loadTexts:
    ccT8Table.setStatus("mandatory")
_CcT8Entry_Object = MibTableRow
ccT8Entry = _CcT8Entry_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 9, 8, 1)
)
ccT8Entry.setIndexNames(
    (0, "SONOMA-FR-MIB", "ccT8EndPointA"),
    (0, "SONOMA-FR-MIB", "ccT8EndPointB"),
)
if mibBuilder.loadTexts:
    ccT8Entry.setStatus("mandatory")


class _CcT8EndPointA_Type(Integer32):
    """Custom type ccT8EndPointA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_CcT8EndPointA_Type.__name__ = "Integer32"
_CcT8EndPointA_Object = MibTableColumn
ccT8EndPointA = _CcT8EndPointA_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 9, 8, 1, 1),
    _CcT8EndPointA_Type()
)
ccT8EndPointA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccT8EndPointA.setStatus("mandatory")


class _CcT8EndPointB_Type(Integer32):
    """Custom type ccT8EndPointB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_CcT8EndPointB_Type.__name__ = "Integer32"
_CcT8EndPointB_Object = MibTableColumn
ccT8EndPointB = _CcT8EndPointB_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 9, 8, 1, 2),
    _CcT8EndPointB_Type()
)
ccT8EndPointB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccT8EndPointB.setStatus("mandatory")


class _CcT8DECLPMapping_Type(Integer32):
    """Custom type ccT8DECLPMapping based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("always0", 1),
          ("always1", 2),
          ("convert", 3))
    )


_CcT8DECLPMapping_Type.__name__ = "Integer32"
_CcT8DECLPMapping_Object = MibTableColumn
ccT8DECLPMapping = _CcT8DECLPMapping_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 9, 8, 1, 3),
    _CcT8DECLPMapping_Type()
)
ccT8DECLPMapping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccT8DECLPMapping.setStatus("mandatory")


class _CcT8FECNEFCIMapping_Type(Integer32):
    """Custom type ccT8FECNEFCIMapping based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("always0", 1),
          ("always1", 2),
          ("convert", 3))
    )


_CcT8FECNEFCIMapping_Type.__name__ = "Integer32"
_CcT8FECNEFCIMapping_Object = MibTableColumn
ccT8FECNEFCIMapping = _CcT8FECNEFCIMapping_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 9, 8, 1, 4),
    _CcT8FECNEFCIMapping_Type()
)
ccT8FECNEFCIMapping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccT8FECNEFCIMapping.setStatus("mandatory")


class _CcT8ULPEncapsulation_Type(Integer32):
    """Custom type ccT8ULPEncapsulation based on Integer32"""
    defaultValue = 2

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


_CcT8ULPEncapsulation_Type.__name__ = "Integer32"
_CcT8ULPEncapsulation_Object = MibTableColumn
ccT8ULPEncapsulation = _CcT8ULPEncapsulation_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 9, 8, 1, 5),
    _CcT8ULPEncapsulation_Type()
)
ccT8ULPEncapsulation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccT8ULPEncapsulation.setStatus("mandatory")


class _CcT8RowStatus_Type(Integer32):
    """Custom type ccT8RowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )


_CcT8RowStatus_Type.__name__ = "Integer32"
_CcT8RowStatus_Object = MibTableColumn
ccT8RowStatus = _CcT8RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 9, 8, 1, 6),
    _CcT8RowStatus_Type()
)
ccT8RowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccT8RowStatus.setStatus("mandatory")
_SonomaFRPortStatsTable_Object = MibTable
sonomaFRPortStatsTable = _SonomaFRPortStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 9, 9)
)
if mibBuilder.loadTexts:
    sonomaFRPortStatsTable.setStatus("mandatory")
_SonomaFRPortStatsEntry_Object = MibTableRow
sonomaFRPortStatsEntry = _SonomaFRPortStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 9, 9, 1)
)
sonomaFRPortStatsEntry.setIndexNames(
    (0, "SONOMA-FR-MIB", "sonomaFRPortStatsPort"),
)
if mibBuilder.loadTexts:
    sonomaFRPortStatsEntry.setStatus("mandatory")


class _SonomaFRPortStatsPort_Type(Integer32):
    """Custom type sonomaFRPortStatsPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_SonomaFRPortStatsPort_Type.__name__ = "Integer32"
_SonomaFRPortStatsPort_Object = MibTableColumn
sonomaFRPortStatsPort = _SonomaFRPortStatsPort_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 9, 9, 1, 1),
    _SonomaFRPortStatsPort_Type()
)
sonomaFRPortStatsPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonomaFRPortStatsPort.setStatus("mandatory")
_SonomaFRPortStatsRecvLIVReqs_Type = Counter32
_SonomaFRPortStatsRecvLIVReqs_Object = MibTableColumn
sonomaFRPortStatsRecvLIVReqs = _SonomaFRPortStatsRecvLIVReqs_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 9, 9, 1, 2),
    _SonomaFRPortStatsRecvLIVReqs_Type()
)
sonomaFRPortStatsRecvLIVReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonomaFRPortStatsRecvLIVReqs.setStatus("mandatory")
_SonomaFRPortStatsSentLIVReqs_Type = Counter32
_SonomaFRPortStatsSentLIVReqs_Object = MibTableColumn
sonomaFRPortStatsSentLIVReqs = _SonomaFRPortStatsSentLIVReqs_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 9, 9, 1, 3),
    _SonomaFRPortStatsSentLIVReqs_Type()
)
sonomaFRPortStatsSentLIVReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonomaFRPortStatsSentLIVReqs.setStatus("mandatory")
_SonomaFRPortStatsRecvLIVRsps_Type = Counter32
_SonomaFRPortStatsRecvLIVRsps_Object = MibTableColumn
sonomaFRPortStatsRecvLIVRsps = _SonomaFRPortStatsRecvLIVRsps_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 9, 9, 1, 4),
    _SonomaFRPortStatsRecvLIVRsps_Type()
)
sonomaFRPortStatsRecvLIVRsps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonomaFRPortStatsRecvLIVRsps.setStatus("mandatory")
_SonomaFRPortStatsSentLIVRsps_Type = Counter32
_SonomaFRPortStatsSentLIVRsps_Object = MibTableColumn
sonomaFRPortStatsSentLIVRsps = _SonomaFRPortStatsSentLIVRsps_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 9, 9, 1, 5),
    _SonomaFRPortStatsSentLIVRsps_Type()
)
sonomaFRPortStatsSentLIVRsps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonomaFRPortStatsSentLIVRsps.setStatus("mandatory")
_SonomaFRPortStatsRecvFullReqs_Type = Counter32
_SonomaFRPortStatsRecvFullReqs_Object = MibTableColumn
sonomaFRPortStatsRecvFullReqs = _SonomaFRPortStatsRecvFullReqs_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 9, 9, 1, 6),
    _SonomaFRPortStatsRecvFullReqs_Type()
)
sonomaFRPortStatsRecvFullReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonomaFRPortStatsRecvFullReqs.setStatus("mandatory")
_SonomaFRPortStatsSentFullReqs_Type = Counter32
_SonomaFRPortStatsSentFullReqs_Object = MibTableColumn
sonomaFRPortStatsSentFullReqs = _SonomaFRPortStatsSentFullReqs_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 9, 9, 1, 7),
    _SonomaFRPortStatsSentFullReqs_Type()
)
sonomaFRPortStatsSentFullReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonomaFRPortStatsSentFullReqs.setStatus("mandatory")
_SonomaFRPortStatsRecvFullRsps_Type = Counter32
_SonomaFRPortStatsRecvFullRsps_Object = MibTableColumn
sonomaFRPortStatsRecvFullRsps = _SonomaFRPortStatsRecvFullRsps_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 9, 9, 1, 8),
    _SonomaFRPortStatsRecvFullRsps_Type()
)
sonomaFRPortStatsRecvFullRsps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonomaFRPortStatsRecvFullRsps.setStatus("mandatory")
_SonomaFRPortStatsSentFullRsps_Type = Counter32
_SonomaFRPortStatsSentFullRsps_Object = MibTableColumn
sonomaFRPortStatsSentFullRsps = _SonomaFRPortStatsSentFullRsps_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 9, 9, 1, 9),
    _SonomaFRPortStatsSentFullRsps_Type()
)
sonomaFRPortStatsSentFullRsps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonomaFRPortStatsSentFullRsps.setStatus("mandatory")
_SonomaFRPortStatsRecvAsyncStatus_Type = Counter32
_SonomaFRPortStatsRecvAsyncStatus_Object = MibTableColumn
sonomaFRPortStatsRecvAsyncStatus = _SonomaFRPortStatsRecvAsyncStatus_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 9, 9, 1, 10),
    _SonomaFRPortStatsRecvAsyncStatus_Type()
)
sonomaFRPortStatsRecvAsyncStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonomaFRPortStatsRecvAsyncStatus.setStatus("mandatory")
_SonomaFRPortStatsSentAsyncStatus_Type = Counter32
_SonomaFRPortStatsSentAsyncStatus_Object = MibTableColumn
sonomaFRPortStatsSentAsyncStatus = _SonomaFRPortStatsSentAsyncStatus_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 9, 9, 1, 11),
    _SonomaFRPortStatsSentAsyncStatus_Type()
)
sonomaFRPortStatsSentAsyncStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonomaFRPortStatsSentAsyncStatus.setStatus("mandatory")
_SonomaFRPortStatsInvalidMessages_Type = Counter32
_SonomaFRPortStatsInvalidMessages_Object = MibTableColumn
sonomaFRPortStatsInvalidMessages = _SonomaFRPortStatsInvalidMessages_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 9, 9, 1, 12),
    _SonomaFRPortStatsInvalidMessages_Type()
)
sonomaFRPortStatsInvalidMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonomaFRPortStatsInvalidMessages.setStatus("mandatory")
_SonomaFRPortStatsInvalidSeqNumbers_Type = Counter32
_SonomaFRPortStatsInvalidSeqNumbers_Object = MibTableColumn
sonomaFRPortStatsInvalidSeqNumbers = _SonomaFRPortStatsInvalidSeqNumbers_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 9, 9, 1, 13),
    _SonomaFRPortStatsInvalidSeqNumbers_Type()
)
sonomaFRPortStatsInvalidSeqNumbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonomaFRPortStatsInvalidSeqNumbers.setStatus("mandatory")
_SonomaFRPortStatsTimeouts_Type = Counter32
_SonomaFRPortStatsTimeouts_Object = MibTableColumn
sonomaFRPortStatsTimeouts = _SonomaFRPortStatsTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 9, 9, 1, 14),
    _SonomaFRPortStatsTimeouts_Type()
)
sonomaFRPortStatsTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonomaFRPortStatsTimeouts.setStatus("mandatory")
_SonomaFRPortStatsServAffectingConditions_Type = Counter32
_SonomaFRPortStatsServAffectingConditions_Object = MibTableColumn
sonomaFRPortStatsServAffectingConditions = _SonomaFRPortStatsServAffectingConditions_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 9, 9, 1, 15),
    _SonomaFRPortStatsServAffectingConditions_Type()
)
sonomaFRPortStatsServAffectingConditions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonomaFRPortStatsServAffectingConditions.setStatus("mandatory")
_SonomaSerialPortStatsTable_Object = MibTable
sonomaSerialPortStatsTable = _SonomaSerialPortStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 9, 10)
)
if mibBuilder.loadTexts:
    sonomaSerialPortStatsTable.setStatus("mandatory")
_SonomaSerialPortStatsEntry_Object = MibTableRow
sonomaSerialPortStatsEntry = _SonomaSerialPortStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 9, 10, 1)
)
sonomaSerialPortStatsEntry.setIndexNames(
    (0, "SONOMA-FR-MIB", "sonomaSerialPortStatsPort"),
)
if mibBuilder.loadTexts:
    sonomaSerialPortStatsEntry.setStatus("mandatory")


class _SonomaSerialPortStatsPort_Type(Integer32):
    """Custom type sonomaSerialPortStatsPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_SonomaSerialPortStatsPort_Type.__name__ = "Integer32"
_SonomaSerialPortStatsPort_Object = MibTableColumn
sonomaSerialPortStatsPort = _SonomaSerialPortStatsPort_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 9, 10, 1, 1),
    _SonomaSerialPortStatsPort_Type()
)
sonomaSerialPortStatsPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonomaSerialPortStatsPort.setStatus("mandatory")
_SonomaSerialPortStatsRecvFrames_Type = Counter32
_SonomaSerialPortStatsRecvFrames_Object = MibTableColumn
sonomaSerialPortStatsRecvFrames = _SonomaSerialPortStatsRecvFrames_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 9, 10, 1, 2),
    _SonomaSerialPortStatsRecvFrames_Type()
)
sonomaSerialPortStatsRecvFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonomaSerialPortStatsRecvFrames.setStatus("mandatory")
_SonomaSerialPortStatsSentFrames_Type = Counter32
_SonomaSerialPortStatsSentFrames_Object = MibTableColumn
sonomaSerialPortStatsSentFrames = _SonomaSerialPortStatsSentFrames_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 9, 10, 1, 3),
    _SonomaSerialPortStatsSentFrames_Type()
)
sonomaSerialPortStatsSentFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonomaSerialPortStatsSentFrames.setStatus("mandatory")
_SonomaSerialPortStatsRecvBytes_Type = Counter32
_SonomaSerialPortStatsRecvBytes_Object = MibTableColumn
sonomaSerialPortStatsRecvBytes = _SonomaSerialPortStatsRecvBytes_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 9, 10, 1, 4),
    _SonomaSerialPortStatsRecvBytes_Type()
)
sonomaSerialPortStatsRecvBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonomaSerialPortStatsRecvBytes.setStatus("mandatory")
_SonomaSerialPortStatsSentBytes_Type = Counter32
_SonomaSerialPortStatsSentBytes_Object = MibTableColumn
sonomaSerialPortStatsSentBytes = _SonomaSerialPortStatsSentBytes_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 9, 10, 1, 5),
    _SonomaSerialPortStatsSentBytes_Type()
)
sonomaSerialPortStatsSentBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonomaSerialPortStatsSentBytes.setStatus("mandatory")
_SonomaSerialPortStatsRecvUtilization_Type = Counter32
_SonomaSerialPortStatsRecvUtilization_Object = MibTableColumn
sonomaSerialPortStatsRecvUtilization = _SonomaSerialPortStatsRecvUtilization_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 9, 10, 1, 6),
    _SonomaSerialPortStatsRecvUtilization_Type()
)
sonomaSerialPortStatsRecvUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonomaSerialPortStatsRecvUtilization.setStatus("mandatory")
_SonomaSerialPortStatsSendUtilization_Type = Counter32
_SonomaSerialPortStatsSendUtilization_Object = MibTableColumn
sonomaSerialPortStatsSendUtilization = _SonomaSerialPortStatsSendUtilization_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 9, 10, 1, 7),
    _SonomaSerialPortStatsSendUtilization_Type()
)
sonomaSerialPortStatsSendUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonomaSerialPortStatsSendUtilization.setStatus("mandatory")
_SonomaSerialPortStatsFrameCheckErrs_Type = Counter32
_SonomaSerialPortStatsFrameCheckErrs_Object = MibTableColumn
sonomaSerialPortStatsFrameCheckErrs = _SonomaSerialPortStatsFrameCheckErrs_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 9, 10, 1, 8),
    _SonomaSerialPortStatsFrameCheckErrs_Type()
)
sonomaSerialPortStatsFrameCheckErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonomaSerialPortStatsFrameCheckErrs.setStatus("mandatory")
_SonomaSerialPortStatsTransmitUnderrunErrs_Type = Counter32
_SonomaSerialPortStatsTransmitUnderrunErrs_Object = MibTableColumn
sonomaSerialPortStatsTransmitUnderrunErrs = _SonomaSerialPortStatsTransmitUnderrunErrs_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 9, 10, 1, 9),
    _SonomaSerialPortStatsTransmitUnderrunErrs_Type()
)
sonomaSerialPortStatsTransmitUnderrunErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonomaSerialPortStatsTransmitUnderrunErrs.setStatus("mandatory")
_SonomaSerialPortStatsReceiveOverrunErrs_Type = Counter32
_SonomaSerialPortStatsReceiveOverrunErrs_Object = MibTableColumn
sonomaSerialPortStatsReceiveOverrunErrs = _SonomaSerialPortStatsReceiveOverrunErrs_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 9, 10, 1, 10),
    _SonomaSerialPortStatsReceiveOverrunErrs_Type()
)
sonomaSerialPortStatsReceiveOverrunErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonomaSerialPortStatsReceiveOverrunErrs.setStatus("mandatory")
_SonomaSerialPortStatsInterruptedFrames_Type = Counter32
_SonomaSerialPortStatsInterruptedFrames_Object = MibTableColumn
sonomaSerialPortStatsInterruptedFrames = _SonomaSerialPortStatsInterruptedFrames_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 9, 10, 1, 11),
    _SonomaSerialPortStatsInterruptedFrames_Type()
)
sonomaSerialPortStatsInterruptedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonomaSerialPortStatsInterruptedFrames.setStatus("mandatory")
_SonomaSerialPortStatsAbortedFrames_Type = Counter32
_SonomaSerialPortStatsAbortedFrames_Object = MibTableColumn
sonomaSerialPortStatsAbortedFrames = _SonomaSerialPortStatsAbortedFrames_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 9, 10, 1, 12),
    _SonomaSerialPortStatsAbortedFrames_Type()
)
sonomaSerialPortStatsAbortedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonomaSerialPortStatsAbortedFrames.setStatus("mandatory")
_SonomaFRDlciStatsTable_Object = MibTable
sonomaFRDlciStatsTable = _SonomaFRDlciStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 9, 11)
)
if mibBuilder.loadTexts:
    sonomaFRDlciStatsTable.setStatus("mandatory")
_SonomaFRDlciStatsEntry_Object = MibTableRow
sonomaFRDlciStatsEntry = _SonomaFRDlciStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 9, 11, 1)
)
sonomaFRDlciStatsEntry.setIndexNames(
    (0, "SONOMA-FR-MIB", "sonomaFRDlciStatsPort"),
    (0, "SONOMA-FR-MIB", "sonomaFRDlciStatsDlci"),
)
if mibBuilder.loadTexts:
    sonomaFRDlciStatsEntry.setStatus("mandatory")


class _SonomaFRDlciStatsPort_Type(Integer32):
    """Custom type sonomaFRDlciStatsPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_SonomaFRDlciStatsPort_Type.__name__ = "Integer32"
_SonomaFRDlciStatsPort_Object = MibTableColumn
sonomaFRDlciStatsPort = _SonomaFRDlciStatsPort_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 9, 11, 1, 1),
    _SonomaFRDlciStatsPort_Type()
)
sonomaFRDlciStatsPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonomaFRDlciStatsPort.setStatus("mandatory")


class _SonomaFRDlciStatsDlci_Type(Integer32):
    """Custom type sonomaFRDlciStatsDlci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_SonomaFRDlciStatsDlci_Type.__name__ = "Integer32"
_SonomaFRDlciStatsDlci_Object = MibTableColumn
sonomaFRDlciStatsDlci = _SonomaFRDlciStatsDlci_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 9, 11, 1, 2),
    _SonomaFRDlciStatsDlci_Type()
)
sonomaFRDlciStatsDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonomaFRDlciStatsDlci.setStatus("mandatory")
_SonomaFRDlciStatsRecvFrames_Type = Counter32
_SonomaFRDlciStatsRecvFrames_Object = MibTableColumn
sonomaFRDlciStatsRecvFrames = _SonomaFRDlciStatsRecvFrames_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 9, 11, 1, 3),
    _SonomaFRDlciStatsRecvFrames_Type()
)
sonomaFRDlciStatsRecvFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonomaFRDlciStatsRecvFrames.setStatus("mandatory")
_SonomaFRDlciStatsSentFrames_Type = Counter32
_SonomaFRDlciStatsSentFrames_Object = MibTableColumn
sonomaFRDlciStatsSentFrames = _SonomaFRDlciStatsSentFrames_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 9, 11, 1, 4),
    _SonomaFRDlciStatsSentFrames_Type()
)
sonomaFRDlciStatsSentFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonomaFRDlciStatsSentFrames.setStatus("mandatory")
_SonomaFRDlciStatsRecvBytes_Type = Counter32
_SonomaFRDlciStatsRecvBytes_Object = MibTableColumn
sonomaFRDlciStatsRecvBytes = _SonomaFRDlciStatsRecvBytes_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 9, 11, 1, 5),
    _SonomaFRDlciStatsRecvBytes_Type()
)
sonomaFRDlciStatsRecvBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonomaFRDlciStatsRecvBytes.setStatus("mandatory")
_SonomaFRDlciStatsSentBytes_Type = Counter32
_SonomaFRDlciStatsSentBytes_Object = MibTableColumn
sonomaFRDlciStatsSentBytes = _SonomaFRDlciStatsSentBytes_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 9, 11, 1, 6),
    _SonomaFRDlciStatsSentBytes_Type()
)
sonomaFRDlciStatsSentBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonomaFRDlciStatsSentBytes.setStatus("mandatory")
_SonomaFRDlciStatsRecvDeFrames_Type = Counter32
_SonomaFRDlciStatsRecvDeFrames_Object = MibTableColumn
sonomaFRDlciStatsRecvDeFrames = _SonomaFRDlciStatsRecvDeFrames_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 9, 11, 1, 7),
    _SonomaFRDlciStatsRecvDeFrames_Type()
)
sonomaFRDlciStatsRecvDeFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonomaFRDlciStatsRecvDeFrames.setStatus("mandatory")
_SonomaFRDlciStatsSentDeFrames_Type = Counter32
_SonomaFRDlciStatsSentDeFrames_Object = MibTableColumn
sonomaFRDlciStatsSentDeFrames = _SonomaFRDlciStatsSentDeFrames_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 9, 11, 1, 8),
    _SonomaFRDlciStatsSentDeFrames_Type()
)
sonomaFRDlciStatsSentDeFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonomaFRDlciStatsSentDeFrames.setStatus("mandatory")
_SonomaFRDlciStatsRecvExcess_Type = Counter32
_SonomaFRDlciStatsRecvExcess_Object = MibTableColumn
sonomaFRDlciStatsRecvExcess = _SonomaFRDlciStatsRecvExcess_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 9, 11, 1, 9),
    _SonomaFRDlciStatsRecvExcess_Type()
)
sonomaFRDlciStatsRecvExcess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonomaFRDlciStatsRecvExcess.setStatus("mandatory")
_SonomaFRDlciStatsSentExcess_Type = Counter32
_SonomaFRDlciStatsSentExcess_Object = MibTableColumn
sonomaFRDlciStatsSentExcess = _SonomaFRDlciStatsSentExcess_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 9, 11, 1, 10),
    _SonomaFRDlciStatsSentExcess_Type()
)
sonomaFRDlciStatsSentExcess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonomaFRDlciStatsSentExcess.setStatus("mandatory")
_SonomaFRDlciStatsRecvDiscards_Type = Counter32
_SonomaFRDlciStatsRecvDiscards_Object = MibTableColumn
sonomaFRDlciStatsRecvDiscards = _SonomaFRDlciStatsRecvDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 9, 11, 1, 11),
    _SonomaFRDlciStatsRecvDiscards_Type()
)
sonomaFRDlciStatsRecvDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonomaFRDlciStatsRecvDiscards.setStatus("mandatory")
_SonomaFRDlciStatsSentDiscards_Type = Counter32
_SonomaFRDlciStatsSentDiscards_Object = MibTableColumn
sonomaFRDlciStatsSentDiscards = _SonomaFRDlciStatsSentDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 9, 11, 1, 12),
    _SonomaFRDlciStatsSentDiscards_Type()
)
sonomaFRDlciStatsSentDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonomaFRDlciStatsSentDiscards.setStatus("mandatory")
_SonomaFRDlciStatsRecvFecns_Type = Counter32
_SonomaFRDlciStatsRecvFecns_Object = MibTableColumn
sonomaFRDlciStatsRecvFecns = _SonomaFRDlciStatsRecvFecns_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 9, 11, 1, 13),
    _SonomaFRDlciStatsRecvFecns_Type()
)
sonomaFRDlciStatsRecvFecns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonomaFRDlciStatsRecvFecns.setStatus("mandatory")
_SonomaFRDlciStatsSentFecns_Type = Counter32
_SonomaFRDlciStatsSentFecns_Object = MibTableColumn
sonomaFRDlciStatsSentFecns = _SonomaFRDlciStatsSentFecns_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 9, 11, 1, 14),
    _SonomaFRDlciStatsSentFecns_Type()
)
sonomaFRDlciStatsSentFecns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonomaFRDlciStatsSentFecns.setStatus("mandatory")
_SonomaFRDlciStatsRecvBecns_Type = Counter32
_SonomaFRDlciStatsRecvBecns_Object = MibTableColumn
sonomaFRDlciStatsRecvBecns = _SonomaFRDlciStatsRecvBecns_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 9, 11, 1, 15),
    _SonomaFRDlciStatsRecvBecns_Type()
)
sonomaFRDlciStatsRecvBecns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonomaFRDlciStatsRecvBecns.setStatus("mandatory")
_SonomaFRDlciStatsSentBecns_Type = Counter32
_SonomaFRDlciStatsSentBecns_Object = MibTableColumn
sonomaFRDlciStatsSentBecns = _SonomaFRDlciStatsSentBecns_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 9, 11, 1, 16),
    _SonomaFRDlciStatsSentBecns_Type()
)
sonomaFRDlciStatsSentBecns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonomaFRDlciStatsSentBecns.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SONOMA-FR-MIB",
    **{"sonomaFR": sonomaFR,
       "sonomaFracTable": sonomaFracTable,
       "sonomaFracEntry": sonomaFracEntry,
       "sonomaFracIndex": sonomaFracIndex,
       "sonomaFracCount": sonomaFracCount,
       "ccT5Table": ccT5Table,
       "ccT5Entry": ccT5Entry,
       "ccT5EndPointA": ccT5EndPointA,
       "ccT5EndPointB": ccT5EndPointB,
       "ccT5FRSSCSDLCI": ccT5FRSSCSDLCI,
       "ccT5DEtoCLPMapping": ccT5DEtoCLPMapping,
       "ccT5CLPtoDEMapping": ccT5CLPtoDEMapping,
       "ccT5SSCSManagement": ccT5SSCSManagement,
       "ccT5RowStatus": ccT5RowStatus,
       "sonomaFRDcePortTable": sonomaFRDcePortTable,
       "sonomaFRDcePortEntry": sonomaFRDcePortEntry,
       "sonomaFRDcePort": sonomaFRDcePort,
       "sonomaFRDcePortType": sonomaFRDcePortType,
       "sonomaFRDcePortIncomingRateControl": sonomaFRDcePortIncomingRateControl,
       "sonomaFRDcePortOutgoingRateControl": sonomaFRDcePortOutgoingRateControl,
       "sonomaFRDlciTable": sonomaFRDlciTable,
       "sonomaFRDlciEntry": sonomaFRDlciEntry,
       "sonomaFRDlciPort": sonomaFRDlciPort,
       "sonomaFRDlci": sonomaFRDlci,
       "sonomaFrDlcmiTable": sonomaFrDlcmiTable,
       "sonomaFrDlcmiEntry": sonomaFrDlcmiEntry,
       "sonomaFrDlcmiIfIndex": sonomaFrDlcmiIfIndex,
       "sonomaFrDlcmiState": sonomaFrDlcmiState,
       "sonomaFrDlcmiPollingInterval": sonomaFrDlcmiPollingInterval,
       "sonomaFrDlcmiFullEnquiryInterval": sonomaFrDlcmiFullEnquiryInterval,
       "sonomaFrDlcmiErrorThreshold": sonomaFrDlcmiErrorThreshold,
       "sonomaFrDlcmiMonitoredEvents": sonomaFrDlcmiMonitoredEvents,
       "sonomaFrDlcmiStatus": sonomaFrDlcmiStatus,
       "sonomaFRDtePortTable": sonomaFRDtePortTable,
       "sonomaFRDtePortEntry": sonomaFRDtePortEntry,
       "sonomaFRDtePort": sonomaFRDtePort,
       "sonomaFRDtePortType": sonomaFRDtePortType,
       "ccT8Table": ccT8Table,
       "ccT8Entry": ccT8Entry,
       "ccT8EndPointA": ccT8EndPointA,
       "ccT8EndPointB": ccT8EndPointB,
       "ccT8DECLPMapping": ccT8DECLPMapping,
       "ccT8FECNEFCIMapping": ccT8FECNEFCIMapping,
       "ccT8ULPEncapsulation": ccT8ULPEncapsulation,
       "ccT8RowStatus": ccT8RowStatus,
       "sonomaFRPortStatsTable": sonomaFRPortStatsTable,
       "sonomaFRPortStatsEntry": sonomaFRPortStatsEntry,
       "sonomaFRPortStatsPort": sonomaFRPortStatsPort,
       "sonomaFRPortStatsRecvLIVReqs": sonomaFRPortStatsRecvLIVReqs,
       "sonomaFRPortStatsSentLIVReqs": sonomaFRPortStatsSentLIVReqs,
       "sonomaFRPortStatsRecvLIVRsps": sonomaFRPortStatsRecvLIVRsps,
       "sonomaFRPortStatsSentLIVRsps": sonomaFRPortStatsSentLIVRsps,
       "sonomaFRPortStatsRecvFullReqs": sonomaFRPortStatsRecvFullReqs,
       "sonomaFRPortStatsSentFullReqs": sonomaFRPortStatsSentFullReqs,
       "sonomaFRPortStatsRecvFullRsps": sonomaFRPortStatsRecvFullRsps,
       "sonomaFRPortStatsSentFullRsps": sonomaFRPortStatsSentFullRsps,
       "sonomaFRPortStatsRecvAsyncStatus": sonomaFRPortStatsRecvAsyncStatus,
       "sonomaFRPortStatsSentAsyncStatus": sonomaFRPortStatsSentAsyncStatus,
       "sonomaFRPortStatsInvalidMessages": sonomaFRPortStatsInvalidMessages,
       "sonomaFRPortStatsInvalidSeqNumbers": sonomaFRPortStatsInvalidSeqNumbers,
       "sonomaFRPortStatsTimeouts": sonomaFRPortStatsTimeouts,
       "sonomaFRPortStatsServAffectingConditions": sonomaFRPortStatsServAffectingConditions,
       "sonomaSerialPortStatsTable": sonomaSerialPortStatsTable,
       "sonomaSerialPortStatsEntry": sonomaSerialPortStatsEntry,
       "sonomaSerialPortStatsPort": sonomaSerialPortStatsPort,
       "sonomaSerialPortStatsRecvFrames": sonomaSerialPortStatsRecvFrames,
       "sonomaSerialPortStatsSentFrames": sonomaSerialPortStatsSentFrames,
       "sonomaSerialPortStatsRecvBytes": sonomaSerialPortStatsRecvBytes,
       "sonomaSerialPortStatsSentBytes": sonomaSerialPortStatsSentBytes,
       "sonomaSerialPortStatsRecvUtilization": sonomaSerialPortStatsRecvUtilization,
       "sonomaSerialPortStatsSendUtilization": sonomaSerialPortStatsSendUtilization,
       "sonomaSerialPortStatsFrameCheckErrs": sonomaSerialPortStatsFrameCheckErrs,
       "sonomaSerialPortStatsTransmitUnderrunErrs": sonomaSerialPortStatsTransmitUnderrunErrs,
       "sonomaSerialPortStatsReceiveOverrunErrs": sonomaSerialPortStatsReceiveOverrunErrs,
       "sonomaSerialPortStatsInterruptedFrames": sonomaSerialPortStatsInterruptedFrames,
       "sonomaSerialPortStatsAbortedFrames": sonomaSerialPortStatsAbortedFrames,
       "sonomaFRDlciStatsTable": sonomaFRDlciStatsTable,
       "sonomaFRDlciStatsEntry": sonomaFRDlciStatsEntry,
       "sonomaFRDlciStatsPort": sonomaFRDlciStatsPort,
       "sonomaFRDlciStatsDlci": sonomaFRDlciStatsDlci,
       "sonomaFRDlciStatsRecvFrames": sonomaFRDlciStatsRecvFrames,
       "sonomaFRDlciStatsSentFrames": sonomaFRDlciStatsSentFrames,
       "sonomaFRDlciStatsRecvBytes": sonomaFRDlciStatsRecvBytes,
       "sonomaFRDlciStatsSentBytes": sonomaFRDlciStatsSentBytes,
       "sonomaFRDlciStatsRecvDeFrames": sonomaFRDlciStatsRecvDeFrames,
       "sonomaFRDlciStatsSentDeFrames": sonomaFRDlciStatsSentDeFrames,
       "sonomaFRDlciStatsRecvExcess": sonomaFRDlciStatsRecvExcess,
       "sonomaFRDlciStatsSentExcess": sonomaFRDlciStatsSentExcess,
       "sonomaFRDlciStatsRecvDiscards": sonomaFRDlciStatsRecvDiscards,
       "sonomaFRDlciStatsSentDiscards": sonomaFRDlciStatsSentDiscards,
       "sonomaFRDlciStatsRecvFecns": sonomaFRDlciStatsRecvFecns,
       "sonomaFRDlciStatsSentFecns": sonomaFRDlciStatsSentFecns,
       "sonomaFRDlciStatsRecvBecns": sonomaFRDlciStatsRecvBecns,
       "sonomaFRDlciStatsSentBecns": sonomaFRDlciStatsSentBecns}
)
