# SNMP MIB module (IBMFRBRS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IBMFRBRS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:07:52 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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

_IbmfrBRS_ObjectIdentity = ObjectIdentity
ibmfrBRS = _IbmfrBRS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 4, 4)
)
_IbmfrBRSOperational_ObjectIdentity = ObjectIdentity
ibmfrBRSOperational = _IbmfrBRSOperational_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 4, 4, 1)
)
_IbmfrBRSInterfaceTable_Object = MibTable
ibmfrBRSInterfaceTable = _IbmfrBRSInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 4, 4, 1, 1)
)
if mibBuilder.loadTexts:
    ibmfrBRSInterfaceTable.setStatus("mandatory")
_IbmfrBRSInterfaceEntry_Object = MibTableRow
ibmfrBRSInterfaceEntry = _IbmfrBRSInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 4, 4, 1, 1, 1)
)
ibmfrBRSInterfaceEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ibmfrBRSInterfaceEntry.setStatus("mandatory")
_IbmfrBRSInterfaceMaxQueue_Type = Integer32
_IbmfrBRSInterfaceMaxQueue_Object = MibTableColumn
ibmfrBRSInterfaceMaxQueue = _IbmfrBRSInterfaceMaxQueue_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 4, 4, 1, 1, 1, 1),
    _IbmfrBRSInterfaceMaxQueue_Type()
)
ibmfrBRSInterfaceMaxQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmfrBRSInterfaceMaxQueue.setStatus("mandatory")
_IbmfrBRSInterfaceMinQueue_Type = Integer32
_IbmfrBRSInterfaceMinQueue_Object = MibTableColumn
ibmfrBRSInterfaceMinQueue = _IbmfrBRSInterfaceMinQueue_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 4, 4, 1, 1, 1, 2),
    _IbmfrBRSInterfaceMinQueue_Type()
)
ibmfrBRSInterfaceMinQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmfrBRSInterfaceMinQueue.setStatus("mandatory")
_IbmfrBRSInterfaceTotalBandwidth_Type = Integer32
_IbmfrBRSInterfaceTotalBandwidth_Object = MibTableColumn
ibmfrBRSInterfaceTotalBandwidth = _IbmfrBRSInterfaceTotalBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 4, 4, 1, 1, 1, 3),
    _IbmfrBRSInterfaceTotalBandwidth_Type()
)
ibmfrBRSInterfaceTotalBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmfrBRSInterfaceTotalBandwidth.setStatus("mandatory")
_IbmfrBRSInterfaceTotalCircuitClasses_Type = Integer32
_IbmfrBRSInterfaceTotalCircuitClasses_Object = MibTableColumn
ibmfrBRSInterfaceTotalCircuitClasses = _IbmfrBRSInterfaceTotalCircuitClasses_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 4, 4, 1, 1, 1, 4),
    _IbmfrBRSInterfaceTotalCircuitClasses_Type()
)
ibmfrBRSInterfaceTotalCircuitClasses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmfrBRSInterfaceTotalCircuitClasses.setStatus("mandatory")
_IbmfrBRSInterfaceDefaultCircuitClassName_Type = DisplayString
_IbmfrBRSInterfaceDefaultCircuitClassName_Object = MibTableColumn
ibmfrBRSInterfaceDefaultCircuitClassName = _IbmfrBRSInterfaceDefaultCircuitClassName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 4, 4, 1, 1, 1, 5),
    _IbmfrBRSInterfaceDefaultCircuitClassName_Type()
)
ibmfrBRSInterfaceDefaultCircuitClassName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmfrBRSInterfaceDefaultCircuitClassName.setStatus("mandatory")
_IbmfrBRSCircuitClassTable_Object = MibTable
ibmfrBRSCircuitClassTable = _IbmfrBRSCircuitClassTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 4, 4, 1, 2)
)
if mibBuilder.loadTexts:
    ibmfrBRSCircuitClassTable.setStatus("mandatory")
_IbmfrBRSCircuitClassEntry_Object = MibTableRow
ibmfrBRSCircuitClassEntry = _IbmfrBRSCircuitClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 4, 4, 1, 2, 1)
)
ibmfrBRSCircuitClassEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "IBMFRBRS-MIB", "ibmfrBRSCircuitClassName"),
)
if mibBuilder.loadTexts:
    ibmfrBRSCircuitClassEntry.setStatus("mandatory")
_IbmfrBRSCircuitClassName_Type = DisplayString
_IbmfrBRSCircuitClassName_Object = MibTableColumn
ibmfrBRSCircuitClassName = _IbmfrBRSCircuitClassName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 4, 4, 1, 2, 1, 1),
    _IbmfrBRSCircuitClassName_Type()
)
ibmfrBRSCircuitClassName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ibmfrBRSCircuitClassName.setStatus("mandatory")
_IbmfrBRSCircuitClassBandwidth_Type = Integer32
_IbmfrBRSCircuitClassBandwidth_Object = MibTableColumn
ibmfrBRSCircuitClassBandwidth = _IbmfrBRSCircuitClassBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 4, 4, 1, 2, 1, 2),
    _IbmfrBRSCircuitClassBandwidth_Type()
)
ibmfrBRSCircuitClassBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmfrBRSCircuitClassBandwidth.setStatus("mandatory")
_IbmfrBRSCircuitClassPacketXmit_Type = Counter32
_IbmfrBRSCircuitClassPacketXmit_Object = MibTableColumn
ibmfrBRSCircuitClassPacketXmit = _IbmfrBRSCircuitClassPacketXmit_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 4, 4, 1, 2, 1, 3),
    _IbmfrBRSCircuitClassPacketXmit_Type()
)
ibmfrBRSCircuitClassPacketXmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmfrBRSCircuitClassPacketXmit.setStatus("mandatory")
_IbmfrBRSCircuitClassBytesXmit_Type = Counter32
_IbmfrBRSCircuitClassBytesXmit_Object = MibTableColumn
ibmfrBRSCircuitClassBytesXmit = _IbmfrBRSCircuitClassBytesXmit_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 4, 4, 1, 2, 1, 4),
    _IbmfrBRSCircuitClassBytesXmit_Type()
)
ibmfrBRSCircuitClassBytesXmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmfrBRSCircuitClassBytesXmit.setStatus("mandatory")
_IbmfrBRSCircuitClassBytesOverflow_Type = Counter32
_IbmfrBRSCircuitClassBytesOverflow_Object = MibTableColumn
ibmfrBRSCircuitClassBytesOverflow = _IbmfrBRSCircuitClassBytesOverflow_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 4, 4, 1, 2, 1, 5),
    _IbmfrBRSCircuitClassBytesOverflow_Type()
)
ibmfrBRSCircuitClassBytesOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmfrBRSCircuitClassBytesOverflow.setStatus("mandatory")
_IbmfrBRSCircuitClassLastPacketXmit_Type = Counter32
_IbmfrBRSCircuitClassLastPacketXmit_Object = MibTableColumn
ibmfrBRSCircuitClassLastPacketXmit = _IbmfrBRSCircuitClassLastPacketXmit_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 4, 4, 1, 2, 1, 6),
    _IbmfrBRSCircuitClassLastPacketXmit_Type()
)
ibmfrBRSCircuitClassLastPacketXmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmfrBRSCircuitClassLastPacketXmit.setStatus("mandatory")
_IbmfrBRSCircuitClassLastBytesXmit_Type = Counter32
_IbmfrBRSCircuitClassLastBytesXmit_Object = MibTableColumn
ibmfrBRSCircuitClassLastBytesXmit = _IbmfrBRSCircuitClassLastBytesXmit_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 4, 4, 1, 2, 1, 7),
    _IbmfrBRSCircuitClassLastBytesXmit_Type()
)
ibmfrBRSCircuitClassLastBytesXmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmfrBRSCircuitClassLastBytesXmit.setStatus("mandatory")
_IbmfrBRSCircuitClassLastBytesOverflow_Type = Counter32
_IbmfrBRSCircuitClassLastBytesOverflow_Object = MibTableColumn
ibmfrBRSCircuitClassLastBytesOverflow = _IbmfrBRSCircuitClassLastBytesOverflow_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 4, 4, 1, 2, 1, 8),
    _IbmfrBRSCircuitClassLastBytesOverflow_Type()
)
ibmfrBRSCircuitClassLastBytesOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmfrBRSCircuitClassLastBytesOverflow.setStatus("mandatory")


