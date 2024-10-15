# SNMP MIB module (ATM2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ATM2-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:44:08 2024
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

(atmInterfaceConfEntry,
 atmMIBObjects,
 atmVcCrossConnectEntry,
 atmVclEntry,
 atmVclVci,
 atmVclVpi,
 atmVpCrossConnectEntry,
 atmVplEntry,
 atmVplVpi) = mibBuilder.importSymbols(
    "ATM-MIB",
    "atmInterfaceConfEntry",
    "atmMIBObjects",
    "atmVcCrossConnectEntry",
    "atmVclEntry",
    "atmVclVci",
    "atmVclVpi",
    "atmVpCrossConnectEntry",
    "atmVplEntry",
    "atmVplVpi")

(AtmAddr,
 AtmIlmiNetworkPrefix,
 AtmInterfaceType,
 AtmSigDescrParamIndex,
 AtmTrafficDescrParamIndex,
 AtmVcIdentifier,
 AtmVpIdentifier) = mibBuilder.importSymbols(
    "ATM-TC-MIB",
    "AtmAddr",
    "AtmIlmiNetworkPrefix",
    "AtmInterfaceType",
    "AtmSigDescrParamIndex",
    "AtmTrafficDescrParamIndex",
    "AtmVcIdentifier",
    "AtmVpIdentifier")

(InterfaceIndex,
 InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero",
    "ifIndex")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

atm2MIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 37, 1, 14)
)
atm2MIB.setRevisions(
        ("2003-09-23 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Atm2MIBObjects_ObjectIdentity = ObjectIdentity
atm2MIBObjects = _Atm2MIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1)
)
_AtmSvcVpCrossConnectTable_Object = MibTable
atmSvcVpCrossConnectTable = _AtmSvcVpCrossConnectTable_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 1)
)
if mibBuilder.loadTexts:
    atmSvcVpCrossConnectTable.setStatus("current")
_AtmSvcVpCrossConnectEntry_Object = MibTableRow
atmSvcVpCrossConnectEntry = _AtmSvcVpCrossConnectEntry_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 1, 1)
)
atmSvcVpCrossConnectEntry.setIndexNames(
    (0, "ATM2-MIB", "atmSvcVpCrossConnectIndex"),
    (0, "ATM2-MIB", "atmSvcVpCrossConnectLowIfIndex"),
    (0, "ATM2-MIB", "atmSvcVpCrossConnectLowVpi"),
    (0, "ATM2-MIB", "atmSvcVpCrossConnectHighIfIndex"),
    (0, "ATM2-MIB", "atmSvcVpCrossConnectHighVpi"),
)
if mibBuilder.loadTexts:
    atmSvcVpCrossConnectEntry.setStatus("current")


class _AtmSvcVpCrossConnectIndex_Type(Integer32):
    """Custom type atmSvcVpCrossConnectIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AtmSvcVpCrossConnectIndex_Type.__name__ = "Integer32"
_AtmSvcVpCrossConnectIndex_Object = MibTableColumn
atmSvcVpCrossConnectIndex = _AtmSvcVpCrossConnectIndex_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 1, 1, 1),
    _AtmSvcVpCrossConnectIndex_Type()
)
atmSvcVpCrossConnectIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmSvcVpCrossConnectIndex.setStatus("current")
_AtmSvcVpCrossConnectLowIfIndex_Type = InterfaceIndex
_AtmSvcVpCrossConnectLowIfIndex_Object = MibTableColumn
atmSvcVpCrossConnectLowIfIndex = _AtmSvcVpCrossConnectLowIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 1, 1, 2),
    _AtmSvcVpCrossConnectLowIfIndex_Type()
)
atmSvcVpCrossConnectLowIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmSvcVpCrossConnectLowIfIndex.setStatus("current")
_AtmSvcVpCrossConnectLowVpi_Type = AtmVpIdentifier
_AtmSvcVpCrossConnectLowVpi_Object = MibTableColumn
atmSvcVpCrossConnectLowVpi = _AtmSvcVpCrossConnectLowVpi_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 1, 1, 3),
    _AtmSvcVpCrossConnectLowVpi_Type()
)
atmSvcVpCrossConnectLowVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmSvcVpCrossConnectLowVpi.setStatus("current")
_AtmSvcVpCrossConnectHighIfIndex_Type = InterfaceIndex
_AtmSvcVpCrossConnectHighIfIndex_Object = MibTableColumn
atmSvcVpCrossConnectHighIfIndex = _AtmSvcVpCrossConnectHighIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 1, 1, 4),
    _AtmSvcVpCrossConnectHighIfIndex_Type()
)
atmSvcVpCrossConnectHighIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmSvcVpCrossConnectHighIfIndex.setStatus("current")
_AtmSvcVpCrossConnectHighVpi_Type = AtmVpIdentifier
_AtmSvcVpCrossConnectHighVpi_Object = MibTableColumn
atmSvcVpCrossConnectHighVpi = _AtmSvcVpCrossConnectHighVpi_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 1, 1, 5),
    _AtmSvcVpCrossConnectHighVpi_Type()
)
atmSvcVpCrossConnectHighVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmSvcVpCrossConnectHighVpi.setStatus("current")
_AtmSvcVpCrossConnectCreationTime_Type = TimeStamp
_AtmSvcVpCrossConnectCreationTime_Object = MibTableColumn
atmSvcVpCrossConnectCreationTime = _AtmSvcVpCrossConnectCreationTime_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 1, 1, 6),
    _AtmSvcVpCrossConnectCreationTime_Type()
)
atmSvcVpCrossConnectCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSvcVpCrossConnectCreationTime.setStatus("current")
_AtmSvcVpCrossConnectRowStatus_Type = RowStatus
_AtmSvcVpCrossConnectRowStatus_Object = MibTableColumn
atmSvcVpCrossConnectRowStatus = _AtmSvcVpCrossConnectRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 1, 1, 7),
    _AtmSvcVpCrossConnectRowStatus_Type()
)
atmSvcVpCrossConnectRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSvcVpCrossConnectRowStatus.setStatus("current")
_AtmSvcVcCrossConnectTable_Object = MibTable
atmSvcVcCrossConnectTable = _AtmSvcVcCrossConnectTable_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 2)
)
if mibBuilder.loadTexts:
    atmSvcVcCrossConnectTable.setStatus("current")
_AtmSvcVcCrossConnectEntry_Object = MibTableRow
atmSvcVcCrossConnectEntry = _AtmSvcVcCrossConnectEntry_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 2, 1)
)
atmSvcVcCrossConnectEntry.setIndexNames(
    (0, "ATM2-MIB", "atmSvcVcCrossConnectIndex"),
    (0, "ATM2-MIB", "atmSvcVcCrossConnectLowIfIndex"),
    (0, "ATM2-MIB", "atmSvcVcCrossConnectLowVpi"),
    (0, "ATM2-MIB", "atmSvcVcCrossConnectLowVci"),
    (0, "ATM2-MIB", "atmSvcVcCrossConnectHighIfIndex"),
    (0, "ATM2-MIB", "atmSvcVcCrossConnectHighVpi"),
    (0, "ATM2-MIB", "atmSvcVcCrossConnectHighVci"),
)
if mibBuilder.loadTexts:
    atmSvcVcCrossConnectEntry.setStatus("current")


class _AtmSvcVcCrossConnectIndex_Type(Integer32):
    """Custom type atmSvcVcCrossConnectIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AtmSvcVcCrossConnectIndex_Type.__name__ = "Integer32"
_AtmSvcVcCrossConnectIndex_Object = MibTableColumn
atmSvcVcCrossConnectIndex = _AtmSvcVcCrossConnectIndex_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 2, 1, 1),
    _AtmSvcVcCrossConnectIndex_Type()
)
atmSvcVcCrossConnectIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmSvcVcCrossConnectIndex.setStatus("current")
_AtmSvcVcCrossConnectLowIfIndex_Type = InterfaceIndex
_AtmSvcVcCrossConnectLowIfIndex_Object = MibTableColumn
atmSvcVcCrossConnectLowIfIndex = _AtmSvcVcCrossConnectLowIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 2, 1, 2),
    _AtmSvcVcCrossConnectLowIfIndex_Type()
)
atmSvcVcCrossConnectLowIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmSvcVcCrossConnectLowIfIndex.setStatus("current")
_AtmSvcVcCrossConnectLowVpi_Type = AtmVpIdentifier
_AtmSvcVcCrossConnectLowVpi_Object = MibTableColumn
atmSvcVcCrossConnectLowVpi = _AtmSvcVcCrossConnectLowVpi_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 2, 1, 3),
    _AtmSvcVcCrossConnectLowVpi_Type()
)
atmSvcVcCrossConnectLowVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmSvcVcCrossConnectLowVpi.setStatus("current")
_AtmSvcVcCrossConnectLowVci_Type = AtmVcIdentifier
_AtmSvcVcCrossConnectLowVci_Object = MibTableColumn
atmSvcVcCrossConnectLowVci = _AtmSvcVcCrossConnectLowVci_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 2, 1, 4),
    _AtmSvcVcCrossConnectLowVci_Type()
)
atmSvcVcCrossConnectLowVci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmSvcVcCrossConnectLowVci.setStatus("current")
_AtmSvcVcCrossConnectHighIfIndex_Type = InterfaceIndex
_AtmSvcVcCrossConnectHighIfIndex_Object = MibTableColumn
atmSvcVcCrossConnectHighIfIndex = _AtmSvcVcCrossConnectHighIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 2, 1, 5),
    _AtmSvcVcCrossConnectHighIfIndex_Type()
)
atmSvcVcCrossConnectHighIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmSvcVcCrossConnectHighIfIndex.setStatus("current")
_AtmSvcVcCrossConnectHighVpi_Type = AtmVpIdentifier
_AtmSvcVcCrossConnectHighVpi_Object = MibTableColumn
atmSvcVcCrossConnectHighVpi = _AtmSvcVcCrossConnectHighVpi_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 2, 1, 6),
    _AtmSvcVcCrossConnectHighVpi_Type()
)
atmSvcVcCrossConnectHighVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmSvcVcCrossConnectHighVpi.setStatus("current")
_AtmSvcVcCrossConnectHighVci_Type = AtmVcIdentifier
_AtmSvcVcCrossConnectHighVci_Object = MibTableColumn
atmSvcVcCrossConnectHighVci = _AtmSvcVcCrossConnectHighVci_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 2, 1, 7),
    _AtmSvcVcCrossConnectHighVci_Type()
)
atmSvcVcCrossConnectHighVci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmSvcVcCrossConnectHighVci.setStatus("current")
_AtmSvcVcCrossConnectCreationTime_Type = TimeStamp
_AtmSvcVcCrossConnectCreationTime_Object = MibTableColumn
atmSvcVcCrossConnectCreationTime = _AtmSvcVcCrossConnectCreationTime_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 2, 1, 8),
    _AtmSvcVcCrossConnectCreationTime_Type()
)
atmSvcVcCrossConnectCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSvcVcCrossConnectCreationTime.setStatus("current")
_AtmSvcVcCrossConnectRowStatus_Type = RowStatus
_AtmSvcVcCrossConnectRowStatus_Object = MibTableColumn
atmSvcVcCrossConnectRowStatus = _AtmSvcVcCrossConnectRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 2, 1, 9),
    _AtmSvcVcCrossConnectRowStatus_Type()
)
atmSvcVcCrossConnectRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSvcVcCrossConnectRowStatus.setStatus("current")
_AtmSigStatTable_Object = MibTable
atmSigStatTable = _AtmSigStatTable_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 3)
)
if mibBuilder.loadTexts:
    atmSigStatTable.setStatus("current")
