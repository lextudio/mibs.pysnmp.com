# SNMP MIB module (DL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:29:29 2024
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
 ObjectName,
 NotificationType,
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
    "ObjectName",
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
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

_Asentria_ObjectIdentity = ObjectIdentity
asentria = _Asentria_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052)
)
_Dl_ObjectIdentity = ObjectIdentity
dl = _Dl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 3)
)
_ProductIds_ObjectIdentity = ObjectIdentity
productIds = _ProductIds_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 3, 3)
)
_SiteID_Type = DisplayString
_SiteID_Object = MibScalar
siteID = _SiteID_Object(
    (1, 3, 6, 1, 4, 1, 3052, 3, 3, 1),
    _SiteID_Type()
)
siteID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    siteID.setStatus("mandatory")
_StockTrapString_Type = DisplayString
_StockTrapString_Object = MibScalar
stockTrapString = _StockTrapString_Object(
    (1, 3, 6, 1, 4, 1, 3052, 3, 3, 3),
    _StockTrapString_Type()
)
stockTrapString.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    stockTrapString.setStatus("mandatory")
_TrapTypeString_Type = DisplayString
_TrapTypeString_Object = MibScalar
trapTypeString = _TrapTypeString_Object(
    (1, 3, 6, 1, 4, 1, 3052, 3, 3, 8),
    _TrapTypeString_Type()
)
trapTypeString.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trapTypeString.setStatus("mandatory")

# Managed Objects groups


# Notification objects

dlStockTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1)
)
dlStockTrap.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"))
)
if mibBuilder.loadTexts:
    dlStockTrap.setStatus(
        ""
    )

dlStockDbasePfullTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 501)
)
dlStockDbasePfullTrap.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlStockDbasePfullTrap.setStatus(
        ""
    )

dlStockDataAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 503)
)
dlStockDataAlarmTrap.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlStockDataAlarmTrap.setStatus(
        ""
    )

dlStockNoDataAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 505)
)
dlStockNoDataAlarmTrap.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlStockNoDataAlarmTrap.setStatus(
        ""
    )

dlStockSchedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 506)
)
dlStockSchedTrap.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlStockSchedTrap.setStatus(
        ""
    )

dlStockImmediateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 507)
)
dlStockImmediateTrap.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlStockImmediateTrap.setStatus(
        ""
    )

dlStockSocketLostTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 508)
)
dlStockSocketLostTrap.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlStockSocketLostTrap.setStatus(
        ""
    )

dlUserTrap1000 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1000)
)
dlUserTrap1000.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1000.setStatus(
        ""
    )

dlUserTrap1001 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1001)
)
dlUserTrap1001.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1001.setStatus(
        ""
    )

dlUserTrap1002 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1002)
)
dlUserTrap1002.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1002.setStatus(
        ""
    )

dlUserTrap1003 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1003)
)
dlUserTrap1003.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1003.setStatus(
        ""
    )

dlUserTrap1004 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1004)
)
dlUserTrap1004.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1004.setStatus(
        ""
    )

dlUserTrap1005 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1005)
)
dlUserTrap1005.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1005.setStatus(
        ""
    )

dlUserTrap1006 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1006)
)
dlUserTrap1006.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1006.setStatus(
        ""
    )

dlUserTrap1007 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1007)
)
dlUserTrap1007.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1007.setStatus(
        ""
    )

dlUserTrap1008 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1008)
)
dlUserTrap1008.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1008.setStatus(
        ""
    )

dlUserTrap1009 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1009)
)
dlUserTrap1009.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1009.setStatus(
        ""
    )

dlUserTrap1010 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1010)
)
dlUserTrap1010.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1010.setStatus(
        ""
    )

dlUserTrap1011 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1011)
)
dlUserTrap1011.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1011.setStatus(
        ""
    )

dlUserTrap1012 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1012)
)
dlUserTrap1012.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1012.setStatus(
        ""
    )

dlUserTrap1013 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1013)
)
dlUserTrap1013.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1013.setStatus(
        ""
    )

dlUserTrap1014 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1014)
)
dlUserTrap1014.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1014.setStatus(
        ""
    )

dlUserTrap1015 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1015)
)
dlUserTrap1015.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1015.setStatus(
        ""
    )

dlUserTrap1016 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1016)
)
dlUserTrap1016.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1016.setStatus(
        ""
    )

dlUserTrap1017 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1017)
)
dlUserTrap1017.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1017.setStatus(
        ""
    )

dlUserTrap1018 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1018)
)
dlUserTrap1018.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1018.setStatus(
        ""
    )

dlUserTrap1019 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1019)
)
dlUserTrap1019.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1019.setStatus(
        ""
    )

