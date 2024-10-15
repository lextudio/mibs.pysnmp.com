# SNMP MIB module (IBM-LAN-EMULATION-EXTENSION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IBM-LAN-EMULATION-EXTENSION-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:07:34 2024
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

(BridgeId,
 Timeout) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "BridgeId",
    "Timeout")

(IfIndexOrZero,) = mibBuilder.importSymbols(
    "LAN-EMULATION-ELAN-MIB",
    "IfIndexOrZero")

(lesConfEntry,) = mibBuilder.importSymbols(
    "LAN-EMULATION-LES-MIB",
    "lesConfEntry")

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
 MacAddress,
 RowStatus,
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY


# Types definitions



class IbmSEBridgeID(Integer32):
    """Custom type IbmSEBridgeID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )





class IbmVlanPortMap(OctetString):
    """Custom type IbmVlanPortMap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )





class IbmVlanIndex(Integer32):
    """Custom type IbmVlanIndex based on Integer32"""




class IbmVlanType(Integer32):
    """Custom type IbmVlanType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("byPort", 6),
          ("ip", 1),
          ("ipMulticast", 7),
          ("ipx", 2),
          ("mac", 5),
          ("netbios", 3),
          ("userDefSldWindo", 4))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ibm_ObjectIdentity = ObjectIdentity
ibm = _Ibm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2)
)
_IbmArchitecture_ObjectIdentity = ObjectIdentity
ibmArchitecture = _IbmArchitecture_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 5)
)
_LanEmulation_ObjectIdentity = ObjectIdentity
lanEmulation = _LanEmulation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 5, 8)
)
_IbmLeServerX_ObjectIdentity = ObjectIdentity
ibmLeServerX = _IbmLeServerX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 3)
)
_IbmLeServerXMonitoring_ObjectIdentity = ObjectIdentity
ibmLeServerXMonitoring = _IbmLeServerXMonitoring_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 3, 1)
)
_IbmLeServerXMon_ObjectIdentity = ObjectIdentity
ibmLeServerXMon = _IbmLeServerXMon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 3, 1, 1)
)
_IbmLeServerXMonLecsInstances_Type = Gauge32
_IbmLeServerXMonLecsInstances_Object = MibScalar
ibmLeServerXMonLecsInstances = _IbmLeServerXMonLecsInstances_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 3, 1, 1, 1),
    _IbmLeServerXMonLecsInstances_Type()
)
ibmLeServerXMonLecsInstances.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmLeServerXMonLecsInstances.setStatus("mandatory")
_IbmLeServerXMonLesInstances_Type = Gauge32
_IbmLeServerXMonLesInstances_Object = MibScalar
ibmLeServerXMonLesInstances = _IbmLeServerXMonLesInstances_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 3, 1, 1, 2),
    _IbmLeServerXMonLesInstances_Type()
)
ibmLeServerXMonLesInstances.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmLeServerXMonLesInstances.setStatus("mandatory")
_IbmLeServerXMonBusInstances_Type = Gauge32
_IbmLeServerXMonBusInstances_Object = MibScalar
ibmLeServerXMonBusInstances = _IbmLeServerXMonBusInstances_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 3, 1, 1, 3),
    _IbmLeServerXMonBusInstances_Type()
)
ibmLeServerXMonBusInstances.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmLeServerXMonBusInstances.setStatus("mandatory")
_IbmLeServerXLecsMonTable_Object = MibTable
ibmLeServerXLecsMonTable = _IbmLeServerXLecsMonTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 3, 1, 2)
)
if mibBuilder.loadTexts:
    ibmLeServerXLecsMonTable.setStatus("mandatory")
_IbmLeServerXLecsMonEntry_Object = MibTableRow
ibmLeServerXLecsMonEntry = _IbmLeServerXLecsMonEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 3, 1, 2, 1)
)
ibmLeServerXLecsMonEntry.setIndexNames(
    (0, "IBM-LAN-EMULATION-EXTENSION-MIB", "ibmLeServerXLecsMonIndex"),
)
if mibBuilder.loadTexts:
    ibmLeServerXLecsMonEntry.setStatus("mandatory")


class _IbmLeServerXLecsMonIndex_Type(Integer32):
    """Custom type ibmLeServerXLecsMonIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 214748364),
    )


_IbmLeServerXLecsMonIndex_Type.__name__ = "Integer32"
_IbmLeServerXLecsMonIndex_Object = MibTableColumn
ibmLeServerXLecsMonIndex = _IbmLeServerXLecsMonIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 3, 1, 2, 1, 1),
    _IbmLeServerXLecsMonIndex_Type()
)
ibmLeServerXLecsMonIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ibmLeServerXLecsMonIndex.setStatus("mandatory")
_IbmLeServerXLecsUsedConnections_Type = Gauge32
_IbmLeServerXLecsUsedConnections_Object = MibTableColumn
ibmLeServerXLecsUsedConnections = _IbmLeServerXLecsUsedConnections_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 3, 1, 2, 1, 2),
    _IbmLeServerXLecsUsedConnections_Type()
)
ibmLeServerXLecsUsedConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmLeServerXLecsUsedConnections.setStatus("mandatory")
_IbmLeServerXLesMonTable_Object = MibTable
ibmLeServerXLesMonTable = _IbmLeServerXLesMonTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 3, 1, 3)
)
if mibBuilder.loadTexts:
    ibmLeServerXLesMonTable.setStatus("mandatory")
_IbmLeServerXLesMonEntry_Object = MibTableRow
ibmLeServerXLesMonEntry = _IbmLeServerXLesMonEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 3, 1, 3, 1)
)
ibmLeServerXLesMonEntry.setIndexNames(
    (0, "IBM-LAN-EMULATION-EXTENSION-MIB", "ibmLeServerXLesMonIndex"),
)
if mibBuilder.loadTexts:
    ibmLeServerXLesMonEntry.setStatus("mandatory")


class _IbmLeServerXLesMonIndex_Type(Integer32):
    """Custom type ibmLeServerXLesMonIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 214748364),
    )


_IbmLeServerXLesMonIndex_Type.__name__ = "Integer32"
_IbmLeServerXLesMonIndex_Object = MibTableColumn
ibmLeServerXLesMonIndex = _IbmLeServerXLesMonIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 3, 1, 3, 1, 1),
    _IbmLeServerXLesMonIndex_Type()
)
ibmLeServerXLesMonIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ibmLeServerXLesMonIndex.setStatus("mandatory")
_IbmLeServerXLesMonUsedConnections_Type = Gauge32
_IbmLeServerXLesMonUsedConnections_Object = MibTableColumn
ibmLeServerXLesMonUsedConnections = _IbmLeServerXLesMonUsedConnections_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 3, 1, 3, 1, 2),
    _IbmLeServerXLesMonUsedConnections_Type()
)
ibmLeServerXLesMonUsedConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmLeServerXLesMonUsedConnections.setStatus("mandatory")
_IbmLeServerXLesMonLesLecInstances_Type = Gauge32
_IbmLeServerXLesMonLesLecInstances_Object = MibTableColumn
ibmLeServerXLesMonLesLecInstances = _IbmLeServerXLesMonLesLecInstances_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 3, 1, 3, 1, 3),
    _IbmLeServerXLesMonLesLecInstances_Type()
)
ibmLeServerXLesMonLesLecInstances.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmLeServerXLesMonLesLecInstances.setStatus("mandatory")
_IbmLeServerXBusMonTable_Object = MibTable
ibmLeServerXBusMonTable = _IbmLeServerXBusMonTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 3, 1, 4)
)
if mibBuilder.loadTexts:
    ibmLeServerXBusMonTable.setStatus("mandatory")
_IbmLeServerXBusMonEntry_Object = MibTableRow
ibmLeServerXBusMonEntry = _IbmLeServerXBusMonEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 3, 1, 4, 1)
)
ibmLeServerXBusMonEntry.setIndexNames(
    (0, "IBM-LAN-EMULATION-EXTENSION-MIB", "ibmLeServerXBusMonIndex"),
)
if mibBuilder.loadTexts:
    ibmLeServerXBusMonEntry.setStatus("mandatory")


class _IbmLeServerXBusMonIndex_Type(Integer32):
    """Custom type ibmLeServerXBusMonIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 214748364),
    )


_IbmLeServerXBusMonIndex_Type.__name__ = "Integer32"
_IbmLeServerXBusMonIndex_Object = MibTableColumn
ibmLeServerXBusMonIndex = _IbmLeServerXBusMonIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 3, 1, 4, 1, 1),
    _IbmLeServerXBusMonIndex_Type()
)
ibmLeServerXBusMonIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ibmLeServerXBusMonIndex.setStatus("mandatory")
_IbmLeServerXBusMonUsedConnections_Type = Gauge32
_IbmLeServerXBusMonUsedConnections_Object = MibTableColumn
ibmLeServerXBusMonUsedConnections = _IbmLeServerXBusMonUsedConnections_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 3, 1, 4, 1, 2),
    _IbmLeServerXBusMonUsedConnections_Type()
)
ibmLeServerXBusMonUsedConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmLeServerXBusMonUsedConnections.setStatus("mandatory")
_IbmLeServerXBusMonBusLecInstances_Type = Gauge32
_IbmLeServerXBusMonBusLecInstances_Object = MibTableColumn
ibmLeServerXBusMonBusLecInstances = _IbmLeServerXBusMonBusLecInstances_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 3, 1, 4, 1, 3),
    _IbmLeServerXBusMonBusLecInstances_Type()
)
ibmLeServerXBusMonBusLecInstances.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmLeServerXBusMonBusLecInstances.setStatus("mandatory")
_IbmLeServerXConfig_ObjectIdentity = ObjectIdentity
ibmLeServerXConfig = _IbmLeServerXConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 3, 2)
)
_IbmLeServerXLesConfigTable_Object = MibTable
ibmLeServerXLesConfigTable = _IbmLeServerXLesConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 3, 2, 1)
)
if mibBuilder.loadTexts:
    ibmLeServerXLesConfigTable.setStatus("mandatory")
_IbmLeServerXLesConfigEntry_Object = MibTableRow
ibmLeServerXLesConfigEntry = _IbmLeServerXLesConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 3, 2, 1, 1)
)
ibmLeServerXLesConfigEntry.setIndexNames(
    (0, "IBM-LAN-EMULATION-EXTENSION-MIB", "lesConfIndex"),
)
if mibBuilder.loadTexts:
    ibmLeServerXLesConfigEntry.setStatus("mandatory")


class _IbmLeServerXLesMinLecID_Type(Integer32):
    """Custom type ibmLeServerXLesMinLecID based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65279),
    )


_IbmLeServerXLesMinLecID_Type.__name__ = "Integer32"
_IbmLeServerXLesMinLecID_Object = MibTableColumn
ibmLeServerXLesMinLecID = _IbmLeServerXLesMinLecID_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 3, 2, 1, 1, 1),
    _IbmLeServerXLesMinLecID_Type()
)
ibmLeServerXLesMinLecID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmLeServerXLesMinLecID.setStatus("mandatory")


class _IbmLeServerXLesMaxLecID_Type(Integer32):
    """Custom type ibmLeServerXLesMaxLecID based on Integer32"""
    defaultValue = 65279

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65279),
    )


_IbmLeServerXLesMaxLecID_Type.__name__ = "Integer32"
_IbmLeServerXLesMaxLecID_Object = MibTableColumn
ibmLeServerXLesMaxLecID = _IbmLeServerXLesMaxLecID_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 3, 2, 1, 1, 2),
    _IbmLeServerXLesMaxLecID_Type()
)
ibmLeServerXLesMaxLecID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmLeServerXLesMaxLecID.setStatus("mandatory")
_IbmLeClientX_ObjectIdentity = ObjectIdentity
ibmLeClientX = _IbmLeClientX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4)
)
_IbmSuperELAN_ObjectIdentity = ObjectIdentity
ibmSuperELAN = _IbmSuperELAN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 1)
)
_IbmSEPortStatisticsTable_Object = MibTable
ibmSEPortStatisticsTable = _IbmSEPortStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 1, 1)
)
if mibBuilder.loadTexts:
    ibmSEPortStatisticsTable.setStatus("mandatory")
_IbmSEPortStatisticsEntry_Object = MibTableRow
ibmSEPortStatisticsEntry = _IbmSEPortStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 1, 1, 1)
)
ibmSEPortStatisticsEntry.setIndexNames(
    (0, "IBM-LAN-EMULATION-EXTENSION-MIB", "ibmSEBridgeId"),
    (0, "IBM-LAN-EMULATION-EXTENSION-MIB", "ibmSEPortNum"),
)
if mibBuilder.loadTexts:
    ibmSEPortStatisticsEntry.setStatus("mandatory")
_IbmSEBridgeId_Type = IbmSEBridgeID
_IbmSEBridgeId_Object = MibTableColumn
ibmSEBridgeId = _IbmSEBridgeId_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 1, 1, 1, 1),
    _IbmSEBridgeId_Type()
)
ibmSEBridgeId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ibmSEBridgeId.setStatus("mandatory")


class _IbmSEPortNum_Type(Integer32):
    """Custom type ibmSEPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IbmSEPortNum_Type.__name__ = "Integer32"