_AtmSigStatEntry_Object = MibTableRow
atmSigStatEntry = _AtmSigStatEntry_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 3, 1)
)
atmSigStatEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    atmSigStatEntry.setStatus("current")
_AtmSigSSCOPConEvents_Type = Counter32
_AtmSigSSCOPConEvents_Object = MibTableColumn
atmSigSSCOPConEvents = _AtmSigSSCOPConEvents_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 3, 1, 1),
    _AtmSigSSCOPConEvents_Type()
)
atmSigSSCOPConEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSigSSCOPConEvents.setStatus("current")
_AtmSigSSCOPErrdPdus_Type = Counter32
_AtmSigSSCOPErrdPdus_Object = MibTableColumn
atmSigSSCOPErrdPdus = _AtmSigSSCOPErrdPdus_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 3, 1, 2),
    _AtmSigSSCOPErrdPdus_Type()
)
atmSigSSCOPErrdPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSigSSCOPErrdPdus.setStatus("current")
_AtmSigDetectSetupAttempts_Type = Counter32
_AtmSigDetectSetupAttempts_Object = MibTableColumn
atmSigDetectSetupAttempts = _AtmSigDetectSetupAttempts_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 3, 1, 3),
    _AtmSigDetectSetupAttempts_Type()
)
atmSigDetectSetupAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSigDetectSetupAttempts.setStatus("current")
_AtmSigEmitSetupAttempts_Type = Counter32
_AtmSigEmitSetupAttempts_Object = MibTableColumn
atmSigEmitSetupAttempts = _AtmSigEmitSetupAttempts_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 3, 1, 4),
    _AtmSigEmitSetupAttempts_Type()
)
atmSigEmitSetupAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSigEmitSetupAttempts.setStatus("current")
_AtmSigDetectUnavailRoutes_Type = Counter32
_AtmSigDetectUnavailRoutes_Object = MibTableColumn
atmSigDetectUnavailRoutes = _AtmSigDetectUnavailRoutes_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 3, 1, 5),
    _AtmSigDetectUnavailRoutes_Type()
)
atmSigDetectUnavailRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSigDetectUnavailRoutes.setStatus("current")
_AtmSigEmitUnavailRoutes_Type = Counter32
_AtmSigEmitUnavailRoutes_Object = MibTableColumn
atmSigEmitUnavailRoutes = _AtmSigEmitUnavailRoutes_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 3, 1, 6),
    _AtmSigEmitUnavailRoutes_Type()
)
atmSigEmitUnavailRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSigEmitUnavailRoutes.setStatus("current")
_AtmSigDetectUnavailResrcs_Type = Counter32
_AtmSigDetectUnavailResrcs_Object = MibTableColumn
atmSigDetectUnavailResrcs = _AtmSigDetectUnavailResrcs_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 3, 1, 7),
    _AtmSigDetectUnavailResrcs_Type()
)
atmSigDetectUnavailResrcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSigDetectUnavailResrcs.setStatus("current")
_AtmSigEmitUnavailResrcs_Type = Counter32
_AtmSigEmitUnavailResrcs_Object = MibTableColumn
atmSigEmitUnavailResrcs = _AtmSigEmitUnavailResrcs_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 3, 1, 8),
    _AtmSigEmitUnavailResrcs_Type()
)
atmSigEmitUnavailResrcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSigEmitUnavailResrcs.setStatus("current")
_AtmSigDetectCldPtyEvents_Type = Counter32
_AtmSigDetectCldPtyEvents_Object = MibTableColumn
atmSigDetectCldPtyEvents = _AtmSigDetectCldPtyEvents_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 3, 1, 9),
    _AtmSigDetectCldPtyEvents_Type()
)
atmSigDetectCldPtyEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSigDetectCldPtyEvents.setStatus("current")
_AtmSigEmitCldPtyEvents_Type = Counter32
_AtmSigEmitCldPtyEvents_Object = MibTableColumn
atmSigEmitCldPtyEvents = _AtmSigEmitCldPtyEvents_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 3, 1, 10),
    _AtmSigEmitCldPtyEvents_Type()
)
atmSigEmitCldPtyEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSigEmitCldPtyEvents.setStatus("current")
_AtmSigDetectMsgErrors_Type = Counter32
_AtmSigDetectMsgErrors_Object = MibTableColumn
atmSigDetectMsgErrors = _AtmSigDetectMsgErrors_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 3, 1, 11),
    _AtmSigDetectMsgErrors_Type()
)
atmSigDetectMsgErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSigDetectMsgErrors.setStatus("current")
_AtmSigEmitMsgErrors_Type = Counter32
_AtmSigEmitMsgErrors_Object = MibTableColumn
atmSigEmitMsgErrors = _AtmSigEmitMsgErrors_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 3, 1, 12),
    _AtmSigEmitMsgErrors_Type()
)
atmSigEmitMsgErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSigEmitMsgErrors.setStatus("current")
_AtmSigDetectClgPtyEvents_Type = Counter32
_AtmSigDetectClgPtyEvents_Object = MibTableColumn
atmSigDetectClgPtyEvents = _AtmSigDetectClgPtyEvents_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 3, 1, 13),
    _AtmSigDetectClgPtyEvents_Type()
)
atmSigDetectClgPtyEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSigDetectClgPtyEvents.setStatus("current")
_AtmSigEmitClgPtyEvents_Type = Counter32
_AtmSigEmitClgPtyEvents_Object = MibTableColumn
atmSigEmitClgPtyEvents = _AtmSigEmitClgPtyEvents_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 3, 1, 14),
    _AtmSigEmitClgPtyEvents_Type()
)
atmSigEmitClgPtyEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSigEmitClgPtyEvents.setStatus("current")
_AtmSigDetectTimerExpireds_Type = Counter32
_AtmSigDetectTimerExpireds_Object = MibTableColumn
atmSigDetectTimerExpireds = _AtmSigDetectTimerExpireds_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 3, 1, 15),
    _AtmSigDetectTimerExpireds_Type()
)
atmSigDetectTimerExpireds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSigDetectTimerExpireds.setStatus("current")
_AtmSigEmitTimerExpireds_Type = Counter32
_AtmSigEmitTimerExpireds_Object = MibTableColumn
atmSigEmitTimerExpireds = _AtmSigEmitTimerExpireds_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 3, 1, 16),
    _AtmSigEmitTimerExpireds_Type()
)
atmSigEmitTimerExpireds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSigEmitTimerExpireds.setStatus("current")
_AtmSigDetectRestarts_Type = Counter32
_AtmSigDetectRestarts_Object = MibTableColumn
atmSigDetectRestarts = _AtmSigDetectRestarts_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 3, 1, 17),
    _AtmSigDetectRestarts_Type()
)
atmSigDetectRestarts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSigDetectRestarts.setStatus("current")
_AtmSigEmitRestarts_Type = Counter32
_AtmSigEmitRestarts_Object = MibTableColumn
atmSigEmitRestarts = _AtmSigEmitRestarts_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 3, 1, 18),
    _AtmSigEmitRestarts_Type()
)
atmSigEmitRestarts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSigEmitRestarts.setStatus("current")
_AtmSigInEstabls_Type = Counter32
_AtmSigInEstabls_Object = MibTableColumn
atmSigInEstabls = _AtmSigInEstabls_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 3, 1, 19),
    _AtmSigInEstabls_Type()
)
atmSigInEstabls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSigInEstabls.setStatus("current")
_AtmSigOutEstabls_Type = Counter32
_AtmSigOutEstabls_Object = MibTableColumn
atmSigOutEstabls = _AtmSigOutEstabls_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 3, 1, 20),
    _AtmSigOutEstabls_Type()
)
atmSigOutEstabls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmSigOutEstabls.setStatus("current")
_AtmSigSupportTable_Object = MibTable
atmSigSupportTable = _AtmSigSupportTable_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 4)
)
if mibBuilder.loadTexts:
    atmSigSupportTable.setStatus("current")
_AtmSigSupportEntry_Object = MibTableRow
atmSigSupportEntry = _AtmSigSupportEntry_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 4, 1)
)
atmSigSupportEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    atmSigSupportEntry.setStatus("current")


class _AtmSigSupportClgPtyNumDel_Type(Integer32):
    """Custom type atmSigSupportClgPtyNumDel based on Integer32"""
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


_AtmSigSupportClgPtyNumDel_Type.__name__ = "Integer32"
_AtmSigSupportClgPtyNumDel_Object = MibTableColumn
atmSigSupportClgPtyNumDel = _AtmSigSupportClgPtyNumDel_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 4, 1, 1),
    _AtmSigSupportClgPtyNumDel_Type()
)
atmSigSupportClgPtyNumDel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSigSupportClgPtyNumDel.setStatus("current")


class _AtmSigSupportClgPtySubAddr_Type(Integer32):
    """Custom type atmSigSupportClgPtySubAddr based on Integer32"""
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


_AtmSigSupportClgPtySubAddr_Type.__name__ = "Integer32"
_AtmSigSupportClgPtySubAddr_Object = MibTableColumn
atmSigSupportClgPtySubAddr = _AtmSigSupportClgPtySubAddr_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 4, 1, 2),
    _AtmSigSupportClgPtySubAddr_Type()
)
atmSigSupportClgPtySubAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSigSupportClgPtySubAddr.setStatus("current")


class _AtmSigSupportCldPtySubAddr_Type(Integer32):
    """Custom type atmSigSupportCldPtySubAddr based on Integer32"""
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


_AtmSigSupportCldPtySubAddr_Type.__name__ = "Integer32"
_AtmSigSupportCldPtySubAddr_Object = MibTableColumn
atmSigSupportCldPtySubAddr = _AtmSigSupportCldPtySubAddr_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 4, 1, 3),
    _AtmSigSupportCldPtySubAddr_Type()
)
atmSigSupportCldPtySubAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSigSupportCldPtySubAddr.setStatus("current")


class _AtmSigSupportHiLyrInfo_Type(Integer32):
    """Custom type atmSigSupportHiLyrInfo based on Integer32"""
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


_AtmSigSupportHiLyrInfo_Type.__name__ = "Integer32"
_AtmSigSupportHiLyrInfo_Object = MibTableColumn
atmSigSupportHiLyrInfo = _AtmSigSupportHiLyrInfo_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 4, 1, 4),
    _AtmSigSupportHiLyrInfo_Type()
)
atmSigSupportHiLyrInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSigSupportHiLyrInfo.setStatus("current")


class _AtmSigSupportLoLyrInfo_Type(Integer32):
    """Custom type atmSigSupportLoLyrInfo based on Integer32"""
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


_AtmSigSupportLoLyrInfo_Type.__name__ = "Integer32"
_AtmSigSupportLoLyrInfo_Object = MibTableColumn
atmSigSupportLoLyrInfo = _AtmSigSupportLoLyrInfo_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 4, 1, 5),
    _AtmSigSupportLoLyrInfo_Type()
)
atmSigSupportLoLyrInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSigSupportLoLyrInfo.setStatus("current")


class _AtmSigSupportBlliRepeatInd_Type(Integer32):
    """Custom type atmSigSupportBlliRepeatInd based on Integer32"""
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


_AtmSigSupportBlliRepeatInd_Type.__name__ = "Integer32"
_AtmSigSupportBlliRepeatInd_Object = MibTableColumn
atmSigSupportBlliRepeatInd = _AtmSigSupportBlliRepeatInd_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 4, 1, 6),
    _AtmSigSupportBlliRepeatInd_Type()
)
atmSigSupportBlliRepeatInd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSigSupportBlliRepeatInd.setStatus("current")


class _AtmSigSupportAALInfo_Type(Integer32):
    """Custom type atmSigSupportAALInfo based on Integer32"""
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


_AtmSigSupportAALInfo_Type.__name__ = "Integer32"
_AtmSigSupportAALInfo_Object = MibTableColumn
atmSigSupportAALInfo = _AtmSigSupportAALInfo_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 4, 1, 7),
    _AtmSigSupportAALInfo_Type()
)
atmSigSupportAALInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSigSupportAALInfo.setStatus("current")


class _AtmSigSupportPrefCarrier_Type(OctetString):
    """Custom type atmSigSupportPrefCarrier based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_AtmSigSupportPrefCarrier_Type.__name__ = "OctetString"
_AtmSigSupportPrefCarrier_Object = MibTableColumn
atmSigSupportPrefCarrier = _AtmSigSupportPrefCarrier_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 4, 1, 8),
    _AtmSigSupportPrefCarrier_Type()
)
atmSigSupportPrefCarrier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmSigSupportPrefCarrier.setStatus("current")
_AtmSigDescrParamTable_Object = MibTable
atmSigDescrParamTable = _AtmSigDescrParamTable_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 5)
)
if mibBuilder.loadTexts:
    atmSigDescrParamTable.setStatus("current")
_AtmSigDescrParamEntry_Object = MibTableRow
atmSigDescrParamEntry = _AtmSigDescrParamEntry_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 5, 1)
)
atmSigDescrParamEntry.setIndexNames(
    (0, "ATM2-MIB", "atmSigDescrParamIndex"),
)
if mibBuilder.loadTexts:
    atmSigDescrParamEntry.setStatus("current")
_AtmSigDescrParamIndex_Type = AtmSigDescrParamIndex
_AtmSigDescrParamIndex_Object = MibTableColumn
atmSigDescrParamIndex = _AtmSigDescrParamIndex_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 5, 1, 1),
    _AtmSigDescrParamIndex_Type()
)
atmSigDescrParamIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmSigDescrParamIndex.setStatus("current")


class _AtmSigDescrParamAalType_Type(Integer32):
    """Custom type atmSigDescrParamAalType based on Integer32"""
    defaultValue = 1

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
        *(("aal1", 2),
          ("aal2", 6),
          ("aal34", 3),
          ("aal5", 4),
          ("other", 1),
          ("userDefined", 5))
    )


_AtmSigDescrParamAalType_Type.__name__ = "Integer32"
_AtmSigDescrParamAalType_Object = MibTableColumn
atmSigDescrParamAalType = _AtmSigDescrParamAalType_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 5, 1, 2),
    _AtmSigDescrParamAalType_Type()
)
atmSigDescrParamAalType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmSigDescrParamAalType.setStatus("current")


class _AtmSigDescrParamAalSscsType_Type(Integer32):
    """Custom type atmSigDescrParamAalSscsType based on Integer32"""
    defaultValue = 1

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
        *(("assured", 2),
          ("frameRelay", 4),
          ("nonassured", 3),
          ("null", 5),
          ("other", 1))
    )


_AtmSigDescrParamAalSscsType_Type.__name__ = "Integer32"
_AtmSigDescrParamAalSscsType_Object = MibTableColumn
atmSigDescrParamAalSscsType = _AtmSigDescrParamAalSscsType_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 5, 1, 3),
    _AtmSigDescrParamAalSscsType_Type()
)
atmSigDescrParamAalSscsType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmSigDescrParamAalSscsType.setStatus("current")


class _AtmSigDescrParamBhliType_Type(Integer32):
    """Custom type atmSigDescrParamBhliType based on Integer32"""
    defaultValue = 1

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
        *(("hiProfile", 4),
          ("iso", 2),
          ("other", 1),
          ("user", 3),
          ("vendorSpecific", 5))
    )


_AtmSigDescrParamBhliType_Type.__name__ = "Integer32"
_AtmSigDescrParamBhliType_Object = MibTableColumn
atmSigDescrParamBhliType = _AtmSigDescrParamBhliType_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 5, 1, 4),
    _AtmSigDescrParamBhliType_Type()
)
atmSigDescrParamBhliType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmSigDescrParamBhliType.setStatus("current")


class _AtmSigDescrParamBhliInfo_Type(OctetString):
    """Custom type atmSigDescrParamBhliInfo based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_AtmSigDescrParamBhliInfo_Type.__name__ = "OctetString"