dlUserTrap1020 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1020)
)
dlUserTrap1020.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1020.setStatus(
        ""
    )

dlUserTrap1021 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1021)
)
dlUserTrap1021.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1021.setStatus(
        ""
    )

dlUserTrap1022 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1022)
)
dlUserTrap1022.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1022.setStatus(
        ""
    )

dlUserTrap1023 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1023)
)
dlUserTrap1023.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1023.setStatus(
        ""
    )

dlUserTrap1024 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1024)
)
dlUserTrap1024.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1024.setStatus(
        ""
    )

dlUserTrap1025 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1025)
)
dlUserTrap1025.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1025.setStatus(
        ""
    )

dlUserTrap1026 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1026)
)
dlUserTrap1026.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1026.setStatus(
        ""
    )

dlUserTrap1027 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1027)
)
dlUserTrap1027.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1027.setStatus(
        ""
    )

dlUserTrap1028 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1028)
)
dlUserTrap1028.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1028.setStatus(
        ""
    )

dlUserTrap1029 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1029)
)
dlUserTrap1029.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1029.setStatus(
        ""
    )

dlUserTrap1030 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1030)
)
dlUserTrap1030.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1030.setStatus(
        ""
    )

dlUserTrap1031 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1031)
)
dlUserTrap1031.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1031.setStatus(
        ""
    )

dlUserTrap1032 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1032)
)
dlUserTrap1032.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1032.setStatus(
        ""
    )

dlUserTrap1033 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1033)
)
dlUserTrap1033.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1033.setStatus(
        ""
    )

dlUserTrap1034 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1034)
)
dlUserTrap1034.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1034.setStatus(
        ""
    )

dlUserTrap1035 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1035)
)
dlUserTrap1035.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1035.setStatus(
        ""
    )

dlUserTrap1036 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1036)
)
dlUserTrap1036.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1036.setStatus(
        ""
    )

dlUserTrap1037 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1037)
)
dlUserTrap1037.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1037.setStatus(
        ""
    )

dlUserTrap1038 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1038)
)
dlUserTrap1038.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1038.setStatus(
        ""
    )

dlUserTrap1039 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1039)
)
dlUserTrap1039.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1039.setStatus(
        ""
    )

dlUserTrap1040 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1040)
)
dlUserTrap1040.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1040.setStatus(
        ""
    )

dlUserTrap1041 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1041)
)
dlUserTrap1041.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1041.setStatus(
        ""
    )

dlUserTrap1042 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1042)
)
dlUserTrap1042.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1042.setStatus(
        ""
    )

dlUserTrap1043 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1043)
)
dlUserTrap1043.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1043.setStatus(
        ""
    )

dlUserTrap1044 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1044)
)
dlUserTrap1044.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1044.setStatus(
        ""
    )

dlUserTrap1045 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1045)
)
dlUserTrap1045.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1045.setStatus(
        ""
    )

dlUserTrap1046 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1046)
)
dlUserTrap1046.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1046.setStatus(
        ""
    )

dlUserTrap1047 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1047)
)
dlUserTrap1047.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1047.setStatus(
        ""
    )

dlUserTrap1048 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1048)
)
dlUserTrap1048.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1048.setStatus(
        ""
    )

dlUserTrap1049 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1049)
)
dlUserTrap1049.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1049.setStatus(
        ""
    )

dlUserTrap1050 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1050)
)
dlUserTrap1050.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1050.setStatus(
        ""
    )

dlUserTrap1051 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1051)
)
dlUserTrap1051.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1051.setStatus(
        ""
    )

dlUserTrap1052 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1052)
)
dlUserTrap1052.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1052.setStatus(
        ""
    )

dlUserTrap1053 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1053)
)
dlUserTrap1053.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1053.setStatus(
        ""
    )

dlUserTrap1054 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1054)
)
dlUserTrap1054.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1054.setStatus(
        ""
    )

dlUserTrap1055 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1055)
)
dlUserTrap1055.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1055.setStatus(
        ""
    )

dlUserTrap1056 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1056)
)
dlUserTrap1056.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1056.setStatus(
        ""
    )

dlUserTrap1057 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1057)
)
dlUserTrap1057.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1057.setStatus(
        ""
    )

dlUserTrap1058 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1058)
)
dlUserTrap1058.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1058.setStatus(
        ""
    )

dlUserTrap1059 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1059)
)
dlUserTrap1059.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1059.setStatus(
        ""
    )

dlUserTrap1060 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1060)
)
dlUserTrap1060.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1060.setStatus(
        ""
    )