_IbmSEPortNum_Object = MibTableColumn
ibmSEPortNum = _IbmSEPortNum_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 1, 1, 1, 2),
    _IbmSEPortNum_Type()
)
ibmSEPortNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ibmSEPortNum.setStatus("mandatory")
_IbmSEPortArpRequestsIn_Type = Counter32
_IbmSEPortArpRequestsIn_Object = MibTableColumn
ibmSEPortArpRequestsIn = _IbmSEPortArpRequestsIn_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 1, 1, 1, 3),
    _IbmSEPortArpRequestsIn_Type()
)
ibmSEPortArpRequestsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmSEPortArpRequestsIn.setStatus("mandatory")
_IbmSEPortArpRequestsOut_Type = Counter32
_IbmSEPortArpRequestsOut_Object = MibTableColumn
ibmSEPortArpRequestsOut = _IbmSEPortArpRequestsOut_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 1, 1, 1, 4),
    _IbmSEPortArpRequestsOut_Type()
)
ibmSEPortArpRequestsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmSEPortArpRequestsOut.setStatus("mandatory")
_IbmSEArpRequestsErrors_Type = Counter32
_IbmSEArpRequestsErrors_Object = MibTableColumn
ibmSEArpRequestsErrors = _IbmSEArpRequestsErrors_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 1, 1, 1, 5),
    _IbmSEArpRequestsErrors_Type()
)
ibmSEArpRequestsErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmSEArpRequestsErrors.setStatus("mandatory")
_IbmSEPortArpRequestsDroppedPortBlocked_Type = Counter32
_IbmSEPortArpRequestsDroppedPortBlocked_Object = MibTableColumn
ibmSEPortArpRequestsDroppedPortBlocked = _IbmSEPortArpRequestsDroppedPortBlocked_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 1, 1, 1, 6),
    _IbmSEPortArpRequestsDroppedPortBlocked_Type()
)
ibmSEPortArpRequestsDroppedPortBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmSEPortArpRequestsDroppedPortBlocked.setStatus("obsolete")
_IbmSEPortArpRequestsFiltered_Type = Counter32
_IbmSEPortArpRequestsFiltered_Object = MibTableColumn
ibmSEPortArpRequestsFiltered = _IbmSEPortArpRequestsFiltered_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 1, 1, 1, 7),
    _IbmSEPortArpRequestsFiltered_Type()
)
ibmSEPortArpRequestsFiltered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmSEPortArpRequestsFiltered.setStatus("mandatory")
_IbmSEPortArpRepliesIn_Type = Counter32
_IbmSEPortArpRepliesIn_Object = MibTableColumn
ibmSEPortArpRepliesIn = _IbmSEPortArpRepliesIn_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 1, 1, 1, 8),
    _IbmSEPortArpRepliesIn_Type()
)
ibmSEPortArpRepliesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmSEPortArpRepliesIn.setStatus("mandatory")
_IbmSEPortArpRepliesOut_Type = Counter32
_IbmSEPortArpRepliesOut_Object = MibTableColumn
ibmSEPortArpRepliesOut = _IbmSEPortArpRepliesOut_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 1, 1, 1, 9),
    _IbmSEPortArpRepliesOut_Type()
)
ibmSEPortArpRepliesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmSEPortArpRepliesOut.setStatus("mandatory")
_IbmSEPortArpRepliesErrors_Type = Counter32
_IbmSEPortArpRepliesErrors_Object = MibTableColumn
ibmSEPortArpRepliesErrors = _IbmSEPortArpRepliesErrors_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 1, 1, 1, 10),
    _IbmSEPortArpRepliesErrors_Type()
)
ibmSEPortArpRepliesErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmSEPortArpRepliesErrors.setStatus("mandatory")
_IbmSEPortNarpRequestsIn_Type = Counter32
_IbmSEPortNarpRequestsIn_Object = MibTableColumn
ibmSEPortNarpRequestsIn = _IbmSEPortNarpRequestsIn_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 1, 1, 1, 11),
    _IbmSEPortNarpRequestsIn_Type()
)
ibmSEPortNarpRequestsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmSEPortNarpRequestsIn.setStatus("mandatory")
_IbmSEPortNarpRequestsOut_Type = Counter32
_IbmSEPortNarpRequestsOut_Object = MibTableColumn
ibmSEPortNarpRequestsOut = _IbmSEPortNarpRequestsOut_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 1, 1, 1, 12),
    _IbmSEPortNarpRequestsOut_Type()
)
ibmSEPortNarpRequestsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmSEPortNarpRequestsOut.setStatus("mandatory")
_IbmSEPortNarpRequestsDroppedPortBlocked_Type = Counter32
_IbmSEPortNarpRequestsDroppedPortBlocked_Object = MibTableColumn
ibmSEPortNarpRequestsDroppedPortBlocked = _IbmSEPortNarpRequestsDroppedPortBlocked_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 1, 1, 1, 13),
    _IbmSEPortNarpRequestsDroppedPortBlocked_Type()
)
ibmSEPortNarpRequestsDroppedPortBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmSEPortNarpRequestsDroppedPortBlocked.setStatus("obsolete")
_IbmSEPortFlushRequestsIn_Type = Counter32
_IbmSEPortFlushRequestsIn_Object = MibTableColumn
ibmSEPortFlushRequestsIn = _IbmSEPortFlushRequestsIn_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 1, 1, 1, 14),
    _IbmSEPortFlushRequestsIn_Type()
)
ibmSEPortFlushRequestsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmSEPortFlushRequestsIn.setStatus("mandatory")
_IbmSEPortFlushRequestsOut_Type = Counter32
_IbmSEPortFlushRequestsOut_Object = MibTableColumn
ibmSEPortFlushRequestsOut = _IbmSEPortFlushRequestsOut_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 1, 1, 1, 15),
    _IbmSEPortFlushRequestsOut_Type()
)
ibmSEPortFlushRequestsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmSEPortFlushRequestsOut.setStatus("mandatory")
_IbmSEPortFlushRepliesIn_Type = Counter32
_IbmSEPortFlushRepliesIn_Object = MibTableColumn
ibmSEPortFlushRepliesIn = _IbmSEPortFlushRepliesIn_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 1, 1, 1, 16),
    _IbmSEPortFlushRepliesIn_Type()
)
ibmSEPortFlushRepliesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmSEPortFlushRepliesIn.setStatus("mandatory")
_IbmSEPortFlushRepliesOut_Type = Counter32
_IbmSEPortFlushRepliesOut_Object = MibTableColumn
ibmSEPortFlushRepliesOut = _IbmSEPortFlushRepliesOut_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 1, 1, 1, 17),
    _IbmSEPortFlushRepliesOut_Type()
)
ibmSEPortFlushRepliesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmSEPortFlushRepliesOut.setStatus("mandatory")
_IbmSEPortFlushRequestErrors_Type = Counter32
_IbmSEPortFlushRequestErrors_Object = MibTableColumn
ibmSEPortFlushRequestErrors = _IbmSEPortFlushRequestErrors_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 1, 1, 1, 18),
    _IbmSEPortFlushRequestErrors_Type()
)
ibmSEPortFlushRequestErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmSEPortFlushRequestErrors.setStatus("mandatory")
_IbmSEPortFlushRepliesErrors_Type = Counter32
_IbmSEPortFlushRepliesErrors_Object = MibTableColumn
ibmSEPortFlushRepliesErrors = _IbmSEPortFlushRepliesErrors_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 1, 1, 1, 19),
    _IbmSEPortFlushRepliesErrors_Type()
)
ibmSEPortFlushRepliesErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmSEPortFlushRepliesErrors.setStatus("mandatory")
_IbmSEPortLeCtrlFramesIn_Type = Counter32
_IbmSEPortLeCtrlFramesIn_Object = MibTableColumn
ibmSEPortLeCtrlFramesIn = _IbmSEPortLeCtrlFramesIn_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 1, 1, 1, 20),
    _IbmSEPortLeCtrlFramesIn_Type()
)
ibmSEPortLeCtrlFramesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmSEPortLeCtrlFramesIn.setStatus("mandatory")
_IbmSEPortLeCtrlFramesOut_Type = Counter32
_IbmSEPortLeCtrlFramesOut_Object = MibTableColumn
ibmSEPortLeCtrlFramesOut = _IbmSEPortLeCtrlFramesOut_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 1, 1, 1, 21),
    _IbmSEPortLeCtrlFramesOut_Type()
)
ibmSEPortLeCtrlFramesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmSEPortLeCtrlFramesOut.setStatus("mandatory")
_IbmSEPortLeCtrlFramesDiscSrcPortNotFwrd_Type = Counter32
_IbmSEPortLeCtrlFramesDiscSrcPortNotFwrd_Object = MibTableColumn
ibmSEPortLeCtrlFramesDiscSrcPortNotFwrd = _IbmSEPortLeCtrlFramesDiscSrcPortNotFwrd_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 1, 1, 1, 22),
    _IbmSEPortLeCtrlFramesDiscSrcPortNotFwrd_Type()
)
ibmSEPortLeCtrlFramesDiscSrcPortNotFwrd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmSEPortLeCtrlFramesDiscSrcPortNotFwrd.setStatus("mandatory")
_IbmSEPortLeCtrlFramesDiscDestPortNotFwrd_Type = Counter32
_IbmSEPortLeCtrlFramesDiscDestPortNotFwrd_Object = MibTableColumn
ibmSEPortLeCtrlFramesDiscDestPortNotFwrd = _IbmSEPortLeCtrlFramesDiscDestPortNotFwrd_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 1, 1, 1, 23),
    _IbmSEPortLeCtrlFramesDiscDestPortNotFwrd_Type()
)
ibmSEPortLeCtrlFramesDiscDestPortNotFwrd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmSEPortLeCtrlFramesDiscDestPortNotFwrd.setStatus("mandatory")
_IbmSEBridgeConfigTable_Object = MibTable
ibmSEBridgeConfigTable = _IbmSEBridgeConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 1, 2)
)
if mibBuilder.loadTexts:
    ibmSEBridgeConfigTable.setStatus("mandatory")
_IbmSEBridgeConfigEntry_Object = MibTableRow
ibmSEBridgeConfigEntry = _IbmSEBridgeConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 1, 2, 1)
)
ibmSEBridgeConfigEntry.setIndexNames(
    (0, "IBM-LAN-EMULATION-EXTENSION-MIB", "ibmSEBridgeId"),
)
if mibBuilder.loadTexts:
    ibmSEBridgeConfigEntry.setStatus("mandatory")


class _IbmSEAtmIfNumber_Type(IfIndexOrZero):
    """Custom type ibmSEAtmIfNumber based on IfIndexOrZero"""
    defaultValue = 0


_IbmSEAtmIfNumber_Object = MibTableColumn
ibmSEAtmIfNumber = _IbmSEAtmIfNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 1, 2, 1, 1),
    _IbmSEAtmIfNumber_Type()
)
ibmSEAtmIfNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmSEAtmIfNumber.setStatus("mandatory")


class _IbmSEEnabled_Type(Integer32):
    """Custom type ibmSEEnabled based on Integer32"""
    defaultValue = 1

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


_IbmSEEnabled_Type.__name__ = "Integer32"
_IbmSEEnabled_Object = MibTableColumn
ibmSEEnabled = _IbmSEEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 1, 2, 1, 2),
    _IbmSEEnabled_Type()
)
ibmSEEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmSEEnabled.setStatus("mandatory")


class _IbmSEName_Type(DisplayString):
    """Custom type ibmSEName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_IbmSEName_Type.__name__ = "DisplayString"
_IbmSEName_Object = MibTableColumn
ibmSEName = _IbmSEName_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 1, 2, 1, 3),
    _IbmSEName_Type()
)
ibmSEName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmSEName.setStatus("mandatory")


class _IbmSEFrameSize_Type(Integer32):
    """Custom type ibmSEFrameSize based on Integer32"""
    defaultValue = 4544

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1516,
              4544,
              9234,
              18190)
        )
    )
    namedValues = NamedValues(
        *(("en1516", 1516),
          ("tr18190", 18190),
          ("tr4544", 4544),
          ("tr9234", 9234))
    )


_IbmSEFrameSize_Type.__name__ = "Integer32"
_IbmSEFrameSize_Object = MibTableColumn
ibmSEFrameSize = _IbmSEFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 1, 2, 1, 4),
    _IbmSEFrameSize_Type()
)
ibmSEFrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmSEFrameSize.setStatus("mandatory")


class _IbmSEMacCacheAge_Type(Integer32):
    """Custom type ibmSEMacCacheAge based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000000),
    )


