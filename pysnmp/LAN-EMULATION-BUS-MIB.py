# SNMP MIB module (LAN-EMULATION-BUS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/LAN-EMULATION-BUS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:07:25 2024
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

(VciInteger,
 VpiInteger,
 atmfLanEmulation) = mibBuilder.importSymbols(
    "LAN-EMULATION-CLIENT-MIB",
    "VciInteger",
    "VpiInteger",
    "atmfLanEmulation")

(AtmLaneMask,
 IfIndexOrZero,
 Integer,
 TIMESTAMP) = mibBuilder.importSymbols(
    "LAN-EMULATION-ELAN-MIB",
    "AtmLaneMask",
    "IfIndexOrZero",
    "Integer",
    "TIMESTAMP")

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



class RowStatus(Integer32):
    """Custom type RowStatus based on Integer32"""




class AtmLaneAddress(OctetString):
    """Custom type AtmLaneAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(20, 20),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BusMIB_ObjectIdentity = ObjectIdentity
busMIB = _BusMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 4)
)
_BusConfGroup_ObjectIdentity = ObjectIdentity
busConfGroup = _BusConfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 4, 1)
)
_BusConfNextId_Type = Integer32
_BusConfNextId_Object = MibScalar
busConfNextId = _BusConfNextId_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 4, 1, 1),
    _BusConfNextId_Type()
)
busConfNextId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busConfNextId.setStatus("mandatory")
_BusConfTable_Object = MibTable
busConfTable = _BusConfTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 4, 1, 2)
)
if mibBuilder.loadTexts:
    busConfTable.setStatus("mandatory")
_BusConfEntry_Object = MibTableRow
busConfEntry = _BusConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 4, 1, 2, 1)
)
busConfEntry.setIndexNames(
    (0, "LAN-EMULATION-BUS-MIB", "busConfIndex"),
)
if mibBuilder.loadTexts:
    busConfEntry.setStatus("mandatory")
_BusConfIndex_Type = Integer32
_BusConfIndex_Object = MibTableColumn
busConfIndex = _BusConfIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 4, 1, 2, 1, 1),
    _BusConfIndex_Type()
)
busConfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    busConfIndex.setStatus("mandatory")
_BusConfAtmAddrSpec_Type = AtmLaneAddress
_BusConfAtmAddrSpec_Object = MibTableColumn
busConfAtmAddrSpec = _BusConfAtmAddrSpec_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 4, 1, 2, 1, 2),
    _BusConfAtmAddrSpec_Type()
)
busConfAtmAddrSpec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    busConfAtmAddrSpec.setStatus("mandatory")


class _BusConfAtmAddrMask_Type(AtmLaneMask):
    """Custom type busConfAtmAddrMask based on AtmLaneMask"""
    defaultHexValue = "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF"


_BusConfAtmAddrMask_Object = MibTableColumn
busConfAtmAddrMask = _BusConfAtmAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 4, 1, 2, 1, 3),
    _BusConfAtmAddrMask_Type()
)
busConfAtmAddrMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    busConfAtmAddrMask.setStatus("mandatory")
_BusConfAtmAddrActual_Type = AtmLaneAddress
_BusConfAtmAddrActual_Object = MibTableColumn
busConfAtmAddrActual = _BusConfAtmAddrActual_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 4, 1, 2, 1, 4),
    _BusConfAtmAddrActual_Type()
)
busConfAtmAddrActual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busConfAtmAddrActual.setStatus("mandatory")


class _BusConfElanName_Type(DisplayString):
    """Custom type busConfElanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BusConfElanName_Type.__name__ = "DisplayString"
_BusConfElanName_Object = MibTableColumn
busConfElanName = _BusConfElanName_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 4, 1, 2, 1, 5),
    _BusConfElanName_Type()
)
busConfElanName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    busConfElanName.setStatus("mandatory")
_BusConfLastChange_Type = TIMESTAMP
_BusConfLastChange_Object = MibTableColumn
busConfLastChange = _BusConfLastChange_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 4, 1, 2, 1, 6),
    _BusConfLastChange_Type()
)
busConfLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busConfLastChange.setStatus("mandatory")


