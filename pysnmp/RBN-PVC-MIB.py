# SNMP MIB module (RBN-PVC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RBN-PVC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:45:20 2024
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

(rbnMgmt,) = mibBuilder.importSymbols(
    "RBN-SMI",
    "rbnMgmt")

(RbnCircuitHandle,
 RbnPort,
 RbnSlot,
 RbnVidOrUntagged) = mibBuilder.importSymbols(
    "RBN-TC",
    "RbnCircuitHandle",
    "RbnPort",
    "RbnSlot",
    "RbnVidOrUntagged")

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
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

rbnPvcMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 7)
)
rbnPvcMib.setRevisions(
        ("2007-10-29 17:00",
         "2004-05-21 17:00",
         "2003-03-17 17:00",
         "2002-12-20 17:00",
         "2002-11-13 00:00",
         "2002-05-23 17:00",
         "2001-05-09 17:00",
         "2001-02-10 17:00",
         "2000-08-30 12:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class RbnFrameRelayEncapsulation(Integer32, TextualConvention):
    status = "current"
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("auto1490", 1),
          ("bridge1490", 2),
          ("clips1490", 11),
          ("dot1q1490", 10),
          ("l2tp", 5),
          ("l2tpVcMuxed", 6),
          ("multi1490", 3),
          ("ppp", 7),
          ("pppAuto", 8),
          ("pppAutoNopoe", 12),
          ("pppOverEthernet", 9),
          ("route1490", 4))
    )



class RbnAtmEncapsulation(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              15,
              16,
              17,
              18)
        )
    )
    namedValues = NamedValues(
        *(("auto1483", 1),
          ("bridge1483", 2),
          ("cell", 18),
          ("clips1483", 16),
          ("dot1q1483", 15),
          ("l2tp", 5),
          ("l2tpVcMuxed", 6),
          ("multi1483", 3),
          ("ppp", 7),
          ("pppAuto", 8),
          ("pppAutoNopoe", 17),
          ("pppLlc", 12),
          ("pppNlpid", 11),
          ("pppOverEthernet", 9),
          ("pppSerial", 10),
          ("pppVcMuxed", 13),
          ("raw", 14),
          ("route1483", 4),
          ("unknown", 0))
    )



class RbnDot1qEncapsulation(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
        *(("dot1qClips", 5),
          ("dot1qMulti", 2),
          ("dot1qRaw", 4),
          ("dot1qTunnelClips", 9),
          ("dot1qTunnelMulti", 6),
          ("dot1qTunnelPppOverEthernet", 7),
          ("dot1qTunnelRaw", 8),
          ("ipOverEthernet", 1),
          ("pppOverEthernet", 3),
          ("unknown", 0))
    )



class RbnPvcCircuitType(Integer32, TextualConvention):
    status = "current"
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
        *(("explicit", 1),
          ("explicitRange", 2),
          ("onDemandRange", 3),
          ("protection", 4))
    )



# MIB Managed Objects in the order of their OIDs

_RbnPvcMIBObjects_ObjectIdentity = ObjectIdentity
rbnPvcMIBObjects = _RbnPvcMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 7, 1)
)
_RbnAtmPvcConfigTable_Object = MibTable
rbnAtmPvcConfigTable = _RbnAtmPvcConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 7, 1, 1)
)
if mibBuilder.loadTexts:
    rbnAtmPvcConfigTable.setStatus("current")
_RbnAtmPvcConfigEntry_Object = MibTableRow
rbnAtmPvcConfigEntry = _RbnAtmPvcConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 7, 1, 1, 1)
)
rbnAtmPvcConfigEntry.setIndexNames(
    (0, "RBN-PVC-MIB", "rbnAtmPvcSlot"),
    (0, "RBN-PVC-MIB", "rbnAtmPvcPort"),
    (0, "RBN-PVC-MIB", "rbnAtmPvcVpi"),
    (0, "RBN-PVC-MIB", "rbnAtmPvcVci"),
)
if mibBuilder.loadTexts:
    rbnAtmPvcConfigEntry.setStatus("current")
_RbnAtmPvcSlot_Type = RbnSlot
_RbnAtmPvcSlot_Object = MibTableColumn
rbnAtmPvcSlot = _RbnAtmPvcSlot_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 7, 1, 1, 1, 1),
    _RbnAtmPvcSlot_Type()
)
rbnAtmPvcSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbnAtmPvcSlot.setStatus("current")
_RbnAtmPvcPort_Type = RbnPort
_RbnAtmPvcPort_Object = MibTableColumn
rbnAtmPvcPort = _RbnAtmPvcPort_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 7, 1, 1, 1, 2),
    _RbnAtmPvcPort_Type()
)
rbnAtmPvcPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbnAtmPvcPort.setStatus("current")


class _RbnAtmPvcVpi_Type(Unsigned32):
    """Custom type rbnAtmPvcVpi based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RbnAtmPvcVpi_Type.__name__ = "Unsigned32"
_RbnAtmPvcVpi_Object = MibTableColumn
rbnAtmPvcVpi = _RbnAtmPvcVpi_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 7, 1, 1, 1, 3),
    _RbnAtmPvcVpi_Type()
)
rbnAtmPvcVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbnAtmPvcVpi.setStatus("current")


class _RbnAtmPvcVci_Type(Unsigned32):
    """Custom type rbnAtmPvcVci based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RbnAtmPvcVci_Type.__name__ = "Unsigned32"
_RbnAtmPvcVci_Object = MibTableColumn
rbnAtmPvcVci = _RbnAtmPvcVci_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 7, 1, 1, 1, 4),
    _RbnAtmPvcVci_Type()
)
rbnAtmPvcVci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbnAtmPvcVci.setStatus("current")


