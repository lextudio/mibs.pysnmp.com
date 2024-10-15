# SNMP MIB module (STATICFDB-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/STATICFDB-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:57:56 2024
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

swStaticFdbMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 70)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SwStaticFdbMgmt_ObjectIdentity = ObjectIdentity
swStaticFdbMgmt = _SwStaticFdbMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 70, 1)
)
_SwStaticFdbMgmtTable_Object = MibTable
swStaticFdbMgmtTable = _SwStaticFdbMgmtTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 70, 1, 1)
)
if mibBuilder.loadTexts:
    swStaticFdbMgmtTable.setStatus("current")
_SwStaticFdbMgmtEntry_Object = MibTableRow
swStaticFdbMgmtEntry = _SwStaticFdbMgmtEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 70, 1, 1, 1)
)
swStaticFdbMgmtEntry.setIndexNames(
    (0, "STATICFDB-MIB", "swStaticFdbMgmtVlanID"),
    (0, "STATICFDB-MIB", "swStaticFdbMgmtMacAddr"),
)
if mibBuilder.loadTexts:
    swStaticFdbMgmtEntry.setStatus("current")


class _SwStaticFdbMgmtVlanID_Type(Integer32):
    """Custom type swStaticFdbMgmtVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_SwStaticFdbMgmtVlanID_Type.__name__ = "Integer32"
_SwStaticFdbMgmtVlanID_Object = MibTableColumn
swStaticFdbMgmtVlanID = _SwStaticFdbMgmtVlanID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 70, 1, 1, 1, 1),
    _SwStaticFdbMgmtVlanID_Type()
)
swStaticFdbMgmtVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swStaticFdbMgmtVlanID.setStatus("current")
_SwStaticFdbMgmtMacAddr_Type = MacAddress
_SwStaticFdbMgmtMacAddr_Object = MibTableColumn
swStaticFdbMgmtMacAddr = _SwStaticFdbMgmtMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 70, 1, 1, 1, 2),
    _SwStaticFdbMgmtMacAddr_Type()
)
swStaticFdbMgmtMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swStaticFdbMgmtMacAddr.setStatus("current")
_SwStaticFdbMgmtVlanName_Type = DisplayString
_SwStaticFdbMgmtVlanName_Object = MibTableColumn
swStaticFdbMgmtVlanName = _SwStaticFdbMgmtVlanName_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 70, 1, 1, 1, 3),
    _SwStaticFdbMgmtVlanName_Type()
)
swStaticFdbMgmtVlanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swStaticFdbMgmtVlanName.setStatus("current")


class _SwStaticFdbMgmtType_Type(Integer32):
    """Custom type swStaticFdbMgmtType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("permanent", 2),
          ("permanentdrop", 3),
          ("self", 1))
    )


_SwStaticFdbMgmtType_Type.__name__ = "Integer32"
_SwStaticFdbMgmtType_Object = MibTableColumn
swStaticFdbMgmtType = _SwStaticFdbMgmtType_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 70, 1, 1, 1, 4),
    _SwStaticFdbMgmtType_Type()
)
swStaticFdbMgmtType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swStaticFdbMgmtType.setStatus("current")
_SwStaticFdbMgmtPortNum_Type = Integer32
_SwStaticFdbMgmtPortNum_Object = MibTableColumn
swStaticFdbMgmtPortNum = _SwStaticFdbMgmtPortNum_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 70, 1, 1, 1, 5),
    _SwStaticFdbMgmtPortNum_Type()
)
swStaticFdbMgmtPortNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swStaticFdbMgmtPortNum.setStatus("current")
_SwStaticFdbMgmtRowStatus_Type = RowStatus
_SwStaticFdbMgmtRowStatus_Object = MibTableColumn
swStaticFdbMgmtRowStatus = _SwStaticFdbMgmtRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 70, 1, 1, 1, 6),
    _SwStaticFdbMgmtRowStatus_Type()
)
swStaticFdbMgmtRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swStaticFdbMgmtRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "STATICFDB-MIB",
    **{"swStaticFdbMIB": swStaticFdbMIB,
       "swStaticFdbMgmt": swStaticFdbMgmt,
       "swStaticFdbMgmtTable": swStaticFdbMgmtTable,
       "swStaticFdbMgmtEntry": swStaticFdbMgmtEntry,
       "swStaticFdbMgmtVlanID": swStaticFdbMgmtVlanID,
       "swStaticFdbMgmtMacAddr": swStaticFdbMgmtMacAddr,
       "swStaticFdbMgmtVlanName": swStaticFdbMgmtVlanName,
       "swStaticFdbMgmtType": swStaticFdbMgmtType,
       "swStaticFdbMgmtPortNum": swStaticFdbMgmtPortNum,
       "swStaticFdbMgmtRowStatus": swStaticFdbMgmtRowStatus}
)