dlUserTrap1061 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1061)
)
dlUserTrap1061.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1061.setStatus(
        ""
    )

dlUserTrap1062 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1062)
)
dlUserTrap1062.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1062.setStatus(
        ""
    )

dlUserTrap1063 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1063)
)
dlUserTrap1063.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1063.setStatus(
        ""
    )

dlUserTrap1064 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1064)
)
dlUserTrap1064.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1064.setStatus(
        ""
    )

dlUserTrap1065 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1065)
)
dlUserTrap1065.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1065.setStatus(
        ""
    )

dlUserTrap1066 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1066)
)
dlUserTrap1066.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1066.setStatus(
        ""
    )

dlUserTrap1067 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1067)
)
dlUserTrap1067.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1067.setStatus(
        ""
    )

dlUserTrap1068 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1068)
)
dlUserTrap1068.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1068.setStatus(
        ""
    )

dlUserTrap1069 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1069)
)
dlUserTrap1069.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1069.setStatus(
        ""
    )

dlUserTrap1070 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1070)
)
dlUserTrap1070.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1070.setStatus(
        ""
    )

dlUserTrap1071 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1071)
)
dlUserTrap1071.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1071.setStatus(
        ""
    )

dlUserTrap1072 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1072)
)
dlUserTrap1072.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1072.setStatus(
        ""
    )

dlUserTrap1073 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1073)
)
dlUserTrap1073.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1073.setStatus(
        ""
    )

dlUserTrap1074 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1074)
)
dlUserTrap1074.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1074.setStatus(
        ""
    )

dlUserTrap1075 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1075)
)
dlUserTrap1075.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1075.setStatus(
        ""
    )

dlUserTrap1076 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1076)
)
dlUserTrap1076.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1076.setStatus(
        ""
    )

dlUserTrap1077 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1077)
)
dlUserTrap1077.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1077.setStatus(
        ""
    )

dlUserTrap1078 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1078)
)
dlUserTrap1078.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1078.setStatus(
        ""
    )

dlUserTrap1079 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1079)
)
dlUserTrap1079.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1079.setStatus(
        ""
    )

dlUserTrap1080 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1080)
)
dlUserTrap1080.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1080.setStatus(
        ""
    )

dlUserTrap1081 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1081)
)
dlUserTrap1081.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1081.setStatus(
        ""
    )

dlUserTrap1082 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1082)
)
dlUserTrap1082.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1082.setStatus(
        ""
    )

dlUserTrap1083 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1083)
)
dlUserTrap1083.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1083.setStatus(
        ""
    )

dlUserTrap1084 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1084)
)
dlUserTrap1084.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1084.setStatus(
        ""
    )

dlUserTrap1085 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1085)
)
dlUserTrap1085.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1085.setStatus(
        ""
    )

dlUserTrap1086 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1086)
)
dlUserTrap1086.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1086.setStatus(
        ""
    )

dlUserTrap1087 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1087)
)
dlUserTrap1087.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1087.setStatus(
        ""
    )

dlUserTrap1088 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1088)
)
dlUserTrap1088.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1088.setStatus(
        ""
    )

dlUserTrap1089 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1089)
)
dlUserTrap1089.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1089.setStatus(
        ""
    )

dlUserTrap1090 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1090)
)
dlUserTrap1090.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1090.setStatus(
        ""
    )

dlUserTrap1091 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1091)
)
dlUserTrap1091.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1091.setStatus(
        ""
    )

dlUserTrap1092 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1092)
)
dlUserTrap1092.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1092.setStatus(
        ""
    )

dlUserTrap1093 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1093)
)
dlUserTrap1093.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1093.setStatus(
        ""
    )

dlUserTrap1094 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1094)
)
dlUserTrap1094.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1094.setStatus(
        ""
    )

dlUserTrap1095 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1095)
)
dlUserTrap1095.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1095.setStatus(
        ""
    )

dlUserTrap1096 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1096)
)
dlUserTrap1096.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1096.setStatus(
        ""
    )

dlUserTrap1097 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1097)
)
dlUserTrap1097.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1097.setStatus(
        ""
    )

dlUserTrap1098 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1098)
)
dlUserTrap1098.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1098.setStatus(
        ""
    )

dlUserTrap1099 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1099)
)
dlUserTrap1099.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1099.setStatus(
        ""
    )

dlUserTrap1100 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1100)
)
dlUserTrap1100.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1100.setStatus(
        ""
    )

dlUserTrap1101 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1101)
)
dlUserTrap1101.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1101.setStatus(
        ""
    )

dlUserTrap1102 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1102)
)
dlUserTrap1102.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1102.setStatus(
        ""
    )

