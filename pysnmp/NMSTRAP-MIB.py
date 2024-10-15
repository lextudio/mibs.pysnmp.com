# SNMP MIB module (NMSTRAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NMSTRAP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:28:09 2024
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

(ifDescr,
 ifIndex,
 ifType) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifDescr",
    "ifIndex",
    "ifType")

(adslCPULoad,
 adslConfigAddr,
 adslLineUser,
 adslMemLoad,
 adslProductID,
 adslPtInCRC,
 adslPtInDrop,
 adslPtInError,
 adslPtInPkts,
 adslPtInSpeed,
 adslPtOutDrop,
 adslPtOutError,
 adslPtOutPkts,
 adslPtOutSpeed,
 adslPtSpeed,
 adslPtStatus) = mibBuilder.importSymbols(
    "NMS-1705",
    "adslCPULoad",
    "adslConfigAddr",
    "adslLineUser",
    "adslMemLoad",
    "adslProductID",
    "adslPtInCRC",
    "adslPtInDrop",
    "adslPtInError",
    "adslPtInPkts",
    "adslPtInSpeed",
    "adslPtOutDrop",
    "adslPtOutError",
    "adslPtOutPkts",
    "adslPtOutSpeed",
    "adslPtSpeed",
    "adslPtStatus")

(nms,) = mibBuilder.importSymbols(
    "NMS-SMI",
    "nms")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(sysUpTime,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysUpTime")

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
 NotificationType,
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
    "NotificationType",
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


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects

adslConnection = NotificationType(
    (1, 3, 6, 1, 4, 1, 11606, 10, 0, 0)
)
adslConnection.setObjects(
      *(("NMS-1705", "adslLineUser"),
        ("NMS-1705", "adslProductID"),
        ("NMS-1705", "adslConfigAddr"))
)
if mibBuilder.loadTexts:
    adslConnection.setStatus(
        ""
    )

adslPeriod = NotificationType(
    (1, 3, 6, 1, 4, 1, 11606, 10, 0, 1)
)
adslPeriod.setObjects(
      *(("NMS-1705", "adslMemLoad"),
        ("NMS-1705", "adslCPULoad"),
        ("NMS-1705", "adslPtInCRC"),
        ("NMS-1705", "adslPtStatus"),
        ("NMS-1705", "adslPtSpeed"),
        ("NMS-1705", "adslPtOutPkts"),
        ("NMS-1705", "adslPtInPkts"),
        ("NMS-1705", "adslPtOutError"),
        ("NMS-1705", "adslPtInError"),
        ("NMS-1705", "adslPtOutSpeed"),
        ("NMS-1705", "adslPtInSpeed"),
        ("NMS-1705", "adslPtOutDrop"),
        ("NMS-1705", "adslPtInDrop"))
)
if mibBuilder.loadTexts:
    adslPeriod.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NMSTRAP-MIB",
    **{"adslConnection": adslConnection,
       "adslPeriod": adslPeriod}
)
