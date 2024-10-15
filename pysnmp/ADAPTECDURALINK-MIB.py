# SNMP MIB module (ADAPTECDURALINK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ADAPTECDURALINK-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:33:43 2024
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
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Adaptec_ObjectIdentity = ObjectIdentity
adaptec = _Adaptec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 795)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 795, 3)
)
_Nic_ObjectIdentity = ObjectIdentity
nic = _Nic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 795, 3, 1)
)
_Npg_ObjectIdentity = ObjectIdentity
npg = _Npg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 795, 3, 1, 2)
)
_Duralink_ObjectIdentity = ObjectIdentity
duralink = _Duralink_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 795, 3, 1, 2, 3)
)
_Information_ObjectIdentity = ObjectIdentity
information = _Information_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 795, 3, 1, 2, 3, 1)
)
_NumInterfaces_Type = Integer32
_NumInterfaces_Object = MibScalar
numInterfaces = _NumInterfaces_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 1, 2, 3, 1, 1),
    _NumInterfaces_Type()
)
numInterfaces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numInterfaces.setStatus("mandatory")
_NumPorts_Type = Integer32
_NumPorts_Object = MibScalar
numPorts = _NumPorts_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 1, 2, 3, 1, 2),
    _NumPorts_Type()
)
numPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numPorts.setStatus("mandatory")
_NumCards_Type = Integer32
_NumCards_Object = MibScalar
numCards = _NumCards_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 1, 2, 3, 1, 3),
    _NumCards_Type()
)
numCards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numCards.setStatus("mandatory")
_InterfaceStatsTable_Object = MibTable
interfaceStatsTable = _InterfaceStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 1, 2, 3, 2)
)
if mibBuilder.loadTexts:
    interfaceStatsTable.setStatus("mandatory")
_InterfaceStatsEntry_Object = MibTableRow
interfaceStatsEntry = _InterfaceStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 1, 2, 3, 2, 1)
)
interfaceStatsEntry.setIndexNames(
    (0, "ADAPTECDURALINK-MIB", "iInterfaceIndex"),
)
if mibBuilder.loadTexts:
    interfaceStatsEntry.setStatus("mandatory")
_IInterfaceIndex_Type = Integer32
_IInterfaceIndex_Object = MibTableColumn
iInterfaceIndex = _IInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 1, 2, 3, 2, 1, 1),
    _IInterfaceIndex_Type()
)
iInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iInterfaceIndex.setStatus("mandatory")


class _IInterfaceName_Type(DisplayString):
    """Custom type iInterfaceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_IInterfaceName_Type.__name__ = "DisplayString"
_IInterfaceName_Object = MibTableColumn
iInterfaceName = _IInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 1, 2, 3, 2, 1, 2),
    _IInterfaceName_Type()
)
iInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iInterfaceName.setStatus("mandatory")
_IInterfacePorts_Type = Integer32
_IInterfacePorts_Object = MibTableColumn
iInterfacePorts = _IInterfacePorts_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 1, 2, 3, 2, 1, 3),
    _IInterfacePorts_Type()
)
iInterfacePorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iInterfacePorts.setStatus("mandatory")
_IPermNetAddress_Type = PhysAddress
_IPermNetAddress_Object = MibTableColumn
iPermNetAddress = _IPermNetAddress_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 1, 2, 3, 2, 1, 4),
    _IPermNetAddress_Type()
)
iPermNetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iPermNetAddress.setStatus("mandatory")
_ICurrentNetAddress_Type = PhysAddress
_ICurrentNetAddress_Object = MibTableColumn
iCurrentNetAddress = _ICurrentNetAddress_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 1, 2, 3, 2, 1, 5),
    _ICurrentNetAddress_Type()
)
iCurrentNetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iCurrentNetAddress.setStatus("mandatory")
_IDataRate_Type = Integer32
_IDataRate_Object = MibTableColumn
iDataRate = _IDataRate_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 1, 2, 3, 2, 1, 6),
    _IDataRate_Type()
)
iDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iDataRate.setStatus("mandatory")
_ITotalPacketsTransmitted_Type = Counter32
_ITotalPacketsTransmitted_Object = MibTableColumn
iTotalPacketsTransmitted = _ITotalPacketsTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 1, 2, 3, 2, 1, 7),
    _ITotalPacketsTransmitted_Type()
)
iTotalPacketsTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iTotalPacketsTransmitted.setStatus("mandatory")
_ITotalBytesTransmitted_Type = Counter32
_ITotalBytesTransmitted_Object = MibTableColumn
iTotalBytesTransmitted = _ITotalBytesTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 1, 2, 3, 2, 1, 8),
    _ITotalBytesTransmitted_Type()
)
iTotalBytesTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iTotalBytesTransmitted.setStatus("mandatory")
_ITotalPacketsReceived_Type = Counter32
_ITotalPacketsReceived_Object = MibTableColumn
iTotalPacketsReceived = _ITotalPacketsReceived_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 1, 2, 3, 2, 1, 9),
    _ITotalPacketsReceived_Type()
)
iTotalPacketsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iTotalPacketsReceived.setStatus("mandatory")
_ITotalBytesReceived_Type = Counter32
_ITotalBytesReceived_Object = MibTableColumn
iTotalBytesReceived = _ITotalBytesReceived_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 1, 2, 3, 2, 1, 10),
    _ITotalBytesReceived_Type()
)
iTotalBytesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iTotalBytesReceived.setStatus("mandatory")
_ITotalTransmitErrors_Type = Counter32
_ITotalTransmitErrors_Object = MibTableColumn
iTotalTransmitErrors = _ITotalTransmitErrors_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 1, 2, 3, 2, 1, 11),
    _ITotalTransmitErrors_Type()
)
iTotalTransmitErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iTotalTransmitErrors.setStatus("mandatory")
_ITotalReceiveErrors_Type = Counter32
_ITotalReceiveErrors_Object = MibTableColumn
iTotalReceiveErrors = _ITotalReceiveErrors_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 1, 2, 3, 2, 1, 12),
    _ITotalReceiveErrors_Type()
)
iTotalReceiveErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iTotalReceiveErrors.setStatus("mandatory")


class _IInterfaceType_Type(Integer32):
    """Custom type iInterfaceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("failover", 2),
          ("loadBalanced", 3),
          ("standalone", 1))
    )