dlUserTrap1103 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1103)
)
dlUserTrap1103.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1103.setStatus(
        ""
    )

dlUserTrap1104 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1104)
)
dlUserTrap1104.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1104.setStatus(
        ""
    )

dlUserTrap1105 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1105)
)
dlUserTrap1105.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1105.setStatus(
        ""
    )

dlUserTrap1106 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1106)
)
dlUserTrap1106.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1106.setStatus(
        ""
    )

dlUserTrap1107 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1107)
)
dlUserTrap1107.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1107.setStatus(
        ""
    )

dlUserTrap1108 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1108)
)
dlUserTrap1108.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1108.setStatus(
        ""
    )

dlUserTrap1109 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1109)
)
dlUserTrap1109.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1109.setStatus(
        ""
    )

dlUserTrap1110 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1110)
)
dlUserTrap1110.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1110.setStatus(
        ""
    )

dlUserTrap1111 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1111)
)
dlUserTrap1111.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1111.setStatus(
        ""
    )

dlUserTrap1112 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1112)
)
dlUserTrap1112.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1112.setStatus(
        ""
    )

dlUserTrap1113 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1113)
)
dlUserTrap1113.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1113.setStatus(
        ""
    )

dlUserTrap1114 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1114)
)
dlUserTrap1114.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1114.setStatus(
        ""
    )

dlUserTrap1115 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1115)
)
dlUserTrap1115.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1115.setStatus(
        ""
    )

dlUserTrap1116 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1116)
)
dlUserTrap1116.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1116.setStatus(
        ""
    )

dlUserTrap1117 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1117)
)
dlUserTrap1117.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1117.setStatus(
        ""
    )

dlUserTrap1118 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1118)
)
dlUserTrap1118.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1118.setStatus(
        ""
    )

dlUserTrap1119 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1119)
)
dlUserTrap1119.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1119.setStatus(
        ""
    )

dlUserTrap1120 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1120)
)
dlUserTrap1120.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1120.setStatus(
        ""
    )

dlUserTrap1121 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1121)
)
dlUserTrap1121.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1121.setStatus(
        ""
    )

dlUserTrap1122 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1122)
)
dlUserTrap1122.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1122.setStatus(
        ""
    )

dlUserTrap1123 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1123)
)
dlUserTrap1123.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1123.setStatus(
        ""
    )

dlUserTrap1124 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1124)
)
dlUserTrap1124.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1124.setStatus(
        ""
    )

dlUserTrap1125 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1125)
)
dlUserTrap1125.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1125.setStatus(
        ""
    )

dlUserTrap1126 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1126)
)
dlUserTrap1126.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1126.setStatus(
        ""
    )

dlUserTrap1127 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1127)
)
dlUserTrap1127.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1127.setStatus(
        ""
    )

dlUserTrap1128 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1128)
)
dlUserTrap1128.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1128.setStatus(
        ""
    )

dlUserTrap1129 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1129)
)
dlUserTrap1129.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1129.setStatus(
        ""
    )

dlUserTrap1130 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1130)
)
dlUserTrap1130.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1130.setStatus(
        ""
    )

dlUserTrap1131 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1131)
)
dlUserTrap1131.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1131.setStatus(
        ""
    )

dlUserTrap1132 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1132)
)
dlUserTrap1132.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1132.setStatus(
        ""
    )

dlUserTrap1133 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1133)
)
dlUserTrap1133.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1133.setStatus(
        ""
    )

dlUserTrap1134 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1134)
)
dlUserTrap1134.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1134.setStatus(
        ""
    )

dlUserTrap1135 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1135)
)
dlUserTrap1135.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1135.setStatus(
        ""
    )

dlUserTrap1136 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1136)
)
dlUserTrap1136.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1136.setStatus(
        ""
    )

dlUserTrap1137 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1137)
)
dlUserTrap1137.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1137.setStatus(
        ""
    )

dlUserTrap1138 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1138)
)
dlUserTrap1138.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1138.setStatus(
        ""
    )

dlUserTrap1139 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1139)
)
dlUserTrap1139.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1139.setStatus(
        ""
    )

dlUserTrap1140 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1140)
)
dlUserTrap1140.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1140.setStatus(
        ""
    )

dlUserTrap1141 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1141)
)
dlUserTrap1141.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1141.setStatus(
        ""
    )

dlUserTrap1142 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1142)
)
dlUserTrap1142.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1142.setStatus(
        ""
    )

dlUserTrap1143 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1143)
)
dlUserTrap1143.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1143.setStatus(
        ""
    )

dlUserTrap1144 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1144)
)
dlUserTrap1144.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1144.setStatus(
        ""
    )