_AtmSigDescrParamBhliInfo_Object = MibTableColumn
atmSigDescrParamBhliInfo = _AtmSigDescrParamBhliInfo_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 5, 1, 5),
    _AtmSigDescrParamBhliInfo_Type()
)
atmSigDescrParamBhliInfo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmSigDescrParamBhliInfo.setStatus("current")


class _AtmSigDescrParamBbcConnConf_Type(Integer32):
    """Custom type atmSigDescrParamBbcConnConf based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ptmp", 2),
          ("ptp", 1))
    )


_AtmSigDescrParamBbcConnConf_Type.__name__ = "Integer32"
_AtmSigDescrParamBbcConnConf_Object = MibTableColumn
atmSigDescrParamBbcConnConf = _AtmSigDescrParamBbcConnConf_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 5, 1, 6),
    _AtmSigDescrParamBbcConnConf_Type()
)
atmSigDescrParamBbcConnConf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmSigDescrParamBbcConnConf.setStatus("current")


class _AtmSigDescrParamBlliLayer2_Type(Integer32):
    """Custom type atmSigDescrParamBlliLayer2 based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("hdlcAbm", 9),
          ("hdlcArm", 7),
          ("hdlcNrm", 8),
          ("iso1745", 2),
          ("iso7776", 14),
          ("iso88022", 10),
          ("lapb", 6),
          ("other", 1),
          ("q921", 3),
          ("q922", 12),
          ("userDef", 13),
          ("x25linklayer", 4),
          ("x25multilink", 5),
          ("x75slp", 11))
    )


_AtmSigDescrParamBlliLayer2_Type.__name__ = "Integer32"
_AtmSigDescrParamBlliLayer2_Object = MibTableColumn
atmSigDescrParamBlliLayer2 = _AtmSigDescrParamBlliLayer2_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 5, 1, 7),
    _AtmSigDescrParamBlliLayer2_Type()
)
atmSigDescrParamBlliLayer2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmSigDescrParamBlliLayer2.setStatus("current")


class _AtmSigDescrParamBlliLayer3_Type(Integer32):
    """Custom type atmSigDescrParamBlliLayer3 based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("isoiec8208", 3),
          ("isoiec8473", 5),
          ("other", 1),
          ("t70", 6),
          ("tr9577", 7),
          ("userDef", 8),
          ("x223iso8878", 4),
          ("x25pkt", 2))
    )


_AtmSigDescrParamBlliLayer3_Type.__name__ = "Integer32"
_AtmSigDescrParamBlliLayer3_Object = MibTableColumn
atmSigDescrParamBlliLayer3 = _AtmSigDescrParamBlliLayer3_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 5, 1, 8),
    _AtmSigDescrParamBlliLayer3_Type()
)
atmSigDescrParamBlliLayer3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmSigDescrParamBlliLayer3.setStatus("current")


class _AtmSigDescrParamBlliPktSize_Type(Integer32):
    """Custom type atmSigDescrParamBlliPktSize based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("s1024", 8),
          ("s128", 5),
          ("s16", 2),
          ("s2048", 9),
          ("s256", 6),
          ("s32", 3),
          ("s4096", 10),
          ("s512", 7),
          ("s64", 4))
    )


_AtmSigDescrParamBlliPktSize_Type.__name__ = "Integer32"
_AtmSigDescrParamBlliPktSize_Object = MibTableColumn
atmSigDescrParamBlliPktSize = _AtmSigDescrParamBlliPktSize_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 5, 1, 9),
    _AtmSigDescrParamBlliPktSize_Type()
)
atmSigDescrParamBlliPktSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmSigDescrParamBlliPktSize.setStatus("current")


class _AtmSigDescrParamBlliSnapId_Type(Integer32):
    """Custom type atmSigDescrParamBlliSnapId based on Integer32"""
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
        *(("false", 3),
          ("other", 1),
          ("true", 2))
    )


_AtmSigDescrParamBlliSnapId_Type.__name__ = "Integer32"
_AtmSigDescrParamBlliSnapId_Object = MibTableColumn
atmSigDescrParamBlliSnapId = _AtmSigDescrParamBlliSnapId_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 5, 1, 10),
    _AtmSigDescrParamBlliSnapId_Type()
)
atmSigDescrParamBlliSnapId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmSigDescrParamBlliSnapId.setStatus("current")


class _AtmSigDescrParamBlliOuiPid_Type(OctetString):
    """Custom type atmSigDescrParamBlliOuiPid based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(5, 5),
    )


_AtmSigDescrParamBlliOuiPid_Type.__name__ = "OctetString"
_AtmSigDescrParamBlliOuiPid_Object = MibTableColumn
atmSigDescrParamBlliOuiPid = _AtmSigDescrParamBlliOuiPid_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 5, 1, 11),
    _AtmSigDescrParamBlliOuiPid_Type()
)
atmSigDescrParamBlliOuiPid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmSigDescrParamBlliOuiPid.setStatus("current")
_AtmSigDescrParamRowStatus_Type = RowStatus
_AtmSigDescrParamRowStatus_Object = MibTableColumn
atmSigDescrParamRowStatus = _AtmSigDescrParamRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 5, 1, 12),
    _AtmSigDescrParamRowStatus_Type()
)
atmSigDescrParamRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmSigDescrParamRowStatus.setStatus("current")
_AtmIfRegisteredAddrTable_Object = MibTable
atmIfRegisteredAddrTable = _AtmIfRegisteredAddrTable_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 6)
)
if mibBuilder.loadTexts:
    atmIfRegisteredAddrTable.setStatus("current")
_AtmIfRegisteredAddrEntry_Object = MibTableRow
atmIfRegisteredAddrEntry = _AtmIfRegisteredAddrEntry_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 6, 1)
)
atmIfRegisteredAddrEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ATM2-MIB", "atmIfRegAddrAddress"),
)
if mibBuilder.loadTexts:
    atmIfRegisteredAddrEntry.setStatus("current")
_AtmIfRegAddrAddress_Type = AtmAddr
_AtmIfRegAddrAddress_Object = MibTableColumn
atmIfRegAddrAddress = _AtmIfRegAddrAddress_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 6, 1, 1),
    _AtmIfRegAddrAddress_Type()
)
atmIfRegAddrAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmIfRegAddrAddress.setStatus("current")


class _AtmIfRegAddrAddressSource_Type(Integer32):
    """Custom type atmIfRegAddrAddressSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 3),
          ("other", 1),
          ("static", 2))
    )


_AtmIfRegAddrAddressSource_Type.__name__ = "Integer32"
_AtmIfRegAddrAddressSource_Object = MibTableColumn
atmIfRegAddrAddressSource = _AtmIfRegAddrAddressSource_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 6, 1, 2),
    _AtmIfRegAddrAddressSource_Type()
)
atmIfRegAddrAddressSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIfRegAddrAddressSource.setStatus("current")


class _AtmIfRegAddrOrgScope_Type(Integer32):
    """Custom type atmIfRegAddrOrgScope based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("communityMinusOne", 10),
          ("communityPlusOne", 12),
          ("global", 15),
          ("interRegional", 14),
          ("intraCommunity", 11),
          ("intraOrganization", 8),
          ("intraSite", 5),
          ("localNetwork", 1),
          ("localNetworkPlusOne", 2),
          ("localNetworkPlusTwo", 3),
          ("organizationMinusOne", 7),
          ("organizationPlusOne", 9),
          ("regional", 13),
          ("siteMinusOne", 4),
          ("sitePlusOne", 6))
    )


_AtmIfRegAddrOrgScope_Type.__name__ = "Integer32"
_AtmIfRegAddrOrgScope_Object = MibTableColumn
atmIfRegAddrOrgScope = _AtmIfRegAddrOrgScope_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 6, 1, 3),
    _AtmIfRegAddrOrgScope_Type()
)
atmIfRegAddrOrgScope.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmIfRegAddrOrgScope.setStatus("current")
_AtmIfRegAddrRowStatus_Type = RowStatus
_AtmIfRegAddrRowStatus_Object = MibTableColumn
atmIfRegAddrRowStatus = _AtmIfRegAddrRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 6, 1, 4),
    _AtmIfRegAddrRowStatus_Type()
)
atmIfRegAddrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmIfRegAddrRowStatus.setStatus("current")
_AtmVclAddrTable_Object = MibTable
atmVclAddrTable = _AtmVclAddrTable_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 7)
)
if mibBuilder.loadTexts:
    atmVclAddrTable.setStatus("current")
_AtmVclAddrEntry_Object = MibTableRow
atmVclAddrEntry = _AtmVclAddrEntry_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 7, 1)
)
atmVclAddrEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ATM-MIB", "atmVclVpi"),
    (0, "ATM-MIB", "atmVclVci"),
    (0, "ATM2-MIB", "atmVclAddrAddr"),
)
if mibBuilder.loadTexts:
    atmVclAddrEntry.setStatus("current")
_AtmVclAddrAddr_Type = AtmAddr
_AtmVclAddrAddr_Object = MibTableColumn
atmVclAddrAddr = _AtmVclAddrAddr_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 7, 1, 1),
    _AtmVclAddrAddr_Type()
)
atmVclAddrAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmVclAddrAddr.setStatus("current")


class _AtmVclAddrType_Type(Integer32):
    """Custom type atmVclAddrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("calledParty", 2),
          ("callingParty", 1))
    )


_AtmVclAddrType_Type.__name__ = "Integer32"
_AtmVclAddrType_Object = MibTableColumn
atmVclAddrType = _AtmVclAddrType_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 7, 1, 2),
    _AtmVclAddrType_Type()
)
atmVclAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmVclAddrType.setStatus("current")
_AtmVclAddrRowStatus_Type = RowStatus
_AtmVclAddrRowStatus_Object = MibTableColumn
atmVclAddrRowStatus = _AtmVclAddrRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 7, 1, 3),
    _AtmVclAddrRowStatus_Type()
)
atmVclAddrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmVclAddrRowStatus.setStatus("current")
_AtmAddrVclTable_Object = MibTable
atmAddrVclTable = _AtmAddrVclTable_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 8)
)
if mibBuilder.loadTexts:
    atmAddrVclTable.setStatus("current")
_AtmAddrVclEntry_Object = MibTableRow
atmAddrVclEntry = _AtmAddrVclEntry_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 8, 1)
)
atmAddrVclEntry.setIndexNames(
    (0, "ATM2-MIB", "atmVclAddrAddr"),
    (0, "ATM2-MIB", "atmAddrVclAtmIfIndex"),
    (0, "ATM2-MIB", "atmAddrVclVpi"),
    (0, "ATM2-MIB", "atmAddrVclVci"),
)
if mibBuilder.loadTexts:
    atmAddrVclEntry.setStatus("current")
_AtmAddrVclAtmIfIndex_Type = InterfaceIndex
_AtmAddrVclAtmIfIndex_Object = MibTableColumn
atmAddrVclAtmIfIndex = _AtmAddrVclAtmIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 8, 1, 1),
    _AtmAddrVclAtmIfIndex_Type()
)
atmAddrVclAtmIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmAddrVclAtmIfIndex.setStatus("current")
_AtmAddrVclVpi_Type = AtmVpIdentifier
_AtmAddrVclVpi_Object = MibTableColumn
atmAddrVclVpi = _AtmAddrVclVpi_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 8, 1, 2),
    _AtmAddrVclVpi_Type()
)
atmAddrVclVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmAddrVclVpi.setStatus("current")
_AtmAddrVclVci_Type = AtmVcIdentifier
_AtmAddrVclVci_Object = MibTableColumn
atmAddrVclVci = _AtmAddrVclVci_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 8, 1, 3),
    _AtmAddrVclVci_Type()
)
atmAddrVclVci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmAddrVclVci.setStatus("current")