class _RbnAtmPvcProfileName_Type(SnmpAdminString):
    """Custom type rbnAtmPvcProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_RbnAtmPvcProfileName_Type.__name__ = "SnmpAdminString"
_RbnAtmPvcProfileName_Object = MibTableColumn
rbnAtmPvcProfileName = _RbnAtmPvcProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 7, 1, 1, 1, 5),
    _RbnAtmPvcProfileName_Type()
)
rbnAtmPvcProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnAtmPvcProfileName.setStatus("current")
_RbnAtmPvcEncapsulation_Type = RbnAtmEncapsulation
_RbnAtmPvcEncapsulation_Object = MibTableColumn
rbnAtmPvcEncapsulation = _RbnAtmPvcEncapsulation_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 7, 1, 1, 1, 6),
    _RbnAtmPvcEncapsulation_Type()
)
rbnAtmPvcEncapsulation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnAtmPvcEncapsulation.setStatus("current")
_RbnAtmPvcRowStatus_Type = RowStatus
_RbnAtmPvcRowStatus_Object = MibTableColumn
rbnAtmPvcRowStatus = _RbnAtmPvcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 7, 1, 1, 1, 8),
    _RbnAtmPvcRowStatus_Type()
)
rbnAtmPvcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnAtmPvcRowStatus.setStatus("current")


class _RbnAtmPvcCircuitType_Type(RbnPvcCircuitType):
    """Custom type rbnAtmPvcCircuitType based on RbnPvcCircuitType"""


_RbnAtmPvcCircuitType_Object = MibTableColumn
rbnAtmPvcCircuitType = _RbnAtmPvcCircuitType_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 7, 1, 1, 1, 9),
    _RbnAtmPvcCircuitType_Type()
)
rbnAtmPvcCircuitType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnAtmPvcCircuitType.setStatus("current")
_RbnAtmPvcCircuitHandle_Type = RbnCircuitHandle
_RbnAtmPvcCircuitHandle_Object = MibTableColumn
rbnAtmPvcCircuitHandle = _RbnAtmPvcCircuitHandle_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 7, 1, 1, 1, 10),
    _RbnAtmPvcCircuitHandle_Type()
)
rbnAtmPvcCircuitHandle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnAtmPvcCircuitHandle.setStatus("current")


class _RbnAtmPvcClearCircuit_Type(TruthValue):
    """Custom type rbnAtmPvcClearCircuit based on TruthValue"""


_RbnAtmPvcClearCircuit_Object = MibTableColumn
rbnAtmPvcClearCircuit = _RbnAtmPvcClearCircuit_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 7, 1, 1, 1, 11),
    _RbnAtmPvcClearCircuit_Type()
)
rbnAtmPvcClearCircuit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnAtmPvcClearCircuit.setStatus("current")
_RbnFrameRelayPvcConfigTable_Object = MibTable
rbnFrameRelayPvcConfigTable = _RbnFrameRelayPvcConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 7, 1, 2)
)
if mibBuilder.loadTexts:
    rbnFrameRelayPvcConfigTable.setStatus("current")
_RbnFrameRelayPvcConfigEntry_Object = MibTableRow
rbnFrameRelayPvcConfigEntry = _RbnFrameRelayPvcConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 7, 1, 2, 1)
)
rbnFrameRelayPvcConfigEntry.setIndexNames(
    (0, "RBN-PVC-MIB", "rbnFrameRelayPvcSlot"),
    (0, "RBN-PVC-MIB", "rbnFrameRelayPvcPort"),
    (0, "RBN-PVC-MIB", "rbnFrameRelayPvcChannel"),
    (0, "RBN-PVC-MIB", "rbnFrameRelayPvcDLCI"),
)
if mibBuilder.loadTexts:
    rbnFrameRelayPvcConfigEntry.setStatus("current")
_RbnFrameRelayPvcSlot_Type = RbnSlot
_RbnFrameRelayPvcSlot_Object = MibTableColumn
rbnFrameRelayPvcSlot = _RbnFrameRelayPvcSlot_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 7, 1, 2, 1, 1),
    _RbnFrameRelayPvcSlot_Type()
)
rbnFrameRelayPvcSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbnFrameRelayPvcSlot.setStatus("current")
_RbnFrameRelayPvcPort_Type = RbnPort
_RbnFrameRelayPvcPort_Object = MibTableColumn
rbnFrameRelayPvcPort = _RbnFrameRelayPvcPort_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 7, 1, 2, 1, 2),
    _RbnFrameRelayPvcPort_Type()
)
rbnFrameRelayPvcPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbnFrameRelayPvcPort.setStatus("current")


class _RbnFrameRelayPvcChannel_Type(Unsigned32):
    """Custom type rbnFrameRelayPvcChannel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RbnFrameRelayPvcChannel_Type.__name__ = "Unsigned32"
_RbnFrameRelayPvcChannel_Object = MibTableColumn
rbnFrameRelayPvcChannel = _RbnFrameRelayPvcChannel_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 7, 1, 2, 1, 3),
    _RbnFrameRelayPvcChannel_Type()
)
rbnFrameRelayPvcChannel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbnFrameRelayPvcChannel.setStatus("current")


class _RbnFrameRelayPvcDLCI_Type(Unsigned32):
    """Custom type rbnFrameRelayPvcDLCI based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RbnFrameRelayPvcDLCI_Type.__name__ = "Unsigned32"
_RbnFrameRelayPvcDLCI_Object = MibTableColumn
rbnFrameRelayPvcDLCI = _RbnFrameRelayPvcDLCI_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 7, 1, 2, 1, 4),
    _RbnFrameRelayPvcDLCI_Type()
)
rbnFrameRelayPvcDLCI.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbnFrameRelayPvcDLCI.setStatus("current")


class _RbnFrameRelayPvcProfileName_Type(SnmpAdminString):
    """Custom type rbnFrameRelayPvcProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_RbnFrameRelayPvcProfileName_Type.__name__ = "SnmpAdminString"
