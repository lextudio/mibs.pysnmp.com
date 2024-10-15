# SNMP MIB module (COLUBRIS-USAGE-INFORMATION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/COLUBRIS-USAGE-INFORMATION-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:16:28 2024
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

(colubrisMgmtV2,) = mibBuilder.importSymbols(
    "COLUBRIS-SMI",
    "colubrisMgmtV2")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

colubrisUsageInformationMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 21)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ColubrisUsageInformationMIBObjects_ObjectIdentity = ObjectIdentity
colubrisUsageInformationMIBObjects = _ColubrisUsageInformationMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 21, 1)
)
_CoUsageInformationGroup_ObjectIdentity = ObjectIdentity
coUsageInformationGroup = _CoUsageInformationGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 21, 1, 1)
)
_CoUsInfoUpTime_Type = TimeTicks
_CoUsInfoUpTime_Object = MibScalar
coUsInfoUpTime = _CoUsInfoUpTime_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 21, 1, 1, 1),
    _CoUsInfoUpTime_Type()
)
coUsInfoUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coUsInfoUpTime.setStatus("current")
_CoUsInfoLoadAverage1Min_Type = Unsigned32
_CoUsInfoLoadAverage1Min_Object = MibScalar
coUsInfoLoadAverage1Min = _CoUsInfoLoadAverage1Min_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 21, 1, 1, 2),
    _CoUsInfoLoadAverage1Min_Type()
)
coUsInfoLoadAverage1Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coUsInfoLoadAverage1Min.setStatus("current")
_CoUsInfoLoadAverage5Min_Type = Unsigned32
_CoUsInfoLoadAverage5Min_Object = MibScalar
coUsInfoLoadAverage5Min = _CoUsInfoLoadAverage5Min_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 21, 1, 1, 3),
    _CoUsInfoLoadAverage5Min_Type()
)
coUsInfoLoadAverage5Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coUsInfoLoadAverage5Min.setStatus("current")
_CoUsInfoLoadAverage15Min_Type = Unsigned32
_CoUsInfoLoadAverage15Min_Object = MibScalar
coUsInfoLoadAverage15Min = _CoUsInfoLoadAverage15Min_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 21, 1, 1, 4),
    _CoUsInfoLoadAverage15Min_Type()
)
coUsInfoLoadAverage15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coUsInfoLoadAverage15Min.setStatus("current")
_CoUsInfoCpuUseNow_Type = Unsigned32
_CoUsInfoCpuUseNow_Object = MibScalar
coUsInfoCpuUseNow = _CoUsInfoCpuUseNow_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 21, 1, 1, 5),
    _CoUsInfoCpuUseNow_Type()
)
coUsInfoCpuUseNow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coUsInfoCpuUseNow.setStatus("current")
if mibBuilder.loadTexts:
    coUsInfoCpuUseNow.setUnits("%")
_CoUsInfoCpuUse5Sec_Type = Unsigned32
_CoUsInfoCpuUse5Sec_Object = MibScalar
coUsInfoCpuUse5Sec = _CoUsInfoCpuUse5Sec_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 21, 1, 1, 6),
    _CoUsInfoCpuUse5Sec_Type()
)
coUsInfoCpuUse5Sec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coUsInfoCpuUse5Sec.setStatus("current")
if mibBuilder.loadTexts:
    coUsInfoCpuUse5Sec.setUnits("%")
_CoUsInfoCpuUse10Sec_Type = Unsigned32
_CoUsInfoCpuUse10Sec_Object = MibScalar
coUsInfoCpuUse10Sec = _CoUsInfoCpuUse10Sec_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 21, 1, 1, 7),
    _CoUsInfoCpuUse10Sec_Type()
)
coUsInfoCpuUse10Sec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coUsInfoCpuUse10Sec.setStatus("current")
if mibBuilder.loadTexts:
    coUsInfoCpuUse10Sec.setUnits("%")