_IbmSEMacCacheAge_Type.__name__ = "Integer32"
_IbmSEMacCacheAge_Object = MibTableColumn
ibmSEMacCacheAge = _IbmSEMacCacheAge_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 1, 2, 1, 5),
    _IbmSEMacCacheAge_Type()
)
ibmSEMacCacheAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmSEMacCacheAge.setStatus("mandatory")


class _IbmSERDCacheAge_Type(Integer32):
    """Custom type ibmSERDCacheAge based on Integer32"""
    defaultValue = 1800

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000000),
    )


_IbmSERDCacheAge_Type.__name__ = "Integer32"
_IbmSERDCacheAge_Object = MibTableColumn
ibmSERDCacheAge = _IbmSERDCacheAge_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 1, 2, 1, 6),
    _IbmSERDCacheAge_Type()
)
ibmSERDCacheAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmSERDCacheAge.setStatus("mandatory")


class _IbmSEPriority_Type(Integer32):
    """Custom type ibmSEPriority based on Integer32"""
    defaultValue = 32768

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IbmSEPriority_Type.__name__ = "Integer32"
_IbmSEPriority_Object = MibTableColumn
ibmSEPriority = _IbmSEPriority_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 1, 2, 1, 7),
    _IbmSEPriority_Type()
)
ibmSEPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmSEPriority.setStatus("mandatory")


class _IbmSEMaxAge_Type(Integer32):
    """Custom type ibmSEMaxAge based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6, 40),
    )


_IbmSEMaxAge_Type.__name__ = "Integer32"
_IbmSEMaxAge_Object = MibTableColumn
ibmSEMaxAge = _IbmSEMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 1, 2, 1, 8),
    _IbmSEMaxAge_Type()
)
ibmSEMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmSEMaxAge.setStatus("mandatory")


class _IbmSEBridgeHelloTime_Type(Integer32):
    """Custom type ibmSEBridgeHelloTime based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_IbmSEBridgeHelloTime_Type.__name__ = "Integer32"
_IbmSEBridgeHelloTime_Object = MibTableColumn
ibmSEBridgeHelloTime = _IbmSEBridgeHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 1, 2, 1, 9),
    _IbmSEBridgeHelloTime_Type()
)
ibmSEBridgeHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmSEBridgeHelloTime.setStatus("mandatory")


class _IbmSEBridgeForwardDelay_Type(Integer32):
    """Custom type ibmSEBridgeForwardDelay based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 30),
    )


_IbmSEBridgeForwardDelay_Type.__name__ = "Integer32"
_IbmSEBridgeForwardDelay_Object = MibTableColumn
ibmSEBridgeForwardDelay = _IbmSEBridgeForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 1, 2, 1, 10),
    _IbmSEBridgeForwardDelay_Type()
)
ibmSEBridgeForwardDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmSEBridgeForwardDelay.setStatus("mandatory")


class _IbmSEBridgeAddress_Type(MacAddress):
    """Custom type ibmSEBridgeAddress based on MacAddress"""
    defaultHexValue = "000000000000"


_IbmSEBridgeAddress_Object = MibTableColumn
ibmSEBridgeAddress = _IbmSEBridgeAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 1, 2, 1, 11),
    _IbmSEBridgeAddress_Type()
)
ibmSEBridgeAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmSEBridgeAddress.setStatus("mandatory")


class _IbmSEType_Type(Integer32):
    """Custom type ibmSEType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sebEN", 1),
          ("sebTR", 2))
    )


_IbmSEType_Type.__name__ = "Integer32"
_IbmSEType_Object = MibTableColumn
ibmSEType = _IbmSEType_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 1, 2, 1, 12),
    _IbmSEType_Type()
)
ibmSEType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmSEType.setStatus("mandatory")
_IbmSEConfigRowStatus_Type = RowStatus
_IbmSEConfigRowStatus_Object = MibTableColumn
ibmSEConfigRowStatus = _IbmSEConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 1, 2, 1, 13),
    _IbmSEConfigRowStatus_Type()
)
ibmSEConfigRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmSEConfigRowStatus.setStatus("mandatory")
_IbmSEPortConfigTable_Object = MibTable
ibmSEPortConfigTable = _IbmSEPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 1, 3)
)
if mibBuilder.loadTexts:
    ibmSEPortConfigTable.setStatus("mandatory")
_IbmSEPortConfigEntry_Object = MibTableRow
ibmSEPortConfigEntry = _IbmSEPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 1, 3, 1)
)
ibmSEPortConfigEntry.setIndexNames(
    (0, "IBM-LAN-EMULATION-EXTENSION-MIB", "ibmSEBridgeId"),
    (0, "IBM-LAN-EMULATION-EXTENSION-MIB", "ibmSEPortNum"),
)
if mibBuilder.loadTexts:
    ibmSEPortConfigEntry.setStatus("mandatory")


class _IbmSEPortIfNumber_Type(Integer32):
    """Custom type ibmSEPortIfNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IbmSEPortIfNumber_Type.__name__ = "Integer32"
_IbmSEPortIfNumber_Object = MibTableColumn
ibmSEPortIfNumber = _IbmSEPortIfNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 1, 3, 1, 1),
    _IbmSEPortIfNumber_Type()
)
ibmSEPortIfNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmSEPortIfNumber.setStatus("mandatory")


class _IbmSEPortElanName_Type(DisplayString):
    """Custom type ibmSEPortElanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_IbmSEPortElanName_Type.__name__ = "DisplayString"
_IbmSEPortElanName_Object = MibTableColumn
ibmSEPortElanName = _IbmSEPortElanName_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 1, 3, 1, 2),
    _IbmSEPortElanName_Type()
)
ibmSEPortElanName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmSEPortElanName.setStatus("mandatory")


class _IbmSEPortRemoteElan_Type(Integer32):
    """Custom type ibmSEPortRemoteElan based on Integer32"""
    defaultValue = 2

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


_IbmSEPortRemoteElan_Type.__name__ = "Integer32"
_IbmSEPortRemoteElan_Object = MibTableColumn
ibmSEPortRemoteElan = _IbmSEPortRemoteElan_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 1, 3, 1, 3),
    _IbmSEPortRemoteElan_Type()
)
ibmSEPortRemoteElan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmSEPortRemoteElan.setStatus("mandatory")


class _IbmSEPortEnabled_Type(Integer32):
    """Custom type ibmSEPortEnabled based on Integer32"""
    defaultValue = 1

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


_IbmSEPortEnabled_Type.__name__ = "Integer32"
_IbmSEPortEnabled_Object = MibTableColumn
ibmSEPortEnabled = _IbmSEPortEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 1, 3, 1, 4),
    _IbmSEPortEnabled_Type()
)
ibmSEPortEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmSEPortEnabled.setStatus("mandatory")


class _IbmSEPortPriority_Type(Integer32):
    """Custom type ibmSEPortPriority based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbmSEPortPriority_Type.__name__ = "Integer32"
_IbmSEPortPriority_Object = MibTableColumn
ibmSEPortPriority = _IbmSEPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 1, 3, 1, 5),
    _IbmSEPortPriority_Type()
)
ibmSEPortPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmSEPortPriority.setStatus("mandatory")


class _IbmSEPortRootCost_Type(Integer32):
    """Custom type ibmSEPortRootCost based on Integer32"""
    defaultValue = 32768

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IbmSEPortRootCost_Type.__name__ = "Integer32"
_IbmSEPortRootCost_Object = MibTableColumn
ibmSEPortRootCost = _IbmSEPortRootCost_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 1, 3, 1, 6),
    _IbmSEPortRootCost_Type()
)
ibmSEPortRootCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmSEPortRootCost.setStatus("mandatory")
_IbmSEPortRowStatus_Type = RowStatus
_IbmSEPortRowStatus_Object = MibTableColumn
ibmSEPortRowStatus = _IbmSEPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 1, 3, 1, 7),
    _IbmSEPortRowStatus_Type()
)
ibmSEPortRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmSEPortRowStatus.setStatus("mandatory")
_IbmSEBridgeTable_Object = MibTable
ibmSEBridgeTable = _IbmSEBridgeTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 1, 4)
)
if mibBuilder.loadTexts:
    ibmSEBridgeTable.setStatus("mandatory")
_IbmSEBridgeEntry_Object = MibTableRow
ibmSEBridgeEntry = _IbmSEBridgeEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 1, 4, 1)
)
ibmSEBridgeEntry.setIndexNames(
    (0, "IBM-LAN-EMULATION-EXTENSION-MIB", "ibmSEBridgeId"),
)
if mibBuilder.loadTexts:
    ibmSEBridgeEntry.setStatus("mandatory")


class _IbmSENumPorts_Type(Integer32):
    """Custom type ibmSENumPorts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IbmSENumPorts_Type.__name__ = "Integer32"
_IbmSENumPorts_Object = MibTableColumn
ibmSENumPorts = _IbmSENumPorts_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 1, 4, 1, 1),
    _IbmSENumPorts_Type()
)
ibmSENumPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmSENumPorts.setStatus("mandatory")


class _IbmSEProtocolSpecification_Type(Integer32):
    """Custom type ibmSEProtocolSpecification based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tbSra", 2),
          ("unknown", 1))
    )


_IbmSEProtocolSpecification_Type.__name__ = "Integer32"
_IbmSEProtocolSpecification_Object = MibTableColumn
ibmSEProtocolSpecification = _IbmSEProtocolSpecification_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 1, 4, 1, 2),
    _IbmSEProtocolSpecification_Type()
)
ibmSEProtocolSpecification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmSEProtocolSpecification.setStatus("mandatory")
_IbmSETimeSinceTopologyChange_Type = TimeTicks
_IbmSETimeSinceTopologyChange_Object = MibTableColumn
ibmSETimeSinceTopologyChange = _IbmSETimeSinceTopologyChange_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 1, 4, 1, 3),
    _IbmSETimeSinceTopologyChange_Type()
)
ibmSETimeSinceTopologyChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmSETimeSinceTopologyChange.setStatus("mandatory")
_IbmSETopChanges_Type = Counter32
_IbmSETopChanges_Object = MibTableColumn
ibmSETopChanges = _IbmSETopChanges_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 1, 4, 1, 4),
    _IbmSETopChanges_Type()
)
ibmSETopChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmSETopChanges.setStatus("mandatory")
_IbmSEDesignatedRoot_Type = BridgeId
_IbmSEDesignatedRoot_Object = MibTableColumn
ibmSEDesignatedRoot = _IbmSEDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 1, 4, 1, 5),
    _IbmSEDesignatedRoot_Type()
)
ibmSEDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmSEDesignatedRoot.setStatus("mandatory")


class _IbmSERootCost_Type(Integer32):
    """Custom type ibmSERootCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IbmSERootCost_Type.__name__ = "Integer32"
_IbmSERootCost_Object = MibTableColumn
ibmSERootCost = _IbmSERootCost_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 1, 4, 1, 6),
    _IbmSERootCost_Type()
)
ibmSERootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmSERootCost.setStatus("mandatory")


class _IbmSERootPort_Type(Integer32):
    """Custom type ibmSERootPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IbmSERootPort_Type.__name__ = "Integer32"
_IbmSERootPort_Object = MibTableColumn
ibmSERootPort = _IbmSERootPort_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 1, 4, 1, 7),
    _IbmSERootPort_Type()
)
ibmSERootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmSERootPort.setStatus("mandatory")


class _IbmSEBridgeMaxAge_Type(Timeout):
    """Custom type ibmSEBridgeMaxAge based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IbmSEBridgeMaxAge_Type.__name__ = "Timeout"
_IbmSEBridgeMaxAge_Object = MibTableColumn
ibmSEBridgeMaxAge = _IbmSEBridgeMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 1, 4, 1, 8),
    _IbmSEBridgeMaxAge_Type()
)
ibmSEBridgeMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmSEBridgeMaxAge.setStatus("mandatory")


class _IbmSEHelloTime_Type(Timeout):
    """Custom type ibmSEHelloTime based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IbmSEHelloTime_Type.__name__ = "Timeout"
_IbmSEHelloTime_Object = MibTableColumn
ibmSEHelloTime = _IbmSEHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 1, 4, 1, 9),
    _IbmSEHelloTime_Type()
)
ibmSEHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmSEHelloTime.setStatus("mandatory")


class _IbmSEHoldTime_Type(Integer32):
    """Custom type ibmSEHoldTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IbmSEHoldTime_Type.__name__ = "Integer32"
_IbmSEHoldTime_Object = MibTableColumn
ibmSEHoldTime = _IbmSEHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 1, 4, 1, 10),
    _IbmSEHoldTime_Type()
)
ibmSEHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmSEHoldTime.setStatus("mandatory")