class _IbmfrBRSCircuitClassClearCounters_Type(Integer32):
    """Custom type ibmfrBRSCircuitClassClearCounters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
    )


_IbmfrBRSCircuitClassClearCounters_Type.__name__ = "Integer32"
_IbmfrBRSCircuitClassClearCounters_Object = MibTableColumn
ibmfrBRSCircuitClassClearCounters = _IbmfrBRSCircuitClassClearCounters_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 4, 4, 1, 2, 1, 9),
    _IbmfrBRSCircuitClassClearCounters_Type()
)
ibmfrBRSCircuitClassClearCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmfrBRSCircuitClassClearCounters.setStatus("mandatory")
_IbmfrBRSCircuitTable_Object = MibTable
ibmfrBRSCircuitTable = _IbmfrBRSCircuitTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 4, 4, 1, 3)
)
if mibBuilder.loadTexts:
    ibmfrBRSCircuitTable.setStatus("mandatory")
_IbmfrBRSCircuitEntry_Object = MibTableRow
ibmfrBRSCircuitEntry = _IbmfrBRSCircuitEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 4, 4, 1, 3, 1)
)
ibmfrBRSCircuitEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "IBMFRBRS-MIB", "ibmfrBRSCircuitClassName"),
    (0, "IBMFRBRS-MIB", "ibmfrBRSCircuitNumber"),
)
if mibBuilder.loadTexts:
    ibmfrBRSCircuitEntry.setStatus("mandatory")
_IbmfrBRSCircuitNumber_Type = Integer32
_IbmfrBRSCircuitNumber_Object = MibTableColumn
ibmfrBRSCircuitNumber = _IbmfrBRSCircuitNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 4, 4, 1, 3, 1, 1),
    _IbmfrBRSCircuitNumber_Type()
)
ibmfrBRSCircuitNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ibmfrBRSCircuitNumber.setStatus("mandatory")
_IbmfrBRSCircuitMaxQueue_Type = Integer32
_IbmfrBRSCircuitMaxQueue_Object = MibTableColumn
ibmfrBRSCircuitMaxQueue = _IbmfrBRSCircuitMaxQueue_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 4, 4, 1, 3, 1, 2),
    _IbmfrBRSCircuitMaxQueue_Type()
)
ibmfrBRSCircuitMaxQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmfrBRSCircuitMaxQueue.setStatus("mandatory")
_IbmfrBRSCircuitMinQueue_Type = Integer32
_IbmfrBRSCircuitMinQueue_Object = MibTableColumn
ibmfrBRSCircuitMinQueue = _IbmfrBRSCircuitMinQueue_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 4, 4, 1, 3, 1, 3),
    _IbmfrBRSCircuitMinQueue_Type()
)
ibmfrBRSCircuitMinQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmfrBRSCircuitMinQueue.setStatus("mandatory")
_IbmfrBRSCircuitTotalBandwidth_Type = Integer32
_IbmfrBRSCircuitTotalBandwidth_Object = MibTableColumn
ibmfrBRSCircuitTotalBandwidth = _IbmfrBRSCircuitTotalBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 4, 4, 1, 3, 1, 4),
    _IbmfrBRSCircuitTotalBandwidth_Type()
)
ibmfrBRSCircuitTotalBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmfrBRSCircuitTotalBandwidth.setStatus("mandatory")
_IbmfrBRSCircuitTotalTrafficClasses_Type = Integer32
_IbmfrBRSCircuitTotalTrafficClasses_Object = MibTableColumn
ibmfrBRSCircuitTotalTrafficClasses = _IbmfrBRSCircuitTotalTrafficClasses_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 4, 4, 1, 3, 1, 5),
    _IbmfrBRSCircuitTotalTrafficClasses_Type()
)
ibmfrBRSCircuitTotalTrafficClasses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmfrBRSCircuitTotalTrafficClasses.setStatus("mandatory")
_IbmfrBRSCircuitDefaultTrafficClassName_Type = DisplayString
_IbmfrBRSCircuitDefaultTrafficClassName_Object = MibTableColumn
ibmfrBRSCircuitDefaultTrafficClassName = _IbmfrBRSCircuitDefaultTrafficClassName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 4, 4, 1, 3, 1, 6),
    _IbmfrBRSCircuitDefaultTrafficClassName_Type()
)
ibmfrBRSCircuitDefaultTrafficClassName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmfrBRSCircuitDefaultTrafficClassName.setStatus("mandatory")


class _IbmfrBRSCircuitDefaultTrafficClassPrio_Type(Integer32):
    """Custom type ibmfrBRSCircuitDefaultTrafficClassPrio based on Integer32"""
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
        *(("high", 3),
          ("low", 1),
          ("normal", 2),
          ("urgent", 4))
    )


_IbmfrBRSCircuitDefaultTrafficClassPrio_Type.__name__ = "Integer32"
_IbmfrBRSCircuitDefaultTrafficClassPrio_Object = MibTableColumn
ibmfrBRSCircuitDefaultTrafficClassPrio = _IbmfrBRSCircuitDefaultTrafficClassPrio_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 4, 4, 1, 3, 1, 7),
    _IbmfrBRSCircuitDefaultTrafficClassPrio_Type()
)
ibmfrBRSCircuitDefaultTrafficClassPrio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmfrBRSCircuitDefaultTrafficClassPrio.setStatus("mandatory")


class _IbmfrBRSCircuitSpecification_Type(Integer32):
    """Custom type ibmfrBRSCircuitSpecification based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("defaults", 1),
          ("specific", 2))
    )