_RbnFrameRelayPvcProfileName_Object = MibTableColumn
rbnFrameRelayPvcProfileName = _RbnFrameRelayPvcProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 7, 1, 2, 1, 5),
    _RbnFrameRelayPvcProfileName_Type()
)
rbnFrameRelayPvcProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnFrameRelayPvcProfileName.setStatus("current")
_RbnFrameRelayPvcEncapsulation_Type = RbnFrameRelayEncapsulation
_RbnFrameRelayPvcEncapsulation_Object = MibTableColumn
rbnFrameRelayPvcEncapsulation = _RbnFrameRelayPvcEncapsulation_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 7, 1, 2, 1, 6),
    _RbnFrameRelayPvcEncapsulation_Type()
)
rbnFrameRelayPvcEncapsulation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnFrameRelayPvcEncapsulation.setStatus("current")
_RbnFrameRelayPvcRowStatus_Type = RowStatus
_RbnFrameRelayPvcRowStatus_Object = MibTableColumn
rbnFrameRelayPvcRowStatus = _RbnFrameRelayPvcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 7, 1, 2, 1, 8),
    _RbnFrameRelayPvcRowStatus_Type()
)
rbnFrameRelayPvcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnFrameRelayPvcRowStatus.setStatus("current")


class _RbnFrameRelayPvcCircuitType_Type(RbnPvcCircuitType):
    """Custom type rbnFrameRelayPvcCircuitType based on RbnPvcCircuitType"""


_RbnFrameRelayPvcCircuitType_Object = MibTableColumn
rbnFrameRelayPvcCircuitType = _RbnFrameRelayPvcCircuitType_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 7, 1, 2, 1, 9),
    _RbnFrameRelayPvcCircuitType_Type()
)
rbnFrameRelayPvcCircuitType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnFrameRelayPvcCircuitType.setStatus("current")
_RbnFrameRelayPvcCircuitHandle_Type = RbnCircuitHandle
_RbnFrameRelayPvcCircuitHandle_Object = MibTableColumn
rbnFrameRelayPvcCircuitHandle = _RbnFrameRelayPvcCircuitHandle_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 7, 1, 2, 1, 10),
    _RbnFrameRelayPvcCircuitHandle_Type()
)
rbnFrameRelayPvcCircuitHandle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnFrameRelayPvcCircuitHandle.setStatus("current")
_RbnFrameRelayPvcClearCircuit_Type = TruthValue
_RbnFrameRelayPvcClearCircuit_Object = MibTableColumn
rbnFrameRelayPvcClearCircuit = _RbnFrameRelayPvcClearCircuit_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 7, 1, 2, 1, 11),
    _RbnFrameRelayPvcClearCircuit_Type()
)
rbnFrameRelayPvcClearCircuit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnFrameRelayPvcClearCircuit.setStatus("current")
_RbnDot1qPvcOnEthConfigTable_Object = MibTable
rbnDot1qPvcOnEthConfigTable = _RbnDot1qPvcOnEthConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 7, 1, 3)
)
if mibBuilder.loadTexts:
    rbnDot1qPvcOnEthConfigTable.setStatus("current")
_RbnDot1qPvcOnEthConfigEntry_Object = MibTableRow
rbnDot1qPvcOnEthConfigEntry = _RbnDot1qPvcOnEthConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 7, 1, 3, 1)
)
rbnDot1qPvcOnEthConfigEntry.setIndexNames(
    (0, "RBN-PVC-MIB", "rbnDot1qPvcOnEthSlot"),
    (0, "RBN-PVC-MIB", "rbnDot1qPvcOnEthPort"),
    (0, "RBN-PVC-MIB", "rbnDot1qPvcOnEthVlanId"),
)
if mibBuilder.loadTexts:
    rbnDot1qPvcOnEthConfigEntry.setStatus("current")
_RbnDot1qPvcOnEthSlot_Type = RbnSlot
_RbnDot1qPvcOnEthSlot_Object = MibTableColumn
rbnDot1qPvcOnEthSlot = _RbnDot1qPvcOnEthSlot_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 7, 1, 3, 1, 1),
    _RbnDot1qPvcOnEthSlot_Type()
)
rbnDot1qPvcOnEthSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbnDot1qPvcOnEthSlot.setStatus("current")
_RbnDot1qPvcOnEthPort_Type = RbnPort
_RbnDot1qPvcOnEthPort_Object = MibTableColumn
rbnDot1qPvcOnEthPort = _RbnDot1qPvcOnEthPort_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 7, 1, 3, 1, 2),
    _RbnDot1qPvcOnEthPort_Type()
)
rbnDot1qPvcOnEthPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbnDot1qPvcOnEthPort.setStatus("current")
_RbnDot1qPvcOnEthVlanId_Type = RbnVidOrUntagged
_RbnDot1qPvcOnEthVlanId_Object = MibTableColumn
rbnDot1qPvcOnEthVlanId = _RbnDot1qPvcOnEthVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 7, 1, 3, 1, 3),
    _RbnDot1qPvcOnEthVlanId_Type()
)
rbnDot1qPvcOnEthVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbnDot1qPvcOnEthVlanId.setStatus("current")
_RbnDot1qPvcOnEthRowStatus_Type = RowStatus
_RbnDot1qPvcOnEthRowStatus_Object = MibTableColumn
rbnDot1qPvcOnEthRowStatus = _RbnDot1qPvcOnEthRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 7, 1, 3, 1, 4),
    _RbnDot1qPvcOnEthRowStatus_Type()
)
rbnDot1qPvcOnEthRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnDot1qPvcOnEthRowStatus.setStatus("current")