class _IbmSEForwardDelay_Type(Timeout):
    """Custom type ibmSEForwardDelay based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IbmSEForwardDelay_Type.__name__ = "Timeout"
_IbmSEForwardDelay_Object = MibTableColumn
ibmSEForwardDelay = _IbmSEForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 1, 4, 1, 11),
    _IbmSEForwardDelay_Type()
)
ibmSEForwardDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmSEForwardDelay.setStatus("mandatory")
_IbmSEMacLearnedEntryDiscards_Type = Counter32
_IbmSEMacLearnedEntryDiscards_Object = MibTableColumn
ibmSEMacLearnedEntryDiscards = _IbmSEMacLearnedEntryDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 1, 4, 1, 12),
    _IbmSEMacLearnedEntryDiscards_Type()
)
ibmSEMacLearnedEntryDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmSEMacLearnedEntryDiscards.setStatus("mandatory")
_IbmSERDLearnedEntryDiscards_Type = Counter32
_IbmSERDLearnedEntryDiscards_Object = MibTableColumn
ibmSERDLearnedEntryDiscards = _IbmSERDLearnedEntryDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 1, 4, 1, 13),
    _IbmSERDLearnedEntryDiscards_Type()
)
ibmSERDLearnedEntryDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmSERDLearnedEntryDiscards.setStatus("mandatory")
_IbmSEStpPortTable_Object = MibTable
ibmSEStpPortTable = _IbmSEStpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 1, 5)
)
if mibBuilder.loadTexts:
    ibmSEStpPortTable.setStatus("mandatory")
_IbmSEStpPortEntry_Object = MibTableRow
ibmSEStpPortEntry = _IbmSEStpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 1, 5, 1)
)
ibmSEStpPortEntry.setIndexNames(
    (0, "IBM-LAN-EMULATION-EXTENSION-MIB", "ibmSEBridgeId"),
    (0, "IBM-LAN-EMULATION-EXTENSION-MIB", "ibmSEPortNum"),
)
if mibBuilder.loadTexts:
    ibmSEStpPortEntry.setStatus("mandatory")


class _IbmSEStpPortState_Type(Integer32):
    """Custom type ibmSEStpPortState based on Integer32"""
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
        *(("blocked", 4),
          ("configured", 5),
          ("configuring", 7),
          ("forwarding", 1),
          ("learning", 2),
          ("listening", 3),
          ("netdown", 6),
          ("unknown", 8))
    )


_IbmSEStpPortState_Type.__name__ = "Integer32"
_IbmSEStpPortState_Object = MibTableColumn
ibmSEStpPortState = _IbmSEStpPortState_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 1, 5, 1, 1),
    _IbmSEStpPortState_Type()
)
ibmSEStpPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmSEStpPortState.setStatus("mandatory")
_IbmSEStpPortDesignatedRoot_Type = BridgeId
_IbmSEStpPortDesignatedRoot_Object = MibTableColumn
ibmSEStpPortDesignatedRoot = _IbmSEStpPortDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 1, 5, 1, 2),
    _IbmSEStpPortDesignatedRoot_Type()
)
ibmSEStpPortDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmSEStpPortDesignatedRoot.setStatus("mandatory")


class _IbmSEStpPortDesignatedCost_Type(Integer32):
    """Custom type ibmSEStpPortDesignatedCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IbmSEStpPortDesignatedCost_Type.__name__ = "Integer32"
_IbmSEStpPortDesignatedCost_Object = MibTableColumn
ibmSEStpPortDesignatedCost = _IbmSEStpPortDesignatedCost_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 1, 5, 1, 3),
    _IbmSEStpPortDesignatedCost_Type()
)
ibmSEStpPortDesignatedCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmSEStpPortDesignatedCost.setStatus("mandatory")
_IbmSEStpPortDesignatedBridge_Type = BridgeId
_IbmSEStpPortDesignatedBridge_Object = MibTableColumn
ibmSEStpPortDesignatedBridge = _IbmSEStpPortDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 1, 5, 1, 4),
    _IbmSEStpPortDesignatedBridge_Type()
)
ibmSEStpPortDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmSEStpPortDesignatedBridge.setStatus("mandatory")


class _IbmSEStpPortDesignatedPort_Type(Integer32):
    """Custom type ibmSEStpPortDesignatedPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IbmSEStpPortDesignatedPort_Type.__name__ = "Integer32"
_IbmSEStpPortDesignatedPort_Object = MibTableColumn
ibmSEStpPortDesignatedPort = _IbmSEStpPortDesignatedPort_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 1, 5, 1, 5),
    _IbmSEStpPortDesignatedPort_Type()
)
ibmSEStpPortDesignatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmSEStpPortDesignatedPort.setStatus("mandatory")
_IbmSEStpPortForwardTransitions_Type = Counter32
_IbmSEStpPortForwardTransitions_Object = MibTableColumn
ibmSEStpPortForwardTransitions = _IbmSEStpPortForwardTransitions_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 1, 5, 1, 6),
    _IbmSEStpPortForwardTransitions_Type()
)
ibmSEStpPortForwardTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmSEStpPortForwardTransitions.setStatus("mandatory")


class _IbmSEPortMaxInfo_Type(Integer32):
    """Custom type ibmSEPortMaxInfo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IbmSEPortMaxInfo_Type.__name__ = "Integer32"
_IbmSEPortMaxInfo_Object = MibTableColumn
ibmSEPortMaxInfo = _IbmSEPortMaxInfo_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 1, 5, 1, 7),
    _IbmSEPortMaxInfo_Type()
)
ibmSEPortMaxInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmSEPortMaxInfo.setStatus("mandatory")
_IbmSEPortDataStatisticsTable_Object = MibTable
ibmSEPortDataStatisticsTable = _IbmSEPortDataStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 1, 8)
)
if mibBuilder.loadTexts:
    ibmSEPortDataStatisticsTable.setStatus("mandatory")
_IbmSEPortDataStatisticsEntry_Object = MibTableRow
ibmSEPortDataStatisticsEntry = _IbmSEPortDataStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 1, 8, 1)
)
ibmSEPortDataStatisticsEntry.setIndexNames(
    (0, "IBM-LAN-EMULATION-EXTENSION-MIB", "ibmSEBridgeId"),
    (0, "IBM-LAN-EMULATION-EXTENSION-MIB", "ibmSEPortNum"),
)
if mibBuilder.loadTexts:
    ibmSEPortDataStatisticsEntry.setStatus("mandatory")
_IbmSEPortInFrames_Type = Counter32
_IbmSEPortInFrames_Object = MibTableColumn
ibmSEPortInFrames = _IbmSEPortInFrames_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 1, 8, 1, 1),
    _IbmSEPortInFrames_Type()
)
ibmSEPortInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmSEPortInFrames.setStatus("mandatory")
_IbmSEPortOutFrames_Type = Counter32
_IbmSEPortOutFrames_Object = MibTableColumn
ibmSEPortOutFrames = _IbmSEPortOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 1, 8, 1, 2),
    _IbmSEPortOutFrames_Type()
)
ibmSEPortOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmSEPortOutFrames.setStatus("mandatory")
_IbmSEPortRoutedInFrames_Type = Counter32
_IbmSEPortRoutedInFrames_Object = MibTableColumn
ibmSEPortRoutedInFrames = _IbmSEPortRoutedInFrames_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 1, 8, 1, 3),
    _IbmSEPortRoutedInFrames_Type()
)
ibmSEPortRoutedInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmSEPortRoutedInFrames.setStatus("mandatory")
_IbmSEPortBpduFrames_Type = Counter32
_IbmSEPortBpduFrames_Object = MibTableColumn
ibmSEPortBpduFrames = _IbmSEPortBpduFrames_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 1, 8, 1, 4),
    _IbmSEPortBpduFrames_Type()
)
ibmSEPortBpduFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmSEPortBpduFrames.setStatus("mandatory")
_IbmSEPortInDiscards_Type = Counter32
_IbmSEPortInDiscards_Object = MibTableColumn
ibmSEPortInDiscards = _IbmSEPortInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 1, 8, 1, 5),
    _IbmSEPortInDiscards_Type()
)
ibmSEPortInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmSEPortInDiscards.setStatus("mandatory")
_IbmSEPortDropSrcAddrFilters_Type = Counter32
_IbmSEPortDropSrcAddrFilters_Object = MibTableColumn
ibmSEPortDropSrcAddrFilters = _IbmSEPortDropSrcAddrFilters_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 1, 8, 1, 6),
    _IbmSEPortDropSrcAddrFilters_Type()
)
ibmSEPortDropSrcAddrFilters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmSEPortDropSrcAddrFilters.setStatus("mandatory")
_IbmSEPortDropDestAddrFilters_Type = Counter32
_IbmSEPortDropDestAddrFilters_Object = MibTableColumn
ibmSEPortDropDestAddrFilters = _IbmSEPortDropDestAddrFilters_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 1, 8, 1, 7),
    _IbmSEPortDropDestAddrFilters_Type()
)
ibmSEPortDropDestAddrFilters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmSEPortDropDestAddrFilters.setStatus("mandatory")
_IbmSEPortDropProtocolFilters_Type = Counter32
_IbmSEPortDropProtocolFilters_Object = MibTableColumn
ibmSEPortDropProtocolFilters = _IbmSEPortDropProtocolFilters_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 1, 8, 1, 8),
    _IbmSEPortDropProtocolFilters_Type()
)
ibmSEPortDropProtocolFilters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmSEPortDropProtocolFilters.setStatus("mandatory")
_IbmSEPortDropSrcNotFwds_Type = Counter32
_IbmSEPortDropSrcNotFwds_Object = MibTableColumn
ibmSEPortDropSrcNotFwds = _IbmSEPortDropSrcNotFwds_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 1, 8, 1, 9),
    _IbmSEPortDropSrcNotFwds_Type()
)
ibmSEPortDropSrcNotFwds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmSEPortDropSrcNotFwds.setStatus("mandatory")
_IbmSEPortDropDestNotFwds_Type = Counter32
_IbmSEPortDropDestNotFwds_Object = MibTableColumn
ibmSEPortDropDestNotFwds = _IbmSEPortDropDestNotFwds_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 1, 8, 1, 10),
    _IbmSEPortDropDestNotFwds_Type()
)
ibmSEPortDropDestNotFwds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmSEPortDropDestNotFwds.setStatus("mandatory")
_IbmSEPortDropInputOverflows_Type = Counter32
_IbmSEPortDropInputOverflows_Object = MibTableColumn
ibmSEPortDropInputOverflows = _IbmSEPortDropInputOverflows_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 1, 8, 1, 11),
    _IbmSEPortDropInputOverflows_Type()
)
ibmSEPortDropInputOverflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmSEPortDropInputOverflows.setStatus("mandatory")
_IbmSEPortDropBpduOverflows_Type = Counter32
_IbmSEPortDropBpduOverflows_Object = MibTableColumn
ibmSEPortDropBpduOverflows = _IbmSEPortDropBpduOverflows_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 1, 8, 1, 12),
    _IbmSEPortDropBpduOverflows_Type()
)
ibmSEPortDropBpduOverflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmSEPortDropBpduOverflows.setStatus("mandatory")
_IbmSEPortDropSrOverflows_Type = Counter32
_IbmSEPortDropSrOverflows_Object = MibTableColumn
ibmSEPortDropSrOverflows = _IbmSEPortDropSrOverflows_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 1, 8, 1, 13),
    _IbmSEPortDropSrOverflows_Type()
)
ibmSEPortDropSrOverflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmSEPortDropSrOverflows.setStatus("mandatory")
_IbmSEPortRecNoBuffFailures_Type = Counter32
_IbmSEPortRecNoBuffFailures_Object = MibTableColumn
ibmSEPortRecNoBuffFailures = _IbmSEPortRecNoBuffFailures_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 1, 8, 1, 14),
    _IbmSEPortRecNoBuffFailures_Type()
)
ibmSEPortRecNoBuffFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmSEPortRecNoBuffFailures.setStatus("mandatory")
_IbmSEPortTransmitFailures_Type = Counter32
_IbmSEPortTransmitFailures_Object = MibTableColumn
ibmSEPortTransmitFailures = _IbmSEPortTransmitFailures_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 1, 8, 1, 15),
    _IbmSEPortTransmitFailures_Type()
)
ibmSEPortTransmitFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmSEPortTransmitFailures.setStatus("mandatory")
_IbmSEPortToBigFailures_Type = Counter32
_IbmSEPortToBigFailures_Object = MibTableColumn
ibmSEPortToBigFailures = _IbmSEPortToBigFailures_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 1, 8, 1, 16),
    _IbmSEPortToBigFailures_Type()
)
ibmSEPortToBigFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmSEPortToBigFailures.setStatus("mandatory")
_IbmSEPortLanIdFailures_Type = Counter32
_IbmSEPortLanIdFailures_Object = MibTableColumn
ibmSEPortLanIdFailures = _IbmSEPortLanIdFailures_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 1, 8, 1, 17),
    _IbmSEPortLanIdFailures_Type()
)
ibmSEPortLanIdFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmSEPortLanIdFailures.setStatus("mandatory")
_IbmSEPortStpLanIdFailures_Type = Counter32
_IbmSEPortStpLanIdFailures_Object = MibTableColumn
ibmSEPortStpLanIdFailures = _IbmSEPortStpLanIdFailures_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 1, 8, 1, 18),
    _IbmSEPortStpLanIdFailures_Type()
)
ibmSEPortStpLanIdFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmSEPortStpLanIdFailures.setStatus("mandatory")
_IbmBbcmMIB_ObjectIdentity = ObjectIdentity
ibmBbcmMIB = _IbmBbcmMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 2)
)
_IbmBbcmConfigGroup_ObjectIdentity = ObjectIdentity
ibmBbcmConfigGroup = _IbmBbcmConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 2, 1)
)