dlUserTrap1145 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1145)
)
dlUserTrap1145.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1145.setStatus(
        ""
    )

dlUserTrap1146 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1146)
)
dlUserTrap1146.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1146.setStatus(
        ""
    )

dlUserTrap1147 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1147)
)
dlUserTrap1147.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1147.setStatus(
        ""
    )

dlUserTrap1148 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1148)
)
dlUserTrap1148.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1148.setStatus(
        ""
    )

dlUserTrap1149 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1149)
)
dlUserTrap1149.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1149.setStatus(
        ""
    )

dlUserTrap1150 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1150)
)
dlUserTrap1150.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1150.setStatus(
        ""
    )

dlUserTrap1151 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1151)
)
dlUserTrap1151.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1151.setStatus(
        ""
    )

dlUserTrap1152 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1152)
)
dlUserTrap1152.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1152.setStatus(
        ""
    )

dlUserTrap1153 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1153)
)
dlUserTrap1153.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1153.setStatus(
        ""
    )

dlUserTrap1154 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1154)
)
dlUserTrap1154.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1154.setStatus(
        ""
    )

dlUserTrap1155 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1155)
)
dlUserTrap1155.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1155.setStatus(
        ""
    )

dlUserTrap1156 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1156)
)
dlUserTrap1156.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1156.setStatus(
        ""
    )

dlUserTrap1157 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1157)
)
dlUserTrap1157.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1157.setStatus(
        ""
    )

dlUserTrap1158 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1158)
)
dlUserTrap1158.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1158.setStatus(
        ""
    )

dlUserTrap1159 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1159)
)
dlUserTrap1159.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1159.setStatus(
        ""
    )

dlUserTrap1160 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1160)
)
dlUserTrap1160.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1160.setStatus(
        ""
    )

dlUserTrap1161 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1161)
)
dlUserTrap1161.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1161.setStatus(
        ""
    )

dlUserTrap1162 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1162)
)
dlUserTrap1162.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1162.setStatus(
        ""
    )

dlUserTrap1163 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1163)
)
dlUserTrap1163.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1163.setStatus(
        ""
    )

dlUserTrap1164 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1164)
)
dlUserTrap1164.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1164.setStatus(
        ""
    )

dlUserTrap1165 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1165)
)
dlUserTrap1165.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1165.setStatus(
        ""
    )

dlUserTrap1166 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1166)
)
dlUserTrap1166.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1166.setStatus(
        ""
    )

dlUserTrap1167 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1167)
)
dlUserTrap1167.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1167.setStatus(
        ""
    )

dlUserTrap1168 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1168)
)
dlUserTrap1168.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1168.setStatus(
        ""
    )

dlUserTrap1169 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1169)
)
dlUserTrap1169.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1169.setStatus(
        ""
    )

dlUserTrap1170 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1170)
)
dlUserTrap1170.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1170.setStatus(
        ""
    )

dlUserTrap1171 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1171)
)
dlUserTrap1171.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1171.setStatus(
        ""
    )

dlUserTrap1172 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1172)
)
dlUserTrap1172.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1172.setStatus(
        ""
    )

dlUserTrap1173 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1173)
)
dlUserTrap1173.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1173.setStatus(
        ""
    )

dlUserTrap1174 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1174)
)
dlUserTrap1174.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1174.setStatus(
        ""
    )

dlUserTrap1175 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1175)
)
dlUserTrap1175.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1175.setStatus(
        ""
    )

dlUserTrap1176 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1176)
)
dlUserTrap1176.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1176.setStatus(
        ""
    )

dlUserTrap1177 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1177)
)
dlUserTrap1177.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1177.setStatus(
        ""
    )

dlUserTrap1178 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1178)
)
dlUserTrap1178.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1178.setStatus(
        ""
    )

dlUserTrap1179 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1179)
)
dlUserTrap1179.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1179.setStatus(
        ""
    )

dlUserTrap1180 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1180)
)
dlUserTrap1180.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1180.setStatus(
        ""
    )

dlUserTrap1181 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1181)
)
dlUserTrap1181.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1181.setStatus(
        ""
    )

dlUserTrap1182 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1182)
)
dlUserTrap1182.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1182.setStatus(
        ""
    )

dlUserTrap1183 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1183)
)
dlUserTrap1183.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1183.setStatus(
        ""
    )

dlUserTrap1184 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1184)
)
dlUserTrap1184.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1184.setStatus(
        ""
    )

dlUserTrap1185 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1185)
)
dlUserTrap1185.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1185.setStatus(
        ""
    )

dlUserTrap1186 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1186)
)
dlUserTrap1186.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1186.setStatus(
        ""
    )