class _AtmAddrVclAddrType_Type(Integer32):
    """Custom type atmAddrVclAddrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("calledParty", 2),
          ("callingParty", 1))
    )


_AtmAddrVclAddrType_Type.__name__ = "Integer32"
_AtmAddrVclAddrType_Object = MibTableColumn
atmAddrVclAddrType = _AtmAddrVclAddrType_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 8, 1, 4),
    _AtmAddrVclAddrType_Type()
)
atmAddrVclAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmAddrVclAddrType.setStatus("current")
_AtmVplStatTable_Object = MibTable
atmVplStatTable = _AtmVplStatTable_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 9)
)
if mibBuilder.loadTexts:
    atmVplStatTable.setStatus("current")
_AtmVplStatEntry_Object = MibTableRow
atmVplStatEntry = _AtmVplStatEntry_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 9, 1)
)
atmVplStatEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ATM-MIB", "atmVplVpi"),
)
if mibBuilder.loadTexts:
    atmVplStatEntry.setStatus("current")
_AtmVplStatTotalCellIns_Type = Counter32
_AtmVplStatTotalCellIns_Object = MibTableColumn
atmVplStatTotalCellIns = _AtmVplStatTotalCellIns_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 9, 1, 1),
    _AtmVplStatTotalCellIns_Type()
)
atmVplStatTotalCellIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVplStatTotalCellIns.setStatus("current")
_AtmVplStatClp0CellIns_Type = Counter32
_AtmVplStatClp0CellIns_Object = MibTableColumn
atmVplStatClp0CellIns = _AtmVplStatClp0CellIns_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 9, 1, 2),
    _AtmVplStatClp0CellIns_Type()
)
atmVplStatClp0CellIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVplStatClp0CellIns.setStatus("current")
_AtmVplStatTotalDiscards_Type = Counter32
_AtmVplStatTotalDiscards_Object = MibTableColumn
atmVplStatTotalDiscards = _AtmVplStatTotalDiscards_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 9, 1, 3),
    _AtmVplStatTotalDiscards_Type()
)
atmVplStatTotalDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVplStatTotalDiscards.setStatus("current")
_AtmVplStatClp0Discards_Type = Counter32
_AtmVplStatClp0Discards_Object = MibTableColumn
atmVplStatClp0Discards = _AtmVplStatClp0Discards_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 9, 1, 4),
    _AtmVplStatClp0Discards_Type()
)
atmVplStatClp0Discards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVplStatClp0Discards.setStatus("current")
_AtmVplStatTotalCellOuts_Type = Counter32
_AtmVplStatTotalCellOuts_Object = MibTableColumn
atmVplStatTotalCellOuts = _AtmVplStatTotalCellOuts_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 9, 1, 5),
    _AtmVplStatTotalCellOuts_Type()
)
atmVplStatTotalCellOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVplStatTotalCellOuts.setStatus("current")
_AtmVplStatClp0CellOuts_Type = Counter32
_AtmVplStatClp0CellOuts_Object = MibTableColumn
atmVplStatClp0CellOuts = _AtmVplStatClp0CellOuts_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 9, 1, 6),
    _AtmVplStatClp0CellOuts_Type()
)
atmVplStatClp0CellOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVplStatClp0CellOuts.setStatus("current")
_AtmVplStatClp0Tagged_Type = Counter32
_AtmVplStatClp0Tagged_Object = MibTableColumn
atmVplStatClp0Tagged = _AtmVplStatClp0Tagged_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 9, 1, 7),
    _AtmVplStatClp0Tagged_Type()
)
atmVplStatClp0Tagged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVplStatClp0Tagged.setStatus("current")
_AtmVplLogicalPortTable_Object = MibTable
atmVplLogicalPortTable = _AtmVplLogicalPortTable_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 10)
)
if mibBuilder.loadTexts:
    atmVplLogicalPortTable.setStatus("current")
_AtmVplLogicalPortEntry_Object = MibTableRow
atmVplLogicalPortEntry = _AtmVplLogicalPortEntry_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 10, 1)
)
if mibBuilder.loadTexts:
    atmVplLogicalPortEntry.setStatus("current")


class _AtmVplLogicalPortDef_Type(Integer32):
    """Custom type atmVplLogicalPortDef based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("isLogicalIf", 2),
          ("notLogicalIf", 1))
    )


_AtmVplLogicalPortDef_Type.__name__ = "Integer32"
_AtmVplLogicalPortDef_Object = MibTableColumn
atmVplLogicalPortDef = _AtmVplLogicalPortDef_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 10, 1, 1),
    _AtmVplLogicalPortDef_Type()
)
atmVplLogicalPortDef.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmVplLogicalPortDef.setStatus("current")
_AtmVplLogicalPortIndex_Type = InterfaceIndexOrZero
_AtmVplLogicalPortIndex_Object = MibTableColumn
atmVplLogicalPortIndex = _AtmVplLogicalPortIndex_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 10, 1, 2),
    _AtmVplLogicalPortIndex_Type()
)
atmVplLogicalPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVplLogicalPortIndex.setStatus("current")
_AtmVclStatTable_Object = MibTable
atmVclStatTable = _AtmVclStatTable_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 11)
)
if mibBuilder.loadTexts:
    atmVclStatTable.setStatus("current")
_AtmVclStatEntry_Object = MibTableRow
atmVclStatEntry = _AtmVclStatEntry_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 11, 1)
)
atmVclStatEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ATM-MIB", "atmVclVpi"),
    (0, "ATM-MIB", "atmVclVci"),
)
if mibBuilder.loadTexts:
    atmVclStatEntry.setStatus("current")
_AtmVclStatTotalCellIns_Type = Counter32
_AtmVclStatTotalCellIns_Object = MibTableColumn
atmVclStatTotalCellIns = _AtmVclStatTotalCellIns_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 11, 1, 1),
    _AtmVclStatTotalCellIns_Type()
)
atmVclStatTotalCellIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVclStatTotalCellIns.setStatus("current")
_AtmVclStatClp0CellIns_Type = Counter32
_AtmVclStatClp0CellIns_Object = MibTableColumn
atmVclStatClp0CellIns = _AtmVclStatClp0CellIns_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 11, 1, 2),
    _AtmVclStatClp0CellIns_Type()
)
atmVclStatClp0CellIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVclStatClp0CellIns.setStatus("current")
_AtmVclStatTotalDiscards_Type = Counter32
_AtmVclStatTotalDiscards_Object = MibTableColumn
atmVclStatTotalDiscards = _AtmVclStatTotalDiscards_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 11, 1, 3),
    _AtmVclStatTotalDiscards_Type()
)
atmVclStatTotalDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVclStatTotalDiscards.setStatus("current")
_AtmVclStatClp0Discards_Type = Counter32
_AtmVclStatClp0Discards_Object = MibTableColumn
atmVclStatClp0Discards = _AtmVclStatClp0Discards_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 11, 1, 4),
    _AtmVclStatClp0Discards_Type()
)
atmVclStatClp0Discards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVclStatClp0Discards.setStatus("current")
_AtmVclStatTotalCellOuts_Type = Counter32
_AtmVclStatTotalCellOuts_Object = MibTableColumn
atmVclStatTotalCellOuts = _AtmVclStatTotalCellOuts_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 11, 1, 5),
    _AtmVclStatTotalCellOuts_Type()
)
atmVclStatTotalCellOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVclStatTotalCellOuts.setStatus("current")
_AtmVclStatClp0CellOuts_Type = Counter32
_AtmVclStatClp0CellOuts_Object = MibTableColumn
atmVclStatClp0CellOuts = _AtmVclStatClp0CellOuts_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 11, 1, 6),
    _AtmVclStatClp0CellOuts_Type()
)
atmVclStatClp0CellOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVclStatClp0CellOuts.setStatus("current")
_AtmVclStatClp0Tagged_Type = Counter32
_AtmVclStatClp0Tagged_Object = MibTableColumn
atmVclStatClp0Tagged = _AtmVclStatClp0Tagged_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 11, 1, 7),
    _AtmVclStatClp0Tagged_Type()
)
atmVclStatClp0Tagged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVclStatClp0Tagged.setStatus("current")
_AtmAal5VclStatTable_Object = MibTable
atmAal5VclStatTable = _AtmAal5VclStatTable_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 12)
)
if mibBuilder.loadTexts:
    atmAal5VclStatTable.setStatus("current")
_AtmAal5VclStatEntry_Object = MibTableRow
atmAal5VclStatEntry = _AtmAal5VclStatEntry_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 12, 1)
)
atmAal5VclStatEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ATM-MIB", "atmVclVpi"),
    (0, "ATM-MIB", "atmVclVci"),
)
if mibBuilder.loadTexts:
    atmAal5VclStatEntry.setStatus("current")
_AtmAal5VclInPkts_Type = Counter32
_AtmAal5VclInPkts_Object = MibTableColumn
atmAal5VclInPkts = _AtmAal5VclInPkts_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 12, 1, 1),
    _AtmAal5VclInPkts_Type()
)
atmAal5VclInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmAal5VclInPkts.setStatus("current")
_AtmAal5VclOutPkts_Type = Counter32
_AtmAal5VclOutPkts_Object = MibTableColumn
atmAal5VclOutPkts = _AtmAal5VclOutPkts_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 12, 1, 2),
    _AtmAal5VclOutPkts_Type()
)
atmAal5VclOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmAal5VclOutPkts.setStatus("current")
_AtmAal5VclInOctets_Type = Counter32
_AtmAal5VclInOctets_Object = MibTableColumn
atmAal5VclInOctets = _AtmAal5VclInOctets_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 12, 1, 3),
    _AtmAal5VclInOctets_Type()
)
atmAal5VclInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmAal5VclInOctets.setStatus("current")
_AtmAal5VclOutOctets_Type = Counter32
_AtmAal5VclOutOctets_Object = MibTableColumn
atmAal5VclOutOctets = _AtmAal5VclOutOctets_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 12, 1, 4),
    _AtmAal5VclOutOctets_Type()
)
atmAal5VclOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmAal5VclOutOctets.setStatus("current")
_AtmVclGenTable_Object = MibTable
atmVclGenTable = _AtmVclGenTable_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 13)
)
if mibBuilder.loadTexts:
    atmVclGenTable.setStatus("current")
_AtmVclGenEntry_Object = MibTableRow
atmVclGenEntry = _AtmVclGenEntry_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 13, 1)
)
if mibBuilder.loadTexts:
    atmVclGenEntry.setStatus("current")
_AtmVclGenSigDescrIndex_Type = AtmSigDescrParamIndex
_AtmVclGenSigDescrIndex_Object = MibTableColumn
atmVclGenSigDescrIndex = _AtmVclGenSigDescrIndex_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 13, 1, 1),
    _AtmVclGenSigDescrIndex_Type()
)
atmVclGenSigDescrIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmVclGenSigDescrIndex.setStatus("current")
_AtmInterfaceExtTable_Object = MibTable
atmInterfaceExtTable = _AtmInterfaceExtTable_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 14)
)
if mibBuilder.loadTexts:
    atmInterfaceExtTable.setStatus("current")
_AtmInterfaceExtEntry_Object = MibTableRow
atmInterfaceExtEntry = _AtmInterfaceExtEntry_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 14, 1)
)
if mibBuilder.loadTexts:
    atmInterfaceExtEntry.setStatus("current")


class _AtmIntfConfigType_Type(AtmInterfaceType):
    """Custom type atmIntfConfigType based on AtmInterfaceType"""


_AtmIntfConfigType_Object = MibTableColumn
atmIntfConfigType = _AtmIntfConfigType_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 14, 1, 1),
    _AtmIntfConfigType_Type()
)
atmIntfConfigType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIntfConfigType.setStatus("current")
_AtmIntfActualType_Type = AtmInterfaceType
_AtmIntfActualType_Object = MibTableColumn
atmIntfActualType = _AtmIntfActualType_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 14, 1, 2),
    _AtmIntfActualType_Type()
)
atmIntfActualType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIntfActualType.setStatus("current")


class _AtmIntfConfigSide_Type(Integer32):
    """Custom type atmIntfConfigSide based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("network", 3),
          ("other", 1),
          ("user", 2))
    )


_AtmIntfConfigSide_Type.__name__ = "Integer32"
_AtmIntfConfigSide_Object = MibTableColumn
atmIntfConfigSide = _AtmIntfConfigSide_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 14, 1, 3),
    _AtmIntfConfigSide_Type()
)
atmIntfConfigSide.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIntfConfigSide.setStatus("current")


class _AtmIntfActualSide_Type(Integer32):
    """Custom type atmIntfActualSide based on Integer32"""
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
        *(("network", 3),
          ("other", 1),
          ("symmetric", 4),
          ("user", 2))
    )


_AtmIntfActualSide_Type.__name__ = "Integer32"
_AtmIntfActualSide_Object = MibTableColumn
atmIntfActualSide = _AtmIntfActualSide_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 14, 1, 4),
    _AtmIntfActualSide_Type()
)
atmIntfActualSide.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIntfActualSide.setStatus("current")


class _AtmIntfIlmiAdminStatus_Type(Bits):
    """Custom type atmIntfIlmiAdminStatus based on Bits"""
    namedValues = NamedValues(
        *(("ilmi", 0),
          ("ilmiAddressRegistration", 1),
          ("ilmiConnectivity", 2),
          ("ilmiPvcPvpMgmt", 3),
          ("ilmiSigVccParamNegotiation", 4))
    )

_AtmIntfIlmiAdminStatus_Type.__name__ = "Bits"
_AtmIntfIlmiAdminStatus_Object = MibTableColumn
atmIntfIlmiAdminStatus = _AtmIntfIlmiAdminStatus_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 14, 1, 5),
    _AtmIntfIlmiAdminStatus_Type()
)
atmIntfIlmiAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIntfIlmiAdminStatus.setStatus("current")


class _AtmIntfIlmiOperStatus_Type(Bits):
    """Custom type atmIntfIlmiOperStatus based on Bits"""
    namedValues = NamedValues(
        *(("ilmi", 0),
          ("ilmiAddressRegistration", 1),
          ("ilmiConnectivity", 2),
          ("ilmiPvcPvpMgmt", 3),
          ("ilmiSigVccParamNegotiation", 4))
    )

_AtmIntfIlmiOperStatus_Type.__name__ = "Bits"
_AtmIntfIlmiOperStatus_Object = MibTableColumn
atmIntfIlmiOperStatus = _AtmIntfIlmiOperStatus_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 14, 1, 6),
    _AtmIntfIlmiOperStatus_Type()
)
atmIntfIlmiOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIntfIlmiOperStatus.setStatus("current")


class _AtmIntfIlmiFsmState_Type(Integer32):
    """Custom type atmIntfIlmiFsmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("configuring", 4),
          ("establishing", 3),
          ("linkFailing", 2),
          ("registeringAddresses", 8),
          ("registeringNetworkPrefixes", 6),
          ("retrievingAddresses", 7),
          ("retrievingNetworkPrefixes", 5),
          ("stopped", 1),
          ("verifying", 9))
    )