_IInterfaceType_Type.__name__ = "Integer32"
_IInterfaceType_Object = MibTableColumn
iInterfaceType = _IInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 1, 2, 3, 2, 1, 13),
    _IInterfaceType_Type()
)
iInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iInterfaceType.setStatus("mandatory")
_PortStatsTable_Object = MibTable
portStatsTable = _PortStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 1, 2, 3, 3)
)
if mibBuilder.loadTexts:
    portStatsTable.setStatus("mandatory")
_PortStatsEntry_Object = MibTableRow
portStatsEntry = _PortStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 1, 2, 3, 3, 1)
)
portStatsEntry.setIndexNames(
    (0, "ADAPTECDURALINK-MIB", "pInterfaceIndex"),
    (0, "ADAPTECDURALINK-MIB", "pPortIndex"),
)
if mibBuilder.loadTexts:
    portStatsEntry.setStatus("mandatory")
_PInterfaceIndex_Type = Integer32
_PInterfaceIndex_Object = MibTableColumn
pInterfaceIndex = _PInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 1, 2, 3, 3, 1, 1),
    _PInterfaceIndex_Type()
)
pInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pInterfaceIndex.setStatus("mandatory")
_PPortIndex_Type = Integer32
_PPortIndex_Object = MibTableColumn
pPortIndex = _PPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 1, 2, 3, 3, 1, 2),
    _PPortIndex_Type()
)
pPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pPortIndex.setStatus("mandatory")