dlUserTrap1187 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1187)
)
dlUserTrap1187.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1187.setStatus(
        ""
    )

dlUserTrap1188 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1188)
)
dlUserTrap1188.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1188.setStatus(
        ""
    )

dlUserTrap1189 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1189)
)
dlUserTrap1189.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1189.setStatus(
        ""
    )

dlUserTrap1190 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1190)
)
dlUserTrap1190.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1190.setStatus(
        ""
    )

dlUserTrap1191 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1191)
)
dlUserTrap1191.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1191.setStatus(
        ""
    )

dlUserTrap1192 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1192)
)
dlUserTrap1192.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1192.setStatus(
        ""
    )

dlUserTrap1193 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1193)
)
dlUserTrap1193.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1193.setStatus(
        ""
    )

dlUserTrap1194 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1194)
)
dlUserTrap1194.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1194.setStatus(
        ""
    )

dlUserTrap1195 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1195)
)
dlUserTrap1195.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1195.setStatus(
        ""
    )

dlUserTrap1196 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1196)
)
dlUserTrap1196.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1196.setStatus(
        ""
    )

dlUserTrap1197 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1197)
)
dlUserTrap1197.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1197.setStatus(
        ""
    )

dlUserTrap1198 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1198)
)
dlUserTrap1198.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1198.setStatus(
        ""
    )