class _BusConfMaxFrameAge_Type(Integer32):
    """Custom type busConfMaxFrameAge based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_BusConfMaxFrameAge_Type.__name__ = "Integer32"
_BusConfMaxFrameAge_Object = MibTableColumn
busConfMaxFrameAge = _BusConfMaxFrameAge_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 4, 1, 2, 1, 7),
    _BusConfMaxFrameAge_Type()
)
busConfMaxFrameAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    busConfMaxFrameAge.setStatus("mandatory")


class _BusConfOperStatus_Type(Integer32):
    """Custom type busConfOperStatus based on Integer32"""
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


_BusConfOperStatus_Type.__name__ = "Integer32"
_BusConfOperStatus_Object = MibTableColumn
busConfOperStatus = _BusConfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 4, 1, 2, 1, 8),
    _BusConfOperStatus_Type()
)
busConfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busConfOperStatus.setStatus("mandatory")


class _BusConfAdminStatus_Type(Integer32):
    """Custom type busConfAdminStatus based on Integer32"""
    defaultValue = 2

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


_BusConfAdminStatus_Type.__name__ = "Integer32"
_BusConfAdminStatus_Object = MibTableColumn
busConfAdminStatus = _BusConfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 4, 1, 2, 1, 9),
    _BusConfAdminStatus_Type()
)
busConfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    busConfAdminStatus.setStatus("mandatory")
_BusConfRowStatus_Type = RowStatus
_BusConfRowStatus_Object = MibTableColumn
busConfRowStatus = _BusConfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 4, 1, 2, 1, 10),
    _BusConfRowStatus_Type()
)
busConfRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    busConfRowStatus.setStatus("mandatory")
_BusVccTable_Object = MibTable
busVccTable = _BusVccTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 4, 1, 3)
)
if mibBuilder.loadTexts:
    busVccTable.setStatus("mandatory")
_BusVccEntry_Object = MibTableRow
busVccEntry = _BusVccEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 4, 1, 3, 1)
)
busVccEntry.setIndexNames(
    (0, "LAN-EMULATION-BUS-MIB", "busConfIndex"),
    (0, "LAN-EMULATION-BUS-MIB", "busVccAtmIfIndex"),
    (0, "LAN-EMULATION-BUS-MIB", "busVccMtFwdVpi"),
    (0, "LAN-EMULATION-BUS-MIB", "busVccMtFwdVci"),
)
if mibBuilder.loadTexts:
    busVccEntry.setStatus("mandatory")
_BusVccAtmIfIndex_Type = IfIndexOrZero
_BusVccAtmIfIndex_Object = MibTableColumn
busVccAtmIfIndex = _BusVccAtmIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 4, 1, 3, 1, 1),
    _BusVccAtmIfIndex_Type()
)
busVccAtmIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    busVccAtmIfIndex.setStatus("mandatory")
_BusVccMtFwdVpi_Type = VpiInteger
_BusVccMtFwdVpi_Object = MibTableColumn
busVccMtFwdVpi = _BusVccMtFwdVpi_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 4, 1, 3, 1, 2),
    _BusVccMtFwdVpi_Type()
)
busVccMtFwdVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    busVccMtFwdVpi.setStatus("mandatory")
_BusVccMtFwdVci_Type = VciInteger
_BusVccMtFwdVci_Object = MibTableColumn
busVccMtFwdVci = _BusVccMtFwdVci_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 4, 1, 3, 1, 3),
    _BusVccMtFwdVci_Type()
)
busVccMtFwdVci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    busVccMtFwdVci.setStatus("mandatory")
_BusVccRowStatus_Type = RowStatus
_BusVccRowStatus_Object = MibTableColumn
busVccRowStatus = _BusVccRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 4, 1, 3, 1, 4),
    _BusVccRowStatus_Type()
)
busVccRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    busVccRowStatus.setStatus("mandatory")
_BusLecTableLastChange_Type = TIMESTAMP
_BusLecTableLastChange_Object = MibScalar
busLecTableLastChange = _BusLecTableLastChange_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 4, 1, 4),
    _BusLecTableLastChange_Type()
)
busLecTableLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busLecTableLastChange.setStatus("mandatory")
_BusLecTable_Object = MibTable
busLecTable = _BusLecTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 4, 1, 5)
)
if mibBuilder.loadTexts:
    busLecTable.setStatus("mandatory")
_BusLecEntry_Object = MibTableRow
busLecEntry = _BusLecEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 4, 1, 5, 1)
)
busLecEntry.setIndexNames(
    (0, "LAN-EMULATION-BUS-MIB", "busConfIndex"),
    (0, "LAN-EMULATION-BUS-MIB", "busLecAtmAddr"),
)
if mibBuilder.loadTexts:
    busLecEntry.setStatus("mandatory")
_BusLecAtmAddr_Type = AtmLaneAddress
_BusLecAtmAddr_Object = MibTableColumn
busLecAtmAddr = _BusLecAtmAddr_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 4, 1, 5, 1, 1),
    _BusLecAtmAddr_Type()
)
busLecAtmAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    busLecAtmAddr.setStatus("mandatory")
_BusLecMcastSendAtmIfIndex_Type = IfIndexOrZero
_BusLecMcastSendAtmIfIndex_Object = MibTableColumn
busLecMcastSendAtmIfIndex = _BusLecMcastSendAtmIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 4, 1, 5, 1, 2),
    _BusLecMcastSendAtmIfIndex_Type()
)
busLecMcastSendAtmIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    busLecMcastSendAtmIfIndex.setStatus("mandatory")
_BusLecMcastSendVpi_Type = VpiInteger
_BusLecMcastSendVpi_Object = MibTableColumn
busLecMcastSendVpi = _BusLecMcastSendVpi_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 4, 1, 5, 1, 4),
    _BusLecMcastSendVpi_Type()
)
busLecMcastSendVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    busLecMcastSendVpi.setStatus("mandatory")
_BusLecMcastSendVci_Type = VciInteger
_BusLecMcastSendVci_Object = MibTableColumn
busLecMcastSendVci = _BusLecMcastSendVci_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 4, 1, 5, 1, 5),
    _BusLecMcastSendVci_Type()
)
busLecMcastSendVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    busLecMcastSendVci.setStatus("mandatory")
_BusLecRowStatus_Type = RowStatus
_BusLecRowStatus_Object = MibTableColumn
busLecRowStatus = _BusLecRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 4, 1, 5, 1, 6),
    _BusLecRowStatus_Type()
)
busLecRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    busLecRowStatus.setStatus("mandatory")
_BusStatGroup_ObjectIdentity = ObjectIdentity
busStatGroup = _BusStatGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 4, 2)
)
_BusStatTable_Object = MibTable
busStatTable = _BusStatTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 4, 2, 1)
)
if mibBuilder.loadTexts:
    busStatTable.setStatus("mandatory")
_BusStatEntry_Object = MibTableRow
busStatEntry = _BusStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 4, 2, 1, 1)
)
busStatEntry.setIndexNames(
    (0, "LAN-EMULATION-BUS-MIB", "busConfIndex"),
)
if mibBuilder.loadTexts:
    busStatEntry.setStatus("mandatory")
_BusStatInDiscards_Type = Counter32
_BusStatInDiscards_Object = MibTableColumn
busStatInDiscards = _BusStatInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 4, 2, 1, 1, 1),
    _BusStatInDiscards_Type()
)
busStatInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busStatInDiscards.setStatus("mandatory")
_BusStatInOctets_Type = Counter32
_BusStatInOctets_Object = MibTableColumn
busStatInOctets = _BusStatInOctets_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 4, 2, 1, 1, 2),
    _BusStatInOctets_Type()
)
busStatInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busStatInOctets.setStatus("mandatory")
_BusStatInUcastFrms_Type = Counter32
_BusStatInUcastFrms_Object = MibTableColumn
busStatInUcastFrms = _BusStatInUcastFrms_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 4, 2, 1, 1, 3),
    _BusStatInUcastFrms_Type()
)
busStatInUcastFrms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busStatInUcastFrms.setStatus("mandatory")
_BusStatInMcastFrms_Type = Counter32
_BusStatInMcastFrms_Object = MibTableColumn
busStatInMcastFrms = _BusStatInMcastFrms_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 4, 2, 1, 1, 4),
    _BusStatInMcastFrms_Type()
)
busStatInMcastFrms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busStatInMcastFrms.setStatus("mandatory")
_BusStatFrmTimeOuts_Type = Counter32
_BusStatFrmTimeOuts_Object = MibTableColumn
busStatFrmTimeOuts = _BusStatFrmTimeOuts_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 4, 2, 1, 1, 5),
    _BusStatFrmTimeOuts_Type()
)
busStatFrmTimeOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busStatFrmTimeOuts.setStatus("mandatory")
_BusStatMcastSendRefused_Type = Counter32
_BusStatMcastSendRefused_Object = MibTableColumn
busStatMcastSendRefused = _BusStatMcastSendRefused_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 4, 2, 1, 1, 6),
    _BusStatMcastSendRefused_Type()
)
busStatMcastSendRefused.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busStatMcastSendRefused.setStatus("mandatory")
_BusStatMcastFwdFailure_Type = Counter32
_BusStatMcastFwdFailure_Object = MibTableColumn
busStatMcastFwdFailure = _BusStatMcastFwdFailure_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 4, 2, 1, 1, 7),
    _BusStatMcastFwdFailure_Type()
)
busStatMcastFwdFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busStatMcastFwdFailure.setStatus("mandatory")
_BusLecStatTable_Object = MibTable
busLecStatTable = _BusLecStatTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 4, 2, 2)
)
if mibBuilder.loadTexts:
    busLecStatTable.setStatus("mandatory")
_BusLecStatEntry_Object = MibTableRow
busLecStatEntry = _BusLecStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 4, 2, 2, 1)
)
busLecStatEntry.setIndexNames(
    (0, "LAN-EMULATION-BUS-MIB", "busConfIndex"),
    (0, "LAN-EMULATION-BUS-MIB", "busLecAtmAddr"),
)
if mibBuilder.loadTexts:
    busLecStatEntry.setStatus("mandatory")
_BusLecRecvs_Type = Counter32
_BusLecRecvs_Object = MibTableColumn
busLecRecvs = _BusLecRecvs_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 4, 2, 2, 1, 1),
    _BusLecRecvs_Type()
)
busLecRecvs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busLecRecvs.setStatus("mandatory")
_BusLecForwards_Type = Counter32
_BusLecForwards_Object = MibTableColumn
busLecForwards = _BusLecForwards_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 4, 2, 2, 1, 2),
    _BusLecForwards_Type()
)
busLecForwards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busLecForwards.setStatus("mandatory")
_BusLecDiscards_Type = Counter32
_BusLecDiscards_Object = MibTableColumn
busLecDiscards = _BusLecDiscards_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 4, 2, 2, 1, 3),
    _BusLecDiscards_Type()
)
busLecDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busLecDiscards.setStatus("mandatory")
_BusFaultGroup_ObjectIdentity = ObjectIdentity
busFaultGroup = _BusFaultGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 4, 3)
)
_BusErrCtlTable_Object = MibTable
busErrCtlTable = _BusErrCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 4, 3, 1)
)
if mibBuilder.loadTexts:
    busErrCtlTable.setStatus("mandatory")
_BusErrCtlEntry_Object = MibTableRow
busErrCtlEntry = _BusErrCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 4, 3, 1, 1)
)
busErrCtlEntry.setIndexNames(
    (0, "LAN-EMULATION-BUS-MIB", "busConfIndex"),
)
if mibBuilder.loadTexts:
    busErrCtlEntry.setStatus("mandatory")


class _BusErrCtlAdminStatus_Type(Integer32):
    """Custom type busErrCtlAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_BusErrCtlAdminStatus_Type.__name__ = "Integer32"