class _IbmBbcmConfigNextId_Type(Integer32):
    """Custom type ibmBbcmConfigNextId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 214748364),
    )


_IbmBbcmConfigNextId_Type.__name__ = "Integer32"
_IbmBbcmConfigNextId_Object = MibScalar
ibmBbcmConfigNextId = _IbmBbcmConfigNextId_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 2, 1, 1),
    _IbmBbcmConfigNextId_Type()
)
ibmBbcmConfigNextId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmBbcmConfigNextId.setStatus("obsolete")
_IbmBbcmConfigTable_Object = MibTable
ibmBbcmConfigTable = _IbmBbcmConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ibmBbcmConfigTable.setStatus("mandatory")
_IbmBbcmConfigEntry_Object = MibTableRow
ibmBbcmConfigEntry = _IbmBbcmConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 2, 1, 2, 1)
)
ibmBbcmConfigEntry.setIndexNames(
    (0, "IBM-LAN-EMULATION-EXTENSION-MIB", "ibmBbcmConfigIndex"),
)
if mibBuilder.loadTexts:
    ibmBbcmConfigEntry.setStatus("mandatory")
_IbmBbcmConfigIndex_Type = IbmSEBridgeID
_IbmBbcmConfigIndex_Object = MibTableColumn
ibmBbcmConfigIndex = _IbmBbcmConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 2, 1, 2, 1, 1),
    _IbmBbcmConfigIndex_Type()
)
ibmBbcmConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ibmBbcmConfigIndex.setStatus("mandatory")


class _IbmBbcmName_Type(DisplayString):
    """Custom type ibmBbcmName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_IbmBbcmName_Type.__name__ = "DisplayString"
_IbmBbcmName_Object = MibTableColumn
ibmBbcmName = _IbmBbcmName_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 2, 1, 2, 1, 2),
    _IbmBbcmName_Type()
)
ibmBbcmName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmBbcmName.setStatus("mandatory")
_IbmBbcmConfigRowStatus_Type = RowStatus
_IbmBbcmConfigRowStatus_Object = MibTableColumn
ibmBbcmConfigRowStatus = _IbmBbcmConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 2, 1, 2, 1, 3),
    _IbmBbcmConfigRowStatus_Type()
)
ibmBbcmConfigRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmBbcmConfigRowStatus.setStatus("mandatory")
_IbmBbcmProtocolConfigTable_Object = MibTable
ibmBbcmProtocolConfigTable = _IbmBbcmProtocolConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 2, 1, 3)
)
if mibBuilder.loadTexts:
    ibmBbcmProtocolConfigTable.setStatus("mandatory")
_IbmBbcmProtocolConfigEntry_Object = MibTableRow
ibmBbcmProtocolConfigEntry = _IbmBbcmProtocolConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 2, 1, 3, 1)
)
ibmBbcmProtocolConfigEntry.setIndexNames(
    (0, "IBM-LAN-EMULATION-EXTENSION-MIB", "ibmBbcmProtocolType"),
    (0, "IBM-LAN-EMULATION-EXTENSION-MIB", "ibmBbcmConfigIndex"),
)
if mibBuilder.loadTexts:
    ibmBbcmProtocolConfigEntry.setStatus("mandatory")


class _IbmBbcmProtocolType_Type(Integer32):
    """Custom type ibmBbcmProtocolType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ip", 2),
          ("reserved", 1))
    )


_IbmBbcmProtocolType_Type.__name__ = "Integer32"
_IbmBbcmProtocolType_Object = MibTableColumn
ibmBbcmProtocolType = _IbmBbcmProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 2, 1, 3, 1, 1),
    _IbmBbcmProtocolType_Type()
)
ibmBbcmProtocolType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ibmBbcmProtocolType.setStatus("mandatory")


class _IbmBbcmProtocolOperStatus_Type(Integer32):
    """Custom type ibmBbcmProtocolOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 3),
          ("other", 1),
          ("up", 2))
    )


_IbmBbcmProtocolOperStatus_Type.__name__ = "Integer32"
_IbmBbcmProtocolOperStatus_Object = MibTableColumn
ibmBbcmProtocolOperStatus = _IbmBbcmProtocolOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 2, 1, 3, 1, 2),
    _IbmBbcmProtocolOperStatus_Type()
)
ibmBbcmProtocolOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmBbcmProtocolOperStatus.setStatus("mandatory")


class _IbmBbcmProtocolAdminStatus_Type(Integer32):
    """Custom type ibmBbcmProtocolAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 3),
          ("up", 2))
    )


_IbmBbcmProtocolAdminStatus_Type.__name__ = "Integer32"
_IbmBbcmProtocolAdminStatus_Object = MibTableColumn
ibmBbcmProtocolAdminStatus = _IbmBbcmProtocolAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 2, 1, 3, 1, 3),
    _IbmBbcmProtocolAdminStatus_Type()
)
ibmBbcmProtocolAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmBbcmProtocolAdminStatus.setStatus("mandatory")


class _IbmBbcmProtocolCacheAge_Type(Integer32):
    """Custom type ibmBbcmProtocolCacheAge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 214748364),
    )


_IbmBbcmProtocolCacheAge_Type.__name__ = "Integer32"
_IbmBbcmProtocolCacheAge_Object = MibTableColumn
ibmBbcmProtocolCacheAge = _IbmBbcmProtocolCacheAge_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 2, 1, 3, 1, 4),
    _IbmBbcmProtocolCacheAge_Type()
)
ibmBbcmProtocolCacheAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmBbcmProtocolCacheAge.setStatus("mandatory")
_IbmBbcmStatsGroup_ObjectIdentity = ObjectIdentity
ibmBbcmStatsGroup = _IbmBbcmStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 2, 2)
)
_IbmBbcmStatTable_Object = MibTable
ibmBbcmStatTable = _IbmBbcmStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 2, 2, 1)
)
if mibBuilder.loadTexts:
    ibmBbcmStatTable.setStatus("mandatory")
_IbmBbcmStatEntry_Object = MibTableRow
ibmBbcmStatEntry = _IbmBbcmStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 2, 2, 1, 1)
)
ibmBbcmStatEntry.setIndexNames(
    (0, "IBM-LAN-EMULATION-EXTENSION-MIB", "ibmBbcmStatProtocolType"),
    (0, "IBM-LAN-EMULATION-EXTENSION-MIB", "ibmBbcmConfigIndex"),
)
if mibBuilder.loadTexts:
    ibmBbcmStatEntry.setStatus("mandatory")


class _IbmBbcmStatProtocolType_Type(Integer32):
    """Custom type ibmBbcmStatProtocolType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allprotocols", 1),
          ("ip", 2))
    )


_IbmBbcmStatProtocolType_Type.__name__ = "Integer32"
_IbmBbcmStatProtocolType_Object = MibTableColumn
ibmBbcmStatProtocolType = _IbmBbcmStatProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 2, 2, 1, 1, 1),
    _IbmBbcmStatProtocolType_Type()
)
ibmBbcmStatProtocolType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ibmBbcmStatProtocolType.setStatus("mandatory")
_IbmBbcmStatInReceives_Type = Counter32
_IbmBbcmStatInReceives_Object = MibTableColumn
ibmBbcmStatInReceives = _IbmBbcmStatInReceives_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 2, 2, 1, 1, 2),
    _IbmBbcmStatInReceives_Type()
)
ibmBbcmStatInReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmBbcmStatInReceives.setStatus("mandatory")
_IbmBbcmStatInOctets_Type = Counter32
_IbmBbcmStatInOctets_Object = MibTableColumn
ibmBbcmStatInOctets = _IbmBbcmStatInOctets_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 2, 2, 1, 1, 3),
    _IbmBbcmStatInOctets_Type()
)
ibmBbcmStatInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmBbcmStatInOctets.setStatus("mandatory")
_IbmBbcmStatOutManaged_Type = Counter32
_IbmBbcmStatOutManaged_Object = MibTableColumn
ibmBbcmStatOutManaged = _IbmBbcmStatOutManaged_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 2, 2, 1, 1, 4),
    _IbmBbcmStatOutManaged_Type()
)
ibmBbcmStatOutManaged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmBbcmStatOutManaged.setStatus("mandatory")
_IbmBbcmStatOutManagedOctets_Type = Counter32
_IbmBbcmStatOutManagedOctets_Object = MibTableColumn
ibmBbcmStatOutManagedOctets = _IbmBbcmStatOutManagedOctets_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 2, 2, 1, 1, 5),
    _IbmBbcmStatOutManagedOctets_Type()
)
ibmBbcmStatOutManagedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmBbcmStatOutManagedOctets.setStatus("mandatory")
_IbmBbcmStatOutNotManaged_Type = Counter32
_IbmBbcmStatOutNotManaged_Object = MibTableColumn
ibmBbcmStatOutNotManaged = _IbmBbcmStatOutNotManaged_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 2, 2, 1, 1, 6),
    _IbmBbcmStatOutNotManaged_Type()
)
ibmBbcmStatOutNotManaged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmBbcmStatOutNotManaged.setStatus("mandatory")
_IbmBbcmStatOutNotManagedOctets_Type = Counter32
_IbmBbcmStatOutNotManagedOctets_Object = MibTableColumn
ibmBbcmStatOutNotManagedOctets = _IbmBbcmStatOutNotManagedOctets_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 2, 2, 1, 1, 7),
    _IbmBbcmStatOutNotManagedOctets_Type()
)
ibmBbcmStatOutNotManagedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmBbcmStatOutNotManagedOctets.setStatus("mandatory")
_IbmBbcmStatOutFiltered_Type = Counter32
_IbmBbcmStatOutFiltered_Object = MibTableColumn
ibmBbcmStatOutFiltered = _IbmBbcmStatOutFiltered_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 2, 2, 1, 1, 8),
    _IbmBbcmStatOutFiltered_Type()
)
ibmBbcmStatOutFiltered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmBbcmStatOutFiltered.setStatus("mandatory")
_IbmBbcmStatOutFilteredOctets_Type = Counter32
_IbmBbcmStatOutFilteredOctets_Object = MibTableColumn
ibmBbcmStatOutFilteredOctets = _IbmBbcmStatOutFilteredOctets_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 2, 2, 1, 1, 9),
    _IbmBbcmStatOutFilteredOctets_Type()
)
ibmBbcmStatOutFilteredOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmBbcmStatOutFilteredOctets.setStatus("mandatory")
_IbmVlan_ObjectIdentity = ObjectIdentity
ibmVlan = _IbmVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 3)
)
_IbmVlanGGroup_ObjectIdentity = ObjectIdentity
ibmVlanGGroup = _IbmVlanGGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 3, 1)
)
_IbmVlanGOGroup_ObjectIdentity = ObjectIdentity
ibmVlanGOGroup = _IbmVlanGOGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 3, 1, 1)
)
_IbmVlanConfIndexNextID_Type = IbmVlanIndex
_IbmVlanConfIndexNextID_Object = MibScalar
ibmVlanConfIndexNextID = _IbmVlanConfIndexNextID_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 3, 1, 1, 1),
    _IbmVlanConfIndexNextID_Type()
)
ibmVlanConfIndexNextID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmVlanConfIndexNextID.setStatus("mandatory")
_IbmVlanTopologyChange_Type = TimeStamp
_IbmVlanTopologyChange_Object = MibScalar
ibmVlanTopologyChange = _IbmVlanTopologyChange_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 3, 1, 1, 2),
    _IbmVlanTopologyChange_Type()
)
ibmVlanTopologyChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmVlanTopologyChange.setStatus("mandatory")
_IbmVlanMaxPortMap_Type = Integer32
_IbmVlanMaxPortMap_Object = MibScalar
ibmVlanMaxPortMap = _IbmVlanMaxPortMap_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 3, 1, 1, 3),
    _IbmVlanMaxPortMap_Type()
)
ibmVlanMaxPortMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmVlanMaxPortMap.setStatus("mandatory")
_IbmVlanMaxUDSWMaskFilter_Type = Integer32
_IbmVlanMaxUDSWMaskFilter_Object = MibScalar
ibmVlanMaxUDSWMaskFilter = _IbmVlanMaxUDSWMaskFilter_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 3, 1, 1, 4),
    _IbmVlanMaxUDSWMaskFilter_Type()
)
ibmVlanMaxUDSWMaskFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmVlanMaxUDSWMaskFilter.setStatus("mandatory")
_IbmVlanCGroup_ObjectIdentity = ObjectIdentity
ibmVlanCGroup = _IbmVlanCGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 3, 2)
)
_IbmVlanConfGroup_ObjectIdentity = ObjectIdentity
ibmVlanConfGroup = _IbmVlanConfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 3, 2, 1)
)
_IbmVlanConfTable_Object = MibTable
ibmVlanConfTable = _IbmVlanConfTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 3, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ibmVlanConfTable.setStatus("mandatory")
_IbmVlanConfEntry_Object = MibTableRow
ibmVlanConfEntry = _IbmVlanConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 3, 2, 1, 1, 1)
)
ibmVlanConfEntry.setIndexNames(
    (0, "IBM-LAN-EMULATION-EXTENSION-MIB", "ibmVlanConfIndex"),
)
if mibBuilder.loadTexts:
    ibmVlanConfEntry.setStatus("mandatory")
_IbmVlanConfIndex_Type = IbmVlanIndex
_IbmVlanConfIndex_Object = MibTableColumn
ibmVlanConfIndex = _IbmVlanConfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 3, 2, 1, 1, 1, 1),
    _IbmVlanConfIndex_Type()
)
ibmVlanConfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ibmVlanConfIndex.setStatus("mandatory")
_IbmVlanConfBridgeId_Type = IbmSEBridgeID
_IbmVlanConfBridgeId_Object = MibTableColumn
ibmVlanConfBridgeId = _IbmVlanConfBridgeId_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 3, 2, 1, 1, 1, 2),
    _IbmVlanConfBridgeId_Type()
)
ibmVlanConfBridgeId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmVlanConfBridgeId.setStatus("mandatory")
_IbmVlanConfType_Type = IbmVlanType
_IbmVlanConfType_Object = MibTableColumn
ibmVlanConfType = _IbmVlanConfType_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 3, 2, 1, 1, 1, 3),
    _IbmVlanConfType_Type()
)
ibmVlanConfType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmVlanConfType.setStatus("mandatory")


class _IbmVlanConfAgingTimer_Type(Unsigned32):
    """Custom type ibmVlanConfAgingTimer based on Unsigned32"""
    defaultValue = 5000


_IbmVlanConfAgingTimer_Object = MibTableColumn
ibmVlanConfAgingTimer = _IbmVlanConfAgingTimer_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 3, 2, 1, 1, 1, 4),
    _IbmVlanConfAgingTimer_Type()
)
ibmVlanConfAgingTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmVlanConfAgingTimer.setStatus("mandatory")
_IbmVlanConfForwardingPortMap_Type = IbmVlanPortMap
_IbmVlanConfForwardingPortMap_Object = MibTableColumn
ibmVlanConfForwardingPortMap = _IbmVlanConfForwardingPortMap_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 3, 2, 1, 1, 1, 5),
    _IbmVlanConfForwardingPortMap_Type()
)
ibmVlanConfForwardingPortMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmVlanConfForwardingPortMap.setStatus("mandatory")


class _IbmVlanConfIncludedPortMap_Type(IbmVlanPortMap):
    """Custom type ibmVlanConfIncludedPortMap based on IbmVlanPortMap"""
    defaultHexValue = "0"


_IbmVlanConfIncludedPortMap_Object = MibTableColumn
ibmVlanConfIncludedPortMap = _IbmVlanConfIncludedPortMap_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 3, 2, 1, 1, 1, 6),
    _IbmVlanConfIncludedPortMap_Type()
)
ibmVlanConfIncludedPortMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmVlanConfIncludedPortMap.setStatus("mandatory")


class _IbmVlanConfExcludedPortMap_Type(IbmVlanPortMap):
    """Custom type ibmVlanConfExcludedPortMap based on IbmVlanPortMap"""
    defaultHexValue = "0"


_IbmVlanConfExcludedPortMap_Object = MibTableColumn
ibmVlanConfExcludedPortMap = _IbmVlanConfExcludedPortMap_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 3, 2, 1, 1, 1, 7),
    _IbmVlanConfExcludedPortMap_Type()
)
ibmVlanConfExcludedPortMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmVlanConfExcludedPortMap.setStatus("mandatory")


class _IbmVlanConfName_Type(DisplayString):
    """Custom type ibmVlanConfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_IbmVlanConfName_Type.__name__ = "DisplayString"