dlUserTrap1199 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 3, 0, 1199)
)
dlUserTrap1199.setObjects(
      *(("DL-MIB", "siteID"),
        ("DL-MIB", "stockTrapString"),
        ("DL-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dlUserTrap1199.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DL-MIB",
    **{"asentria": asentria,
       "dl": dl,
       "dlStockTrap": dlStockTrap,
       "dlStockDbasePfullTrap": dlStockDbasePfullTrap,
       "dlStockDataAlarmTrap": dlStockDataAlarmTrap,
       "dlStockNoDataAlarmTrap": dlStockNoDataAlarmTrap,
       "dlStockSchedTrap": dlStockSchedTrap,
       "dlStockImmediateTrap": dlStockImmediateTrap,
       "dlStockSocketLostTrap": dlStockSocketLostTrap,
       "dlUserTrap1000": dlUserTrap1000,
       "dlUserTrap1001": dlUserTrap1001,
       "dlUserTrap1002": dlUserTrap1002,
       "dlUserTrap1003": dlUserTrap1003,
       "dlUserTrap1004": dlUserTrap1004,
       "dlUserTrap1005": dlUserTrap1005,
       "dlUserTrap1006": dlUserTrap1006,
       "dlUserTrap1007": dlUserTrap1007,
       "dlUserTrap1008": dlUserTrap1008,
       "dlUserTrap1009": dlUserTrap1009,
       "dlUserTrap1010": dlUserTrap1010,
       "dlUserTrap1011": dlUserTrap1011,
       "dlUserTrap1012": dlUserTrap1012,
       "dlUserTrap1013": dlUserTrap1013,
       "dlUserTrap1014": dlUserTrap1014,
       "dlUserTrap1015": dlUserTrap1015,
       "dlUserTrap1016": dlUserTrap1016,
       "dlUserTrap1017": dlUserTrap1017,
       "dlUserTrap1018": dlUserTrap1018,
       "dlUserTrap1019": dlUserTrap1019,
       "dlUserTrap1020": dlUserTrap1020,
       "dlUserTrap1021": dlUserTrap1021,
       "dlUserTrap1022": dlUserTrap1022,
       "dlUserTrap1023": dlUserTrap1023,
       "dlUserTrap1024": dlUserTrap1024,
       "dlUserTrap1025": dlUserTrap1025,
       "dlUserTrap1026": dlUserTrap1026,
       "dlUserTrap1027": dlUserTrap1027,
       "dlUserTrap1028": dlUserTrap1028,
       "dlUserTrap1029": dlUserTrap1029,
       "dlUserTrap1030": dlUserTrap1030,
       "dlUserTrap1031": dlUserTrap1031,
       "dlUserTrap1032": dlUserTrap1032,
       "dlUserTrap1033": dlUserTrap1033,
       "dlUserTrap1034": dlUserTrap1034,
       "dlUserTrap1035": dlUserTrap1035,
       "dlUserTrap1036": dlUserTrap1036,
       "dlUserTrap1037": dlUserTrap1037,
       "dlUserTrap1038": dlUserTrap1038,
       "dlUserTrap1039": dlUserTrap1039,
       "dlUserTrap1040": dlUserTrap1040,
       "dlUserTrap1041": dlUserTrap1041,
       "dlUserTrap1042": dlUserTrap1042,
       "dlUserTrap1043": dlUserTrap1043,
       "dlUserTrap1044": dlUserTrap1044,
       "dlUserTrap1045": dlUserTrap1045,
       "dlUserTrap1046": dlUserTrap1046,
       "dlUserTrap1047": dlUserTrap1047,
       "dlUserTrap1048": dlUserTrap1048,
       "dlUserTrap1049": dlUserTrap1049,
       "dlUserTrap1050": dlUserTrap1050,
       "dlUserTrap1051": dlUserTrap1051,
       "dlUserTrap1052": dlUserTrap1052,
       "dlUserTrap1053": dlUserTrap1053,
       "dlUserTrap1054": dlUserTrap1054,
       "dlUserTrap1055": dlUserTrap1055,
       "dlUserTrap1056": dlUserTrap1056,
       "dlUserTrap1057": dlUserTrap1057,
       "dlUserTrap1058": dlUserTrap1058,
       "dlUserTrap1059": dlUserTrap1059,
       "dlUserTrap1060": dlUserTrap1060,
       "dlUserTrap1061": dlUserTrap1061,
       "dlUserTrap1062": dlUserTrap1062,
       "dlUserTrap1063": dlUserTrap1063,
       "dlUserTrap1064": dlUserTrap1064,
       "dlUserTrap1065": dlUserTrap1065,
       "dlUserTrap1066": dlUserTrap1066,
       "dlUserTrap1067": dlUserTrap1067,
       "dlUserTrap1068": dlUserTrap1068,
       "dlUserTrap1069": dlUserTrap1069,
       "dlUserTrap1070": dlUserTrap1070,
       "dlUserTrap1071": dlUserTrap1071,
       "dlUserTrap1072": dlUserTrap1072,
       "dlUserTrap1073": dlUserTrap1073,
       "dlUserTrap1074": dlUserTrap1074,
       "dlUserTrap1075": dlUserTrap1075,
       "dlUserTrap1076": dlUserTrap1076,
       "dlUserTrap1077": dlUserTrap1077,
       "dlUserTrap1078": dlUserTrap1078,
       "dlUserTrap1079": dlUserTrap1079,
       "dlUserTrap1080": dlUserTrap1080,
       "dlUserTrap1081": dlUserTrap1081,
       "dlUserTrap1082": dlUserTrap1082,
       "dlUserTrap1083": dlUserTrap1083,
       "dlUserTrap1084": dlUserTrap1084,
       "dlUserTrap1085": dlUserTrap1085,
       "dlUserTrap1086": dlUserTrap1086,
       "dlUserTrap1087": dlUserTrap1087,
       "dlUserTrap1088": dlUserTrap1088,
       "dlUserTrap1089": dlUserTrap1089,
       "dlUserTrap1090": dlUserTrap1090,
       "dlUserTrap1091": dlUserTrap1091,
       "dlUserTrap1092": dlUserTrap1092,
       "dlUserTrap1093": dlUserTrap1093,
       "dlUserTrap1094": dlUserTrap1094,
       "dlUserTrap1095": dlUserTrap1095,
       "dlUserTrap1096": dlUserTrap1096,
       "dlUserTrap1097": dlUserTrap1097,
       "dlUserTrap1098": dlUserTrap1098,
       "dlUserTrap1099": dlUserTrap1099,
       "dlUserTrap1100": dlUserTrap1100,
       "dlUserTrap1101": dlUserTrap1101,
       "dlUserTrap1102": dlUserTrap1102,
       "dlUserTrap1103": dlUserTrap1103,
       "dlUserTrap1104": dlUserTrap1104,
       "dlUserTrap1105": dlUserTrap1105,
       "dlUserTrap1106": dlUserTrap1106,
       "dlUserTrap1107": dlUserTrap1107,
       "dlUserTrap1108": dlUserTrap1108,
       "dlUserTrap1109": dlUserTrap1109,
       "dlUserTrap1110": dlUserTrap1110,
       "dlUserTrap1111": dlUserTrap1111,
       "dlUserTrap1112": dlUserTrap1112,
       "dlUserTrap1113": dlUserTrap1113,
       "dlUserTrap1114": dlUserTrap1114,
       "dlUserTrap1115": dlUserTrap1115,
       "dlUserTrap1116": dlUserTrap1116,
       "dlUserTrap1117": dlUserTrap1117,
       "dlUserTrap1118": dlUserTrap1118,
       "dlUserTrap1119": dlUserTrap1119,
       "dlUserTrap1120": dlUserTrap1120,
       "dlUserTrap1121": dlUserTrap1121,
       "dlUserTrap1122": dlUserTrap1122,
       "dlUserTrap1123": dlUserTrap1123,
       "dlUserTrap1124": dlUserTrap1124,
       "dlUserTrap1125": dlUserTrap1125,
       "dlUserTrap1126": dlUserTrap1126,
       "dlUserTrap1127": dlUserTrap1127,
       "dlUserTrap1128": dlUserTrap1128,
       "dlUserTrap1129": dlUserTrap1129,
       "dlUserTrap1130": dlUserTrap1130,
       "dlUserTrap1131": dlUserTrap1131,
       "dlUserTrap1132": dlUserTrap1132,
       "dlUserTrap1133": dlUserTrap1133,
       "dlUserTrap1134": dlUserTrap1134,
       "dlUserTrap1135": dlUserTrap1135,
       "dlUserTrap1136": dlUserTrap1136,
       "dlUserTrap1137": dlUserTrap1137,
       "dlUserTrap1138": dlUserTrap1138,
       "dlUserTrap1139": dlUserTrap1139,
       "dlUserTrap1140": dlUserTrap1140,
       "dlUserTrap1141": dlUserTrap1141,
       "dlUserTrap1142": dlUserTrap1142,
       "dlUserTrap1143": dlUserTrap1143,
       "dlUserTrap1144": dlUserTrap1144,
       "dlUserTrap1145": dlUserTrap1145,
       "dlUserTrap1146": dlUserTrap1146,
       "dlUserTrap1147": dlUserTrap1147,
       "dlUserTrap1148": dlUserTrap1148,
       "dlUserTrap1149": dlUserTrap1149,
       "dlUserTrap1150": dlUserTrap1150,
       "dlUserTrap1151": dlUserTrap1151,
       "dlUserTrap1152": dlUserTrap1152,
       "dlUserTrap1153": dlUserTrap1153,
       "dlUserTrap1154": dlUserTrap1154,
       "dlUserTrap1155": dlUserTrap1155,
       "dlUserTrap1156": dlUserTrap1156,
       "dlUserTrap1157": dlUserTrap1157,
       "dlUserTrap1158": dlUserTrap1158,
       "dlUserTrap1159": dlUserTrap1159,
       "dlUserTrap1160": dlUserTrap1160,
       "dlUserTrap1161": dlUserTrap1161,
       "dlUserTrap1162": dlUserTrap1162,
       "dlUserTrap1163": dlUserTrap1163,
       "dlUserTrap1164": dlUserTrap1164,
       "dlUserTrap1165": dlUserTrap1165,
       "dlUserTrap1166": dlUserTrap1166,
       "dlUserTrap1167": dlUserTrap1167,
       "dlUserTrap1168": dlUserTrap1168,
       "dlUserTrap1169": dlUserTrap1169,
       "dlUserTrap1170": dlUserTrap1170,
       "dlUserTrap1171": dlUserTrap1171,
       "dlUserTrap1172": dlUserTrap1172,
       "dlUserTrap1173": dlUserTrap1173,
       "dlUserTrap1174": dlUserTrap1174,
       "dlUserTrap1175": dlUserTrap1175,
       "dlUserTrap1176": dlUserTrap1176,
       "dlUserTrap1177": dlUserTrap1177,
       "dlUserTrap1178": dlUserTrap1178,
       "dlUserTrap1179": dlUserTrap1179,
       "dlUserTrap1180": dlUserTrap1180,
       "dlUserTrap1181": dlUserTrap1181,
       "dlUserTrap1182": dlUserTrap1182,
       "dlUserTrap1183": dlUserTrap1183,
       "dlUserTrap1184": dlUserTrap1184,
       "dlUserTrap1185": dlUserTrap1185,
       "dlUserTrap1186": dlUserTrap1186,
       "dlUserTrap1187": dlUserTrap1187,
       "dlUserTrap1188": dlUserTrap1188,
       "dlUserTrap1189": dlUserTrap1189,
       "dlUserTrap1190": dlUserTrap1190,
       "dlUserTrap1191": dlUserTrap1191,
       "dlUserTrap1192": dlUserTrap1192,
       "dlUserTrap1193": dlUserTrap1193,
       "dlUserTrap1194": dlUserTrap1194,
       "dlUserTrap1195": dlUserTrap1195,
       "dlUserTrap1196": dlUserTrap1196,
       "dlUserTrap1197": dlUserTrap1197,
       "dlUserTrap1198": dlUserTrap1198,
       "dlUserTrap1199": dlUserTrap1199,
       "productIds": productIds,
       "siteID": siteID,
       "stockTrapString": stockTrapString,
       "trapTypeString": trapTypeString}
)