_BusErrCtlAdminStatus_Object = MibTableColumn
busErrCtlAdminStatus = _BusErrCtlAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 4, 3, 1, 1, 1),
    _BusErrCtlAdminStatus_Type()
)
busErrCtlAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    busErrCtlAdminStatus.setStatus("mandatory")


class _BusErrCtlOperStatus_Type(Integer32):
    """Custom type busErrCtlOperStatus based on Integer32"""
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
        *(("active", 2),
          ("disabled", 5),
          ("failed", 4),
          ("other", 1),
          ("outOfRes", 3))
    )


_BusErrCtlOperStatus_Type.__name__ = "Integer32"
_BusErrCtlOperStatus_Object = MibTableColumn
busErrCtlOperStatus = _BusErrCtlOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 4, 3, 1, 1, 2),
    _BusErrCtlOperStatus_Type()
)
busErrCtlOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busErrCtlOperStatus.setStatus("mandatory")


class _BusErrCtlClearLog_Type(Integer32):
    """Custom type busErrCtlClearLog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("noOp", 1))
    )


_BusErrCtlClearLog_Type.__name__ = "Integer32"
_BusErrCtlClearLog_Object = MibTableColumn
busErrCtlClearLog = _BusErrCtlClearLog_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 4, 3, 1, 1, 3),
    _BusErrCtlClearLog_Type()
)
busErrCtlClearLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    busErrCtlClearLog.setStatus("mandatory")


class _BusErrCtlMaxEntries_Type(Integer32):
    """Custom type busErrCtlMaxEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_BusErrCtlMaxEntries_Type.__name__ = "Integer32"
