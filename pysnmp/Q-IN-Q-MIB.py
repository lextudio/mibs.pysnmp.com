# SNMP MIB module (Q-IN-Q-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Q-IN-Q-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:40:36 2024
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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

swQinQMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 57)
)


# Types definitions



class VlanId(Integer32):
    """Custom type VlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SwQinQCtrl_ObjectIdentity = ObjectIdentity
swQinQCtrl = _SwQinQCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 57, 1)
)


class _SwQinQState_Type(Integer32):
    """Custom type swQinQState based on Integer32"""
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


_SwQinQState_Type.__name__ = "Integer32"
_SwQinQState_Object = MibScalar
swQinQState = _SwQinQState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 57, 1, 1),
    _SwQinQState_Type()
)
swQinQState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swQinQState.setStatus("current")
_SwQinQInfo_ObjectIdentity = ObjectIdentity
swQinQInfo = _SwQinQInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 57, 2)
)
_SwQinQPortMgmt_ObjectIdentity = ObjectIdentity
swQinQPortMgmt = _SwQinQPortMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 57, 3)
)
_SwQinQPortTable_Object = MibTable
swQinQPortTable = _SwQinQPortTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 57, 3, 1)
)
if mibBuilder.loadTexts:
    swQinQPortTable.setStatus("current")
_SwQinQPortEntry_Object = MibTableRow
swQinQPortEntry = _SwQinQPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 57, 3, 1, 1)
)
swQinQPortEntry.setIndexNames(
    (0, "Q-IN-Q-MIB", "swQinQPortIndex"),
)
if mibBuilder.loadTexts:
    swQinQPortEntry.setStatus("current")


class _SwQinQPortIndex_Type(Integer32):
    """Custom type swQinQPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SwQinQPortIndex_Type.__name__ = "Integer32"
_SwQinQPortIndex_Object = MibTableColumn
swQinQPortIndex = _SwQinQPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 57, 3, 1, 1, 1),
    _SwQinQPortIndex_Type()
)
swQinQPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swQinQPortIndex.setStatus("current")


class _SwQinQPortRole_Type(Integer32):
    """Custom type swQinQPortRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nni", 1),
          ("uni", 2))
    )


_SwQinQPortRole_Type.__name__ = "Integer32"
_SwQinQPortRole_Object = MibTableColumn
swQinQPortRole = _SwQinQPortRole_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 57, 3, 1, 1, 2),
    _SwQinQPortRole_Type()
)
swQinQPortRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swQinQPortRole.setStatus("current")


class _SwQinQPortTpid_Type(OctetString):
    """Custom type swQinQPortTpid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_SwQinQPortTpid_Type.__name__ = "OctetString"
_SwQinQPortTpid_Object = MibTableColumn
swQinQPortTpid = _SwQinQPortTpid_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 57, 3, 1, 1, 4),
    _SwQinQPortTpid_Type()
)
swQinQPortTpid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swQinQPortTpid.setStatus("current")
_SwQinQMgmt_ObjectIdentity = ObjectIdentity
swQinQMgmt = _SwQinQMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 57, 4)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Q-IN-Q-MIB",
    **{"VlanId": VlanId,
       "swQinQMIB": swQinQMIB,
       "swQinQCtrl": swQinQCtrl,
       "swQinQState": swQinQState,
       "swQinQInfo": swQinQInfo,
       "swQinQPortMgmt": swQinQPortMgmt,
       "swQinQPortTable": swQinQPortTable,
       "swQinQPortEntry": swQinQPortEntry,
       "swQinQPortIndex": swQinQPortIndex,
       "swQinQPortRole": swQinQPortRole,
       "swQinQPortTpid": swQinQPortTpid,
       "swQinQMgmt": swQinQMgmt}
)
