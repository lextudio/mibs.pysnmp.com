# SNMP MIB module (BPDU-TUNNELING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BPDU-TUNNELING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:48:34 2024
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

(dlink_common_mgmt,) = mibBuilder.importSymbols(
    "DLINK-ID-REC-MIB",
    "dlink-common-mgmt")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention")


# MODULE-IDENTITY

swBPDUTunnelMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 60)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SwBPDUTunnelCtrl_ObjectIdentity = ObjectIdentity
swBPDUTunnelCtrl = _SwBPDUTunnelCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 60, 1)
)


class _SwBPDUTunnelState_Type(Integer32):
    """Custom type swBPDUTunnelState based on Integer32"""
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


_SwBPDUTunnelState_Type.__name__ = "Integer32"
_SwBPDUTunnelState_Object = MibScalar
swBPDUTunnelState = _SwBPDUTunnelState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 60, 1, 1),
    _SwBPDUTunnelState_Type()
)
swBPDUTunnelState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swBPDUTunnelState.setStatus("current")
_SwBPDUTunnelInfo_ObjectIdentity = ObjectIdentity
swBPDUTunnelInfo = _SwBPDUTunnelInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 60, 2)
)
_SwBPDUTunnelSTPMcastAddress_Type = MacAddress
_SwBPDUTunnelSTPMcastAddress_Object = MibScalar
swBPDUTunnelSTPMcastAddress = _SwBPDUTunnelSTPMcastAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 60, 2, 1),
    _SwBPDUTunnelSTPMcastAddress_Type()
)
swBPDUTunnelSTPMcastAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swBPDUTunnelSTPMcastAddress.setStatus("current")
_SwBPDUTunnelGVRPMcastAddress_Type = MacAddress
_SwBPDUTunnelGVRPMcastAddress_Object = MibScalar
swBPDUTunnelGVRPMcastAddress = _SwBPDUTunnelGVRPMcastAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 60, 2, 2),
    _SwBPDUTunnelGVRPMcastAddress_Type()
)
swBPDUTunnelGVRPMcastAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swBPDUTunnelGVRPMcastAddress.setStatus("current")
_SwBPDUTunnelMgmt_ObjectIdentity = ObjectIdentity
swBPDUTunnelMgmt = _SwBPDUTunnelMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 60, 3)
)
_SwBPDUTunnelTable_Object = MibTable
swBPDUTunnelTable = _SwBPDUTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 60, 3, 1)
)
if mibBuilder.loadTexts:
    swBPDUTunnelTable.setStatus("current")
_SwBPDUTunnelEntry_Object = MibTableRow
swBPDUTunnelEntry = _SwBPDUTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 60, 3, 1, 1)
)
swBPDUTunnelEntry.setIndexNames(
    (0, "BPDU-TUNNELING-MIB", "swBPDUTunnelPortIndex"),
)
if mibBuilder.loadTexts:
    swBPDUTunnelEntry.setStatus("current")


class _SwBPDUTunnelPortIndex_Type(Integer32):
    """Custom type swBPDUTunnelPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwBPDUTunnelPortIndex_Type.__name__ = "Integer32"
_SwBPDUTunnelPortIndex_Object = MibTableColumn
swBPDUTunnelPortIndex = _SwBPDUTunnelPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 60, 3, 1, 1, 1),
    _SwBPDUTunnelPortIndex_Type()
)
swBPDUTunnelPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swBPDUTunnelPortIndex.setStatus("current")


class _SwBPDUTunnelPortType_Type(Integer32):
    """Custom type swBPDUTunnelPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("tunnel", 2),
          ("uplink", 3))
    )


_SwBPDUTunnelPortType_Type.__name__ = "Integer32"
_SwBPDUTunnelPortType_Object = MibTableColumn
swBPDUTunnelPortType = _SwBPDUTunnelPortType_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 60, 3, 1, 1, 2),
    _SwBPDUTunnelPortType_Type()
)
swBPDUTunnelPortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swBPDUTunnelPortType.setStatus("current")


class _SwBPDUTunnelSTPState_Type(Integer32):
    """Custom type swBPDUTunnelSTPState based on Integer32"""
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


_SwBPDUTunnelSTPState_Type.__name__ = "Integer32"
_SwBPDUTunnelSTPState_Object = MibTableColumn
swBPDUTunnelSTPState = _SwBPDUTunnelSTPState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 60, 3, 1, 1, 3),
    _SwBPDUTunnelSTPState_Type()
)
swBPDUTunnelSTPState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swBPDUTunnelSTPState.setStatus("current")


class _SwBPDUTunnelGVRPState_Type(Integer32):
    """Custom type swBPDUTunnelGVRPState based on Integer32"""
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


_SwBPDUTunnelGVRPState_Type.__name__ = "Integer32"
_SwBPDUTunnelGVRPState_Object = MibTableColumn
swBPDUTunnelGVRPState = _SwBPDUTunnelGVRPState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 60, 3, 1, 1, 4),
    _SwBPDUTunnelGVRPState_Type()
)
swBPDUTunnelGVRPState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swBPDUTunnelGVRPState.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BPDU-TUNNELING-MIB",
    **{"swBPDUTunnelMIB": swBPDUTunnelMIB,
       "swBPDUTunnelCtrl": swBPDUTunnelCtrl,
       "swBPDUTunnelState": swBPDUTunnelState,
       "swBPDUTunnelInfo": swBPDUTunnelInfo,
       "swBPDUTunnelSTPMcastAddress": swBPDUTunnelSTPMcastAddress,
       "swBPDUTunnelGVRPMcastAddress": swBPDUTunnelGVRPMcastAddress,
       "swBPDUTunnelMgmt": swBPDUTunnelMgmt,
       "swBPDUTunnelTable": swBPDUTunnelTable,
       "swBPDUTunnelEntry": swBPDUTunnelEntry,
       "swBPDUTunnelPortIndex": swBPDUTunnelPortIndex,
       "swBPDUTunnelPortType": swBPDUTunnelPortType,
       "swBPDUTunnelSTPState": swBPDUTunnelSTPState,
       "swBPDUTunnelGVRPState": swBPDUTunnelGVRPState}
)