class _PPortName_Type(DisplayString):
    """Custom type pPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_PPortName_Type.__name__ = "DisplayString"
_PPortName_Object = MibTableColumn
pPortName = _PPortName_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 1, 2, 3, 3, 1, 3),
    _PPortName_Type()
)
pPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pPortName.setStatus("mandatory")
_PCardNumber_Type = Integer32
_PCardNumber_Object = MibTableColumn
pCardNumber = _PCardNumber_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 1, 2, 3, 3, 1, 4),
    _PCardNumber_Type()
)
pCardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pCardNumber.setStatus("mandatory")
_PCardPortNumber_Type = Integer32
_PCardPortNumber_Object = MibTableColumn
pCardPortNumber = _PCardPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 1, 2, 3, 3, 1, 5),
    _PCardPortNumber_Type()
)
pCardPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pCardPortNumber.setStatus("mandatory")
_PPermNetAddress_Type = PhysAddress
_PPermNetAddress_Object = MibTableColumn
pPermNetAddress = _PPermNetAddress_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 1, 2, 3, 3, 1, 6),
    _PPermNetAddress_Type()
)
pPermNetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pPermNetAddress.setStatus("mandatory")
_PCurrentNetAddress_Type = PhysAddress
_PCurrentNetAddress_Object = MibTableColumn
pCurrentNetAddress = _PCurrentNetAddress_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 1, 2, 3, 3, 1, 7),
    _PCurrentNetAddress_Type()
)
pCurrentNetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pCurrentNetAddress.setStatus("mandatory")
_PDataRate_Type = Integer32
_PDataRate_Object = MibTableColumn
pDataRate = _PDataRate_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 1, 2, 3, 3, 1, 8),
    _PDataRate_Type()
)
pDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pDataRate.setStatus("mandatory")
_PTotalPacketsTransmitted_Type = Counter32
_PTotalPacketsTransmitted_Object = MibTableColumn
pTotalPacketsTransmitted = _PTotalPacketsTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 1, 2, 3, 3, 1, 9),
    _PTotalPacketsTransmitted_Type()
)
pTotalPacketsTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pTotalPacketsTransmitted.setStatus("mandatory")
_PTotalBytesTransmitted_Type = Counter32
_PTotalBytesTransmitted_Object = MibTableColumn
pTotalBytesTransmitted = _PTotalBytesTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 1, 2, 3, 3, 1, 10),
    _PTotalBytesTransmitted_Type()
)
pTotalBytesTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pTotalBytesTransmitted.setStatus("mandatory")
_PTotalPacketsReceived_Type = Counter32
_PTotalPacketsReceived_Object = MibTableColumn
pTotalPacketsReceived = _PTotalPacketsReceived_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 1, 2, 3, 3, 1, 11),
    _PTotalPacketsReceived_Type()
)
pTotalPacketsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pTotalPacketsReceived.setStatus("mandatory")
_PTotalBytesReceived_Type = Counter32
_PTotalBytesReceived_Object = MibTableColumn
pTotalBytesReceived = _PTotalBytesReceived_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 1, 2, 3, 3, 1, 12),
    _PTotalBytesReceived_Type()
)
pTotalBytesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pTotalBytesReceived.setStatus("mandatory")
_PTotalTransmitErrors_Type = Counter32
_PTotalTransmitErrors_Object = MibTableColumn
pTotalTransmitErrors = _PTotalTransmitErrors_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 1, 2, 3, 3, 1, 13),
    _PTotalTransmitErrors_Type()
)
pTotalTransmitErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pTotalTransmitErrors.setStatus("mandatory")
_PTotalReceiveErrors_Type = Counter32
_PTotalReceiveErrors_Object = MibTableColumn
pTotalReceiveErrors = _PTotalReceiveErrors_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 1, 2, 3, 3, 1, 14),
    _PTotalReceiveErrors_Type()
)
pTotalReceiveErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pTotalReceiveErrors.setStatus("mandatory")


class _PStatus_Type(Integer32):
    """Custom type pStatus based on Integer32"""
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
        *(("portActive", 1),
          ("portDisabled", 4),
          ("portDown", 2),
          ("portInStandby", 3))
    )


_PStatus_Type.__name__ = "Integer32"
_PStatus_Object = MibTableColumn
pStatus = _PStatus_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 1, 2, 3, 3, 1, 15),
    _PStatus_Type()
)
pStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pStatus.setStatus("mandatory")
_CardInformationTable_Object = MibTable
cardInformationTable = _CardInformationTable_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 1, 2, 3, 4)
)
if mibBuilder.loadTexts:
    cardInformationTable.setStatus("mandatory")
_CardInformationEntry_Object = MibTableRow
cardInformationEntry = _CardInformationEntry_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 1, 2, 3, 4, 1)
)
cardInformationEntry.setIndexNames(
    (0, "ADAPTECDURALINK-MIB", "cCardIndex"),
)
if mibBuilder.loadTexts:
    cardInformationEntry.setStatus("mandatory")
_CCardIndex_Type = Integer32
_CCardIndex_Object = MibTableColumn
cCardIndex = _CCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 1, 2, 3, 4, 1, 1),
    _CCardIndex_Type()
)
cCardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCardIndex.setStatus("mandatory")


class _CCardDescription_Type(DisplayString):
    """Custom type cCardDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_CCardDescription_Type.__name__ = "DisplayString"
_CCardDescription_Object = MibTableColumn
cCardDescription = _CCardDescription_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 1, 2, 3, 4, 1, 2),
    _CCardDescription_Type()
)
cCardDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCardDescription.setStatus("mandatory")
_CPortsOnCard_Type = Integer32
_CPortsOnCard_Object = MibTableColumn
cPortsOnCard = _CPortsOnCard_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 1, 2, 3, 4, 1, 3),
    _CPortsOnCard_Type()
)
cPortsOnCard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cPortsOnCard.setStatus("mandatory")
_CardPortInfoTable_Object = MibTable
cardPortInfoTable = _CardPortInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 1, 2, 3, 5)
)
if mibBuilder.loadTexts:
    cardPortInfoTable.setStatus("mandatory")
_CardPortInfoEntry_Object = MibTableRow
cardPortInfoEntry = _CardPortInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 1, 2, 3, 5, 1)
)
cardPortInfoEntry.setIndexNames(
    (0, "ADAPTECDURALINK-MIB", "cpCardIndex"),
    (0, "ADAPTECDURALINK-MIB", "cpPortIndex"),
)
if mibBuilder.loadTexts:
    cardPortInfoEntry.setStatus("mandatory")
