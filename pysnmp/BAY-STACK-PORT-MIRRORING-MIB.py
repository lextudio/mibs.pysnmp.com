# SNMP MIB module (BAY-STACK-PORT-MIRRORING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BAY-STACK-PORT-MIRRORING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:46:19 2024
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(PortList,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList")

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
 MacAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(bayStackMibs,) = mibBuilder.importSymbols(
    "SYNOPTICS-ROOT-MIB",
    "bayStackMibs")


# MODULE-IDENTITY

bayStackPortMirroringMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 28)
)
bayStackPortMirroringMib.setRevisions(
        ("2012-10-10 00:00",
         "2009-05-28 00:00",
         "2008-01-18 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BsPortMirroringNotifications_ObjectIdentity = ObjectIdentity
bsPortMirroringNotifications = _BsPortMirroringNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 28, 0)
)
_BsPortMirroringObjects_ObjectIdentity = ObjectIdentity
bsPortMirroringObjects = _BsPortMirroringObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 28, 1)
)
_BsPortMirroringCtrlTable_Object = MibTable
bsPortMirroringCtrlTable = _BsPortMirroringCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 28, 1, 1)
)
if mibBuilder.loadTexts:
    bsPortMirroringCtrlTable.setStatus("current")
_BsPortMirroringCtrlEntry_Object = MibTableRow
bsPortMirroringCtrlEntry = _BsPortMirroringCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 28, 1, 1, 1)
)
bsPortMirroringCtrlEntry.setIndexNames(
    (0, "BAY-STACK-PORT-MIRRORING-MIB", "bsPortMirroringCtrlInstance"),
)
if mibBuilder.loadTexts:
    bsPortMirroringCtrlEntry.setStatus("current")