_CoUsInfoCpuUse20Sec_Type = Unsigned32
_CoUsInfoCpuUse20Sec_Object = MibScalar
coUsInfoCpuUse20Sec = _CoUsInfoCpuUse20Sec_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 21, 1, 1, 8),
    _CoUsInfoCpuUse20Sec_Type()
)
coUsInfoCpuUse20Sec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coUsInfoCpuUse20Sec.setStatus("current")
if mibBuilder.loadTexts:
    coUsInfoCpuUse20Sec.setUnits("%")
_CoUsInfoRamTotal_Type = Unsigned32
_CoUsInfoRamTotal_Object = MibScalar
coUsInfoRamTotal = _CoUsInfoRamTotal_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 21, 1, 1, 9),
    _CoUsInfoRamTotal_Type()
)
coUsInfoRamTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coUsInfoRamTotal.setStatus("current")
if mibBuilder.loadTexts:
    coUsInfoRamTotal.setUnits("Kb")
_CoUsInfoRamFree_Type = Unsigned32
_CoUsInfoRamFree_Object = MibScalar
coUsInfoRamFree = _CoUsInfoRamFree_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 21, 1, 1, 10),
    _CoUsInfoRamFree_Type()
)
coUsInfoRamFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coUsInfoRamFree.setStatus("current")
if mibBuilder.loadTexts:
    coUsInfoRamFree.setUnits("Kb")
_CoUsInfoRamBuffer_Type = Unsigned32
_CoUsInfoRamBuffer_Object = MibScalar
coUsInfoRamBuffer = _CoUsInfoRamBuffer_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 21, 1, 1, 11),
    _CoUsInfoRamBuffer_Type()
)
coUsInfoRamBuffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coUsInfoRamBuffer.setStatus("current")
if mibBuilder.loadTexts:
    coUsInfoRamBuffer.setUnits("Kb")
_CoUsInfoRamCached_Type = Unsigned32
_CoUsInfoRamCached_Object = MibScalar
coUsInfoRamCached = _CoUsInfoRamCached_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 21, 1, 1, 12),
    _CoUsInfoRamCached_Type()
)
coUsInfoRamCached.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coUsInfoRamCached.setStatus("current")
if mibBuilder.loadTexts:
    coUsInfoRamCached.setUnits("Kb")
_CoUsInfoStorageUsePermanent_Type = Unsigned32
_CoUsInfoStorageUsePermanent_Object = MibScalar
coUsInfoStorageUsePermanent = _CoUsInfoStorageUsePermanent_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 21, 1, 1, 13),
    _CoUsInfoStorageUsePermanent_Type()
)
coUsInfoStorageUsePermanent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coUsInfoStorageUsePermanent.setStatus("current")
if mibBuilder.loadTexts:
    coUsInfoStorageUsePermanent.setUnits("%")
_CoUsInfoStorageUseTemporary_Type = Unsigned32
_CoUsInfoStorageUseTemporary_Object = MibScalar
coUsInfoStorageUseTemporary = _CoUsInfoStorageUseTemporary_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 21, 1, 1, 14),
    _CoUsInfoStorageUseTemporary_Type()
)
coUsInfoStorageUseTemporary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coUsInfoStorageUseTemporary.setStatus("current")
if mibBuilder.loadTexts:
    coUsInfoStorageUseTemporary.setUnits("%")
_ColubrisUsageInformationMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
colubrisUsageInformationMIBNotificationPrefix = _ColubrisUsageInformationMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 21, 2)
)
_ColubrisUsageInformationMIBNotifications_ObjectIdentity = ObjectIdentity
colubrisUsageInformationMIBNotifications = _ColubrisUsageInformationMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 21, 2, 0)
)
_ColubrisUsageInformationMIBConformance_ObjectIdentity = ObjectIdentity
colubrisUsageInformationMIBConformance = _ColubrisUsageInformationMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 21, 3)
)
_ColubrisUsageInformationMIBCompliances_ObjectIdentity = ObjectIdentity
colubrisUsageInformationMIBCompliances = _ColubrisUsageInformationMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 21, 3, 1)
)
_ColubrisUsageInformationMIBGroups_ObjectIdentity = ObjectIdentity
colubrisUsageInformationMIBGroups = _ColubrisUsageInformationMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 21, 3, 2)
)