_IbmVlanConfName_Object = MibTableColumn
ibmVlanConfName = _IbmVlanConfName_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 3, 2, 1, 1, 1, 8),
    _IbmVlanConfName_Type()
)
ibmVlanConfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmVlanConfName.setStatus("mandatory")
_IbmVlanConfRowStatus_Type = RowStatus
_IbmVlanConfRowStatus_Object = MibTableColumn
ibmVlanConfRowStatus = _IbmVlanConfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 3, 2, 1, 1, 1, 9),
    _IbmVlanConfRowStatus_Type()
)
ibmVlanConfRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmVlanConfRowStatus.setStatus("mandatory")
_IbmVlanIpConfTable_Object = MibTable
ibmVlanIpConfTable = _IbmVlanIpConfTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 3, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ibmVlanIpConfTable.setStatus("mandatory")
_IbmVlanIpConfEntry_Object = MibTableRow
ibmVlanIpConfEntry = _IbmVlanIpConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 3, 2, 1, 2, 1)
)
ibmVlanIpConfEntry.setIndexNames(
    (0, "IBM-LAN-EMULATION-EXTENSION-MIB", "ibmVlanConfIndex"),
)
if mibBuilder.loadTexts:
    ibmVlanIpConfEntry.setStatus("mandatory")
_IbmVlanIpNetworkAddr_Type = IpAddress
_IbmVlanIpNetworkAddr_Object = MibTableColumn
ibmVlanIpNetworkAddr = _IbmVlanIpNetworkAddr_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 3, 2, 1, 2, 1, 1),
    _IbmVlanIpNetworkAddr_Type()
)
ibmVlanIpNetworkAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmVlanIpNetworkAddr.setStatus("mandatory")
_IbmVlanIpNetworkMask_Type = IpAddress
_IbmVlanIpNetworkMask_Object = MibTableColumn
ibmVlanIpNetworkMask = _IbmVlanIpNetworkMask_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 3, 2, 1, 2, 1, 2),
    _IbmVlanIpNetworkMask_Type()
)
ibmVlanIpNetworkMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmVlanIpNetworkMask.setStatus("mandatory")


class _IbmVlanIpCutThruFromHere_Type(Integer32):
    """Custom type ibmVlanIpCutThruFromHere based on Integer32"""
    defaultValue = 2

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


_IbmVlanIpCutThruFromHere_Type.__name__ = "Integer32"
_IbmVlanIpCutThruFromHere_Object = MibTableColumn
ibmVlanIpCutThruFromHere = _IbmVlanIpCutThruFromHere_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 3, 2, 1, 2, 1, 3),
    _IbmVlanIpCutThruFromHere_Type()
)
ibmVlanIpCutThruFromHere.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmVlanIpCutThruFromHere.setStatus("mandatory")


class _IbmVlanIpCutThruToHere_Type(Integer32):
    """Custom type ibmVlanIpCutThruToHere based on Integer32"""
    defaultValue = 2

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


_IbmVlanIpCutThruToHere_Type.__name__ = "Integer32"
_IbmVlanIpCutThruToHere_Object = MibTableColumn
ibmVlanIpCutThruToHere = _IbmVlanIpCutThruToHere_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 3, 2, 1, 2, 1, 4),
    _IbmVlanIpCutThruToHere_Type()
)
ibmVlanIpCutThruToHere.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmVlanIpCutThruToHere.setStatus("mandatory")
_IbmVlanIpxConfTable_Object = MibTable
ibmVlanIpxConfTable = _IbmVlanIpxConfTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 3, 2, 1, 3)
)
if mibBuilder.loadTexts:
    ibmVlanIpxConfTable.setStatus("mandatory")
_IbmVlanIpxConfEntry_Object = MibTableRow
ibmVlanIpxConfEntry = _IbmVlanIpxConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 3, 2, 1, 3, 1)
)
ibmVlanIpxConfEntry.setIndexNames(
    (0, "IBM-LAN-EMULATION-EXTENSION-MIB", "ibmVlanConfIndex"),
)
if mibBuilder.loadTexts:
    ibmVlanIpxConfEntry.setStatus("mandatory")


class _IbmVlanIpxNetworkAddr_Type(OctetString):
    """Custom type ibmVlanIpxNetworkAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_IbmVlanIpxNetworkAddr_Type.__name__ = "OctetString"
_IbmVlanIpxNetworkAddr_Object = MibTableColumn
ibmVlanIpxNetworkAddr = _IbmVlanIpxNetworkAddr_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 3, 2, 1, 3, 1, 1),
    _IbmVlanIpxNetworkAddr_Type()
)
ibmVlanIpxNetworkAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmVlanIpxNetworkAddr.setStatus("mandatory")
_IbmVlanUDSWConfTable_Object = MibTable
ibmVlanUDSWConfTable = _IbmVlanUDSWConfTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 3, 2, 1, 4)
)
if mibBuilder.loadTexts:
    ibmVlanUDSWConfTable.setStatus("mandatory")
_IbmVlanUDSWConfEntry_Object = MibTableRow
ibmVlanUDSWConfEntry = _IbmVlanUDSWConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 3, 2, 1, 4, 1)
)
ibmVlanUDSWConfEntry.setIndexNames(
    (0, "IBM-LAN-EMULATION-EXTENSION-MIB", "ibmVlanConfIndex"),
)
if mibBuilder.loadTexts:
    ibmVlanUDSWConfEntry.setStatus("mandatory")


class _IbmVlanUDSWOffsetType_Type(Integer32):
    """Custom type ibmVlanUDSWOffsetType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("udswInfoOffset", 2),
          ("udswMacOffset", 1))
    )


_IbmVlanUDSWOffsetType_Type.__name__ = "Integer32"
_IbmVlanUDSWOffsetType_Object = MibTableColumn
ibmVlanUDSWOffsetType = _IbmVlanUDSWOffsetType_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 3, 2, 1, 4, 1, 1),
    _IbmVlanUDSWOffsetType_Type()
)
ibmVlanUDSWOffsetType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmVlanUDSWOffsetType.setStatus("mandatory")


class _IbmVlanUDSWOffset_Type(Integer32):
    """Custom type ibmVlanUDSWOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbmVlanUDSWOffset_Type.__name__ = "Integer32"
_IbmVlanUDSWOffset_Object = MibTableColumn
ibmVlanUDSWOffset = _IbmVlanUDSWOffset_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 3, 2, 1, 4, 1, 2),
    _IbmVlanUDSWOffset_Type()
)
ibmVlanUDSWOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmVlanUDSWOffset.setStatus("mandatory")


class _IbmVlanUDSWMask_Type(OctetString):
    """Custom type ibmVlanUDSWMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_IbmVlanUDSWMask_Type.__name__ = "OctetString"
_IbmVlanUDSWMask_Object = MibTableColumn
ibmVlanUDSWMask = _IbmVlanUDSWMask_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 3, 2, 1, 4, 1, 3),
    _IbmVlanUDSWMask_Type()
)
ibmVlanUDSWMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmVlanUDSWMask.setStatus("mandatory")


class _IbmVlanUDSWFilter_Type(OctetString):
    """Custom type ibmVlanUDSWFilter based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_IbmVlanUDSWFilter_Type.__name__ = "OctetString"
_IbmVlanUDSWFilter_Object = MibTableColumn
ibmVlanUDSWFilter = _IbmVlanUDSWFilter_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 3, 2, 1, 4, 1, 4),
    _IbmVlanUDSWFilter_Type()
)
ibmVlanUDSWFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmVlanUDSWFilter.setStatus("mandatory")
_IbmVlanMacConfTable_Object = MibTable
ibmVlanMacConfTable = _IbmVlanMacConfTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 3, 2, 1, 5)
)
if mibBuilder.loadTexts:
    ibmVlanMacConfTable.setStatus("mandatory")
_IbmVlanMacConfEntry_Object = MibTableRow
ibmVlanMacConfEntry = _IbmVlanMacConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 3, 2, 1, 5, 1)
)
ibmVlanMacConfEntry.setIndexNames(
    (0, "IBM-LAN-EMULATION-EXTENSION-MIB", "ibmVlanConfIndex"),
    (0, "IBM-LAN-EMULATION-EXTENSION-MIB", "ibmVlanMacAddrIndex"),
)
if mibBuilder.loadTexts:
    ibmVlanMacConfEntry.setStatus("mandatory")
_IbmVlanMacAddrIndex_Type = Integer32
_IbmVlanMacAddrIndex_Object = MibTableColumn
ibmVlanMacAddrIndex = _IbmVlanMacAddrIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 3, 2, 1, 5, 1, 1),
    _IbmVlanMacAddrIndex_Type()
)
ibmVlanMacAddrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ibmVlanMacAddrIndex.setStatus("mandatory")


class _IbmVlanMacAddresses_Type(OctetString):
    """Custom type ibmVlanMacAddresses based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 600),
    )


