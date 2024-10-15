# SNMP MIB module (RSPAN-MGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RSPAN-MGMT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:48:28 2024
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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

swRSPANMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 68)
)


# Types definitions



class VlanId(Integer32):
    """Custom type VlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )





class PortList(OctetString):
    """Custom type PortList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SwRSPANCtrl_ObjectIdentity = ObjectIdentity
swRSPANCtrl = _SwRSPANCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 68, 1)
)


class _SwRSPANState_Type(Integer32):
    """Custom type swRSPANState based on Integer32"""
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


_SwRSPANState_Type.__name__ = "Integer32"
_SwRSPANState_Object = MibScalar
swRSPANState = _SwRSPANState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 68, 1, 1),
    _SwRSPANState_Type()
)
swRSPANState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swRSPANState.setStatus("current")
_SwRSPANInfo_ObjectIdentity = ObjectIdentity
swRSPANInfo = _SwRSPANInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 68, 2)
)


class _SwRSPANMaxSupportedEntry_Type(Integer32):
    """Custom type swRSPANMaxSupportedEntry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwRSPANMaxSupportedEntry_Type.__name__ = "Integer32"
_SwRSPANMaxSupportedEntry_Object = MibScalar
swRSPANMaxSupportedEntry = _SwRSPANMaxSupportedEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 68, 2, 1),
    _SwRSPANMaxSupportedEntry_Type()
)
swRSPANMaxSupportedEntry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swRSPANMaxSupportedEntry.setStatus("current")


class _SwRSPANCurrentNumEntries_Type(Integer32):
    """Custom type swRSPANCurrentNumEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwRSPANCurrentNumEntries_Type.__name__ = "Integer32"
_SwRSPANCurrentNumEntries_Object = MibScalar
swRSPANCurrentNumEntries = _SwRSPANCurrentNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 68, 2, 2),
    _SwRSPANCurrentNumEntries_Type()
)
swRSPANCurrentNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swRSPANCurrentNumEntries.setStatus("current")
_SwRSPANMgmt_ObjectIdentity = ObjectIdentity
swRSPANMgmt = _SwRSPANMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 68, 3)
)
_SwRSPANTable_Object = MibTable
swRSPANTable = _SwRSPANTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 68, 3, 1)
)
if mibBuilder.loadTexts:
    swRSPANTable.setStatus("current")
_SwRSPANEntry_Object = MibTableRow
swRSPANEntry = _SwRSPANEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 68, 3, 1, 1)
)
swRSPANEntry.setIndexNames(
    (0, "RSPAN-MGMT-MIB", "swRSPANVLANID"),
)
if mibBuilder.loadTexts:
    swRSPANEntry.setStatus("current")
_SwRSPANVLANID_Type = VlanId
_SwRSPANVLANID_Object = MibTableColumn
swRSPANVLANID = _SwRSPANVLANID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 68, 3, 1, 1, 1),
    _SwRSPANVLANID_Type()
)
swRSPANVLANID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swRSPANVLANID.setStatus("current")
_SwRSPANSourceIngress_Type = PortList
_SwRSPANSourceIngress_Object = MibTableColumn
swRSPANSourceIngress = _SwRSPANSourceIngress_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 68, 3, 1, 1, 2),
    _SwRSPANSourceIngress_Type()
)
swRSPANSourceIngress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swRSPANSourceIngress.setStatus("current")
_SwRSPANSourceEgress_Type = PortList
_SwRSPANSourceEgress_Object = MibTableColumn
swRSPANSourceEgress = _SwRSPANSourceEgress_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 68, 3, 1, 1, 3),
    _SwRSPANSourceEgress_Type()
)
swRSPANSourceEgress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swRSPANSourceEgress.setStatus("current")
_SwRSPANRedirct_Type = PortList
_SwRSPANRedirct_Object = MibTableColumn
swRSPANRedirct = _SwRSPANRedirct_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 68, 3, 1, 1, 4),
    _SwRSPANRedirct_Type()
)
swRSPANRedirct.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swRSPANRedirct.setStatus("current")
_SwRSPANRowStatus_Type = RowStatus
_SwRSPANRowStatus_Object = MibTableColumn
swRSPANRowStatus = _SwRSPANRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 68, 3, 1, 1, 5),
    _SwRSPANRowStatus_Type()
)
swRSPANRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swRSPANRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RSPAN-MGMT-MIB",
    **{"VlanId": VlanId,
       "PortList": PortList,
       "swRSPANMIB": swRSPANMIB,
       "swRSPANCtrl": swRSPANCtrl,
       "swRSPANState": swRSPANState,
       "swRSPANInfo": swRSPANInfo,
       "swRSPANMaxSupportedEntry": swRSPANMaxSupportedEntry,
       "swRSPANCurrentNumEntries": swRSPANCurrentNumEntries,
       "swRSPANMgmt": swRSPANMgmt,
       "swRSPANTable": swRSPANTable,
       "swRSPANEntry": swRSPANEntry,
       "swRSPANVLANID": swRSPANVLANID,
       "swRSPANSourceIngress": swRSPANSourceIngress,
       "swRSPANSourceEgress": swRSPANSourceEgress,
       "swRSPANRedirct": swRSPANRedirct,
       "swRSPANRowStatus": swRSPANRowStatus}
)