class _BsPortMirroringCtrlInstance_Type(Integer32):
    """Custom type bsPortMirroringCtrlInstance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_BsPortMirroringCtrlInstance_Type.__name__ = "Integer32"
_BsPortMirroringCtrlInstance_Object = MibTableColumn
bsPortMirroringCtrlInstance = _BsPortMirroringCtrlInstance_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 28, 1, 1, 1, 1),
    _BsPortMirroringCtrlInstance_Type()
)
bsPortMirroringCtrlInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bsPortMirroringCtrlInstance.setStatus("current")


class _BsPortMirroringCtrlPortMode_Type(Integer32):
    """Custom type bsPortMirroringCtrlPortMode based on Integer32"""
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
        *(("adst", 2),
          ("asrc", 3),
          ("asrcBdst", 4),
          ("asrcBdstOrBsrcAdst", 5),
          ("asrcOrAdst", 6),
          ("disable", 1),
          ("manytoOneRx", 7),
          ("manytoOneRxTx", 8),
          ("manytoOneTx", 9),
          ("xrx", 10),
          ("xrxOrXtx", 11),
          ("xrxOrYtx", 12),
          ("xrxYtx", 13),
          ("xrxYtxOrYrxXtx", 14),
          ("xtx", 15))
    )


_BsPortMirroringCtrlPortMode_Type.__name__ = "Integer32"
_BsPortMirroringCtrlPortMode_Object = MibTableColumn
bsPortMirroringCtrlPortMode = _BsPortMirroringCtrlPortMode_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 28, 1, 1, 1, 2),
    _BsPortMirroringCtrlPortMode_Type()
)
bsPortMirroringCtrlPortMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsPortMirroringCtrlPortMode.setStatus("current")
_BsPortMirroringCtrlMonitorPort_Type = InterfaceIndex
_BsPortMirroringCtrlMonitorPort_Object = MibTableColumn
bsPortMirroringCtrlMonitorPort = _BsPortMirroringCtrlMonitorPort_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 28, 1, 1, 1, 3),
    _BsPortMirroringCtrlMonitorPort_Type()
)
bsPortMirroringCtrlMonitorPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsPortMirroringCtrlMonitorPort.setStatus("current")


class _BsPortMirroringCtrlPortListX_Type(PortList):
    """Custom type bsPortMirroringCtrlPortListX based on PortList"""
    subtypeSpec = PortList.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_BsPortMirroringCtrlPortListX_Type.__name__ = "PortList"
_BsPortMirroringCtrlPortListX_Object = MibTableColumn
bsPortMirroringCtrlPortListX = _BsPortMirroringCtrlPortListX_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 28, 1, 1, 1, 4),
    _BsPortMirroringCtrlPortListX_Type()
)
bsPortMirroringCtrlPortListX.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsPortMirroringCtrlPortListX.setStatus("current")


class _BsPortMirroringCtrlPortListY_Type(PortList):
    """Custom type bsPortMirroringCtrlPortListY based on PortList"""
    subtypeSpec = PortList.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_BsPortMirroringCtrlPortListY_Type.__name__ = "PortList"
_BsPortMirroringCtrlPortListY_Object = MibTableColumn
bsPortMirroringCtrlPortListY = _BsPortMirroringCtrlPortListY_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 28, 1, 1, 1, 5),
    _BsPortMirroringCtrlPortListY_Type()
)
bsPortMirroringCtrlPortListY.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsPortMirroringCtrlPortListY.setStatus("current")
_BsPortMirroringCtrlMacAddressA_Type = MacAddress
_BsPortMirroringCtrlMacAddressA_Object = MibTableColumn
bsPortMirroringCtrlMacAddressA = _BsPortMirroringCtrlMacAddressA_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 28, 1, 1, 1, 6),
    _BsPortMirroringCtrlMacAddressA_Type()
)
bsPortMirroringCtrlMacAddressA.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsPortMirroringCtrlMacAddressA.setStatus("current")
_BsPortMirroringCtrlMacAddressB_Type = MacAddress
_BsPortMirroringCtrlMacAddressB_Object = MibTableColumn
bsPortMirroringCtrlMacAddressB = _BsPortMirroringCtrlMacAddressB_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 28, 1, 1, 1, 7),
    _BsPortMirroringCtrlMacAddressB_Type()
)
bsPortMirroringCtrlMacAddressB.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsPortMirroringCtrlMacAddressB.setStatus("current")
_BsPortMirroringCtrlRowStatus_Type = RowStatus
_BsPortMirroringCtrlRowStatus_Object = MibTableColumn
bsPortMirroringCtrlRowStatus = _BsPortMirroringCtrlRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 28, 1, 1, 1, 8),
    _BsPortMirroringCtrlRowStatus_Type()
)
bsPortMirroringCtrlRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsPortMirroringCtrlRowStatus.setStatus("current")
_BsPortMirroringCtrlAllowTraffic_Type = TruthValue
_BsPortMirroringCtrlAllowTraffic_Object = MibTableColumn
bsPortMirroringCtrlAllowTraffic = _BsPortMirroringCtrlAllowTraffic_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 28, 1, 1, 1, 9),
    _BsPortMirroringCtrlAllowTraffic_Type()
)
bsPortMirroringCtrlAllowTraffic.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsPortMirroringCtrlAllowTraffic.setStatus("current")


class _BsPortMirroringCtrlRspanVlan_Type(Integer32):
    """Custom type bsPortMirroringCtrlRspanVlan based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2, 4094),
    )


_BsPortMirroringCtrlRspanVlan_Type.__name__ = "Integer32"
_BsPortMirroringCtrlRspanVlan_Object = MibTableColumn
bsPortMirroringCtrlRspanVlan = _BsPortMirroringCtrlRspanVlan_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 28, 1, 1, 1, 10),
    _BsPortMirroringCtrlRspanVlan_Type()
)
bsPortMirroringCtrlRspanVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsPortMirroringCtrlRspanVlan.setStatus("current")
_BsPortMirroringRspanTable_Object = MibTable
bsPortMirroringRspanTable = _BsPortMirroringRspanTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 28, 1, 2)
)
if mibBuilder.loadTexts:
    bsPortMirroringRspanTable.setStatus("current")
