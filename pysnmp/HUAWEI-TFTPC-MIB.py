# SNMP MIB module (HUAWEI-TFTPC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-TFTPC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:06:14 2024
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

(hwDatacomm,) = mibBuilder.importSymbols(
    "HUAWEI-MIB",
    "hwDatacomm")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

hwTftpc = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 197)
)
hwTftpc.setRevisions(
        ("2010-06-01 00:00",
         "2010-12-08 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwTftpClientInfo_ObjectIdentity = ObjectIdentity
hwTftpClientInfo = _HwTftpClientInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 197, 2)
)


class _HwTftpClientSourceAddress_Type(OctetString):
    """Custom type hwTftpClientSourceAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_HwTftpClientSourceAddress_Type.__name__ = "OctetString"
_HwTftpClientSourceAddress_Object = MibScalar
hwTftpClientSourceAddress = _HwTftpClientSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 197, 2, 1),
    _HwTftpClientSourceAddress_Type()
)
hwTftpClientSourceAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwTftpClientSourceAddress.setStatus("current")


class _HwTftpClientSourceInterfaceName_Type(OctetString):
    """Custom type hwTftpClientSourceInterfaceName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_HwTftpClientSourceInterfaceName_Type.__name__ = "OctetString"
_HwTftpClientSourceInterfaceName_Object = MibScalar
hwTftpClientSourceInterfaceName = _HwTftpClientSourceInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 197, 2, 2),
    _HwTftpClientSourceInterfaceName_Type()
)
hwTftpClientSourceInterfaceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwTftpClientSourceInterfaceName.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-TFTPC-MIB",
    **{"hwTftpc": hwTftpc,
       "hwTftpClientInfo": hwTftpClientInfo,
       "hwTftpClientSourceAddress": hwTftpClientSourceAddress,
       "hwTftpClientSourceInterfaceName": hwTftpClientSourceInterfaceName}
)