_AtmIntfIlmiFsmState_Type.__name__ = "Integer32"
_AtmIntfIlmiFsmState_Object = MibTableColumn
atmIntfIlmiFsmState = _AtmIntfIlmiFsmState_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 14, 1, 7),
    _AtmIntfIlmiFsmState_Type()
)
atmIntfIlmiFsmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIntfIlmiFsmState.setStatus("current")


class _AtmIntfIlmiEstablishConPollIntvl_Type(Integer32):
    """Custom type atmIntfIlmiEstablishConPollIntvl based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AtmIntfIlmiEstablishConPollIntvl_Type.__name__ = "Integer32"
_AtmIntfIlmiEstablishConPollIntvl_Object = MibTableColumn
atmIntfIlmiEstablishConPollIntvl = _AtmIntfIlmiEstablishConPollIntvl_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 14, 1, 8),
    _AtmIntfIlmiEstablishConPollIntvl_Type()
)
atmIntfIlmiEstablishConPollIntvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIntfIlmiEstablishConPollIntvl.setStatus("current")
if mibBuilder.loadTexts:
    atmIntfIlmiEstablishConPollIntvl.setUnits("seconds")


class _AtmIntfIlmiCheckConPollIntvl_Type(Integer32):
    """Custom type atmIntfIlmiCheckConPollIntvl based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AtmIntfIlmiCheckConPollIntvl_Type.__name__ = "Integer32"
_AtmIntfIlmiCheckConPollIntvl_Object = MibTableColumn
atmIntfIlmiCheckConPollIntvl = _AtmIntfIlmiCheckConPollIntvl_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 14, 1, 9),
    _AtmIntfIlmiCheckConPollIntvl_Type()
)
atmIntfIlmiCheckConPollIntvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIntfIlmiCheckConPollIntvl.setStatus("current")
if mibBuilder.loadTexts:
    atmIntfIlmiCheckConPollIntvl.setUnits("seconds")


class _AtmIntfIlmiConPollInactFactor_Type(Integer32):
    """Custom type atmIntfIlmiConPollInactFactor based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AtmIntfIlmiConPollInactFactor_Type.__name__ = "Integer32"
_AtmIntfIlmiConPollInactFactor_Object = MibTableColumn
atmIntfIlmiConPollInactFactor = _AtmIntfIlmiConPollInactFactor_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 14, 1, 10),
    _AtmIntfIlmiConPollInactFactor_Type()
)
atmIntfIlmiConPollInactFactor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIntfIlmiConPollInactFactor.setStatus("current")


class _AtmIntfIlmiPublicPrivateIndctr_Type(Integer32):
    """Custom type atmIntfIlmiPublicPrivateIndctr based on Integer32"""
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
        *(("other", 1),
          ("private", 3),
          ("public", 2))
    )


_AtmIntfIlmiPublicPrivateIndctr_Type.__name__ = "Integer32"
_AtmIntfIlmiPublicPrivateIndctr_Object = MibTableColumn
atmIntfIlmiPublicPrivateIndctr = _AtmIntfIlmiPublicPrivateIndctr_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 14, 1, 11),
    _AtmIntfIlmiPublicPrivateIndctr_Type()
)
atmIntfIlmiPublicPrivateIndctr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIntfIlmiPublicPrivateIndctr.setStatus("current")


class _AtmInterfaceConfMaxSvpcVpi_Type(Integer32):
    """Custom type atmInterfaceConfMaxSvpcVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_AtmInterfaceConfMaxSvpcVpi_Type.__name__ = "Integer32"
_AtmInterfaceConfMaxSvpcVpi_Object = MibTableColumn
atmInterfaceConfMaxSvpcVpi = _AtmInterfaceConfMaxSvpcVpi_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 14, 1, 12),
    _AtmInterfaceConfMaxSvpcVpi_Type()
)
atmInterfaceConfMaxSvpcVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmInterfaceConfMaxSvpcVpi.setStatus("current")


class _AtmInterfaceCurrentMaxSvpcVpi_Type(Integer32):
    """Custom type atmInterfaceCurrentMaxSvpcVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_AtmInterfaceCurrentMaxSvpcVpi_Type.__name__ = "Integer32"
_AtmInterfaceCurrentMaxSvpcVpi_Object = MibTableColumn
atmInterfaceCurrentMaxSvpcVpi = _AtmInterfaceCurrentMaxSvpcVpi_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 14, 1, 13),
    _AtmInterfaceCurrentMaxSvpcVpi_Type()
)
atmInterfaceCurrentMaxSvpcVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmInterfaceCurrentMaxSvpcVpi.setStatus("current")


class _AtmInterfaceConfMaxSvccVpi_Type(Integer32):
    """Custom type atmInterfaceConfMaxSvccVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_AtmInterfaceConfMaxSvccVpi_Type.__name__ = "Integer32"
_AtmInterfaceConfMaxSvccVpi_Object = MibTableColumn
atmInterfaceConfMaxSvccVpi = _AtmInterfaceConfMaxSvccVpi_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 14, 1, 14),
    _AtmInterfaceConfMaxSvccVpi_Type()
)
atmInterfaceConfMaxSvccVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmInterfaceConfMaxSvccVpi.setStatus("current")


class _AtmInterfaceCurrentMaxSvccVpi_Type(Integer32):
    """Custom type atmInterfaceCurrentMaxSvccVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_AtmInterfaceCurrentMaxSvccVpi_Type.__name__ = "Integer32"
_AtmInterfaceCurrentMaxSvccVpi_Object = MibTableColumn
atmInterfaceCurrentMaxSvccVpi = _AtmInterfaceCurrentMaxSvccVpi_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 14, 1, 15),
    _AtmInterfaceCurrentMaxSvccVpi_Type()
)
atmInterfaceCurrentMaxSvccVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmInterfaceCurrentMaxSvccVpi.setStatus("current")


class _AtmInterfaceConfMinSvccVci_Type(Integer32):
    """Custom type atmInterfaceConfMinSvccVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AtmInterfaceConfMinSvccVci_Type.__name__ = "Integer32"
_AtmInterfaceConfMinSvccVci_Object = MibTableColumn
atmInterfaceConfMinSvccVci = _AtmInterfaceConfMinSvccVci_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 14, 1, 16),
    _AtmInterfaceConfMinSvccVci_Type()
)
atmInterfaceConfMinSvccVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmInterfaceConfMinSvccVci.setStatus("current")


class _AtmInterfaceCurrentMinSvccVci_Type(Integer32):
    """Custom type atmInterfaceCurrentMinSvccVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AtmInterfaceCurrentMinSvccVci_Type.__name__ = "Integer32"
_AtmInterfaceCurrentMinSvccVci_Object = MibTableColumn
atmInterfaceCurrentMinSvccVci = _AtmInterfaceCurrentMinSvccVci_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 14, 1, 17),
    _AtmInterfaceCurrentMinSvccVci_Type()
)
atmInterfaceCurrentMinSvccVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmInterfaceCurrentMinSvccVci.setStatus("current")
_AtmIntfSigVccRxTrafficDescrIndex_Type = AtmTrafficDescrParamIndex
_AtmIntfSigVccRxTrafficDescrIndex_Object = MibTableColumn
atmIntfSigVccRxTrafficDescrIndex = _AtmIntfSigVccRxTrafficDescrIndex_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 14, 1, 18),
    _AtmIntfSigVccRxTrafficDescrIndex_Type()
)
atmIntfSigVccRxTrafficDescrIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIntfSigVccRxTrafficDescrIndex.setStatus("current")
_AtmIntfSigVccTxTrafficDescrIndex_Type = AtmTrafficDescrParamIndex
_AtmIntfSigVccTxTrafficDescrIndex_Object = MibTableColumn
atmIntfSigVccTxTrafficDescrIndex = _AtmIntfSigVccTxTrafficDescrIndex_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 14, 1, 19),
    _AtmIntfSigVccTxTrafficDescrIndex_Type()
)
atmIntfSigVccTxTrafficDescrIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIntfSigVccTxTrafficDescrIndex.setStatus("current")
_AtmIntfPvcFailures_Type = Counter32
_AtmIntfPvcFailures_Object = MibTableColumn
atmIntfPvcFailures = _AtmIntfPvcFailures_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 14, 1, 20),
    _AtmIntfPvcFailures_Type()
)
atmIntfPvcFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIntfPvcFailures.setStatus("current")
_AtmIntfCurrentlyFailingPVpls_Type = Gauge32
_AtmIntfCurrentlyFailingPVpls_Object = MibTableColumn
atmIntfCurrentlyFailingPVpls = _AtmIntfCurrentlyFailingPVpls_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 14, 1, 21),
    _AtmIntfCurrentlyFailingPVpls_Type()
)
atmIntfCurrentlyFailingPVpls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIntfCurrentlyFailingPVpls.setStatus("current")
_AtmIntfCurrentlyFailingPVcls_Type = Gauge32
_AtmIntfCurrentlyFailingPVcls_Object = MibTableColumn
atmIntfCurrentlyFailingPVcls = _AtmIntfCurrentlyFailingPVcls_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 14, 1, 22),
    _AtmIntfCurrentlyFailingPVcls_Type()
)
atmIntfCurrentlyFailingPVcls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIntfCurrentlyFailingPVcls.setStatus("current")


class _AtmIntfPvcFailuresTrapEnable_Type(TruthValue):
    """Custom type atmIntfPvcFailuresTrapEnable based on TruthValue"""


_AtmIntfPvcFailuresTrapEnable_Object = MibTableColumn
atmIntfPvcFailuresTrapEnable = _AtmIntfPvcFailuresTrapEnable_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 14, 1, 23),
    _AtmIntfPvcFailuresTrapEnable_Type()
)
atmIntfPvcFailuresTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIntfPvcFailuresTrapEnable.setStatus("current")


class _AtmIntfPvcNotificationInterval_Type(Integer32):
    """Custom type atmIntfPvcNotificationInterval based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_AtmIntfPvcNotificationInterval_Type.__name__ = "Integer32"
_AtmIntfPvcNotificationInterval_Object = MibTableColumn
atmIntfPvcNotificationInterval = _AtmIntfPvcNotificationInterval_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 14, 1, 24),
    _AtmIntfPvcNotificationInterval_Type()
)
atmIntfPvcNotificationInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmIntfPvcNotificationInterval.setStatus("current")
if mibBuilder.loadTexts:
    atmIntfPvcNotificationInterval.setUnits("seconds")
_AtmIntfLeafSetupFailures_Type = Counter32
_AtmIntfLeafSetupFailures_Object = MibTableColumn
atmIntfLeafSetupFailures = _AtmIntfLeafSetupFailures_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 14, 1, 25),
    _AtmIntfLeafSetupFailures_Type()
)
atmIntfLeafSetupFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIntfLeafSetupFailures.setStatus("current")
_AtmIntfLeafSetupRequests_Type = Counter32
_AtmIntfLeafSetupRequests_Object = MibTableColumn
atmIntfLeafSetupRequests = _AtmIntfLeafSetupRequests_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 14, 1, 26),
    _AtmIntfLeafSetupRequests_Type()
)
atmIntfLeafSetupRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmIntfLeafSetupRequests.setStatus("current")
_AtmIlmiSrvcRegTable_Object = MibTable
atmIlmiSrvcRegTable = _AtmIlmiSrvcRegTable_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 15)
)
if mibBuilder.loadTexts:
    atmIlmiSrvcRegTable.setStatus("current")
_AtmIlmiSrvcRegEntry_Object = MibTableRow
atmIlmiSrvcRegEntry = _AtmIlmiSrvcRegEntry_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 15, 1)
)
atmIlmiSrvcRegEntry.setIndexNames(
    (0, "ATM2-MIB", "atmIlmiSrvcRegIndex"),
    (0, "ATM2-MIB", "atmIlmiSrvcRegServiceID"),
    (0, "ATM2-MIB", "atmIlmiSrvcRegAddressIndex"),
)
if mibBuilder.loadTexts:
    atmIlmiSrvcRegEntry.setStatus("current")