_IbmfrBRSCircuitSpecification_Type.__name__ = "Integer32"
_IbmfrBRSCircuitSpecification_Object = MibTableColumn
ibmfrBRSCircuitSpecification = _IbmfrBRSCircuitSpecification_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 4, 4, 1, 3, 1, 8),
    _IbmfrBRSCircuitSpecification_Type()
)
ibmfrBRSCircuitSpecification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmfrBRSCircuitSpecification.setStatus("mandatory")
_IbmfrBRSCircuitSuperClassName_Type = DisplayString
_IbmfrBRSCircuitSuperClassName_Object = MibTableColumn
ibmfrBRSCircuitSuperClassName = _IbmfrBRSCircuitSuperClassName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 4, 4, 1, 3, 1, 9),
    _IbmfrBRSCircuitSuperClassName_Type()
)
ibmfrBRSCircuitSuperClassName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmfrBRSCircuitSuperClassName.setStatus("mandatory")
_IbmfrBRSCircuitSVCName_Type = DisplayString
_IbmfrBRSCircuitSVCName_Object = MibTableColumn
ibmfrBRSCircuitSVCName = _IbmfrBRSCircuitSVCName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 4, 4, 1, 3, 1, 10),
    _IbmfrBRSCircuitSVCName_Type()
)
ibmfrBRSCircuitSVCName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmfrBRSCircuitSVCName.setStatus("mandatory")
_IbmfrBRSTrafficClassTable_Object = MibTable
ibmfrBRSTrafficClassTable = _IbmfrBRSTrafficClassTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 4, 4, 1, 4)
)
if mibBuilder.loadTexts:
    ibmfrBRSTrafficClassTable.setStatus("mandatory")
_IbmfrBRSTrafficClassEntry_Object = MibTableRow
ibmfrBRSTrafficClassEntry = _IbmfrBRSTrafficClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 4, 4, 1, 4, 1)
)
ibmfrBRSTrafficClassEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "IBMFRBRS-MIB", "ibmfrBRSCircuitClassName"),
    (0, "IBMFRBRS-MIB", "ibmfrBRSCircuitNumber"),
    (0, "IBMFRBRS-MIB", "ibmfrBRSTrafficClassName"),
)
if mibBuilder.loadTexts:
    ibmfrBRSTrafficClassEntry.setStatus("mandatory")