# Managed Objects groups

colubrisUsageInformationMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8744, 5, 21, 3, 2, 1)
)
colubrisUsageInformationMIBGroup.setObjects(
      *(("COLUBRIS-USAGE-INFORMATION-MIB", "coUsInfoUpTime"),
        ("COLUBRIS-USAGE-INFORMATION-MIB", "coUsInfoLoadAverage1Min"),
        ("COLUBRIS-USAGE-INFORMATION-MIB", "coUsInfoLoadAverage5Min"),
        ("COLUBRIS-USAGE-INFORMATION-MIB", "coUsInfoLoadAverage15Min"),
        ("COLUBRIS-USAGE-INFORMATION-MIB", "coUsInfoCpuUseNow"),
        ("COLUBRIS-USAGE-INFORMATION-MIB", "coUsInfoCpuUse5Sec"),
        ("COLUBRIS-USAGE-INFORMATION-MIB", "coUsInfoCpuUse10Sec"),
        ("COLUBRIS-USAGE-INFORMATION-MIB", "coUsInfoCpuUse20Sec"),
        ("COLUBRIS-USAGE-INFORMATION-MIB", "coUsInfoRamTotal"),
        ("COLUBRIS-USAGE-INFORMATION-MIB", "coUsInfoRamFree"),
        ("COLUBRIS-USAGE-INFORMATION-MIB", "coUsInfoRamBuffer"),
        ("COLUBRIS-USAGE-INFORMATION-MIB", "coUsInfoRamCached"),
        ("COLUBRIS-USAGE-INFORMATION-MIB", "coUsInfoStorageUsePermanent"),
        ("COLUBRIS-USAGE-INFORMATION-MIB", "coUsInfoStorageUseTemporary"))
)
if mibBuilder.loadTexts:
    colubrisUsageInformationMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

colubrisUsageInformationMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8744, 5, 21, 3, 1, 1)
)
if mibBuilder.loadTexts:
    colubrisUsageInformationMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "COLUBRIS-USAGE-INFORMATION-MIB",
    **{"colubrisUsageInformationMIB": colubrisUsageInformationMIB,
       "colubrisUsageInformationMIBObjects": colubrisUsageInformationMIBObjects,
       "coUsageInformationGroup": coUsageInformationGroup,
       "coUsInfoUpTime": coUsInfoUpTime,
       "coUsInfoLoadAverage1Min": coUsInfoLoadAverage1Min,
       "coUsInfoLoadAverage5Min": coUsInfoLoadAverage5Min,
       "coUsInfoLoadAverage15Min": coUsInfoLoadAverage15Min,
       "coUsInfoCpuUseNow": coUsInfoCpuUseNow,
       "coUsInfoCpuUse5Sec": coUsInfoCpuUse5Sec,
       "coUsInfoCpuUse10Sec": coUsInfoCpuUse10Sec,
       "coUsInfoCpuUse20Sec": coUsInfoCpuUse20Sec,
       "coUsInfoRamTotal": coUsInfoRamTotal,
       "coUsInfoRamFree": coUsInfoRamFree,
       "coUsInfoRamBuffer": coUsInfoRamBuffer,
       "coUsInfoRamCached": coUsInfoRamCached,
       "coUsInfoStorageUsePermanent": coUsInfoStorageUsePermanent,
       "coUsInfoStorageUseTemporary": coUsInfoStorageUseTemporary,
       "colubrisUsageInformationMIBNotificationPrefix": colubrisUsageInformationMIBNotificationPrefix,
       "colubrisUsageInformationMIBNotifications": colubrisUsageInformationMIBNotifications,
       "colubrisUsageInformationMIBConformance": colubrisUsageInformationMIBConformance,
       "colubrisUsageInformationMIBCompliances": colubrisUsageInformationMIBCompliances,
       "colubrisUsageInformationMIBCompliance": colubrisUsageInformationMIBCompliance,
       "colubrisUsageInformationMIBGroups": colubrisUsageInformationMIBGroups,
       "colubrisUsageInformationMIBGroup": colubrisUsageInformationMIBGroup}
)