_AtmIlmiSrvcRegIndex_Type = InterfaceIndexOrZero
_AtmIlmiSrvcRegIndex_Object = MibTableColumn
atmIlmiSrvcRegIndex = _AtmIlmiSrvcRegIndex_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 15, 1, 1),
    _AtmIlmiSrvcRegIndex_Type()
)
atmIlmiSrvcRegIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmIlmiSrvcRegIndex.setStatus("current")
_AtmIlmiSrvcRegServiceID_Type = ObjectIdentifier
_AtmIlmiSrvcRegServiceID_Object = MibTableColumn
atmIlmiSrvcRegServiceID = _AtmIlmiSrvcRegServiceID_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 15, 1, 2),
    _AtmIlmiSrvcRegServiceID_Type()
)
atmIlmiSrvcRegServiceID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmIlmiSrvcRegServiceID.setStatus("current")


class _AtmIlmiSrvcRegAddressIndex_Type(Integer32):
    """Custom type atmIlmiSrvcRegAddressIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AtmIlmiSrvcRegAddressIndex_Type.__name__ = "Integer32"
_AtmIlmiSrvcRegAddressIndex_Object = MibTableColumn
atmIlmiSrvcRegAddressIndex = _AtmIlmiSrvcRegAddressIndex_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 15, 1, 3),
    _AtmIlmiSrvcRegAddressIndex_Type()
)
atmIlmiSrvcRegAddressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmIlmiSrvcRegAddressIndex.setStatus("current")
_AtmIlmiSrvcRegATMAddress_Type = AtmAddr
_AtmIlmiSrvcRegATMAddress_Object = MibTableColumn
atmIlmiSrvcRegATMAddress = _AtmIlmiSrvcRegATMAddress_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 15, 1, 4),
    _AtmIlmiSrvcRegATMAddress_Type()
)
atmIlmiSrvcRegATMAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmIlmiSrvcRegATMAddress.setStatus("current")


class _AtmIlmiSrvcRegParm1_Type(OctetString):
    """Custom type atmIlmiSrvcRegParm1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_AtmIlmiSrvcRegParm1_Type.__name__ = "OctetString"
_AtmIlmiSrvcRegParm1_Object = MibTableColumn
atmIlmiSrvcRegParm1 = _AtmIlmiSrvcRegParm1_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 15, 1, 5),
    _AtmIlmiSrvcRegParm1_Type()
)
atmIlmiSrvcRegParm1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmIlmiSrvcRegParm1.setStatus("current")
_AtmIlmiSrvcRegRowStatus_Type = RowStatus
_AtmIlmiSrvcRegRowStatus_Object = MibTableColumn
atmIlmiSrvcRegRowStatus = _AtmIlmiSrvcRegRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 15, 1, 6),
    _AtmIlmiSrvcRegRowStatus_Type()
)
atmIlmiSrvcRegRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmIlmiSrvcRegRowStatus.setStatus("current")
_AtmIlmiNetworkPrefixTable_Object = MibTable
atmIlmiNetworkPrefixTable = _AtmIlmiNetworkPrefixTable_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 16)
)
if mibBuilder.loadTexts:
    atmIlmiNetworkPrefixTable.setStatus("current")
_AtmIlmiNetworkPrefixEntry_Object = MibTableRow
atmIlmiNetworkPrefixEntry = _AtmIlmiNetworkPrefixEntry_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 16, 1)
)
atmIlmiNetworkPrefixEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ATM2-MIB", "atmIlmiNetPrefixPrefix"),
)
if mibBuilder.loadTexts:
    atmIlmiNetworkPrefixEntry.setStatus("current")
_AtmIlmiNetPrefixPrefix_Type = AtmIlmiNetworkPrefix
_AtmIlmiNetPrefixPrefix_Object = MibTableColumn
atmIlmiNetPrefixPrefix = _AtmIlmiNetPrefixPrefix_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 16, 1, 1),
    _AtmIlmiNetPrefixPrefix_Type()
)
atmIlmiNetPrefixPrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmIlmiNetPrefixPrefix.setStatus("current")
_AtmIlmiNetPrefixRowStatus_Type = RowStatus
_AtmIlmiNetPrefixRowStatus_Object = MibTableColumn
atmIlmiNetPrefixRowStatus = _AtmIlmiNetPrefixRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 16, 1, 2),
    _AtmIlmiNetPrefixRowStatus_Type()
)
atmIlmiNetPrefixRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmIlmiNetPrefixRowStatus.setStatus("current")
_AtmSwitchAddressTable_Object = MibTable
atmSwitchAddressTable = _AtmSwitchAddressTable_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 17)
)
if mibBuilder.loadTexts:
    atmSwitchAddressTable.setStatus("current")
_AtmSwitchAddressEntry_Object = MibTableRow
atmSwitchAddressEntry = _AtmSwitchAddressEntry_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 17, 1)
)
atmSwitchAddressEntry.setIndexNames(
    (0, "ATM2-MIB", "atmSwitchAddressIndex"),
)
if mibBuilder.loadTexts:
    atmSwitchAddressEntry.setStatus("current")


class _AtmSwitchAddressIndex_Type(Integer32):
    """Custom type atmSwitchAddressIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AtmSwitchAddressIndex_Type.__name__ = "Integer32"
_AtmSwitchAddressIndex_Object = MibTableColumn
atmSwitchAddressIndex = _AtmSwitchAddressIndex_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 17, 1, 1),
    _AtmSwitchAddressIndex_Type()
)
atmSwitchAddressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    atmSwitchAddressIndex.setStatus("current")


class _AtmSwitchAddressAddress_Type(OctetString):
    """Custom type atmSwitchAddressAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(13, 13),
        ValueSizeConstraint(20, 20),
    )


_AtmSwitchAddressAddress_Type.__name__ = "OctetString"
_AtmSwitchAddressAddress_Object = MibTableColumn
atmSwitchAddressAddress = _AtmSwitchAddressAddress_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 17, 1, 2),
    _AtmSwitchAddressAddress_Type()
)
atmSwitchAddressAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmSwitchAddressAddress.setStatus("current")
_AtmSwitchAddressRowStatus_Type = RowStatus
_AtmSwitchAddressRowStatus_Object = MibTableColumn
atmSwitchAddressRowStatus = _AtmSwitchAddressRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 17, 1, 3),
    _AtmSwitchAddressRowStatus_Type()
)
atmSwitchAddressRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmSwitchAddressRowStatus.setStatus("current")
_AtmVpCrossConnectXTable_Object = MibTable
atmVpCrossConnectXTable = _AtmVpCrossConnectXTable_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 18)
)
if mibBuilder.loadTexts:
    atmVpCrossConnectXTable.setStatus("current")
_AtmVpCrossConnectXEntry_Object = MibTableRow
atmVpCrossConnectXEntry = _AtmVpCrossConnectXEntry_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 18, 1)
)
if mibBuilder.loadTexts:
    atmVpCrossConnectXEntry.setStatus("current")


class _AtmVpCrossConnectUserName_Type(SnmpAdminString):
    """Custom type atmVpCrossConnectUserName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AtmVpCrossConnectUserName_Type.__name__ = "SnmpAdminString"
_AtmVpCrossConnectUserName_Object = MibTableColumn
atmVpCrossConnectUserName = _AtmVpCrossConnectUserName_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 18, 1, 1),
    _AtmVpCrossConnectUserName_Type()
)
atmVpCrossConnectUserName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmVpCrossConnectUserName.setStatus("current")


class _AtmVpCrossConnectProviderName_Type(SnmpAdminString):
    """Custom type atmVpCrossConnectProviderName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AtmVpCrossConnectProviderName_Type.__name__ = "SnmpAdminString"
_AtmVpCrossConnectProviderName_Object = MibTableColumn
atmVpCrossConnectProviderName = _AtmVpCrossConnectProviderName_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 18, 1, 2),
    _AtmVpCrossConnectProviderName_Type()
)
atmVpCrossConnectProviderName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVpCrossConnectProviderName.setStatus("current")
_AtmVcCrossConnectXTable_Object = MibTable
atmVcCrossConnectXTable = _AtmVcCrossConnectXTable_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 19)
)
if mibBuilder.loadTexts:
    atmVcCrossConnectXTable.setStatus("current")
_AtmVcCrossConnectXEntry_Object = MibTableRow
atmVcCrossConnectXEntry = _AtmVcCrossConnectXEntry_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 19, 1)
)
if mibBuilder.loadTexts:
    atmVcCrossConnectXEntry.setStatus("current")


class _AtmVcCrossConnectUserName_Type(SnmpAdminString):
    """Custom type atmVcCrossConnectUserName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AtmVcCrossConnectUserName_Type.__name__ = "SnmpAdminString"
_AtmVcCrossConnectUserName_Object = MibTableColumn
atmVcCrossConnectUserName = _AtmVcCrossConnectUserName_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 19, 1, 1),
    _AtmVcCrossConnectUserName_Type()
)
atmVcCrossConnectUserName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    atmVcCrossConnectUserName.setStatus("current")


class _AtmVcCrossConnectProviderName_Type(SnmpAdminString):
    """Custom type atmVcCrossConnectProviderName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AtmVcCrossConnectProviderName_Type.__name__ = "SnmpAdminString"
_AtmVcCrossConnectProviderName_Object = MibTableColumn
atmVcCrossConnectProviderName = _AtmVcCrossConnectProviderName_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 19, 1, 2),
    _AtmVcCrossConnectProviderName_Type()
)
atmVcCrossConnectProviderName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmVcCrossConnectProviderName.setStatus("current")
_AtmCurrentlyFailingPVplTable_Object = MibTable
atmCurrentlyFailingPVplTable = _AtmCurrentlyFailingPVplTable_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 20)
)
if mibBuilder.loadTexts:
    atmCurrentlyFailingPVplTable.setStatus("current")
_AtmCurrentlyFailingPVplEntry_Object = MibTableRow
atmCurrentlyFailingPVplEntry = _AtmCurrentlyFailingPVplEntry_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 20, 1)
)
atmCurrentlyFailingPVplEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ATM-MIB", "atmVplVpi"),
)
if mibBuilder.loadTexts:
    atmCurrentlyFailingPVplEntry.setStatus("current")
_AtmCurrentlyFailingPVplTimeStamp_Type = TimeStamp
_AtmCurrentlyFailingPVplTimeStamp_Object = MibTableColumn
atmCurrentlyFailingPVplTimeStamp = _AtmCurrentlyFailingPVplTimeStamp_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 20, 1, 1),
    _AtmCurrentlyFailingPVplTimeStamp_Type()
)
atmCurrentlyFailingPVplTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmCurrentlyFailingPVplTimeStamp.setStatus("current")
_AtmCurrentlyFailingPVclTable_Object = MibTable
atmCurrentlyFailingPVclTable = _AtmCurrentlyFailingPVclTable_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 21)
)
if mibBuilder.loadTexts:
    atmCurrentlyFailingPVclTable.setStatus("current")
_AtmCurrentlyFailingPVclEntry_Object = MibTableRow
atmCurrentlyFailingPVclEntry = _AtmCurrentlyFailingPVclEntry_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 21, 1)
)
atmCurrentlyFailingPVclEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ATM-MIB", "atmVclVpi"),
    (0, "ATM-MIB", "atmVclVci"),
)
if mibBuilder.loadTexts:
    atmCurrentlyFailingPVclEntry.setStatus("current")
_AtmCurrentlyFailingPVclTimeStamp_Type = TimeStamp
_AtmCurrentlyFailingPVclTimeStamp_Object = MibTableColumn
atmCurrentlyFailingPVclTimeStamp = _AtmCurrentlyFailingPVclTimeStamp_Object(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 1, 21, 1, 1),
    _AtmCurrentlyFailingPVclTimeStamp_Type()
)
atmCurrentlyFailingPVclTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmCurrentlyFailingPVclTimeStamp.setStatus("current")
_Atm2MIBTraps_ObjectIdentity = ObjectIdentity
atm2MIBTraps = _Atm2MIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 2)
)
_AtmPvcTraps_ObjectIdentity = ObjectIdentity
atmPvcTraps = _AtmPvcTraps_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 2, 1)
)
_AtmPvcTrapsPrefix_ObjectIdentity = ObjectIdentity
atmPvcTrapsPrefix = _AtmPvcTrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 2, 1, 0)
)
_Atm2MIBConformance_ObjectIdentity = ObjectIdentity
atm2MIBConformance = _Atm2MIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 3)
)
_Atm2MIBGroups_ObjectIdentity = ObjectIdentity
atm2MIBGroups = _Atm2MIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 3, 1)
)
_Atm2MIBCompliances_ObjectIdentity = ObjectIdentity
atm2MIBCompliances = _Atm2MIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 3, 2)
)
atmVplEntry.registerAugmentions(
    ("ATM2-MIB",
     "atmVplLogicalPortEntry")
)
atmVplLogicalPortEntry.setIndexNames(*atmVplEntry.getIndexNames())
atmVclEntry.registerAugmentions(
    ("ATM2-MIB",
     "atmVclGenEntry")
)
atmVclGenEntry.setIndexNames(*atmVclEntry.getIndexNames())
atmInterfaceConfEntry.registerAugmentions(
    ("ATM2-MIB",
     "atmInterfaceExtEntry")
)
atmInterfaceExtEntry.setIndexNames(*atmInterfaceConfEntry.getIndexNames())
atmVpCrossConnectEntry.registerAugmentions(
    ("ATM2-MIB",
     "atmVpCrossConnectXEntry")
)
atmVpCrossConnectXEntry.setIndexNames(*atmVpCrossConnectEntry.getIndexNames())
atmVcCrossConnectEntry.registerAugmentions(
    ("ATM2-MIB",
     "atmVcCrossConnectXEntry")
)
atmVcCrossConnectXEntry.setIndexNames(*atmVcCrossConnectEntry.getIndexNames())