_BusErrCtlMaxEntries_Object = MibTableColumn
busErrCtlMaxEntries = _BusErrCtlMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 4, 3, 1, 1, 4),
    _BusErrCtlMaxEntries_Type()
)
busErrCtlMaxEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busErrCtlMaxEntries.setStatus("mandatory")


class _BusErrCtlLastEntry_Type(Integer32):
    """Custom type busErrCtlLastEntry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_BusErrCtlLastEntry_Type.__name__ = "Integer32"
_BusErrCtlLastEntry_Object = MibTableColumn
busErrCtlLastEntry = _BusErrCtlLastEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 4, 3, 1, 1, 5),
    _BusErrCtlLastEntry_Type()
)
busErrCtlLastEntry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    busErrCtlLastEntry.setStatus("mandatory")
_BusErrLogTable_Object = MibTable
busErrLogTable = _BusErrLogTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 4, 3, 2)
)
if mibBuilder.loadTexts:
    busErrLogTable.setStatus("mandatory")
_BusErrLogEntry_Object = MibTableRow
busErrLogEntry = _BusErrLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 4, 3, 2, 1)
)
busErrLogEntry.setIndexNames(
    (0, "LAN-EMULATION-BUS-MIB", "busConfIndex"),
    (0, "LAN-EMULATION-BUS-MIB", "busErrLogIndex"),
)
if mibBuilder.loadTexts:
    busErrLogEntry.setStatus("mandatory")


class _BusErrLogIndex_Type(Integer32):
    """Custom type busErrLogIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_BusErrLogIndex_Type.__name__ = "Integer32"