_IbmVlanMacAddresses_Type.__name__ = "OctetString"
_IbmVlanMacAddresses_Object = MibTableColumn
ibmVlanMacAddresses = _IbmVlanMacAddresses_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 3, 2, 1, 5, 1, 2),
    _IbmVlanMacAddresses_Type()
)
ibmVlanMacAddresses.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmVlanMacAddresses.setStatus("mandatory")
_IbmVlanMacAddrConfRowStatus_Type = RowStatus
_IbmVlanMacAddrConfRowStatus_Object = MibTableColumn
ibmVlanMacAddrConfRowStatus = _IbmVlanMacAddrConfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 3, 2, 1, 5, 1, 3),
    _IbmVlanMacAddrConfRowStatus_Type()
)
ibmVlanMacAddrConfRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmVlanMacAddrConfRowStatus.setStatus("mandatory")
_IbmVlanStatusGroup_ObjectIdentity = ObjectIdentity
ibmVlanStatusGroup = _IbmVlanStatusGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 3, 3)
)
_IbmVlanStatusTable_Object = MibTable
ibmVlanStatusTable = _IbmVlanStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 3, 3, 1)
)
if mibBuilder.loadTexts:
    ibmVlanStatusTable.setStatus("mandatory")
_IbmVlanStatusEntry_Object = MibTableRow
ibmVlanStatusEntry = _IbmVlanStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 3, 3, 1, 1)
)
ibmVlanStatusEntry.setIndexNames(
    (0, "IBM-LAN-EMULATION-EXTENSION-MIB", "ibmVlanConfIndex"),
)
if mibBuilder.loadTexts:
    ibmVlanStatusEntry.setStatus("mandatory")


class _IbmVlanOperStatus_Type(Integer32):
    """Custom type ibmVlanOperStatus based on Integer32"""
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


_IbmVlanOperStatus_Type.__name__ = "Integer32"
_IbmVlanOperStatus_Object = MibTableColumn
ibmVlanOperStatus = _IbmVlanOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 3, 3, 1, 1, 1),
    _IbmVlanOperStatus_Type()
)
ibmVlanOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmVlanOperStatus.setStatus("mandatory")


class _IbmVlanAdminStatus_Type(Integer32):
    """Custom type ibmVlanAdminStatus based on Integer32"""
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


_IbmVlanAdminStatus_Type.__name__ = "Integer32"
_IbmVlanAdminStatus_Object = MibTableColumn
ibmVlanAdminStatus = _IbmVlanAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 3, 3, 1, 1, 2),
    _IbmVlanAdminStatus_Type()
)
ibmVlanAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmVlanAdminStatus.setStatus("mandatory")
_IbmVlanProcessedPackets_Type = Counter32
_IbmVlanProcessedPackets_Object = MibTableColumn
ibmVlanProcessedPackets = _IbmVlanProcessedPackets_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 3, 3, 1, 1, 3),
    _IbmVlanProcessedPackets_Type()
)
ibmVlanProcessedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmVlanProcessedPackets.setStatus("mandatory")
_IbmVlanDiscardedPackets_Type = Counter32
_IbmVlanDiscardedPackets_Object = MibTableColumn
ibmVlanDiscardedPackets = _IbmVlanDiscardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 3, 3, 1, 1, 4),
    _IbmVlanDiscardedPackets_Type()
)
ibmVlanDiscardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmVlanDiscardedPackets.setStatus("mandatory")
_IbmVlanDiscPktsMac_Type = MacAddress
_IbmVlanDiscPktsMac_Object = MibTableColumn
ibmVlanDiscPktsMac = _IbmVlanDiscPktsMac_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 3, 3, 1, 1, 5),
    _IbmVlanDiscPktsMac_Type()
)
ibmVlanDiscPktsMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmVlanDiscPktsMac.setStatus("mandatory")
_IbmVlanIpStatusTable_Object = MibTable
ibmVlanIpStatusTable = _IbmVlanIpStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 3, 3, 2)
)
if mibBuilder.loadTexts:
    ibmVlanIpStatusTable.setStatus("mandatory")
_IbmVlanIpStatusEntry_Object = MibTableRow
ibmVlanIpStatusEntry = _IbmVlanIpStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 3, 3, 2, 1)
)
ibmVlanIpStatusEntry.setIndexNames(
    (0, "IBM-LAN-EMULATION-EXTENSION-MIB", "ibmVlanConfIndex"),
)
if mibBuilder.loadTexts:
    ibmVlanIpStatusEntry.setStatus("mandatory")