_BsPortMirroringRspanEntry_Object = MibTableRow
bsPortMirroringRspanEntry = _BsPortMirroringRspanEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 28, 1, 2, 1)
)
bsPortMirroringRspanEntry.setIndexNames(
    (0, "BAY-STACK-PORT-MIRRORING-MIB", "bsPortMirroringRspanInstance"),
)
if mibBuilder.loadTexts:
    bsPortMirroringRspanEntry.setStatus("current")


class _BsPortMirroringRspanInstance_Type(Integer32):
    """Custom type bsPortMirroringRspanInstance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_BsPortMirroringRspanInstance_Type.__name__ = "Integer32"
_BsPortMirroringRspanInstance_Object = MibTableColumn
bsPortMirroringRspanInstance = _BsPortMirroringRspanInstance_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 28, 1, 2, 1, 1),
    _BsPortMirroringRspanInstance_Type()
)
bsPortMirroringRspanInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bsPortMirroringRspanInstance.setStatus("current")
_BsPortMirroringRspanMtp_Type = InterfaceIndex
_BsPortMirroringRspanMtp_Object = MibTableColumn
bsPortMirroringRspanMtp = _BsPortMirroringRspanMtp_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 28, 1, 2, 1, 2),
    _BsPortMirroringRspanMtp_Type()
)
bsPortMirroringRspanMtp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsPortMirroringRspanMtp.setStatus("current")


class _BsPortMirroringRspanVlan_Type(Integer32):
    """Custom type bsPortMirroringRspanVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 4094),
    )


_BsPortMirroringRspanVlan_Type.__name__ = "Integer32"
_BsPortMirroringRspanVlan_Object = MibTableColumn
bsPortMirroringRspanVlan = _BsPortMirroringRspanVlan_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 28, 1, 2, 1, 3),
    _BsPortMirroringRspanVlan_Type()
)
bsPortMirroringRspanVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsPortMirroringRspanVlan.setStatus("current")
_BsPortMirroringRspanRowStatus_Type = RowStatus
_BsPortMirroringRspanRowStatus_Object = MibTableColumn
bsPortMirroringRspanRowStatus = _BsPortMirroringRspanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 28, 1, 2, 1, 4),
    _BsPortMirroringRspanRowStatus_Type()
)
bsPortMirroringRspanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsPortMirroringRspanRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BAY-STACK-PORT-MIRRORING-MIB",
    **{"bayStackPortMirroringMib": bayStackPortMirroringMib,
       "bsPortMirroringNotifications": bsPortMirroringNotifications,
       "bsPortMirroringObjects": bsPortMirroringObjects,
       "bsPortMirroringCtrlTable": bsPortMirroringCtrlTable,
       "bsPortMirroringCtrlEntry": bsPortMirroringCtrlEntry,
       "bsPortMirroringCtrlInstance": bsPortMirroringCtrlInstance,
       "bsPortMirroringCtrlPortMode": bsPortMirroringCtrlPortMode,
       "bsPortMirroringCtrlMonitorPort": bsPortMirroringCtrlMonitorPort,
       "bsPortMirroringCtrlPortListX": bsPortMirroringCtrlPortListX,
       "bsPortMirroringCtrlPortListY": bsPortMirroringCtrlPortListY,
       "bsPortMirroringCtrlMacAddressA": bsPortMirroringCtrlMacAddressA,
       "bsPortMirroringCtrlMacAddressB": bsPortMirroringCtrlMacAddressB,
       "bsPortMirroringCtrlRowStatus": bsPortMirroringCtrlRowStatus,
       "bsPortMirroringCtrlAllowTraffic": bsPortMirroringCtrlAllowTraffic,
       "bsPortMirroringCtrlRspanVlan": bsPortMirroringCtrlRspanVlan,
       "bsPortMirroringRspanTable": bsPortMirroringRspanTable,
       "bsPortMirroringRspanEntry": bsPortMirroringRspanEntry,
       "bsPortMirroringRspanInstance": bsPortMirroringRspanInstance,
       "bsPortMirroringRspanMtp": bsPortMirroringRspanMtp,
       "bsPortMirroringRspanVlan": bsPortMirroringRspanVlan,
       "bsPortMirroringRspanRowStatus": bsPortMirroringRspanRowStatus}
)