_CpCardIndex_Type = Integer32
_CpCardIndex_Object = MibTableColumn
cpCardIndex = _CpCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 1, 2, 3, 5, 1, 1),
    _CpCardIndex_Type()
)
cpCardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpCardIndex.setStatus("mandatory")
_CpPortIndex_Type = Integer32
_CpPortIndex_Object = MibTableColumn
cpPortIndex = _CpPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 1, 2, 3, 5, 1, 2),
    _CpPortIndex_Type()
)
cpPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpPortIndex.setStatus("mandatory")
_CpInterfaceNumber_Type = Integer32
_CpInterfaceNumber_Object = MibTableColumn
cpInterfaceNumber = _CpInterfaceNumber_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 1, 2, 3, 5, 1, 3),
    _CpInterfaceNumber_Type()
)
cpInterfaceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpInterfaceNumber.setStatus("mandatory")
_CpPortNumber_Type = Integer32
_CpPortNumber_Object = MibTableColumn
cpPortNumber = _CpPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 1, 2, 3, 5, 1, 4),
    _CpPortNumber_Type()
)
cpPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpPortNumber.setStatus("mandatory")
_CpTableNumber1_Type = Integer32
_CpTableNumber1_Object = MibTableColumn
cpTableNumber1 = _CpTableNumber1_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 1, 2, 3, 5, 1, 5),
    _CpTableNumber1_Type()
)
cpTableNumber1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpTableNumber1.setStatus("mandatory")

# Managed Objects groups


# Notification objects

duralinkStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 3, 1, 2, 3, 0, 1)
)
duralinkStatusTrap.setObjects(
      *(("ADAPTECDURALINK-MIB", "pInterfaceIndex"),
        ("ADAPTECDURALINK-MIB", "pPortIndex"),
        ("ADAPTECDURALINK-MIB", "pStatus"))
)
if mibBuilder.loadTexts:
    duralinkStatusTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADAPTECDURALINK-MIB",
    **{"adaptec": adaptec,
       "products": products,
       "nic": nic,
       "npg": npg,
       "duralink": duralink,
       "duralinkStatusTrap": duralinkStatusTrap,
       "information": information,
       "numInterfaces": numInterfaces,
       "numPorts": numPorts,
       "numCards": numCards,
       "interfaceStatsTable": interfaceStatsTable,
       "interfaceStatsEntry": interfaceStatsEntry,
       "iInterfaceIndex": iInterfaceIndex,
       "iInterfaceName": iInterfaceName,
       "iInterfacePorts": iInterfacePorts,
       "iPermNetAddress": iPermNetAddress,
       "iCurrentNetAddress": iCurrentNetAddress,
       "iDataRate": iDataRate,
       "iTotalPacketsTransmitted": iTotalPacketsTransmitted,
       "iTotalBytesTransmitted": iTotalBytesTransmitted,
       "iTotalPacketsReceived": iTotalPacketsReceived,
       "iTotalBytesReceived": iTotalBytesReceived,
       "iTotalTransmitErrors": iTotalTransmitErrors,
       "iTotalReceiveErrors": iTotalReceiveErrors,
       "iInterfaceType": iInterfaceType,
       "portStatsTable": portStatsTable,
       "portStatsEntry": portStatsEntry,
       "pInterfaceIndex": pInterfaceIndex,
       "pPortIndex": pPortIndex,
       "pPortName": pPortName,
       "pCardNumber": pCardNumber,
       "pCardPortNumber": pCardPortNumber,
       "pPermNetAddress": pPermNetAddress,
       "pCurrentNetAddress": pCurrentNetAddress,
       "pDataRate": pDataRate,
       "pTotalPacketsTransmitted": pTotalPacketsTransmitted,
       "pTotalBytesTransmitted": pTotalBytesTransmitted,
       "pTotalPacketsReceived": pTotalPacketsReceived,
       "pTotalBytesReceived": pTotalBytesReceived,
       "pTotalTransmitErrors": pTotalTransmitErrors,
       "pTotalReceiveErrors": pTotalReceiveErrors,
       "pStatus": pStatus,
       "cardInformationTable": cardInformationTable,
       "cardInformationEntry": cardInformationEntry,
       "cCardIndex": cCardIndex,
       "cCardDescription": cCardDescription,
       "cPortsOnCard": cPortsOnCard,
       "cardPortInfoTable": cardPortInfoTable,
       "cardPortInfoEntry": cardPortInfoEntry,
       "cpCardIndex": cpCardIndex,
       "cpPortIndex": cpPortIndex,
       "cpInterfaceNumber": cpInterfaceNumber,
       "cpPortNumber": cpPortNumber,
       "cpTableNumber1": cpTableNumber1}
)