class _RbnDot1qPvcOnEthProfileName_Type(SnmpAdminString):
    """Custom type rbnDot1qPvcOnEthProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_RbnDot1qPvcOnEthProfileName_Type.__name__ = "SnmpAdminString"
_RbnDot1qPvcOnEthProfileName_Object = MibTableColumn
rbnDot1qPvcOnEthProfileName = _RbnDot1qPvcOnEthProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 7, 1, 3, 1, 5),
    _RbnDot1qPvcOnEthProfileName_Type()
)
rbnDot1qPvcOnEthProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnDot1qPvcOnEthProfileName.setStatus("current")
_RbnDot1qPvcOnEthEncapsulation_Type = RbnDot1qEncapsulation
_RbnDot1qPvcOnEthEncapsulation_Object = MibTableColumn
rbnDot1qPvcOnEthEncapsulation = _RbnDot1qPvcOnEthEncapsulation_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 7, 1, 3, 1, 6),
    _RbnDot1qPvcOnEthEncapsulation_Type()
)
rbnDot1qPvcOnEthEncapsulation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnDot1qPvcOnEthEncapsulation.setStatus("current")


class _RbnDot1qPvcOnEthCircuitType_Type(RbnPvcCircuitType):
    """Custom type rbnDot1qPvcOnEthCircuitType based on RbnPvcCircuitType"""


_RbnDot1qPvcOnEthCircuitType_Object = MibTableColumn
rbnDot1qPvcOnEthCircuitType = _RbnDot1qPvcOnEthCircuitType_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 7, 1, 3, 1, 7),
    _RbnDot1qPvcOnEthCircuitType_Type()
)
rbnDot1qPvcOnEthCircuitType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnDot1qPvcOnEthCircuitType.setStatus("current")
_RbnDot1qPvcOnEthCircuitHandle_Type = RbnCircuitHandle
_RbnDot1qPvcOnEthCircuitHandle_Object = MibTableColumn
rbnDot1qPvcOnEthCircuitHandle = _RbnDot1qPvcOnEthCircuitHandle_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 7, 1, 3, 1, 8),
    _RbnDot1qPvcOnEthCircuitHandle_Type()
)
rbnDot1qPvcOnEthCircuitHandle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnDot1qPvcOnEthCircuitHandle.setStatus("current")


class _RbnDot1qPvcOnEthClearCircuit_Type(TruthValue):
    """Custom type rbnDot1qPvcOnEthClearCircuit based on TruthValue"""


_RbnDot1qPvcOnEthClearCircuit_Object = MibTableColumn
rbnDot1qPvcOnEthClearCircuit = _RbnDot1qPvcOnEthClearCircuit_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 7, 1, 3, 1, 9),
    _RbnDot1qPvcOnEthClearCircuit_Type()
)
rbnDot1qPvcOnEthClearCircuit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnDot1qPvcOnEthClearCircuit.setStatus("current")
_RbnDot1qPvcOnAtmConfigTable_Object = MibTable
rbnDot1qPvcOnAtmConfigTable = _RbnDot1qPvcOnAtmConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 7, 1, 4)
)
if mibBuilder.loadTexts:
    rbnDot1qPvcOnAtmConfigTable.setStatus("current")
_RbnDot1qPvcOnAtmConfigEntry_Object = MibTableRow
rbnDot1qPvcOnAtmConfigEntry = _RbnDot1qPvcOnAtmConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 7, 1, 4, 1)
)
rbnDot1qPvcOnAtmConfigEntry.setIndexNames(
    (0, "RBN-PVC-MIB", "rbnDot1qPvcOnAtmSlot"),
    (0, "RBN-PVC-MIB", "rbnDot1qPvcOnAtmPort"),
    (0, "RBN-PVC-MIB", "rbnDot1qPvcOnAtmVpi"),
    (0, "RBN-PVC-MIB", "rbnDot1qPvcOnAtmVci"),
    (0, "RBN-PVC-MIB", "rbnDot1qPvcOnAtmVlanId"),
)
if mibBuilder.loadTexts:
    rbnDot1qPvcOnAtmConfigEntry.setStatus("current")
_RbnDot1qPvcOnAtmSlot_Type = RbnSlot
_RbnDot1qPvcOnAtmSlot_Object = MibTableColumn
rbnDot1qPvcOnAtmSlot = _RbnDot1qPvcOnAtmSlot_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 7, 1, 4, 1, 1),
    _RbnDot1qPvcOnAtmSlot_Type()
)
rbnDot1qPvcOnAtmSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbnDot1qPvcOnAtmSlot.setStatus("current")
_RbnDot1qPvcOnAtmPort_Type = RbnPort
_RbnDot1qPvcOnAtmPort_Object = MibTableColumn
rbnDot1qPvcOnAtmPort = _RbnDot1qPvcOnAtmPort_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 7, 1, 4, 1, 2),
    _RbnDot1qPvcOnAtmPort_Type()
)
rbnDot1qPvcOnAtmPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbnDot1qPvcOnAtmPort.setStatus("current")


class _RbnDot1qPvcOnAtmVpi_Type(Unsigned32):
    """Custom type rbnDot1qPvcOnAtmVpi based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RbnDot1qPvcOnAtmVpi_Type.__name__ = "Unsigned32"
_RbnDot1qPvcOnAtmVpi_Object = MibTableColumn
rbnDot1qPvcOnAtmVpi = _RbnDot1qPvcOnAtmVpi_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 7, 1, 4, 1, 3),
    _RbnDot1qPvcOnAtmVpi_Type()
)
rbnDot1qPvcOnAtmVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbnDot1qPvcOnAtmVpi.setStatus("current")


class _RbnDot1qPvcOnAtmVci_Type(Unsigned32):
    """Custom type rbnDot1qPvcOnAtmVci based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RbnDot1qPvcOnAtmVci_Type.__name__ = "Unsigned32"
_RbnDot1qPvcOnAtmVci_Object = MibTableColumn
rbnDot1qPvcOnAtmVci = _RbnDot1qPvcOnAtmVci_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 7, 1, 4, 1, 4),
    _RbnDot1qPvcOnAtmVci_Type()
)
rbnDot1qPvcOnAtmVci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbnDot1qPvcOnAtmVci.setStatus("current")
_RbnDot1qPvcOnAtmVlanId_Type = RbnVidOrUntagged
_RbnDot1qPvcOnAtmVlanId_Object = MibTableColumn
rbnDot1qPvcOnAtmVlanId = _RbnDot1qPvcOnAtmVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 7, 1, 4, 1, 5),
    _RbnDot1qPvcOnAtmVlanId_Type()
)
rbnDot1qPvcOnAtmVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbnDot1qPvcOnAtmVlanId.setStatus("current")
_RbnDot1qPvcOnAtmRowStatus_Type = RowStatus
_RbnDot1qPvcOnAtmRowStatus_Object = MibTableColumn
rbnDot1qPvcOnAtmRowStatus = _RbnDot1qPvcOnAtmRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 7, 1, 4, 1, 6),
    _RbnDot1qPvcOnAtmRowStatus_Type()
)
rbnDot1qPvcOnAtmRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnDot1qPvcOnAtmRowStatus.setStatus("current")


class _RbnDot1qPvcOnAtmProfileName_Type(SnmpAdminString):
    """Custom type rbnDot1qPvcOnAtmProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_RbnDot1qPvcOnAtmProfileName_Type.__name__ = "SnmpAdminString"