_IbmfrBRSTrafficClassName_Type = DisplayString
_IbmfrBRSTrafficClassName_Object = MibTableColumn
ibmfrBRSTrafficClassName = _IbmfrBRSTrafficClassName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 4, 4, 1, 4, 1, 1),
    _IbmfrBRSTrafficClassName_Type()
)
ibmfrBRSTrafficClassName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ibmfrBRSTrafficClassName.setStatus("mandatory")
_IbmfrBRSTrafficClassBandwidth_Type = Integer32
_IbmfrBRSTrafficClassBandwidth_Object = MibTableColumn
ibmfrBRSTrafficClassBandwidth = _IbmfrBRSTrafficClassBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 4, 4, 1, 4, 1, 2),
    _IbmfrBRSTrafficClassBandwidth_Type()
)
ibmfrBRSTrafficClassBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmfrBRSTrafficClassBandwidth.setStatus("mandatory")
_IbmfrBRSTrafficClassTotalPacketXmit_Type = Counter32
_IbmfrBRSTrafficClassTotalPacketXmit_Object = MibTableColumn
ibmfrBRSTrafficClassTotalPacketXmit = _IbmfrBRSTrafficClassTotalPacketXmit_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 4, 4, 1, 4, 1, 3),
    _IbmfrBRSTrafficClassTotalPacketXmit_Type()
)
ibmfrBRSTrafficClassTotalPacketXmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmfrBRSTrafficClassTotalPacketXmit.setStatus("mandatory")
_IbmfrBRSTrafficClassPacketXmitLow_Type = Counter32
_IbmfrBRSTrafficClassPacketXmitLow_Object = MibTableColumn
ibmfrBRSTrafficClassPacketXmitLow = _IbmfrBRSTrafficClassPacketXmitLow_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 4, 4, 1, 4, 1, 4),
    _IbmfrBRSTrafficClassPacketXmitLow_Type()
)
ibmfrBRSTrafficClassPacketXmitLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmfrBRSTrafficClassPacketXmitLow.setStatus("mandatory")
_IbmfrBRSTrafficClassPacketXmitNormal_Type = Counter32
_IbmfrBRSTrafficClassPacketXmitNormal_Object = MibTableColumn
ibmfrBRSTrafficClassPacketXmitNormal = _IbmfrBRSTrafficClassPacketXmitNormal_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 4, 4, 1, 4, 1, 5),
    _IbmfrBRSTrafficClassPacketXmitNormal_Type()
)
ibmfrBRSTrafficClassPacketXmitNormal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmfrBRSTrafficClassPacketXmitNormal.setStatus("mandatory")
_IbmfrBRSTrafficClassPacketXmitHigh_Type = Counter32
_IbmfrBRSTrafficClassPacketXmitHigh_Object = MibTableColumn
ibmfrBRSTrafficClassPacketXmitHigh = _IbmfrBRSTrafficClassPacketXmitHigh_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 4, 4, 1, 4, 1, 6),
    _IbmfrBRSTrafficClassPacketXmitHigh_Type()
)
ibmfrBRSTrafficClassPacketXmitHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmfrBRSTrafficClassPacketXmitHigh.setStatus("mandatory")
_IbmfrBRSTrafficClassPacketXmitUrgent_Type = Counter32
_IbmfrBRSTrafficClassPacketXmitUrgent_Object = MibTableColumn
ibmfrBRSTrafficClassPacketXmitUrgent = _IbmfrBRSTrafficClassPacketXmitUrgent_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 4, 4, 1, 4, 1, 7),
    _IbmfrBRSTrafficClassPacketXmitUrgent_Type()
)
ibmfrBRSTrafficClassPacketXmitUrgent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmfrBRSTrafficClassPacketXmitUrgent.setStatus("mandatory")
_IbmfrBRSTrafficClassTotalBytesXmit_Type = Counter32
_IbmfrBRSTrafficClassTotalBytesXmit_Object = MibTableColumn
ibmfrBRSTrafficClassTotalBytesXmit = _IbmfrBRSTrafficClassTotalBytesXmit_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 4, 4, 1, 4, 1, 8),
    _IbmfrBRSTrafficClassTotalBytesXmit_Type()
)
ibmfrBRSTrafficClassTotalBytesXmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmfrBRSTrafficClassTotalBytesXmit.setStatus("mandatory")
_IbmfrBRSTrafficClassBytesXmitLow_Type = Counter32
_IbmfrBRSTrafficClassBytesXmitLow_Object = MibTableColumn
ibmfrBRSTrafficClassBytesXmitLow = _IbmfrBRSTrafficClassBytesXmitLow_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 4, 4, 1, 4, 1, 9),
    _IbmfrBRSTrafficClassBytesXmitLow_Type()
)
ibmfrBRSTrafficClassBytesXmitLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmfrBRSTrafficClassBytesXmitLow.setStatus("mandatory")
_IbmfrBRSTrafficClassBytesXmitNormal_Type = Counter32
_IbmfrBRSTrafficClassBytesXmitNormal_Object = MibTableColumn
ibmfrBRSTrafficClassBytesXmitNormal = _IbmfrBRSTrafficClassBytesXmitNormal_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 4, 4, 1, 4, 1, 10),
    _IbmfrBRSTrafficClassBytesXmitNormal_Type()
)
ibmfrBRSTrafficClassBytesXmitNormal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmfrBRSTrafficClassBytesXmitNormal.setStatus("mandatory")
_IbmfrBRSTrafficClassBytesXmitHigh_Type = Counter32
_IbmfrBRSTrafficClassBytesXmitHigh_Object = MibTableColumn
ibmfrBRSTrafficClassBytesXmitHigh = _IbmfrBRSTrafficClassBytesXmitHigh_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 4, 4, 1, 4, 1, 11),
    _IbmfrBRSTrafficClassBytesXmitHigh_Type()
)
ibmfrBRSTrafficClassBytesXmitHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmfrBRSTrafficClassBytesXmitHigh.setStatus("mandatory")
_IbmfrBRSTrafficClassBytesXmitUrgent_Type = Counter32
_IbmfrBRSTrafficClassBytesXmitUrgent_Object = MibTableColumn
ibmfrBRSTrafficClassBytesXmitUrgent = _IbmfrBRSTrafficClassBytesXmitUrgent_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 4, 4, 1, 4, 1, 12),
    _IbmfrBRSTrafficClassBytesXmitUrgent_Type()
)
ibmfrBRSTrafficClassBytesXmitUrgent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmfrBRSTrafficClassBytesXmitUrgent.setStatus("mandatory")
_IbmfrBRSTrafficClassTotalBytesOverflow_Type = Counter32
_IbmfrBRSTrafficClassTotalBytesOverflow_Object = MibTableColumn
ibmfrBRSTrafficClassTotalBytesOverflow = _IbmfrBRSTrafficClassTotalBytesOverflow_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 4, 4, 1, 4, 1, 13),
    _IbmfrBRSTrafficClassTotalBytesOverflow_Type()
)
ibmfrBRSTrafficClassTotalBytesOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmfrBRSTrafficClassTotalBytesOverflow.setStatus("mandatory")
_IbmfrBRSTrafficClassBytesOverflowLow_Type = Counter32
_IbmfrBRSTrafficClassBytesOverflowLow_Object = MibTableColumn
ibmfrBRSTrafficClassBytesOverflowLow = _IbmfrBRSTrafficClassBytesOverflowLow_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 4, 4, 1, 4, 1, 14),
    _IbmfrBRSTrafficClassBytesOverflowLow_Type()
)
ibmfrBRSTrafficClassBytesOverflowLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmfrBRSTrafficClassBytesOverflowLow.setStatus("mandatory")
_IbmfrBRSTrafficClassBytesOverflowNormal_Type = Counter32
_IbmfrBRSTrafficClassBytesOverflowNormal_Object = MibTableColumn
ibmfrBRSTrafficClassBytesOverflowNormal = _IbmfrBRSTrafficClassBytesOverflowNormal_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 4, 4, 1, 4, 1, 15),
    _IbmfrBRSTrafficClassBytesOverflowNormal_Type()
)
ibmfrBRSTrafficClassBytesOverflowNormal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmfrBRSTrafficClassBytesOverflowNormal.setStatus("mandatory")
_IbmfrBRSTrafficClassBytesOverflowHigh_Type = Counter32
_IbmfrBRSTrafficClassBytesOverflowHigh_Object = MibTableColumn
ibmfrBRSTrafficClassBytesOverflowHigh = _IbmfrBRSTrafficClassBytesOverflowHigh_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 4, 4, 1, 4, 1, 16),
    _IbmfrBRSTrafficClassBytesOverflowHigh_Type()
)
ibmfrBRSTrafficClassBytesOverflowHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmfrBRSTrafficClassBytesOverflowHigh.setStatus("mandatory")
_IbmfrBRSTrafficClassBytesOverflowUrgent_Type = Counter32
_IbmfrBRSTrafficClassBytesOverflowUrgent_Object = MibTableColumn
ibmfrBRSTrafficClassBytesOverflowUrgent = _IbmfrBRSTrafficClassBytesOverflowUrgent_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 4, 4, 1, 4, 1, 17),
    _IbmfrBRSTrafficClassBytesOverflowUrgent_Type()
)
ibmfrBRSTrafficClassBytesOverflowUrgent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmfrBRSTrafficClassBytesOverflowUrgent.setStatus("mandatory")
_IbmfrBRSTrafficClassTotalPacketOverflow_Type = Counter32
_IbmfrBRSTrafficClassTotalPacketOverflow_Object = MibTableColumn
ibmfrBRSTrafficClassTotalPacketOverflow = _IbmfrBRSTrafficClassTotalPacketOverflow_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 4, 4, 1, 4, 1, 18),
    _IbmfrBRSTrafficClassTotalPacketOverflow_Type()
)
ibmfrBRSTrafficClassTotalPacketOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmfrBRSTrafficClassTotalPacketOverflow.setStatus("mandatory")
_IbmfrBRSTrafficClassPacketOverflowLow_Type = Counter32
_IbmfrBRSTrafficClassPacketOverflowLow_Object = MibTableColumn
ibmfrBRSTrafficClassPacketOverflowLow = _IbmfrBRSTrafficClassPacketOverflowLow_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 4, 4, 1, 4, 1, 19),
    _IbmfrBRSTrafficClassPacketOverflowLow_Type()
)
ibmfrBRSTrafficClassPacketOverflowLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmfrBRSTrafficClassPacketOverflowLow.setStatus("mandatory")
_IbmfrBRSTrafficClassPacketOverflowNormal_Type = Counter32
_IbmfrBRSTrafficClassPacketOverflowNormal_Object = MibTableColumn
ibmfrBRSTrafficClassPacketOverflowNormal = _IbmfrBRSTrafficClassPacketOverflowNormal_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 4, 4, 1, 4, 1, 20),
    _IbmfrBRSTrafficClassPacketOverflowNormal_Type()
)
ibmfrBRSTrafficClassPacketOverflowNormal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmfrBRSTrafficClassPacketOverflowNormal.setStatus("mandatory")
_IbmfrBRSTrafficClassPacketOverflowHigh_Type = Counter32
_IbmfrBRSTrafficClassPacketOverflowHigh_Object = MibTableColumn
ibmfrBRSTrafficClassPacketOverflowHigh = _IbmfrBRSTrafficClassPacketOverflowHigh_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 4, 4, 1, 4, 1, 21),
    _IbmfrBRSTrafficClassPacketOverflowHigh_Type()
)
ibmfrBRSTrafficClassPacketOverflowHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmfrBRSTrafficClassPacketOverflowHigh.setStatus("mandatory")
_IbmfrBRSTrafficClassPacketOverflowUrgent_Type = Counter32
_IbmfrBRSTrafficClassPacketOverflowUrgent_Object = MibTableColumn
ibmfrBRSTrafficClassPacketOverflowUrgent = _IbmfrBRSTrafficClassPacketOverflowUrgent_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 4, 4, 1, 4, 1, 22),
    _IbmfrBRSTrafficClassPacketOverflowUrgent_Type()
)
ibmfrBRSTrafficClassPacketOverflowUrgent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmfrBRSTrafficClassPacketOverflowUrgent.setStatus("mandatory")
_IbmfrBRSTrafficClassTotalLastPacketXmit_Type = Counter32
_IbmfrBRSTrafficClassTotalLastPacketXmit_Object = MibTableColumn
ibmfrBRSTrafficClassTotalLastPacketXmit = _IbmfrBRSTrafficClassTotalLastPacketXmit_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 4, 4, 1, 4, 1, 23),
    _IbmfrBRSTrafficClassTotalLastPacketXmit_Type()
)
ibmfrBRSTrafficClassTotalLastPacketXmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmfrBRSTrafficClassTotalLastPacketXmit.setStatus("mandatory")
_IbmfrBRSTrafficClassLastPacketXmitLow_Type = Counter32
_IbmfrBRSTrafficClassLastPacketXmitLow_Object = MibTableColumn
ibmfrBRSTrafficClassLastPacketXmitLow = _IbmfrBRSTrafficClassLastPacketXmitLow_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 4, 4, 1, 4, 1, 24),
    _IbmfrBRSTrafficClassLastPacketXmitLow_Type()
)
ibmfrBRSTrafficClassLastPacketXmitLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmfrBRSTrafficClassLastPacketXmitLow.setStatus("mandatory")
_IbmfrBRSTrafficClassLastPacketXmitNormal_Type = Counter32
_IbmfrBRSTrafficClassLastPacketXmitNormal_Object = MibTableColumn
ibmfrBRSTrafficClassLastPacketXmitNormal = _IbmfrBRSTrafficClassLastPacketXmitNormal_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 4, 4, 1, 4, 1, 25),
    _IbmfrBRSTrafficClassLastPacketXmitNormal_Type()
)
ibmfrBRSTrafficClassLastPacketXmitNormal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmfrBRSTrafficClassLastPacketXmitNormal.setStatus("mandatory")
_IbmfrBRSTrafficClassLastPacketXmitHigh_Type = Counter32
_IbmfrBRSTrafficClassLastPacketXmitHigh_Object = MibTableColumn
ibmfrBRSTrafficClassLastPacketXmitHigh = _IbmfrBRSTrafficClassLastPacketXmitHigh_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 4, 4, 1, 4, 1, 26),
    _IbmfrBRSTrafficClassLastPacketXmitHigh_Type()
)
ibmfrBRSTrafficClassLastPacketXmitHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmfrBRSTrafficClassLastPacketXmitHigh.setStatus("mandatory")
_IbmfrBRSTrafficClassLastPacketXmitUrgent_Type = Counter32
_IbmfrBRSTrafficClassLastPacketXmitUrgent_Object = MibTableColumn
ibmfrBRSTrafficClassLastPacketXmitUrgent = _IbmfrBRSTrafficClassLastPacketXmitUrgent_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 4, 4, 1, 4, 1, 27),
    _IbmfrBRSTrafficClassLastPacketXmitUrgent_Type()
)
ibmfrBRSTrafficClassLastPacketXmitUrgent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmfrBRSTrafficClassLastPacketXmitUrgent.setStatus("mandatory")
_IbmfrBRSTrafficClassTotalLastBytesXmit_Type = Counter32
_IbmfrBRSTrafficClassTotalLastBytesXmit_Object = MibTableColumn
ibmfrBRSTrafficClassTotalLastBytesXmit = _IbmfrBRSTrafficClassTotalLastBytesXmit_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 4, 4, 1, 4, 1, 28),
    _IbmfrBRSTrafficClassTotalLastBytesXmit_Type()
)
ibmfrBRSTrafficClassTotalLastBytesXmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmfrBRSTrafficClassTotalLastBytesXmit.setStatus("mandatory")
_IbmfrBRSTrafficClassLastBytesXmitLow_Type = Counter32
_IbmfrBRSTrafficClassLastBytesXmitLow_Object = MibTableColumn
ibmfrBRSTrafficClassLastBytesXmitLow = _IbmfrBRSTrafficClassLastBytesXmitLow_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 4, 4, 1, 4, 1, 29),
    _IbmfrBRSTrafficClassLastBytesXmitLow_Type()
)
ibmfrBRSTrafficClassLastBytesXmitLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmfrBRSTrafficClassLastBytesXmitLow.setStatus("mandatory")
_IbmfrBRSTrafficClassLastBytesXmitNormal_Type = Counter32
_IbmfrBRSTrafficClassLastBytesXmitNormal_Object = MibTableColumn
ibmfrBRSTrafficClassLastBytesXmitNormal = _IbmfrBRSTrafficClassLastBytesXmitNormal_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 4, 4, 1, 4, 1, 30),
    _IbmfrBRSTrafficClassLastBytesXmitNormal_Type()
)
ibmfrBRSTrafficClassLastBytesXmitNormal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmfrBRSTrafficClassLastBytesXmitNormal.setStatus("mandatory")
_IbmfrBRSTrafficClassLastBytesXmitHigh_Type = Counter32
_IbmfrBRSTrafficClassLastBytesXmitHigh_Object = MibTableColumn
ibmfrBRSTrafficClassLastBytesXmitHigh = _IbmfrBRSTrafficClassLastBytesXmitHigh_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 4, 4, 1, 4, 1, 31),
    _IbmfrBRSTrafficClassLastBytesXmitHigh_Type()
)
ibmfrBRSTrafficClassLastBytesXmitHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmfrBRSTrafficClassLastBytesXmitHigh.setStatus("mandatory")
_IbmfrBRSTrafficClassLastBytesXmitUrgent_Type = Counter32
_IbmfrBRSTrafficClassLastBytesXmitUrgent_Object = MibTableColumn
ibmfrBRSTrafficClassLastBytesXmitUrgent = _IbmfrBRSTrafficClassLastBytesXmitUrgent_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 4, 4, 1, 4, 1, 32),
    _IbmfrBRSTrafficClassLastBytesXmitUrgent_Type()
)
ibmfrBRSTrafficClassLastBytesXmitUrgent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmfrBRSTrafficClassLastBytesXmitUrgent.setStatus("mandatory")
_IbmfrBRSTrafficClassTotalLastBytesOverflow_Type = Counter32
_IbmfrBRSTrafficClassTotalLastBytesOverflow_Object = MibTableColumn
ibmfrBRSTrafficClassTotalLastBytesOverflow = _IbmfrBRSTrafficClassTotalLastBytesOverflow_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 4, 4, 1, 4, 1, 33),
    _IbmfrBRSTrafficClassTotalLastBytesOverflow_Type()
)
ibmfrBRSTrafficClassTotalLastBytesOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmfrBRSTrafficClassTotalLastBytesOverflow.setStatus("mandatory")
_IbmfrBRSTrafficClassLastBytesOverflowLow_Type = Counter32
_IbmfrBRSTrafficClassLastBytesOverflowLow_Object = MibTableColumn
ibmfrBRSTrafficClassLastBytesOverflowLow = _IbmfrBRSTrafficClassLastBytesOverflowLow_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 4, 4, 1, 4, 1, 34),
    _IbmfrBRSTrafficClassLastBytesOverflowLow_Type()
)
ibmfrBRSTrafficClassLastBytesOverflowLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmfrBRSTrafficClassLastBytesOverflowLow.setStatus("mandatory")
_IbmfrBRSTrafficClassLastBytesOverflowNmal_Type = Counter32
_IbmfrBRSTrafficClassLastBytesOverflowNmal_Object = MibTableColumn
ibmfrBRSTrafficClassLastBytesOverflowNmal = _IbmfrBRSTrafficClassLastBytesOverflowNmal_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 4, 4, 1, 4, 1, 35),
    _IbmfrBRSTrafficClassLastBytesOverflowNmal_Type()
)
ibmfrBRSTrafficClassLastBytesOverflowNmal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmfrBRSTrafficClassLastBytesOverflowNmal.setStatus("mandatory")
_IbmfrBRSTrafficClassLastBytesOverflowHigh_Type = Counter32
_IbmfrBRSTrafficClassLastBytesOverflowHigh_Object = MibTableColumn
ibmfrBRSTrafficClassLastBytesOverflowHigh = _IbmfrBRSTrafficClassLastBytesOverflowHigh_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 4, 4, 1, 4, 1, 36),
    _IbmfrBRSTrafficClassLastBytesOverflowHigh_Type()
)
ibmfrBRSTrafficClassLastBytesOverflowHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmfrBRSTrafficClassLastBytesOverflowHigh.setStatus("mandatory")
_IbmfrBRSTrafficClassLastBytesOverflowUgent_Type = Counter32
_IbmfrBRSTrafficClassLastBytesOverflowUgent_Object = MibTableColumn
ibmfrBRSTrafficClassLastBytesOverflowUgent = _IbmfrBRSTrafficClassLastBytesOverflowUgent_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 4, 4, 1, 4, 1, 37),
    _IbmfrBRSTrafficClassLastBytesOverflowUgent_Type()
)
ibmfrBRSTrafficClassLastBytesOverflowUgent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmfrBRSTrafficClassLastBytesOverflowUgent.setStatus("mandatory")
_IbmfrBRSTrafficClassTotalLastPacketOverflow_Type = Counter32
_IbmfrBRSTrafficClassTotalLastPacketOverflow_Object = MibTableColumn
ibmfrBRSTrafficClassTotalLastPacketOverflow = _IbmfrBRSTrafficClassTotalLastPacketOverflow_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 4, 4, 1, 4, 1, 38),
    _IbmfrBRSTrafficClassTotalLastPacketOverflow_Type()
)
ibmfrBRSTrafficClassTotalLastPacketOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmfrBRSTrafficClassTotalLastPacketOverflow.setStatus("mandatory")
_IbmfrBRSTrafficClassLastPacketOverflowLow_Type = Counter32
_IbmfrBRSTrafficClassLastPacketOverflowLow_Object = MibTableColumn
ibmfrBRSTrafficClassLastPacketOverflowLow = _IbmfrBRSTrafficClassLastPacketOverflowLow_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 4, 4, 1, 4, 1, 39),
    _IbmfrBRSTrafficClassLastPacketOverflowLow_Type()
)
ibmfrBRSTrafficClassLastPacketOverflowLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmfrBRSTrafficClassLastPacketOverflowLow.setStatus("mandatory")
_IbmfrBRSTrafficClassLastPacketOverflowNmal_Type = Counter32
_IbmfrBRSTrafficClassLastPacketOverflowNmal_Object = MibTableColumn
ibmfrBRSTrafficClassLastPacketOverflowNmal = _IbmfrBRSTrafficClassLastPacketOverflowNmal_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 4, 4, 1, 4, 1, 40),
    _IbmfrBRSTrafficClassLastPacketOverflowNmal_Type()
)
ibmfrBRSTrafficClassLastPacketOverflowNmal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmfrBRSTrafficClassLastPacketOverflowNmal.setStatus("mandatory")
_IbmfrBRSTrafficClassLastPacketOverflowHigh_Type = Counter32
_IbmfrBRSTrafficClassLastPacketOverflowHigh_Object = MibTableColumn
ibmfrBRSTrafficClassLastPacketOverflowHigh = _IbmfrBRSTrafficClassLastPacketOverflowHigh_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 4, 4, 1, 4, 1, 41),
    _IbmfrBRSTrafficClassLastPacketOverflowHigh_Type()
)
ibmfrBRSTrafficClassLastPacketOverflowHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmfrBRSTrafficClassLastPacketOverflowHigh.setStatus("mandatory")
_IbmfrBRSTrafficClassLastPacketOverflowUgent_Type = Counter32
_IbmfrBRSTrafficClassLastPacketOverflowUgent_Object = MibTableColumn
ibmfrBRSTrafficClassLastPacketOverflowUgent = _IbmfrBRSTrafficClassLastPacketOverflowUgent_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 4, 4, 1, 4, 1, 42),
    _IbmfrBRSTrafficClassLastPacketOverflowUgent_Type()
)
ibmfrBRSTrafficClassLastPacketOverflowUgent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmfrBRSTrafficClassLastPacketOverflowUgent.setStatus("mandatory")