# Managed Objects groups

atmCommonGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 3, 1, 1)
)
atmCommonGroup.setObjects(
      *(("ATM2-MIB", "atmSigSSCOPConEvents"),
        ("ATM2-MIB", "atmSigSSCOPErrdPdus"),
        ("ATM2-MIB", "atmSigDetectSetupAttempts"),
        ("ATM2-MIB", "atmSigEmitSetupAttempts"),
        ("ATM2-MIB", "atmSigDetectUnavailRoutes"),
        ("ATM2-MIB", "atmSigEmitUnavailRoutes"),
        ("ATM2-MIB", "atmSigDetectUnavailResrcs"),
        ("ATM2-MIB", "atmSigEmitUnavailResrcs"),
        ("ATM2-MIB", "atmSigDetectCldPtyEvents"),
        ("ATM2-MIB", "atmSigEmitCldPtyEvents"),
        ("ATM2-MIB", "atmSigDetectMsgErrors"),
        ("ATM2-MIB", "atmSigEmitMsgErrors"),
        ("ATM2-MIB", "atmSigDetectClgPtyEvents"),
        ("ATM2-MIB", "atmSigEmitClgPtyEvents"),
        ("ATM2-MIB", "atmSigDetectTimerExpireds"),
        ("ATM2-MIB", "atmSigEmitTimerExpireds"),
        ("ATM2-MIB", "atmSigDetectRestarts"),
        ("ATM2-MIB", "atmSigEmitRestarts"),
        ("ATM2-MIB", "atmSigInEstabls"),
        ("ATM2-MIB", "atmSigOutEstabls"),
        ("ATM2-MIB", "atmVplLogicalPortDef"),
        ("ATM2-MIB", "atmVplLogicalPortIndex"),
        ("ATM2-MIB", "atmInterfaceConfMaxSvpcVpi"),
        ("ATM2-MIB", "atmInterfaceCurrentMaxSvpcVpi"),
        ("ATM2-MIB", "atmInterfaceConfMaxSvccVpi"),
        ("ATM2-MIB", "atmInterfaceCurrentMaxSvccVpi"),
        ("ATM2-MIB", "atmInterfaceConfMinSvccVci"),
        ("ATM2-MIB", "atmInterfaceCurrentMinSvccVci"),
        ("ATM2-MIB", "atmIntfSigVccRxTrafficDescrIndex"),
        ("ATM2-MIB", "atmIntfSigVccTxTrafficDescrIndex"),
        ("ATM2-MIB", "atmIntfPvcFailures"),
        ("ATM2-MIB", "atmIntfCurrentlyFailingPVpls"),
        ("ATM2-MIB", "atmIntfCurrentlyFailingPVcls"),
        ("ATM2-MIB", "atmIntfPvcNotificationInterval"),
        ("ATM2-MIB", "atmIntfPvcFailuresTrapEnable"),
        ("ATM2-MIB", "atmIntfLeafSetupFailures"),
        ("ATM2-MIB", "atmIntfLeafSetupRequests"),
        ("ATM2-MIB", "atmIntfConfigType"),
        ("ATM2-MIB", "atmIntfActualType"),
        ("ATM2-MIB", "atmIntfConfigSide"),
        ("ATM2-MIB", "atmIntfActualSide"),
        ("ATM2-MIB", "atmIntfIlmiAdminStatus"),
        ("ATM2-MIB", "atmIntfIlmiOperStatus"),
        ("ATM2-MIB", "atmIntfIlmiFsmState"),
        ("ATM2-MIB", "atmIntfIlmiEstablishConPollIntvl"),
        ("ATM2-MIB", "atmIntfIlmiCheckConPollIntvl"),
        ("ATM2-MIB", "atmIntfIlmiConPollInactFactor"),
        ("ATM2-MIB", "atmIntfIlmiPublicPrivateIndctr"),
        ("ATM2-MIB", "atmCurrentlyFailingPVplTimeStamp"),
        ("ATM2-MIB", "atmCurrentlyFailingPVclTimeStamp"))
)
if mibBuilder.loadTexts:
    atmCommonGroup.setStatus("current")

atmCommonStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 3, 1, 2)
)
atmCommonStatsGroup.setObjects(
      *(("ATM2-MIB", "atmVclStatTotalCellIns"),
        ("ATM2-MIB", "atmVclStatClp0CellIns"),
        ("ATM2-MIB", "atmVclStatTotalDiscards"),
        ("ATM2-MIB", "atmVclStatClp0Discards"),
        ("ATM2-MIB", "atmVclStatTotalCellOuts"),
        ("ATM2-MIB", "atmVclStatClp0CellOuts"),
        ("ATM2-MIB", "atmVclStatClp0Tagged"),
        ("ATM2-MIB", "atmVplStatTotalCellIns"),
        ("ATM2-MIB", "atmVplStatClp0CellIns"),
        ("ATM2-MIB", "atmVplStatTotalDiscards"),
        ("ATM2-MIB", "atmVplStatClp0Discards"),
        ("ATM2-MIB", "atmVplStatTotalCellOuts"),
        ("ATM2-MIB", "atmVplStatClp0CellOuts"),
        ("ATM2-MIB", "atmVplStatClp0Tagged"))
)
if mibBuilder.loadTexts:
    atmCommonStatsGroup.setStatus("current")

atmSwitchServcGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 3, 1, 3)
)
atmSwitchServcGroup.setObjects(
      *(("ATM2-MIB", "atmIlmiSrvcRegATMAddress"),
        ("ATM2-MIB", "atmIlmiSrvcRegParm1"),
        ("ATM2-MIB", "atmIlmiSrvcRegRowStatus"),
        ("ATM2-MIB", "atmIlmiNetPrefixRowStatus"),
        ("ATM2-MIB", "atmSvcVpCrossConnectCreationTime"),
        ("ATM2-MIB", "atmSvcVpCrossConnectRowStatus"),
        ("ATM2-MIB", "atmSvcVcCrossConnectCreationTime"),
        ("ATM2-MIB", "atmSvcVcCrossConnectRowStatus"),
        ("ATM2-MIB", "atmIfRegAddrAddressSource"),
        ("ATM2-MIB", "atmIfRegAddrOrgScope"),
        ("ATM2-MIB", "atmIfRegAddrRowStatus"))
)
if mibBuilder.loadTexts:
    atmSwitchServcGroup.setStatus("current")

atmSwitchServcSigGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 3, 1, 4)
)
atmSwitchServcSigGroup.setObjects(
      *(("ATM2-MIB", "atmSigSupportClgPtyNumDel"),
        ("ATM2-MIB", "atmSigSupportClgPtySubAddr"),
        ("ATM2-MIB", "atmSigSupportCldPtySubAddr"),
        ("ATM2-MIB", "atmSigSupportHiLyrInfo"),
        ("ATM2-MIB", "atmSigSupportLoLyrInfo"),
        ("ATM2-MIB", "atmSigSupportBlliRepeatInd"),
        ("ATM2-MIB", "atmSigSupportAALInfo"),
        ("ATM2-MIB", "atmSigSupportPrefCarrier"))
)
if mibBuilder.loadTexts:
    atmSwitchServcSigGroup.setStatus("current")

atmSwitchGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 3, 1, 6)
)
atmSwitchGroup.setObjects(
      *(("ATM2-MIB", "atmSwitchAddressAddress"),
        ("ATM2-MIB", "atmSwitchAddressRowStatus"))
)
if mibBuilder.loadTexts:
    atmSwitchGroup.setStatus("current")

atmServcGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 3, 1, 7)
)
atmServcGroup.setObjects(
      *(("ATM2-MIB", "atmVpCrossConnectUserName"),
        ("ATM2-MIB", "atmVpCrossConnectProviderName"),
        ("ATM2-MIB", "atmVcCrossConnectUserName"),
        ("ATM2-MIB", "atmVcCrossConnectProviderName"))
)
if mibBuilder.loadTexts:
    atmServcGroup.setStatus("current")

atmHostGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 3, 1, 8)
)
atmHostGroup.setObjects(
      *(("ATM2-MIB", "atmAal5VclInPkts"),
        ("ATM2-MIB", "atmAal5VclOutPkts"),
        ("ATM2-MIB", "atmAal5VclInOctets"),
        ("ATM2-MIB", "atmAal5VclOutOctets"),
        ("ATM2-MIB", "atmVclAddrType"),
        ("ATM2-MIB", "atmVclAddrRowStatus"),
        ("ATM2-MIB", "atmAddrVclAddrType"),
        ("ATM2-MIB", "atmVclGenSigDescrIndex"))
)
if mibBuilder.loadTexts:
    atmHostGroup.setStatus("current")

atmHostSigDescrGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 3, 1, 9)
)
atmHostSigDescrGroup.setObjects(
      *(("ATM2-MIB", "atmSigDescrParamAalType"),
        ("ATM2-MIB", "atmSigDescrParamAalSscsType"),
        ("ATM2-MIB", "atmSigDescrParamBhliType"),
        ("ATM2-MIB", "atmSigDescrParamBhliInfo"),
        ("ATM2-MIB", "atmSigDescrParamBbcConnConf"),
        ("ATM2-MIB", "atmSigDescrParamBlliLayer2"),
        ("ATM2-MIB", "atmSigDescrParamBlliLayer3"),
        ("ATM2-MIB", "atmSigDescrParamBlliPktSize"),
        ("ATM2-MIB", "atmSigDescrParamBlliSnapId"),
        ("ATM2-MIB", "atmSigDescrParamBlliOuiPid"),
        ("ATM2-MIB", "atmSigDescrParamRowStatus"))
)
if mibBuilder.loadTexts:
    atmHostSigDescrGroup.setStatus("current")


# Notification objects

atmIntfPvcFailuresTrap = NotificationType(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 2, 1, 0, 1)
)
atmIntfPvcFailuresTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ATM2-MIB", "atmIntfPvcFailures"),
        ("ATM2-MIB", "atmIntfCurrentlyFailingPVpls"),
        ("ATM2-MIB", "atmIntfCurrentlyFailingPVcls"))
)
if mibBuilder.loadTexts:
    atmIntfPvcFailuresTrap.setStatus(
        "current"
    )


# Notifications groups

atmSwitchServcNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 3, 1, 5)
)
atmSwitchServcNotifGroup.setObjects(
    ("ATM2-MIB", "atmIntfPvcFailuresTrap")
)
if mibBuilder.loadTexts:
    atmSwitchServcNotifGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