_RbnDot1qPvcOnAtmProfileName_Object = MibTableColumn
rbnDot1qPvcOnAtmProfileName = _RbnDot1qPvcOnAtmProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 7, 1, 4, 1, 7),
    _RbnDot1qPvcOnAtmProfileName_Type()
)
rbnDot1qPvcOnAtmProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnDot1qPvcOnAtmProfileName.setStatus("current")
_RbnDot1qPvcOnAtmEncapsulation_Type = RbnDot1qEncapsulation
_RbnDot1qPvcOnAtmEncapsulation_Object = MibTableColumn
rbnDot1qPvcOnAtmEncapsulation = _RbnDot1qPvcOnAtmEncapsulation_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 7, 1, 4, 1, 8),
    _RbnDot1qPvcOnAtmEncapsulation_Type()
)
rbnDot1qPvcOnAtmEncapsulation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnDot1qPvcOnAtmEncapsulation.setStatus("current")


class _RbnDot1qPvcOnAtmCircuitType_Type(RbnPvcCircuitType):
    """Custom type rbnDot1qPvcOnAtmCircuitType based on RbnPvcCircuitType"""


_RbnDot1qPvcOnAtmCircuitType_Object = MibTableColumn
rbnDot1qPvcOnAtmCircuitType = _RbnDot1qPvcOnAtmCircuitType_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 7, 1, 4, 1, 9),
    _RbnDot1qPvcOnAtmCircuitType_Type()
)
rbnDot1qPvcOnAtmCircuitType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnDot1qPvcOnAtmCircuitType.setStatus("current")
_RbnDot1qPvcOnAtmCircuitHandle_Type = RbnCircuitHandle
_RbnDot1qPvcOnAtmCircuitHandle_Object = MibTableColumn
rbnDot1qPvcOnAtmCircuitHandle = _RbnDot1qPvcOnAtmCircuitHandle_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 7, 1, 4, 1, 10),
    _RbnDot1qPvcOnAtmCircuitHandle_Type()
)
rbnDot1qPvcOnAtmCircuitHandle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnDot1qPvcOnAtmCircuitHandle.setStatus("current")


class _RbnDot1qPvcOnAtmClearCircuit_Type(TruthValue):
    """Custom type rbnDot1qPvcOnAtmClearCircuit based on TruthValue"""


_RbnDot1qPvcOnAtmClearCircuit_Object = MibTableColumn
rbnDot1qPvcOnAtmClearCircuit = _RbnDot1qPvcOnAtmClearCircuit_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 7, 1, 4, 1, 11),
    _RbnDot1qPvcOnAtmClearCircuit_Type()
)
rbnDot1qPvcOnAtmClearCircuit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnDot1qPvcOnAtmClearCircuit.setStatus("current")
_RbnDot1qPvcOnFrConfigTable_Object = MibTable
rbnDot1qPvcOnFrConfigTable = _RbnDot1qPvcOnFrConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 7, 1, 5)
)
if mibBuilder.loadTexts:
    rbnDot1qPvcOnFrConfigTable.setStatus("current")
_RbnDot1qPvcOnFrConfigEntry_Object = MibTableRow
rbnDot1qPvcOnFrConfigEntry = _RbnDot1qPvcOnFrConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 7, 1, 5, 1)
)
rbnDot1qPvcOnFrConfigEntry.setIndexNames(
    (0, "RBN-PVC-MIB", "rbnDot1qPvcOnFrSlot"),
    (0, "RBN-PVC-MIB", "rbnDot1qPvcOnFrPort"),
    (0, "RBN-PVC-MIB", "rbnDot1qPvcOnFrChannel"),
    (0, "RBN-PVC-MIB", "rbnDot1qPvcOnFrDLCI"),
    (0, "RBN-PVC-MIB", "rbnDot1qPvcOnFrVlanId"),
)
if mibBuilder.loadTexts:
    rbnDot1qPvcOnFrConfigEntry.setStatus("current")
_RbnDot1qPvcOnFrSlot_Type = RbnSlot
_RbnDot1qPvcOnFrSlot_Object = MibTableColumn
rbnDot1qPvcOnFrSlot = _RbnDot1qPvcOnFrSlot_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 7, 1, 5, 1, 1),
    _RbnDot1qPvcOnFrSlot_Type()
)
rbnDot1qPvcOnFrSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbnDot1qPvcOnFrSlot.setStatus("current")
_RbnDot1qPvcOnFrPort_Type = RbnPort
_RbnDot1qPvcOnFrPort_Object = MibTableColumn
rbnDot1qPvcOnFrPort = _RbnDot1qPvcOnFrPort_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 7, 1, 5, 1, 2),
    _RbnDot1qPvcOnFrPort_Type()
)
rbnDot1qPvcOnFrPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbnDot1qPvcOnFrPort.setStatus("current")


class _RbnDot1qPvcOnFrChannel_Type(Unsigned32):
    """Custom type rbnDot1qPvcOnFrChannel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RbnDot1qPvcOnFrChannel_Type.__name__ = "Unsigned32"
_RbnDot1qPvcOnFrChannel_Object = MibTableColumn
rbnDot1qPvcOnFrChannel = _RbnDot1qPvcOnFrChannel_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 7, 1, 5, 1, 3),
    _RbnDot1qPvcOnFrChannel_Type()
)
rbnDot1qPvcOnFrChannel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbnDot1qPvcOnFrChannel.setStatus("current")


class _RbnDot1qPvcOnFrDLCI_Type(Unsigned32):
    """Custom type rbnDot1qPvcOnFrDLCI based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RbnDot1qPvcOnFrDLCI_Type.__name__ = "Unsigned32"