class _IbmfrBRSTrafficClassClearCounters_Type(Integer32):
    """Custom type ibmfrBRSTrafficClassClearCounters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
    )


_IbmfrBRSTrafficClassClearCounters_Type.__name__ = "Integer32"
_IbmfrBRSTrafficClassClearCounters_Object = MibTableColumn
ibmfrBRSTrafficClassClearCounters = _IbmfrBRSTrafficClassClearCounters_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 4, 4, 1, 4, 1, 43),
    _IbmfrBRSTrafficClassClearCounters_Type()
)
ibmfrBRSTrafficClassClearCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmfrBRSTrafficClassClearCounters.setStatus("mandatory")
_IbmfrBRSTrafficClassSVCName_Type = DisplayString
_IbmfrBRSTrafficClassSVCName_Object = MibTableColumn
ibmfrBRSTrafficClassSVCName = _IbmfrBRSTrafficClassSVCName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 4, 4, 1, 4, 1, 44),
    _IbmfrBRSTrafficClassSVCName_Type()
)
ibmfrBRSTrafficClassSVCName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmfrBRSTrafficClassSVCName.setStatus("mandatory")
_IbmfrBRSProtFiltTable_Object = MibTable
ibmfrBRSProtFiltTable = _IbmfrBRSProtFiltTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 4, 4, 1, 5)
)
if mibBuilder.loadTexts:
    ibmfrBRSProtFiltTable.setStatus("mandatory")
_IbmfrBRSProtFiltEntry_Object = MibTableRow
ibmfrBRSProtFiltEntry = _IbmfrBRSProtFiltEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 4, 4, 1, 5, 1)
)
ibmfrBRSProtFiltEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "IBMFRBRS-MIB", "ibmfrBRSCircuitClassName"),
    (0, "IBMFRBRS-MIB", "ibmfrBRSCircuitNumber"),
    (0, "IBMFRBRS-MIB", "ibmfrBRSTrafficClassName"),
    (0, "IBMFRBRS-MIB", "ibmfrBRSProtFiltId"),
)
if mibBuilder.loadTexts:
    ibmfrBRSProtFiltEntry.setStatus("mandatory")
_IbmfrBRSProtFiltId_Type = DisplayString
_IbmfrBRSProtFiltId_Object = MibTableColumn
ibmfrBRSProtFiltId = _IbmfrBRSProtFiltId_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 4, 4, 1, 5, 1, 1),
    _IbmfrBRSProtFiltId_Type()
)
ibmfrBRSProtFiltId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ibmfrBRSProtFiltId.setStatus("mandatory")


class _IbmfrBRSProtFiltPrio_Type(Integer32):
    """Custom type ibmfrBRSProtFiltPrio based on Integer32"""
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
        *(("high", 3),
          ("low", 1),
          ("normal", 2),
          ("urgent", 4))
    )


_IbmfrBRSProtFiltPrio_Type.__name__ = "Integer32"
_IbmfrBRSProtFiltPrio_Object = MibTableColumn
ibmfrBRSProtFiltPrio = _IbmfrBRSProtFiltPrio_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 4, 4, 1, 5, 1, 2),
    _IbmfrBRSProtFiltPrio_Type()
)
ibmfrBRSProtFiltPrio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmfrBRSProtFiltPrio.setStatus("mandatory")


class _IbmfrBRSProtFiltDE_Type(Integer32):
    """Custom type ibmfrBRSProtFiltDE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_IbmfrBRSProtFiltDE_Type.__name__ = "Integer32"