_BusErrLogIndex_Object = MibTableColumn
busErrLogIndex = _BusErrLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 4, 3, 2, 1, 1),
    _BusErrLogIndex_Type()
)
busErrLogIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    busErrLogIndex.setStatus("mandatory")
_BusErrLogAtmAddr_Type = AtmLaneAddress
_BusErrLogAtmAddr_Object = MibTableColumn
busErrLogAtmAddr = _BusErrLogAtmAddr_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 4, 3, 2, 1, 2),
    _BusErrLogAtmAddr_Type()
)
busErrLogAtmAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busErrLogAtmAddr.setStatus("mandatory")


class _BusErrLogErrCode_Type(Integer32):
    """Custom type busErrLogErrCode based on Integer32"""
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
        *(("badCtlFrame", 2),
          ("badDataFrame", 3),
          ("other", 4),
          ("outOfRes", 1))
    )


_BusErrLogErrCode_Type.__name__ = "Integer32"
_BusErrLogErrCode_Object = MibTableColumn
busErrLogErrCode = _BusErrLogErrCode_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 4, 3, 2, 1, 3),
    _BusErrLogErrCode_Type()
)
busErrLogErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busErrLogErrCode.setStatus("mandatory")
_BusErrLogTime_Type = TIMESTAMP
_BusErrLogTime_Object = MibTableColumn
busErrLogTime = _BusErrLogTime_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 3, 4, 3, 2, 1, 4),
    _BusErrLogTime_Type()
)
busErrLogTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busErrLogTime.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LAN-EMULATION-BUS-MIB",
    **{"RowStatus": RowStatus,
       "AtmLaneAddress": AtmLaneAddress,
       "busMIB": busMIB,
       "busConfGroup": busConfGroup,
       "busConfNextId": busConfNextId,
       "busConfTable": busConfTable,
       "busConfEntry": busConfEntry,
       "busConfIndex": busConfIndex,
       "busConfAtmAddrSpec": busConfAtmAddrSpec,
       "busConfAtmAddrMask": busConfAtmAddrMask,
       "busConfAtmAddrActual": busConfAtmAddrActual,
       "busConfElanName": busConfElanName,
       "busConfLastChange": busConfLastChange,
       "busConfMaxFrameAge": busConfMaxFrameAge,
       "busConfOperStatus": busConfOperStatus,
       "busConfAdminStatus": busConfAdminStatus,
       "busConfRowStatus": busConfRowStatus,
       "busVccTable": busVccTable,
       "busVccEntry": busVccEntry,
       "busVccAtmIfIndex": busVccAtmIfIndex,
       "busVccMtFwdVpi": busVccMtFwdVpi,
       "busVccMtFwdVci": busVccMtFwdVci,
       "busVccRowStatus": busVccRowStatus,
       "busLecTableLastChange": busLecTableLastChange,
       "busLecTable": busLecTable,
       "busLecEntry": busLecEntry,
       "busLecAtmAddr": busLecAtmAddr,
       "busLecMcastSendAtmIfIndex": busLecMcastSendAtmIfIndex,
       "busLecMcastSendVpi": busLecMcastSendVpi,
       "busLecMcastSendVci": busLecMcastSendVci,
       "busLecRowStatus": busLecRowStatus,
       "busStatGroup": busStatGroup,
       "busStatTable": busStatTable,
       "busStatEntry": busStatEntry,
       "busStatInDiscards": busStatInDiscards,
       "busStatInOctets": busStatInOctets,
       "busStatInUcastFrms": busStatInUcastFrms,
       "busStatInMcastFrms": busStatInMcastFrms,
       "busStatFrmTimeOuts": busStatFrmTimeOuts,
       "busStatMcastSendRefused": busStatMcastSendRefused,
       "busStatMcastFwdFailure": busStatMcastFwdFailure,
       "busLecStatTable": busLecStatTable,
       "busLecStatEntry": busLecStatEntry,
       "busLecRecvs": busLecRecvs,
       "busLecForwards": busLecForwards,
       "busLecDiscards": busLecDiscards,
       "busFaultGroup": busFaultGroup,
       "busErrCtlTable": busErrCtlTable,
       "busErrCtlEntry": busErrCtlEntry,
       "busErrCtlAdminStatus": busErrCtlAdminStatus,
       "busErrCtlOperStatus": busErrCtlOperStatus,
       "busErrCtlClearLog": busErrCtlClearLog,
       "busErrCtlMaxEntries": busErrCtlMaxEntries,
       "busErrCtlLastEntry": busErrCtlLastEntry,
       "busErrLogTable": busErrLogTable,
       "busErrLogEntry": busErrLogEntry,
       "busErrLogIndex": busErrLogIndex,
       "busErrLogAtmAddr": busErrLogAtmAddr,
       "busErrLogErrCode": busErrLogErrCode,
       "busErrLogTime": busErrLogTime}
)