_RbnDot1qPvcOnFrDLCI_Object = MibTableColumn
rbnDot1qPvcOnFrDLCI = _RbnDot1qPvcOnFrDLCI_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 7, 1, 5, 1, 4),
    _RbnDot1qPvcOnFrDLCI_Type()
)
rbnDot1qPvcOnFrDLCI.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbnDot1qPvcOnFrDLCI.setStatus("current")
_RbnDot1qPvcOnFrVlanId_Type = RbnVidOrUntagged
_RbnDot1qPvcOnFrVlanId_Object = MibTableColumn
rbnDot1qPvcOnFrVlanId = _RbnDot1qPvcOnFrVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 7, 1, 5, 1, 5),
    _RbnDot1qPvcOnFrVlanId_Type()
)
rbnDot1qPvcOnFrVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbnDot1qPvcOnFrVlanId.setStatus("current")
_RbnDot1qPvcOnFrRowStatus_Type = RowStatus
_RbnDot1qPvcOnFrRowStatus_Object = MibTableColumn
rbnDot1qPvcOnFrRowStatus = _RbnDot1qPvcOnFrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 7, 1, 5, 1, 6),
    _RbnDot1qPvcOnFrRowStatus_Type()
)
rbnDot1qPvcOnFrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnDot1qPvcOnFrRowStatus.setStatus("current")