atm2MIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 37, 1, 14, 3, 2, 1)
)
if mibBuilder.loadTexts:
    atm2MIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ATM2-MIB",
    **{"atm2MIB": atm2MIB,
       "atm2MIBObjects": atm2MIBObjects,
       "atmSvcVpCrossConnectTable": atmSvcVpCrossConnectTable,
       "atmSvcVpCrossConnectEntry": atmSvcVpCrossConnectEntry,
       "atmSvcVpCrossConnectIndex": atmSvcVpCrossConnectIndex,
       "atmSvcVpCrossConnectLowIfIndex": atmSvcVpCrossConnectLowIfIndex,
       "atmSvcVpCrossConnectLowVpi": atmSvcVpCrossConnectLowVpi,
       "atmSvcVpCrossConnectHighIfIndex": atmSvcVpCrossConnectHighIfIndex,
       "atmSvcVpCrossConnectHighVpi": atmSvcVpCrossConnectHighVpi,
       "atmSvcVpCrossConnectCreationTime": atmSvcVpCrossConnectCreationTime,
       "atmSvcVpCrossConnectRowStatus": atmSvcVpCrossConnectRowStatus,
       "atmSvcVcCrossConnectTable": atmSvcVcCrossConnectTable,
       "atmSvcVcCrossConnectEntry": atmSvcVcCrossConnectEntry,
       "atmSvcVcCrossConnectIndex": atmSvcVcCrossConnectIndex,
       "atmSvcVcCrossConnectLowIfIndex": atmSvcVcCrossConnectLowIfIndex,
       "atmSvcVcCrossConnectLowVpi": atmSvcVcCrossConnectLowVpi,
       "atmSvcVcCrossConnectLowVci": atmSvcVcCrossConnectLowVci,
       "atmSvcVcCrossConnectHighIfIndex": atmSvcVcCrossConnectHighIfIndex,
       "atmSvcVcCrossConnectHighVpi": atmSvcVcCrossConnectHighVpi,
       "atmSvcVcCrossConnectHighVci": atmSvcVcCrossConnectHighVci,
       "atmSvcVcCrossConnectCreationTime": atmSvcVcCrossConnectCreationTime,
       "atmSvcVcCrossConnectRowStatus": atmSvcVcCrossConnectRowStatus,
       "atmSigStatTable": atmSigStatTable,
       "atmSigStatEntry": atmSigStatEntry,
       "atmSigSSCOPConEvents": atmSigSSCOPConEvents,
       "atmSigSSCOPErrdPdus": atmSigSSCOPErrdPdus,
       "atmSigDetectSetupAttempts": atmSigDetectSetupAttempts,
       "atmSigEmitSetupAttempts": atmSigEmitSetupAttempts,
       "atmSigDetectUnavailRoutes": atmSigDetectUnavailRoutes,
       "atmSigEmitUnavailRoutes": atmSigEmitUnavailRoutes,
       "atmSigDetectUnavailResrcs": atmSigDetectUnavailResrcs,
       "atmSigEmitUnavailResrcs": atmSigEmitUnavailResrcs,
       "atmSigDetectCldPtyEvents": atmSigDetectCldPtyEvents,
       "atmSigEmitCldPtyEvents": atmSigEmitCldPtyEvents,
       "atmSigDetectMsgErrors": atmSigDetectMsgErrors,
       "atmSigEmitMsgErrors": atmSigEmitMsgErrors,
       "atmSigDetectClgPtyEvents": atmSigDetectClgPtyEvents,
       "atmSigEmitClgPtyEvents": atmSigEmitClgPtyEvents,
       "atmSigDetectTimerExpireds": atmSigDetectTimerExpireds,
       "atmSigEmitTimerExpireds": atmSigEmitTimerExpireds,
       "atmSigDetectRestarts": atmSigDetectRestarts,
       "atmSigEmitRestarts": atmSigEmitRestarts,
       "atmSigInEstabls": atmSigInEstabls,
       "atmSigOutEstabls": atmSigOutEstabls,
       "atmSigSupportTable": atmSigSupportTable,
       "atmSigSupportEntry": atmSigSupportEntry,
       "atmSigSupportClgPtyNumDel": atmSigSupportClgPtyNumDel,
       "atmSigSupportClgPtySubAddr": atmSigSupportClgPtySubAddr,
       "atmSigSupportCldPtySubAddr": atmSigSupportCldPtySubAddr,
       "atmSigSupportHiLyrInfo": atmSigSupportHiLyrInfo,
       "atmSigSupportLoLyrInfo": atmSigSupportLoLyrInfo,
       "atmSigSupportBlliRepeatInd": atmSigSupportBlliRepeatInd,
       "atmSigSupportAALInfo": atmSigSupportAALInfo,
       "atmSigSupportPrefCarrier": atmSigSupportPrefCarrier,
       "atmSigDescrParamTable": atmSigDescrParamTable,
       "atmSigDescrParamEntry": atmSigDescrParamEntry,
       "atmSigDescrParamIndex": atmSigDescrParamIndex,
       "atmSigDescrParamAalType": atmSigDescrParamAalType,
       "atmSigDescrParamAalSscsType": atmSigDescrParamAalSscsType,
       "atmSigDescrParamBhliType": atmSigDescrParamBhliType,
       "atmSigDescrParamBhliInfo": atmSigDescrParamBhliInfo,
       "atmSigDescrParamBbcConnConf": atmSigDescrParamBbcConnConf,
       "atmSigDescrParamBlliLayer2": atmSigDescrParamBlliLayer2,
       "atmSigDescrParamBlliLayer3": atmSigDescrParamBlliLayer3,
       "atmSigDescrParamBlliPktSize": atmSigDescrParamBlliPktSize,
       "atmSigDescrParamBlliSnapId": atmSigDescrParamBlliSnapId,
       "atmSigDescrParamBlliOuiPid": atmSigDescrParamBlliOuiPid,
       "atmSigDescrParamRowStatus": atmSigDescrParamRowStatus,
       "atmIfRegisteredAddrTable": atmIfRegisteredAddrTable,
       "atmIfRegisteredAddrEntry": atmIfRegisteredAddrEntry,
       "atmIfRegAddrAddress": atmIfRegAddrAddress,
       "atmIfRegAddrAddressSource": atmIfRegAddrAddressSource,
       "atmIfRegAddrOrgScope": atmIfRegAddrOrgScope,
       "atmIfRegAddrRowStatus": atmIfRegAddrRowStatus,
       "atmVclAddrTable": atmVclAddrTable,
       "atmVclAddrEntry": atmVclAddrEntry,
       "atmVclAddrAddr": atmVclAddrAddr,
       "atmVclAddrType": atmVclAddrType,
       "atmVclAddrRowStatus": atmVclAddrRowStatus,
       "atmAddrVclTable": atmAddrVclTable,
       "atmAddrVclEntry": atmAddrVclEntry,
       "atmAddrVclAtmIfIndex": atmAddrVclAtmIfIndex,
       "atmAddrVclVpi": atmAddrVclVpi,
       "atmAddrVclVci": atmAddrVclVci,
       "atmAddrVclAddrType": atmAddrVclAddrType,
       "atmVplStatTable": atmVplStatTable,
       "atmVplStatEntry": atmVplStatEntry,
       "atmVplStatTotalCellIns": atmVplStatTotalCellIns,
       "atmVplStatClp0CellIns": atmVplStatClp0CellIns,
       "atmVplStatTotalDiscards": atmVplStatTotalDiscards,
       "atmVplStatClp0Discards": atmVplStatClp0Discards,
       "atmVplStatTotalCellOuts": atmVplStatTotalCellOuts,
       "atmVplStatClp0CellOuts": atmVplStatClp0CellOuts,
       "atmVplStatClp0Tagged": atmVplStatClp0Tagged,
       "atmVplLogicalPortTable": atmVplLogicalPortTable,
       "atmVplLogicalPortEntry": atmVplLogicalPortEntry,
       "atmVplLogicalPortDef": atmVplLogicalPortDef,
       "atmVplLogicalPortIndex": atmVplLogicalPortIndex,
       "atmVclStatTable": atmVclStatTable,
       "atmVclStatEntry": atmVclStatEntry,
       "atmVclStatTotalCellIns": atmVclStatTotalCellIns,
       "atmVclStatClp0CellIns": atmVclStatClp0CellIns,
       "atmVclStatTotalDiscards": atmVclStatTotalDiscards,
       "atmVclStatClp0Discards": atmVclStatClp0Discards,
       "atmVclStatTotalCellOuts": atmVclStatTotalCellOuts,
       "atmVclStatClp0CellOuts": atmVclStatClp0CellOuts,
       "atmVclStatClp0Tagged": atmVclStatClp0Tagged,
       "atmAal5VclStatTable": atmAal5VclStatTable,
       "atmAal5VclStatEntry": atmAal5VclStatEntry,
       "atmAal5VclInPkts": atmAal5VclInPkts,
       "atmAal5VclOutPkts": atmAal5VclOutPkts,
       "atmAal5VclInOctets": atmAal5VclInOctets,
       "atmAal5VclOutOctets": atmAal5VclOutOctets,
       "atmVclGenTable": atmVclGenTable,
       "atmVclGenEntry": atmVclGenEntry,
       "atmVclGenSigDescrIndex": atmVclGenSigDescrIndex,
       "atmInterfaceExtTable": atmInterfaceExtTable,
       "atmInterfaceExtEntry": atmInterfaceExtEntry,
       "atmIntfConfigType": atmIntfConfigType,
       "atmIntfActualType": atmIntfActualType,
       "atmIntfConfigSide": atmIntfConfigSide,
       "atmIntfActualSide": atmIntfActualSide,
       "atmIntfIlmiAdminStatus": atmIntfIlmiAdminStatus,
       "atmIntfIlmiOperStatus": atmIntfIlmiOperStatus,
       "atmIntfIlmiFsmState": atmIntfIlmiFsmState,
       "atmIntfIlmiEstablishConPollIntvl": atmIntfIlmiEstablishConPollIntvl,
       "atmIntfIlmiCheckConPollIntvl": atmIntfIlmiCheckConPollIntvl,
       "atmIntfIlmiConPollInactFactor": atmIntfIlmiConPollInactFactor,
       "atmIntfIlmiPublicPrivateIndctr": atmIntfIlmiPublicPrivateIndctr,
       "atmInterfaceConfMaxSvpcVpi": atmInterfaceConfMaxSvpcVpi,
       "atmInterfaceCurrentMaxSvpcVpi": atmInterfaceCurrentMaxSvpcVpi,
       "atmInterfaceConfMaxSvccVpi": atmInterfaceConfMaxSvccVpi,
       "atmInterfaceCurrentMaxSvccVpi": atmInterfaceCurrentMaxSvccVpi,
       "atmInterfaceConfMinSvccVci": atmInterfaceConfMinSvccVci,
       "atmInterfaceCurrentMinSvccVci": atmInterfaceCurrentMinSvccVci,
       "atmIntfSigVccRxTrafficDescrIndex": atmIntfSigVccRxTrafficDescrIndex,
       "atmIntfSigVccTxTrafficDescrIndex": atmIntfSigVccTxTrafficDescrIndex,
       "atmIntfPvcFailures": atmIntfPvcFailures,
       "atmIntfCurrentlyFailingPVpls": atmIntfCurrentlyFailingPVpls,
       "atmIntfCurrentlyFailingPVcls": atmIntfCurrentlyFailingPVcls,
       "atmIntfPvcFailuresTrapEnable": atmIntfPvcFailuresTrapEnable,
       "atmIntfPvcNotificationInterval": atmIntfPvcNotificationInterval,
       "atmIntfLeafSetupFailures": atmIntfLeafSetupFailures,
       "atmIntfLeafSetupRequests": atmIntfLeafSetupRequests,
       "atmIlmiSrvcRegTable": atmIlmiSrvcRegTable,
       "atmIlmiSrvcRegEntry": atmIlmiSrvcRegEntry,
       "atmIlmiSrvcRegIndex": atmIlmiSrvcRegIndex,
       "atmIlmiSrvcRegServiceID": atmIlmiSrvcRegServiceID,
       "atmIlmiSrvcRegAddressIndex": atmIlmiSrvcRegAddressIndex,
       "atmIlmiSrvcRegATMAddress": atmIlmiSrvcRegATMAddress,
       "atmIlmiSrvcRegParm1": atmIlmiSrvcRegParm1,
       "atmIlmiSrvcRegRowStatus": atmIlmiSrvcRegRowStatus,
       "atmIlmiNetworkPrefixTable": atmIlmiNetworkPrefixTable,
       "atmIlmiNetworkPrefixEntry": atmIlmiNetworkPrefixEntry,
       "atmIlmiNetPrefixPrefix": atmIlmiNetPrefixPrefix,
       "atmIlmiNetPrefixRowStatus": atmIlmiNetPrefixRowStatus,
       "atmSwitchAddressTable": atmSwitchAddressTable,
       "atmSwitchAddressEntry": atmSwitchAddressEntry,
       "atmSwitchAddressIndex": atmSwitchAddressIndex,
       "atmSwitchAddressAddress": atmSwitchAddressAddress,
       "atmSwitchAddressRowStatus": atmSwitchAddressRowStatus,
       "atmVpCrossConnectXTable": atmVpCrossConnectXTable,
       "atmVpCrossConnectXEntry": atmVpCrossConnectXEntry,
       "atmVpCrossConnectUserName": atmVpCrossConnectUserName,
       "atmVpCrossConnectProviderName": atmVpCrossConnectProviderName,
       "atmVcCrossConnectXTable": atmVcCrossConnectXTable,
       "atmVcCrossConnectXEntry": atmVcCrossConnectXEntry,
       "atmVcCrossConnectUserName": atmVcCrossConnectUserName,
       "atmVcCrossConnectProviderName": atmVcCrossConnectProviderName,
       "atmCurrentlyFailingPVplTable": atmCurrentlyFailingPVplTable,
       "atmCurrentlyFailingPVplEntry": atmCurrentlyFailingPVplEntry,
       "atmCurrentlyFailingPVplTimeStamp": atmCurrentlyFailingPVplTimeStamp,
       "atmCurrentlyFailingPVclTable": atmCurrentlyFailingPVclTable,
       "atmCurrentlyFailingPVclEntry": atmCurrentlyFailingPVclEntry,
       "atmCurrentlyFailingPVclTimeStamp": atmCurrentlyFailingPVclTimeStamp,
       "atm2MIBTraps": atm2MIBTraps,
       "atmPvcTraps": atmPvcTraps,
       "atmPvcTrapsPrefix": atmPvcTrapsPrefix,
       "atmIntfPvcFailuresTrap": atmIntfPvcFailuresTrap,
       "atm2MIBConformance": atm2MIBConformance,
       "atm2MIBGroups": atm2MIBGroups,
       "atmCommonGroup": atmCommonGroup,
       "atmCommonStatsGroup": atmCommonStatsGroup,
       "atmSwitchServcGroup": atmSwitchServcGroup,
       "atmSwitchServcSigGroup": atmSwitchServcSigGroup,
       "atmSwitchServcNotifGroup": atmSwitchServcNotifGroup,
       "atmSwitchGroup": atmSwitchGroup,
       "atmServcGroup": atmServcGroup,
       "atmHostGroup": atmHostGroup,
       "atmHostSigDescrGroup": atmHostSigDescrGroup,
       "atm2MIBCompliances": atm2MIBCompliances,
       "atm2MIBCompliance": atm2MIBCompliance}
)