_IbmfrBRSProtFiltDE_Object = MibTableColumn
ibmfrBRSProtFiltDE = _IbmfrBRSProtFiltDE_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 4, 4, 1, 5, 1, 3),
    _IbmfrBRSProtFiltDE_Type()
)
ibmfrBRSProtFiltDE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmfrBRSProtFiltDE.setStatus("mandatory")
_IbmfrBRSProtFiltSVCName_Type = DisplayString
_IbmfrBRSProtFiltSVCName_Object = MibTableColumn
ibmfrBRSProtFiltSVCName = _IbmfrBRSProtFiltSVCName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 4, 4, 1, 5, 1, 4),
    _IbmfrBRSProtFiltSVCName_Type()
)
ibmfrBRSProtFiltSVCName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmfrBRSProtFiltSVCName.setStatus("mandatory")
_IbmfrBRSAdministravive_ObjectIdentity = ObjectIdentity
ibmfrBRSAdministravive = _IbmfrBRSAdministravive_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 4, 4, 4, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IBMFRBRS-MIB",
    **{"ibmfrBRS": ibmfrBRS,
       "ibmfrBRSOperational": ibmfrBRSOperational,
       "ibmfrBRSInterfaceTable": ibmfrBRSInterfaceTable,
       "ibmfrBRSInterfaceEntry": ibmfrBRSInterfaceEntry,
       "ibmfrBRSInterfaceMaxQueue": ibmfrBRSInterfaceMaxQueue,
       "ibmfrBRSInterfaceMinQueue": ibmfrBRSInterfaceMinQueue,
       "ibmfrBRSInterfaceTotalBandwidth": ibmfrBRSInterfaceTotalBandwidth,
       "ibmfrBRSInterfaceTotalCircuitClasses": ibmfrBRSInterfaceTotalCircuitClasses,
       "ibmfrBRSInterfaceDefaultCircuitClassName": ibmfrBRSInterfaceDefaultCircuitClassName,
       "ibmfrBRSCircuitClassTable": ibmfrBRSCircuitClassTable,
       "ibmfrBRSCircuitClassEntry": ibmfrBRSCircuitClassEntry,
       "ibmfrBRSCircuitClassName": ibmfrBRSCircuitClassName,
       "ibmfrBRSCircuitClassBandwidth": ibmfrBRSCircuitClassBandwidth,
       "ibmfrBRSCircuitClassPacketXmit": ibmfrBRSCircuitClassPacketXmit,
       "ibmfrBRSCircuitClassBytesXmit": ibmfrBRSCircuitClassBytesXmit,
       "ibmfrBRSCircuitClassBytesOverflow": ibmfrBRSCircuitClassBytesOverflow,
       "ibmfrBRSCircuitClassLastPacketXmit": ibmfrBRSCircuitClassLastPacketXmit,
       "ibmfrBRSCircuitClassLastBytesXmit": ibmfrBRSCircuitClassLastBytesXmit,
       "ibmfrBRSCircuitClassLastBytesOverflow": ibmfrBRSCircuitClassLastBytesOverflow,
       "ibmfrBRSCircuitClassClearCounters": ibmfrBRSCircuitClassClearCounters,
       "ibmfrBRSCircuitTable": ibmfrBRSCircuitTable,
       "ibmfrBRSCircuitEntry": ibmfrBRSCircuitEntry,
       "ibmfrBRSCircuitNumber": ibmfrBRSCircuitNumber,
       "ibmfrBRSCircuitMaxQueue": ibmfrBRSCircuitMaxQueue,
       "ibmfrBRSCircuitMinQueue": ibmfrBRSCircuitMinQueue,
       "ibmfrBRSCircuitTotalBandwidth": ibmfrBRSCircuitTotalBandwidth,
       "ibmfrBRSCircuitTotalTrafficClasses": ibmfrBRSCircuitTotalTrafficClasses,
       "ibmfrBRSCircuitDefaultTrafficClassName": ibmfrBRSCircuitDefaultTrafficClassName,
       "ibmfrBRSCircuitDefaultTrafficClassPrio": ibmfrBRSCircuitDefaultTrafficClassPrio,
       "ibmfrBRSCircuitSpecification": ibmfrBRSCircuitSpecification,
       "ibmfrBRSCircuitSuperClassName": ibmfrBRSCircuitSuperClassName,
       "ibmfrBRSCircuitSVCName": ibmfrBRSCircuitSVCName,
       "ibmfrBRSTrafficClassTable": ibmfrBRSTrafficClassTable,
       "ibmfrBRSTrafficClassEntry": ibmfrBRSTrafficClassEntry,
       "ibmfrBRSTrafficClassName": ibmfrBRSTrafficClassName,
       "ibmfrBRSTrafficClassBandwidth": ibmfrBRSTrafficClassBandwidth,
       "ibmfrBRSTrafficClassTotalPacketXmit": ibmfrBRSTrafficClassTotalPacketXmit,
       "ibmfrBRSTrafficClassPacketXmitLow": ibmfrBRSTrafficClassPacketXmitLow,
       "ibmfrBRSTrafficClassPacketXmitNormal": ibmfrBRSTrafficClassPacketXmitNormal,
       "ibmfrBRSTrafficClassPacketXmitHigh": ibmfrBRSTrafficClassPacketXmitHigh,
       "ibmfrBRSTrafficClassPacketXmitUrgent": ibmfrBRSTrafficClassPacketXmitUrgent,
       "ibmfrBRSTrafficClassTotalBytesXmit": ibmfrBRSTrafficClassTotalBytesXmit,
       "ibmfrBRSTrafficClassBytesXmitLow": ibmfrBRSTrafficClassBytesXmitLow,
       "ibmfrBRSTrafficClassBytesXmitNormal": ibmfrBRSTrafficClassBytesXmitNormal,
       "ibmfrBRSTrafficClassBytesXmitHigh": ibmfrBRSTrafficClassBytesXmitHigh,
       "ibmfrBRSTrafficClassBytesXmitUrgent": ibmfrBRSTrafficClassBytesXmitUrgent,
       "ibmfrBRSTrafficClassTotalBytesOverflow": ibmfrBRSTrafficClassTotalBytesOverflow,
       "ibmfrBRSTrafficClassBytesOverflowLow": ibmfrBRSTrafficClassBytesOverflowLow,
       "ibmfrBRSTrafficClassBytesOverflowNormal": ibmfrBRSTrafficClassBytesOverflowNormal,
       "ibmfrBRSTrafficClassBytesOverflowHigh": ibmfrBRSTrafficClassBytesOverflowHigh,
       "ibmfrBRSTrafficClassBytesOverflowUrgent": ibmfrBRSTrafficClassBytesOverflowUrgent,
       "ibmfrBRSTrafficClassTotalPacketOverflow": ibmfrBRSTrafficClassTotalPacketOverflow,
       "ibmfrBRSTrafficClassPacketOverflowLow": ibmfrBRSTrafficClassPacketOverflowLow,
       "ibmfrBRSTrafficClassPacketOverflowNormal": ibmfrBRSTrafficClassPacketOverflowNormal,
       "ibmfrBRSTrafficClassPacketOverflowHigh": ibmfrBRSTrafficClassPacketOverflowHigh,
       "ibmfrBRSTrafficClassPacketOverflowUrgent": ibmfrBRSTrafficClassPacketOverflowUrgent,
       "ibmfrBRSTrafficClassTotalLastPacketXmit": ibmfrBRSTrafficClassTotalLastPacketXmit,
       "ibmfrBRSTrafficClassLastPacketXmitLow": ibmfrBRSTrafficClassLastPacketXmitLow,
       "ibmfrBRSTrafficClassLastPacketXmitNormal": ibmfrBRSTrafficClassLastPacketXmitNormal,
       "ibmfrBRSTrafficClassLastPacketXmitHigh": ibmfrBRSTrafficClassLastPacketXmitHigh,
       "ibmfrBRSTrafficClassLastPacketXmitUrgent": ibmfrBRSTrafficClassLastPacketXmitUrgent,
       "ibmfrBRSTrafficClassTotalLastBytesXmit": ibmfrBRSTrafficClassTotalLastBytesXmit,
       "ibmfrBRSTrafficClassLastBytesXmitLow": ibmfrBRSTrafficClassLastBytesXmitLow,
       "ibmfrBRSTrafficClassLastBytesXmitNormal": ibmfrBRSTrafficClassLastBytesXmitNormal,
       "ibmfrBRSTrafficClassLastBytesXmitHigh": ibmfrBRSTrafficClassLastBytesXmitHigh,
       "ibmfrBRSTrafficClassLastBytesXmitUrgent": ibmfrBRSTrafficClassLastBytesXmitUrgent,
       "ibmfrBRSTrafficClassTotalLastBytesOverflow": ibmfrBRSTrafficClassTotalLastBytesOverflow,
       "ibmfrBRSTrafficClassLastBytesOverflowLow": ibmfrBRSTrafficClassLastBytesOverflowLow,
       "ibmfrBRSTrafficClassLastBytesOverflowNmal": ibmfrBRSTrafficClassLastBytesOverflowNmal,
       "ibmfrBRSTrafficClassLastBytesOverflowHigh": ibmfrBRSTrafficClassLastBytesOverflowHigh,
       "ibmfrBRSTrafficClassLastBytesOverflowUgent": ibmfrBRSTrafficClassLastBytesOverflowUgent,
       "ibmfrBRSTrafficClassTotalLastPacketOverflow": ibmfrBRSTrafficClassTotalLastPacketOverflow,
       "ibmfrBRSTrafficClassLastPacketOverflowLow": ibmfrBRSTrafficClassLastPacketOverflowLow,
       "ibmfrBRSTrafficClassLastPacketOverflowNmal": ibmfrBRSTrafficClassLastPacketOverflowNmal,
       "ibmfrBRSTrafficClassLastPacketOverflowHigh": ibmfrBRSTrafficClassLastPacketOverflowHigh,
       "ibmfrBRSTrafficClassLastPacketOverflowUgent": ibmfrBRSTrafficClassLastPacketOverflowUgent,
       "ibmfrBRSTrafficClassClearCounters": ibmfrBRSTrafficClassClearCounters,
       "ibmfrBRSTrafficClassSVCName": ibmfrBRSTrafficClassSVCName,
       "ibmfrBRSProtFiltTable": ibmfrBRSProtFiltTable,
       "ibmfrBRSProtFiltEntry": ibmfrBRSProtFiltEntry,
       "ibmfrBRSProtFiltId": ibmfrBRSProtFiltId,
       "ibmfrBRSProtFiltPrio": ibmfrBRSProtFiltPrio,
       "ibmfrBRSProtFiltDE": ibmfrBRSProtFiltDE,
       "ibmfrBRSProtFiltSVCName": ibmfrBRSProtFiltSVCName,
       "ibmfrBRSAdministravive": ibmfrBRSAdministravive}
)