class _RbnDot1qPvcOnFrProfileName_Type(SnmpAdminString):
    """Custom type rbnDot1qPvcOnFrProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_RbnDot1qPvcOnFrProfileName_Type.__name__ = "SnmpAdminString"
_RbnDot1qPvcOnFrProfileName_Object = MibTableColumn
rbnDot1qPvcOnFrProfileName = _RbnDot1qPvcOnFrProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 7, 1, 5, 1, 7),
    _RbnDot1qPvcOnFrProfileName_Type()
)
rbnDot1qPvcOnFrProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnDot1qPvcOnFrProfileName.setStatus("current")
_RbnDot1qPvcOnFrEncapsulation_Type = RbnDot1qEncapsulation
_RbnDot1qPvcOnFrEncapsulation_Object = MibTableColumn
rbnDot1qPvcOnFrEncapsulation = _RbnDot1qPvcOnFrEncapsulation_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 7, 1, 5, 1, 8),
    _RbnDot1qPvcOnFrEncapsulation_Type()
)
rbnDot1qPvcOnFrEncapsulation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnDot1qPvcOnFrEncapsulation.setStatus("current")


class _RbnDot1qPvcOnFrCircuitType_Type(RbnPvcCircuitType):
    """Custom type rbnDot1qPvcOnFrCircuitType based on RbnPvcCircuitType"""


_RbnDot1qPvcOnFrCircuitType_Object = MibTableColumn
rbnDot1qPvcOnFrCircuitType = _RbnDot1qPvcOnFrCircuitType_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 7, 1, 5, 1, 9),
    _RbnDot1qPvcOnFrCircuitType_Type()
)
rbnDot1qPvcOnFrCircuitType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnDot1qPvcOnFrCircuitType.setStatus("current")
_RbnDot1qPvcOnFrCircuitHandle_Type = RbnCircuitHandle
_RbnDot1qPvcOnFrCircuitHandle_Object = MibTableColumn
rbnDot1qPvcOnFrCircuitHandle = _RbnDot1qPvcOnFrCircuitHandle_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 7, 1, 5, 1, 10),
    _RbnDot1qPvcOnFrCircuitHandle_Type()
)
rbnDot1qPvcOnFrCircuitHandle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnDot1qPvcOnFrCircuitHandle.setStatus("current")


class _RbnDot1qPvcOnFrClearCircuit_Type(TruthValue):
    """Custom type rbnDot1qPvcOnFrClearCircuit based on TruthValue"""


_RbnDot1qPvcOnFrClearCircuit_Object = MibTableColumn
rbnDot1qPvcOnFrClearCircuit = _RbnDot1qPvcOnFrClearCircuit_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 7, 1, 5, 1, 11),
    _RbnDot1qPvcOnFrClearCircuit_Type()
)
rbnDot1qPvcOnFrClearCircuit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbnDot1qPvcOnFrClearCircuit.setStatus("current")
_RbnPvcMIBConformance_ObjectIdentity = ObjectIdentity
rbnPvcMIBConformance = _RbnPvcMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 7, 2)
)
_RbnPvcCompliances_ObjectIdentity = ObjectIdentity
rbnPvcCompliances = _RbnPvcCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 7, 2, 1)
)
_RbnPvcGroups_ObjectIdentity = ObjectIdentity
rbnPvcGroups = _RbnPvcGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 7, 2, 2)
)
_RbnPvcMIBNotifications_ObjectIdentity = ObjectIdentity
rbnPvcMIBNotifications = _RbnPvcMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 7, 3)
)

# Managed Objects groups

rbnAtmPvcGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 7, 2, 2, 1)
)
rbnAtmPvcGroup.setObjects(
      *(("RBN-PVC-MIB", "rbnAtmPvcProfileName"),
        ("RBN-PVC-MIB", "rbnAtmPvcEncapsulation"),
        ("RBN-PVC-MIB", "rbnAtmPvcRowStatus"))
)
if mibBuilder.loadTexts:
    rbnAtmPvcGroup.setStatus("deprecated")

rbnFrameRelayPvcGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 7, 2, 2, 2)
)
rbnFrameRelayPvcGroup.setObjects(
      *(("RBN-PVC-MIB", "rbnFrameRelayPvcProfileName"),
        ("RBN-PVC-MIB", "rbnFrameRelayPvcEncapsulation"),
        ("RBN-PVC-MIB", "rbnFrameRelayPvcRowStatus"))
)
if mibBuilder.loadTexts:
    rbnFrameRelayPvcGroup.setStatus("deprecated")

rbnAtmPvcGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 7, 2, 2, 3)
)
rbnAtmPvcGroup2.setObjects(
      *(("RBN-PVC-MIB", "rbnAtmPvcProfileName"),
        ("RBN-PVC-MIB", "rbnAtmPvcEncapsulation"),
        ("RBN-PVC-MIB", "rbnAtmPvcRowStatus"),
        ("RBN-PVC-MIB", "rbnAtmPvcCircuitType"),
        ("RBN-PVC-MIB", "rbnAtmPvcCircuitHandle"),
        ("RBN-PVC-MIB", "rbnAtmPvcClearCircuit"))
)
if mibBuilder.loadTexts:
    rbnAtmPvcGroup2.setStatus("current")

rbnFrameRelayPvcGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 7, 2, 2, 4)
)
rbnFrameRelayPvcGroup2.setObjects(
      *(("RBN-PVC-MIB", "rbnFrameRelayPvcProfileName"),
        ("RBN-PVC-MIB", "rbnFrameRelayPvcEncapsulation"),
        ("RBN-PVC-MIB", "rbnFrameRelayPvcRowStatus"),
        ("RBN-PVC-MIB", "rbnFrameRelayPvcCircuitType"),
        ("RBN-PVC-MIB", "rbnFrameRelayPvcCircuitHandle"),
        ("RBN-PVC-MIB", "rbnFrameRelayPvcClearCircuit"))
)
if mibBuilder.loadTexts:
    rbnFrameRelayPvcGroup2.setStatus("current")

rbnDot1qPvcOnEthGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 7, 2, 2, 5)
)
rbnDot1qPvcOnEthGroup.setObjects(
      *(("RBN-PVC-MIB", "rbnDot1qPvcOnEthRowStatus"),
        ("RBN-PVC-MIB", "rbnDot1qPvcOnEthProfileName"),
        ("RBN-PVC-MIB", "rbnDot1qPvcOnEthEncapsulation"),
        ("RBN-PVC-MIB", "rbnDot1qPvcOnEthCircuitType"),
        ("RBN-PVC-MIB", "rbnDot1qPvcOnEthCircuitHandle"),
        ("RBN-PVC-MIB", "rbnDot1qPvcOnEthClearCircuit"))
)
if mibBuilder.loadTexts:
    rbnDot1qPvcOnEthGroup.setStatus("current")

rbnDot1qPvcOnAtmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 7, 2, 2, 6)
)
rbnDot1qPvcOnAtmGroup.setObjects(
      *(("RBN-PVC-MIB", "rbnDot1qPvcOnAtmRowStatus"),
        ("RBN-PVC-MIB", "rbnDot1qPvcOnAtmProfileName"),
        ("RBN-PVC-MIB", "rbnDot1qPvcOnAtmEncapsulation"),
        ("RBN-PVC-MIB", "rbnDot1qPvcOnAtmCircuitType"),
        ("RBN-PVC-MIB", "rbnDot1qPvcOnAtmCircuitHandle"),
        ("RBN-PVC-MIB", "rbnDot1qPvcOnAtmClearCircuit"))
)
if mibBuilder.loadTexts:
    rbnDot1qPvcOnAtmGroup.setStatus("current")

rbnDot1qPvcOnFrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 7, 2, 2, 7)
)
rbnDot1qPvcOnFrGroup.setObjects(
      *(("RBN-PVC-MIB", "rbnDot1qPvcOnFrRowStatus"),
        ("RBN-PVC-MIB", "rbnDot1qPvcOnFrProfileName"),
        ("RBN-PVC-MIB", "rbnDot1qPvcOnFrEncapsulation"),
        ("RBN-PVC-MIB", "rbnDot1qPvcOnFrCircuitType"),
        ("RBN-PVC-MIB", "rbnDot1qPvcOnFrCircuitHandle"),
        ("RBN-PVC-MIB", "rbnDot1qPvcOnFrClearCircuit"))
)
if mibBuilder.loadTexts:
    rbnDot1qPvcOnFrGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

rbnPvcCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2352, 2, 7, 2, 1, 1)
)
if mibBuilder.loadTexts:
    rbnPvcCompliance.setStatus(
        "deprecated"
    )

rbnPvcCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2352, 2, 7, 2, 1, 2)
)
if mibBuilder.loadTexts:
    rbnPvcCompliance2.setStatus(
        "deprecated"
    )

rbnPvcCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2352, 2, 7, 2, 1, 3)
)
if mibBuilder.loadTexts:
    rbnPvcCompliance3.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RBN-PVC-MIB",
    **{"RbnFrameRelayEncapsulation": RbnFrameRelayEncapsulation,
       "RbnAtmEncapsulation": RbnAtmEncapsulation,
       "RbnDot1qEncapsulation": RbnDot1qEncapsulation,
       "RbnPvcCircuitType": RbnPvcCircuitType,
       "rbnPvcMib": rbnPvcMib,
       "rbnPvcMIBObjects": rbnPvcMIBObjects,
       "rbnAtmPvcConfigTable": rbnAtmPvcConfigTable,
       "rbnAtmPvcConfigEntry": rbnAtmPvcConfigEntry,
       "rbnAtmPvcSlot": rbnAtmPvcSlot,
       "rbnAtmPvcPort": rbnAtmPvcPort,
       "rbnAtmPvcVpi": rbnAtmPvcVpi,
       "rbnAtmPvcVci": rbnAtmPvcVci,
       "rbnAtmPvcProfileName": rbnAtmPvcProfileName,
       "rbnAtmPvcEncapsulation": rbnAtmPvcEncapsulation,
       "rbnAtmPvcRowStatus": rbnAtmPvcRowStatus,
       "rbnAtmPvcCircuitType": rbnAtmPvcCircuitType,
       "rbnAtmPvcCircuitHandle": rbnAtmPvcCircuitHandle,
       "rbnAtmPvcClearCircuit": rbnAtmPvcClearCircuit,
       "rbnFrameRelayPvcConfigTable": rbnFrameRelayPvcConfigTable,
       "rbnFrameRelayPvcConfigEntry": rbnFrameRelayPvcConfigEntry,
       "rbnFrameRelayPvcSlot": rbnFrameRelayPvcSlot,
       "rbnFrameRelayPvcPort": rbnFrameRelayPvcPort,
       "rbnFrameRelayPvcChannel": rbnFrameRelayPvcChannel,
       "rbnFrameRelayPvcDLCI": rbnFrameRelayPvcDLCI,
       "rbnFrameRelayPvcProfileName": rbnFrameRelayPvcProfileName,
       "rbnFrameRelayPvcEncapsulation": rbnFrameRelayPvcEncapsulation,
       "rbnFrameRelayPvcRowStatus": rbnFrameRelayPvcRowStatus,
       "rbnFrameRelayPvcCircuitType": rbnFrameRelayPvcCircuitType,
       "rbnFrameRelayPvcCircuitHandle": rbnFrameRelayPvcCircuitHandle,
       "rbnFrameRelayPvcClearCircuit": rbnFrameRelayPvcClearCircuit,
       "rbnDot1qPvcOnEthConfigTable": rbnDot1qPvcOnEthConfigTable,
       "rbnDot1qPvcOnEthConfigEntry": rbnDot1qPvcOnEthConfigEntry,
       "rbnDot1qPvcOnEthSlot": rbnDot1qPvcOnEthSlot,
       "rbnDot1qPvcOnEthPort": rbnDot1qPvcOnEthPort,
       "rbnDot1qPvcOnEthVlanId": rbnDot1qPvcOnEthVlanId,
       "rbnDot1qPvcOnEthRowStatus": rbnDot1qPvcOnEthRowStatus,
       "rbnDot1qPvcOnEthProfileName": rbnDot1qPvcOnEthProfileName,
       "rbnDot1qPvcOnEthEncapsulation": rbnDot1qPvcOnEthEncapsulation,
       "rbnDot1qPvcOnEthCircuitType": rbnDot1qPvcOnEthCircuitType,
       "rbnDot1qPvcOnEthCircuitHandle": rbnDot1qPvcOnEthCircuitHandle,
       "rbnDot1qPvcOnEthClearCircuit": rbnDot1qPvcOnEthClearCircuit,
       "rbnDot1qPvcOnAtmConfigTable": rbnDot1qPvcOnAtmConfigTable,
       "rbnDot1qPvcOnAtmConfigEntry": rbnDot1qPvcOnAtmConfigEntry,
       "rbnDot1qPvcOnAtmSlot": rbnDot1qPvcOnAtmSlot,
       "rbnDot1qPvcOnAtmPort": rbnDot1qPvcOnAtmPort,
       "rbnDot1qPvcOnAtmVpi": rbnDot1qPvcOnAtmVpi,
       "rbnDot1qPvcOnAtmVci": rbnDot1qPvcOnAtmVci,
       "rbnDot1qPvcOnAtmVlanId": rbnDot1qPvcOnAtmVlanId,
       "rbnDot1qPvcOnAtmRowStatus": rbnDot1qPvcOnAtmRowStatus,
       "rbnDot1qPvcOnAtmProfileName": rbnDot1qPvcOnAtmProfileName,
       "rbnDot1qPvcOnAtmEncapsulation": rbnDot1qPvcOnAtmEncapsulation,
       "rbnDot1qPvcOnAtmCircuitType": rbnDot1qPvcOnAtmCircuitType,
       "rbnDot1qPvcOnAtmCircuitHandle": rbnDot1qPvcOnAtmCircuitHandle,
       "rbnDot1qPvcOnAtmClearCircuit": rbnDot1qPvcOnAtmClearCircuit,
       "rbnDot1qPvcOnFrConfigTable": rbnDot1qPvcOnFrConfigTable,
       "rbnDot1qPvcOnFrConfigEntry": rbnDot1qPvcOnFrConfigEntry,
       "rbnDot1qPvcOnFrSlot": rbnDot1qPvcOnFrSlot,
       "rbnDot1qPvcOnFrPort": rbnDot1qPvcOnFrPort,
       "rbnDot1qPvcOnFrChannel": rbnDot1qPvcOnFrChannel,
       "rbnDot1qPvcOnFrDLCI": rbnDot1qPvcOnFrDLCI,
       "rbnDot1qPvcOnFrVlanId": rbnDot1qPvcOnFrVlanId,
       "rbnDot1qPvcOnFrRowStatus": rbnDot1qPvcOnFrRowStatus,
       "rbnDot1qPvcOnFrProfileName": rbnDot1qPvcOnFrProfileName,
       "rbnDot1qPvcOnFrEncapsulation": rbnDot1qPvcOnFrEncapsulation,
       "rbnDot1qPvcOnFrCircuitType": rbnDot1qPvcOnFrCircuitType,
       "rbnDot1qPvcOnFrCircuitHandle": rbnDot1qPvcOnFrCircuitHandle,
       "rbnDot1qPvcOnFrClearCircuit": rbnDot1qPvcOnFrClearCircuit,
       "rbnPvcMIBConformance": rbnPvcMIBConformance,
       "rbnPvcCompliances": rbnPvcCompliances,
       "rbnPvcCompliance": rbnPvcCompliance,
       "rbnPvcCompliance2": rbnPvcCompliance2,
       "rbnPvcCompliance3": rbnPvcCompliance3,
       "rbnPvcGroups": rbnPvcGroups,
       "rbnAtmPvcGroup": rbnAtmPvcGroup,
       "rbnFrameRelayPvcGroup": rbnFrameRelayPvcGroup,
       "rbnAtmPvcGroup2": rbnAtmPvcGroup2,
       "rbnFrameRelayPvcGroup2": rbnFrameRelayPvcGroup2,
       "rbnDot1qPvcOnEthGroup": rbnDot1qPvcOnEthGroup,
       "rbnDot1qPvcOnAtmGroup": rbnDot1qPvcOnAtmGroup,
       "rbnDot1qPvcOnFrGroup": rbnDot1qPvcOnFrGroup,
       "rbnPvcMIBNotifications": rbnPvcMIBNotifications}
)
