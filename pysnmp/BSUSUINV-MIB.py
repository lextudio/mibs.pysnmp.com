# SNMP MIB module (BSUSUINV-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BSUSUINV-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:49:47 2024
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

(aniBsuSuGroup,) = mibBuilder.importSymbols(
    "ANIROOT-MIB",
    "aniBsuSuGroup")

(aniBsuWirelessPort,) = mibBuilder.importSymbols(
    "BSUWIRELESSIF-MIB",
    "aniBsuWirelessPort")

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

aniBsuSuInventory = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4325, 3, 7, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AniBsuSuInvTable_Object = MibTable
aniBsuSuInvTable = _AniBsuSuInvTable_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 7, 1, 1)
)
if mibBuilder.loadTexts:
    aniBsuSuInvTable.setStatus("current")
_AniBsuSuInvEntry_Object = MibTableRow
aniBsuSuInvEntry = _AniBsuSuInvEntry_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 7, 1, 1, 1)
)
aniBsuSuInvEntry.setIndexNames(
    (0, "BSUWIRELESSIF-MIB", "aniBsuWirelessPort"),
    (0, "BSUSUINV-MIB", "aniBsuSuMacAddr"),
)
if mibBuilder.loadTexts:
    aniBsuSuInvEntry.setStatus("current")
_AniBsuSuMacAddr_Type = MacAddress
_AniBsuSuMacAddr_Object = MibTableColumn
aniBsuSuMacAddr = _AniBsuSuMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 7, 1, 1, 1, 1),
    _AniBsuSuMacAddr_Type()
)
aniBsuSuMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniBsuSuMacAddr.setStatus("current")
_AniBsuSuIpAddr_Type = IpAddress
_AniBsuSuIpAddr_Object = MibTableColumn
aniBsuSuIpAddr = _AniBsuSuIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 7, 1, 1, 1, 3),
    _AniBsuSuIpAddr_Type()
)
aniBsuSuIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniBsuSuIpAddr.setStatus("current")


class _AniBsuSuName_Type(DisplayString):
    """Custom type aniBsuSuName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AniBsuSuName_Type.__name__ = "DisplayString"
_AniBsuSuName_Object = MibTableColumn
aniBsuSuName = _AniBsuSuName_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 7, 1, 1, 1, 4),
    _AniBsuSuName_Type()
)
aniBsuSuName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniBsuSuName.setStatus("current")


class _AniBsuSuCustomerName_Type(DisplayString):
    """Custom type aniBsuSuCustomerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AniBsuSuCustomerName_Type.__name__ = "DisplayString"
_AniBsuSuCustomerName_Object = MibTableColumn
aniBsuSuCustomerName = _AniBsuSuCustomerName_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 7, 1, 1, 1, 5),
    _AniBsuSuCustomerName_Type()
)
aniBsuSuCustomerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniBsuSuCustomerName.setStatus("current")


class _AniBsuSuLinkStatus_Type(Integer32):
    """Custom type aniBsuSuLinkStatus based on Integer32"""
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
              15,
              255)
        )
    )
    namedValues = NamedValues(
        *(("config-file-req-rcvd", 8),
          ("config-file-req-sent", 9),
          ("delete", 255),
          ("dhcp-req-rcvd", 4),
          ("dhcp-rsp-sent", 5),
          ("initial", 1),
          ("lic-rsp-recd", 11),
          ("operational", 14),
          ("reg-ack-rcvd", 13),
          ("reg-req-rcvd", 10),
          ("reg-rsp-sent", 12),
          ("stand-by", 15),
          ("tod-req-rcvd", 6),
          ("tod-rsp-sent", 7),
          ("ulm-req-rcvd", 2),
          ("ulm-rsp-sent", 3))
    )


_AniBsuSuLinkStatus_Type.__name__ = "Integer32"
_AniBsuSuLinkStatus_Object = MibTableColumn
aniBsuSuLinkStatus = _AniBsuSuLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 7, 1, 1, 1, 6),
    _AniBsuSuLinkStatus_Type()
)
aniBsuSuLinkStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aniBsuSuLinkStatus.setStatus("current")
_AniBsuSuModelNumber_Type = DisplayString
_AniBsuSuModelNumber_Object = MibTableColumn
aniBsuSuModelNumber = _AniBsuSuModelNumber_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 7, 1, 1, 1, 7),
    _AniBsuSuModelNumber_Type()
)
aniBsuSuModelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniBsuSuModelNumber.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BSUSUINV-MIB",
    **{"aniBsuSuInventory": aniBsuSuInventory,
       "aniBsuSuInvTable": aniBsuSuInvTable,
       "aniBsuSuInvEntry": aniBsuSuInvEntry,
       "aniBsuSuMacAddr": aniBsuSuMacAddr,
       "aniBsuSuIpAddr": aniBsuSuIpAddr,
       "aniBsuSuName": aniBsuSuName,
       "aniBsuSuCustomerName": aniBsuSuCustomerName,
       "aniBsuSuLinkStatus": aniBsuSuLinkStatus,
       "aniBsuSuModelNumber": aniBsuSuModelNumber}
)