_IbmVlanIpCutThruFromPkts_Type = Counter32
_IbmVlanIpCutThruFromPkts_Object = MibTableColumn
ibmVlanIpCutThruFromPkts = _IbmVlanIpCutThruFromPkts_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 3, 3, 2, 1, 1),
    _IbmVlanIpCutThruFromPkts_Type()
)
ibmVlanIpCutThruFromPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmVlanIpCutThruFromPkts.setStatus("mandatory")
_IbmVlanIpCutThruToPkts_Type = Counter32
_IbmVlanIpCutThruToPkts_Object = MibTableColumn
ibmVlanIpCutThruToPkts = _IbmVlanIpCutThruToPkts_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 3, 3, 2, 1, 2),
    _IbmVlanIpCutThruToPkts_Type()
)
ibmVlanIpCutThruToPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmVlanIpCutThruToPkts.setStatus("mandatory")
_IbmVlanIpCutThruFromDiscPkts_Type = Counter32
_IbmVlanIpCutThruFromDiscPkts_Object = MibTableColumn
ibmVlanIpCutThruFromDiscPkts = _IbmVlanIpCutThruFromDiscPkts_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 3, 3, 2, 1, 3),
    _IbmVlanIpCutThruFromDiscPkts_Type()
)
ibmVlanIpCutThruFromDiscPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmVlanIpCutThruFromDiscPkts.setStatus("mandatory")
_IbmVlanIpCutThruToDiscPkts_Type = Counter32
_IbmVlanIpCutThruToDiscPkts_Object = MibTableColumn
ibmVlanIpCutThruToDiscPkts = _IbmVlanIpCutThruToDiscPkts_Object(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 4, 3, 3, 2, 1, 4),
    _IbmVlanIpCutThruToDiscPkts_Type()
)
ibmVlanIpCutThruToDiscPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmVlanIpCutThruToDiscPkts.setStatus("mandatory")
_IbmLeMIBConformance_ObjectIdentity = ObjectIdentity
ibmLeMIBConformance = _IbmLeMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 5)
)
_IbmLeMIBGroups_ObjectIdentity = ObjectIdentity
ibmLeMIBGroups = _IbmLeMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 5, 1)
)
_IbmLeCServerXMonLECSGroup_ObjectIdentity = ObjectIdentity
ibmLeCServerXMonLECSGroup = _IbmLeCServerXMonLECSGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 5, 1, 1)
)
_IbmLeCServerXMonLESGroup_ObjectIdentity = ObjectIdentity
ibmLeCServerXMonLESGroup = _IbmLeCServerXMonLESGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 5, 1, 2)
)
_IbmLeCServerXMonBUSGroup_ObjectIdentity = ObjectIdentity
ibmLeCServerXMonBUSGroup = _IbmLeCServerXMonBUSGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 5, 1, 3)
)
_IbmCSuperELANGroup_ObjectIdentity = ObjectIdentity
ibmCSuperELANGroup = _IbmCSuperELANGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 5, 1, 4)
)
_IbmCBbcmMIBGroup_ObjectIdentity = ObjectIdentity
ibmCBbcmMIBGroup = _IbmCBbcmMIBGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 5, 1, 5)
)
_IbmCVlanMIBGroup_ObjectIdentity = ObjectIdentity
ibmCVlanMIBGroup = _IbmCVlanMIBGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 5, 1, 6)
)
_IbmLeMIBCompliances_ObjectIdentity = ObjectIdentity
ibmLeMIBCompliances = _IbmLeMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 5, 2)
)
_IbmLeMIBCompliance_ObjectIdentity = ObjectIdentity
ibmLeMIBCompliance = _IbmLeMIBCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 5, 8, 5, 2, 1)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IBM-LAN-EMULATION-EXTENSION-MIB",
    **{"IbmSEBridgeID": IbmSEBridgeID,
       "IbmVlanPortMap": IbmVlanPortMap,
       "IbmVlanIndex": IbmVlanIndex,
       "IbmVlanType": IbmVlanType,
       "ibm": ibm,
       "ibmArchitecture": ibmArchitecture,
       "lanEmulation": lanEmulation,
       "ibmLeServerX": ibmLeServerX,
       "ibmLeServerXMonitoring": ibmLeServerXMonitoring,
       "ibmLeServerXMon": ibmLeServerXMon,
       "ibmLeServerXMonLecsInstances": ibmLeServerXMonLecsInstances,
       "ibmLeServerXMonLesInstances": ibmLeServerXMonLesInstances,
       "ibmLeServerXMonBusInstances": ibmLeServerXMonBusInstances,
       "ibmLeServerXLecsMonTable": ibmLeServerXLecsMonTable,
       "ibmLeServerXLecsMonEntry": ibmLeServerXLecsMonEntry,
       "ibmLeServerXLecsMonIndex": ibmLeServerXLecsMonIndex,
       "ibmLeServerXLecsUsedConnections": ibmLeServerXLecsUsedConnections,
       "ibmLeServerXLesMonTable": ibmLeServerXLesMonTable,
       "ibmLeServerXLesMonEntry": ibmLeServerXLesMonEntry,
       "ibmLeServerXLesMonIndex": ibmLeServerXLesMonIndex,
       "ibmLeServerXLesMonUsedConnections": ibmLeServerXLesMonUsedConnections,
       "ibmLeServerXLesMonLesLecInstances": ibmLeServerXLesMonLesLecInstances,
       "ibmLeServerXBusMonTable": ibmLeServerXBusMonTable,
       "ibmLeServerXBusMonEntry": ibmLeServerXBusMonEntry,
       "ibmLeServerXBusMonIndex": ibmLeServerXBusMonIndex,
       "ibmLeServerXBusMonUsedConnections": ibmLeServerXBusMonUsedConnections,
       "ibmLeServerXBusMonBusLecInstances": ibmLeServerXBusMonBusLecInstances,
       "ibmLeServerXConfig": ibmLeServerXConfig,
       "ibmLeServerXLesConfigTable": ibmLeServerXLesConfigTable,
       "ibmLeServerXLesConfigEntry": ibmLeServerXLesConfigEntry,
       "ibmLeServerXLesMinLecID": ibmLeServerXLesMinLecID,
       "ibmLeServerXLesMaxLecID": ibmLeServerXLesMaxLecID,
       "ibmLeClientX": ibmLeClientX,
       "ibmSuperELAN": ibmSuperELAN,
       "ibmSEPortStatisticsTable": ibmSEPortStatisticsTable,
       "ibmSEPortStatisticsEntry": ibmSEPortStatisticsEntry,
       "ibmSEBridgeId": ibmSEBridgeId,
       "ibmSEPortNum": ibmSEPortNum,
       "ibmSEPortArpRequestsIn": ibmSEPortArpRequestsIn,
       "ibmSEPortArpRequestsOut": ibmSEPortArpRequestsOut,
       "ibmSEArpRequestsErrors": ibmSEArpRequestsErrors,
       "ibmSEPortArpRequestsDroppedPortBlocked": ibmSEPortArpRequestsDroppedPortBlocked,
       "ibmSEPortArpRequestsFiltered": ibmSEPortArpRequestsFiltered,
       "ibmSEPortArpRepliesIn": ibmSEPortArpRepliesIn,
       "ibmSEPortArpRepliesOut": ibmSEPortArpRepliesOut,
       "ibmSEPortArpRepliesErrors": ibmSEPortArpRepliesErrors,
       "ibmSEPortNarpRequestsIn": ibmSEPortNarpRequestsIn,
       "ibmSEPortNarpRequestsOut": ibmSEPortNarpRequestsOut,
       "ibmSEPortNarpRequestsDroppedPortBlocked": ibmSEPortNarpRequestsDroppedPortBlocked,
       "ibmSEPortFlushRequestsIn": ibmSEPortFlushRequestsIn,
       "ibmSEPortFlushRequestsOut": ibmSEPortFlushRequestsOut,
       "ibmSEPortFlushRepliesIn": ibmSEPortFlushRepliesIn,
       "ibmSEPortFlushRepliesOut": ibmSEPortFlushRepliesOut,
       "ibmSEPortFlushRequestErrors": ibmSEPortFlushRequestErrors,
       "ibmSEPortFlushRepliesErrors": ibmSEPortFlushRepliesErrors,
       "ibmSEPortLeCtrlFramesIn": ibmSEPortLeCtrlFramesIn,
       "ibmSEPortLeCtrlFramesOut": ibmSEPortLeCtrlFramesOut,
       "ibmSEPortLeCtrlFramesDiscSrcPortNotFwrd": ibmSEPortLeCtrlFramesDiscSrcPortNotFwrd,
       "ibmSEPortLeCtrlFramesDiscDestPortNotFwrd": ibmSEPortLeCtrlFramesDiscDestPortNotFwrd,
       "ibmSEBridgeConfigTable": ibmSEBridgeConfigTable,
       "ibmSEBridgeConfigEntry": ibmSEBridgeConfigEntry,
       "ibmSEAtmIfNumber": ibmSEAtmIfNumber,
       "ibmSEEnabled": ibmSEEnabled,
       "ibmSEName": ibmSEName,
       "ibmSEFrameSize": ibmSEFrameSize,
       "ibmSEMacCacheAge": ibmSEMacCacheAge,
       "ibmSERDCacheAge": ibmSERDCacheAge,
       "ibmSEPriority": ibmSEPriority,
       "ibmSEMaxAge": ibmSEMaxAge,
       "ibmSEBridgeHelloTime": ibmSEBridgeHelloTime,
       "ibmSEBridgeForwardDelay": ibmSEBridgeForwardDelay,
       "ibmSEBridgeAddress": ibmSEBridgeAddress,
       "ibmSEType": ibmSEType,
       "ibmSEConfigRowStatus": ibmSEConfigRowStatus,
       "ibmSEPortConfigTable": ibmSEPortConfigTable,
       "ibmSEPortConfigEntry": ibmSEPortConfigEntry,
       "ibmSEPortIfNumber": ibmSEPortIfNumber,
       "ibmSEPortElanName": ibmSEPortElanName,
       "ibmSEPortRemoteElan": ibmSEPortRemoteElan,
       "ibmSEPortEnabled": ibmSEPortEnabled,
       "ibmSEPortPriority": ibmSEPortPriority,
       "ibmSEPortRootCost": ibmSEPortRootCost,
       "ibmSEPortRowStatus": ibmSEPortRowStatus,
       "ibmSEBridgeTable": ibmSEBridgeTable,
       "ibmSEBridgeEntry": ibmSEBridgeEntry,
       "ibmSENumPorts": ibmSENumPorts,
       "ibmSEProtocolSpecification": ibmSEProtocolSpecification,
       "ibmSETimeSinceTopologyChange": ibmSETimeSinceTopologyChange,
       "ibmSETopChanges": ibmSETopChanges,
       "ibmSEDesignatedRoot": ibmSEDesignatedRoot,
       "ibmSERootCost": ibmSERootCost,
       "ibmSERootPort": ibmSERootPort,
       "ibmSEBridgeMaxAge": ibmSEBridgeMaxAge,
       "ibmSEHelloTime": ibmSEHelloTime,
       "ibmSEHoldTime": ibmSEHoldTime,
       "ibmSEForwardDelay": ibmSEForwardDelay,
       "ibmSEMacLearnedEntryDiscards": ibmSEMacLearnedEntryDiscards,
       "ibmSERDLearnedEntryDiscards": ibmSERDLearnedEntryDiscards,
       "ibmSEStpPortTable": ibmSEStpPortTable,
       "ibmSEStpPortEntry": ibmSEStpPortEntry,
       "ibmSEStpPortState": ibmSEStpPortState,
       "ibmSEStpPortDesignatedRoot": ibmSEStpPortDesignatedRoot,
       "ibmSEStpPortDesignatedCost": ibmSEStpPortDesignatedCost,
       "ibmSEStpPortDesignatedBridge": ibmSEStpPortDesignatedBridge,
       "ibmSEStpPortDesignatedPort": ibmSEStpPortDesignatedPort,
       "ibmSEStpPortForwardTransitions": ibmSEStpPortForwardTransitions,
       "ibmSEPortMaxInfo": ibmSEPortMaxInfo,
       "ibmSEPortDataStatisticsTable": ibmSEPortDataStatisticsTable,
       "ibmSEPortDataStatisticsEntry": ibmSEPortDataStatisticsEntry,
       "ibmSEPortInFrames": ibmSEPortInFrames,
       "ibmSEPortOutFrames": ibmSEPortOutFrames,
       "ibmSEPortRoutedInFrames": ibmSEPortRoutedInFrames,
       "ibmSEPortBpduFrames": ibmSEPortBpduFrames,
       "ibmSEPortInDiscards": ibmSEPortInDiscards,
       "ibmSEPortDropSrcAddrFilters": ibmSEPortDropSrcAddrFilters,
       "ibmSEPortDropDestAddrFilters": ibmSEPortDropDestAddrFilters,
       "ibmSEPortDropProtocolFilters": ibmSEPortDropProtocolFilters,
       "ibmSEPortDropSrcNotFwds": ibmSEPortDropSrcNotFwds,
       "ibmSEPortDropDestNotFwds": ibmSEPortDropDestNotFwds,
       "ibmSEPortDropInputOverflows": ibmSEPortDropInputOverflows,
       "ibmSEPortDropBpduOverflows": ibmSEPortDropBpduOverflows,
       "ibmSEPortDropSrOverflows": ibmSEPortDropSrOverflows,
       "ibmSEPortRecNoBuffFailures": ibmSEPortRecNoBuffFailures,
       "ibmSEPortTransmitFailures": ibmSEPortTransmitFailures,
       "ibmSEPortToBigFailures": ibmSEPortToBigFailures,
       "ibmSEPortLanIdFailures": ibmSEPortLanIdFailures,
       "ibmSEPortStpLanIdFailures": ibmSEPortStpLanIdFailures,
       "ibmBbcmMIB": ibmBbcmMIB,
       "ibmBbcmConfigGroup": ibmBbcmConfigGroup,
       "ibmBbcmConfigNextId": ibmBbcmConfigNextId,
       "ibmBbcmConfigTable": ibmBbcmConfigTable,
       "ibmBbcmConfigEntry": ibmBbcmConfigEntry,
       "ibmBbcmConfigIndex": ibmBbcmConfigIndex,
       "ibmBbcmName": ibmBbcmName,
       "ibmBbcmConfigRowStatus": ibmBbcmConfigRowStatus,
       "ibmBbcmProtocolConfigTable": ibmBbcmProtocolConfigTable,
       "ibmBbcmProtocolConfigEntry": ibmBbcmProtocolConfigEntry,
       "ibmBbcmProtocolType": ibmBbcmProtocolType,
       "ibmBbcmProtocolOperStatus": ibmBbcmProtocolOperStatus,
       "ibmBbcmProtocolAdminStatus": ibmBbcmProtocolAdminStatus,
       "ibmBbcmProtocolCacheAge": ibmBbcmProtocolCacheAge,
       "ibmBbcmStatsGroup": ibmBbcmStatsGroup,
       "ibmBbcmStatTable": ibmBbcmStatTable,
       "ibmBbcmStatEntry": ibmBbcmStatEntry,
       "ibmBbcmStatProtocolType": ibmBbcmStatProtocolType,
       "ibmBbcmStatInReceives": ibmBbcmStatInReceives,
       "ibmBbcmStatInOctets": ibmBbcmStatInOctets,
       "ibmBbcmStatOutManaged": ibmBbcmStatOutManaged,
       "ibmBbcmStatOutManagedOctets": ibmBbcmStatOutManagedOctets,
       "ibmBbcmStatOutNotManaged": ibmBbcmStatOutNotManaged,
       "ibmBbcmStatOutNotManagedOctets": ibmBbcmStatOutNotManagedOctets,
       "ibmBbcmStatOutFiltered": ibmBbcmStatOutFiltered,
       "ibmBbcmStatOutFilteredOctets": ibmBbcmStatOutFilteredOctets,
       "ibmVlan": ibmVlan,
       "ibmVlanGGroup": ibmVlanGGroup,
       "ibmVlanGOGroup": ibmVlanGOGroup,
       "ibmVlanConfIndexNextID": ibmVlanConfIndexNextID,
       "ibmVlanTopologyChange": ibmVlanTopologyChange,
       "ibmVlanMaxPortMap": ibmVlanMaxPortMap,
       "ibmVlanMaxUDSWMaskFilter": ibmVlanMaxUDSWMaskFilter,
       "ibmVlanCGroup": ibmVlanCGroup,
       "ibmVlanConfGroup": ibmVlanConfGroup,
       "ibmVlanConfTable": ibmVlanConfTable,
       "ibmVlanConfEntry": ibmVlanConfEntry,
       "ibmVlanConfIndex": ibmVlanConfIndex,
       "ibmVlanConfBridgeId": ibmVlanConfBridgeId,
       "ibmVlanConfType": ibmVlanConfType,
       "ibmVlanConfAgingTimer": ibmVlanConfAgingTimer,
       "ibmVlanConfForwardingPortMap": ibmVlanConfForwardingPortMap,
       "ibmVlanConfIncludedPortMap": ibmVlanConfIncludedPortMap,
       "ibmVlanConfExcludedPortMap": ibmVlanConfExcludedPortMap,
       "ibmVlanConfName": ibmVlanConfName,
       "ibmVlanConfRowStatus": ibmVlanConfRowStatus,
       "ibmVlanIpConfTable": ibmVlanIpConfTable,
       "ibmVlanIpConfEntry": ibmVlanIpConfEntry,
       "ibmVlanIpNetworkAddr": ibmVlanIpNetworkAddr,
       "ibmVlanIpNetworkMask": ibmVlanIpNetworkMask,
       "ibmVlanIpCutThruFromHere": ibmVlanIpCutThruFromHere,
       "ibmVlanIpCutThruToHere": ibmVlanIpCutThruToHere,
       "ibmVlanIpxConfTable": ibmVlanIpxConfTable,
       "ibmVlanIpxConfEntry": ibmVlanIpxConfEntry,
       "ibmVlanIpxNetworkAddr": ibmVlanIpxNetworkAddr,
       "ibmVlanUDSWConfTable": ibmVlanUDSWConfTable,
       "ibmVlanUDSWConfEntry": ibmVlanUDSWConfEntry,
       "ibmVlanUDSWOffsetType": ibmVlanUDSWOffsetType,
       "ibmVlanUDSWOffset": ibmVlanUDSWOffset,
       "ibmVlanUDSWMask": ibmVlanUDSWMask,
       "ibmVlanUDSWFilter": ibmVlanUDSWFilter,
       "ibmVlanMacConfTable": ibmVlanMacConfTable,
       "ibmVlanMacConfEntry": ibmVlanMacConfEntry,
       "ibmVlanMacAddrIndex": ibmVlanMacAddrIndex,
       "ibmVlanMacAddresses": ibmVlanMacAddresses,
       "ibmVlanMacAddrConfRowStatus": ibmVlanMacAddrConfRowStatus,
       "ibmVlanStatusGroup": ibmVlanStatusGroup,
       "ibmVlanStatusTable": ibmVlanStatusTable,
       "ibmVlanStatusEntry": ibmVlanStatusEntry,
       "ibmVlanOperStatus": ibmVlanOperStatus,
       "ibmVlanAdminStatus": ibmVlanAdminStatus,
       "ibmVlanProcessedPackets": ibmVlanProcessedPackets,
       "ibmVlanDiscardedPackets": ibmVlanDiscardedPackets,
       "ibmVlanDiscPktsMac": ibmVlanDiscPktsMac,
       "ibmVlanIpStatusTable": ibmVlanIpStatusTable,
       "ibmVlanIpStatusEntry": ibmVlanIpStatusEntry,
       "ibmVlanIpCutThruFromPkts": ibmVlanIpCutThruFromPkts,
       "ibmVlanIpCutThruToPkts": ibmVlanIpCutThruToPkts,
       "ibmVlanIpCutThruFromDiscPkts": ibmVlanIpCutThruFromDiscPkts,
       "ibmVlanIpCutThruToDiscPkts": ibmVlanIpCutThruToDiscPkts,
       "ibmLeMIBConformance": ibmLeMIBConformance,
       "ibmLeMIBGroups": ibmLeMIBGroups,
       "ibmLeCServerXMonLECSGroup": ibmLeCServerXMonLECSGroup,
       "ibmLeCServerXMonLESGroup": ibmLeCServerXMonLESGroup,
       "ibmLeCServerXMonBUSGroup": ibmLeCServerXMonBUSGroup,
       "ibmCSuperELANGroup": ibmCSuperELANGroup,
       "ibmCBbcmMIBGroup": ibmCBbcmMIBGroup,
       "ibmCVlanMIBGroup": ibmCVlanMIBGroup,
       "ibmLeMIBCompliances": ibmLeMIBCompliances,
       "ibmLeMIBCompliance": ibmLeMIBCompliance}
)
