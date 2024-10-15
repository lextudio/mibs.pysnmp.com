# SNMP MIB module (TPLINK-QOS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TPLINK-QOS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:06:35 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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

(tplinkMgmt,) = mibBuilder.importSymbols(
    "TPLINK-MIB",
    "tplinkMgmt")


# MODULE-IDENTITY

tplinkQosMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 22)
)
tplinkQosMIB.setRevisions(
        ("2012-12-13 09:30",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TplinkQosMIBObjects_ObjectIdentity = ObjectIdentity
tplinkQosMIBObjects = _TplinkQosMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 22, 1)
)
_TplinkQosBasicConfig_ObjectIdentity = ObjectIdentity
tplinkQosBasicConfig = _TplinkQosBasicConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 22, 1, 1)
)
_TpQosBasicConfigTable_Object = MibTable
tpQosBasicConfigTable = _TpQosBasicConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 22, 1, 1, 1)
)
if mibBuilder.loadTexts:
    tpQosBasicConfigTable.setStatus("current")
_TpQosBasicConfigEntry_Object = MibTableRow
tpQosBasicConfigEntry = _TpQosBasicConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 22, 1, 1, 1, 1)
)
tpQosBasicConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tpQosBasicConfigEntry.setStatus("current")
_TpQosBasicConfigPort_Type = DisplayString
_TpQosBasicConfigPort_Object = MibTableColumn
tpQosBasicConfigPort = _TpQosBasicConfigPort_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 22, 1, 1, 1, 1, 1),
    _TpQosBasicConfigPort_Type()
)
tpQosBasicConfigPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpQosBasicConfigPort.setStatus("current")


class _TpQosBasicConfigPri_Type(Integer32):
    """Custom type tpQosBasicConfigPri based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("cos0", 0),
          ("cos1", 1),
          ("cos2", 2),
          ("cos3", 3),
          ("cos4", 4),
          ("cos5", 5),
          ("cos6", 6),
          ("cos7", 7))
    )


_TpQosBasicConfigPri_Type.__name__ = "Integer32"
_TpQosBasicConfigPri_Object = MibTableColumn
tpQosBasicConfigPri = _TpQosBasicConfigPri_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 22, 1, 1, 1, 1, 2),
    _TpQosBasicConfigPri_Type()
)
tpQosBasicConfigPri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpQosBasicConfigPri.setStatus("current")


class _TpQosBasicConfigLag_Type(OctetString):
    """Custom type tpQosBasicConfigLag based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_TpQosBasicConfigLag_Type.__name__ = "OctetString"
_TpQosBasicConfigLag_Object = MibTableColumn
tpQosBasicConfigLag = _TpQosBasicConfigLag_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 22, 1, 1, 1, 1, 3),
    _TpQosBasicConfigLag_Type()
)
tpQosBasicConfigLag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpQosBasicConfigLag.setStatus("current")
_TplinkQosScheduler_ObjectIdentity = ObjectIdentity
tplinkQosScheduler = _TplinkQosScheduler_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 22, 1, 2)
)


class _TpQosSchedulerConfig_Type(Integer32):
    """Custom type tpQosSchedulerConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("equ-mode", 3),
          ("sp-mode", 0),
          ("sp-wrr-mode", 2),
          ("wrr-mode", 1))
    )


_TpQosSchedulerConfig_Type.__name__ = "Integer32"
_TpQosSchedulerConfig_Object = MibScalar
tpQosSchedulerConfig = _TpQosSchedulerConfig_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 22, 1, 2, 1),
    _TpQosSchedulerConfig_Type()
)
tpQosSchedulerConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpQosSchedulerConfig.setStatus("current")
_TpQosSchedulerWeightTable_Object = MibTable
tpQosSchedulerWeightTable = _TpQosSchedulerWeightTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 22, 1, 2, 2)
)
if mibBuilder.loadTexts:
    tpQosSchedulerWeightTable.setStatus("current")
_TpQosSchedulerWeightEntry_Object = MibTableRow
tpQosSchedulerWeightEntry = _TpQosSchedulerWeightEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 22, 1, 2, 2, 1)
)
tpQosSchedulerWeightEntry.setIndexNames(
    (0, "TPLINK-QOS-MIB", "tpQosSchedulerTc"),
)
if mibBuilder.loadTexts:
    tpQosSchedulerWeightEntry.setStatus("current")


class _TpQosSchedulerTc_Type(Integer32):
    """Custom type tpQosSchedulerTc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("tc0", 0),
          ("tc1", 1),
          ("tc2", 2),
          ("tc3", 3),
          ("tc4", 4),
          ("tc5", 5),
          ("tc6", 6),
          ("tc7", 7))
    )


_TpQosSchedulerTc_Type.__name__ = "Integer32"
_TpQosSchedulerTc_Object = MibTableColumn
tpQosSchedulerTc = _TpQosSchedulerTc_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 22, 1, 2, 2, 1, 1),
    _TpQosSchedulerTc_Type()
)
tpQosSchedulerTc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpQosSchedulerTc.setStatus("current")


class _TpQosSchedulerWeight_Type(Integer32):
    """Custom type tpQosSchedulerWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_TpQosSchedulerWeight_Type.__name__ = "Integer32"
_TpQosSchedulerWeight_Object = MibTableColumn
tpQosSchedulerWeight = _TpQosSchedulerWeight_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 22, 1, 2, 2, 1, 2),
    _TpQosSchedulerWeight_Type()
)
tpQosSchedulerWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpQosSchedulerWeight.setStatus("current")
_TplinkQos8021p_ObjectIdentity = ObjectIdentity
tplinkQos8021p = _TplinkQos8021p_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 22, 1, 3)
)
_TpQos8021pTable_Object = MibTable
tpQos8021pTable = _TpQos8021pTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 22, 1, 3, 2)
)
if mibBuilder.loadTexts:
    tpQos8021pTable.setStatus("current")
_TpQos8021pEntry_Object = MibTableRow
tpQos8021pEntry = _TpQos8021pEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 22, 1, 3, 2, 1)
)
tpQos8021pEntry.setIndexNames(
    (0, "TPLINK-QOS-MIB", "tpQos8021pPriTag"),
)
if mibBuilder.loadTexts:
    tpQos8021pEntry.setStatus("current")
_TpQos8021pPriTag_Type = Integer32
_TpQos8021pPriTag_Object = MibTableColumn
tpQos8021pPriTag = _TpQos8021pPriTag_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 22, 1, 3, 2, 1, 1),
    _TpQos8021pPriTag_Type()
)
tpQos8021pPriTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpQos8021pPriTag.setStatus("current")


class _TpQos8021pPriLevel_Type(Integer32):
    """Custom type tpQos8021pPriLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("tc0", 0),
          ("tc1", 1),
          ("tc2", 2),
          ("tc3", 3),
          ("tc4", 4),
          ("tc5", 5),
          ("tc6", 6),
          ("tc7", 7))
    )


_TpQos8021pPriLevel_Type.__name__ = "Integer32"
_TpQos8021pPriLevel_Object = MibTableColumn
tpQos8021pPriLevel = _TpQos8021pPriLevel_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 22, 1, 3, 2, 1, 2),
    _TpQos8021pPriLevel_Type()
)
tpQos8021pPriLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpQos8021pPriLevel.setStatus("current")
_TplinkQosDSCP_ObjectIdentity = ObjectIdentity
tplinkQosDSCP = _TplinkQosDSCP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 22, 1, 4)
)


class _TpQosDSCPEnable_Type(Integer32):
    """Custom type tpQosDSCPEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_TpQosDSCPEnable_Type.__name__ = "Integer32"
_TpQosDSCPEnable_Object = MibScalar
tpQosDSCPEnable = _TpQosDSCPEnable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 22, 1, 4, 1),
    _TpQosDSCPEnable_Type()
)
tpQosDSCPEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpQosDSCPEnable.setStatus("current")
_TpQosDSCPTable_Object = MibTable
tpQosDSCPTable = _TpQosDSCPTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 22, 1, 4, 2)
)
if mibBuilder.loadTexts:
    tpQosDSCPTable.setStatus("current")
_TpQosDSCPEntry_Object = MibTableRow
tpQosDSCPEntry = _TpQosDSCPEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 22, 1, 4, 2, 1)
)
tpQosDSCPEntry.setIndexNames(
    (0, "TPLINK-QOS-MIB", "tpQosDSCPPriTag"),
)
if mibBuilder.loadTexts:
    tpQosDSCPEntry.setStatus("current")
_TpQosDSCPPriTag_Type = Integer32
_TpQosDSCPPriTag_Object = MibTableColumn
tpQosDSCPPriTag = _TpQosDSCPPriTag_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 22, 1, 4, 2, 1, 1),
    _TpQosDSCPPriTag_Type()
)
tpQosDSCPPriTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpQosDSCPPriTag.setStatus("current")


class _TpQosDSCPPriLevel_Type(Integer32):
    """Custom type tpQosDSCPPriLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("cos0", 0),
          ("cos1", 1),
          ("cos2", 2),
          ("cos3", 3),
          ("cos4", 4),
          ("cos5", 5),
          ("cos6", 6),
          ("cos7", 7))
    )


_TpQosDSCPPriLevel_Type.__name__ = "Integer32"
_TpQosDSCPPriLevel_Object = MibTableColumn
tpQosDSCPPriLevel = _TpQosDSCPPriLevel_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 22, 1, 4, 2, 1, 2),
    _TpQosDSCPPriLevel_Type()
)
tpQosDSCPPriLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpQosDSCPPriLevel.setStatus("current")
_TplinkQosNotifications_ObjectIdentity = ObjectIdentity
tplinkQosNotifications = _TplinkQosNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 22, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPLINK-QOS-MIB",
    **{"tplinkQosMIB": tplinkQosMIB,
       "tplinkQosMIBObjects": tplinkQosMIBObjects,
       "tplinkQosBasicConfig": tplinkQosBasicConfig,
       "tpQosBasicConfigTable": tpQosBasicConfigTable,
       "tpQosBasicConfigEntry": tpQosBasicConfigEntry,
       "tpQosBasicConfigPort": tpQosBasicConfigPort,
       "tpQosBasicConfigPri": tpQosBasicConfigPri,
       "tpQosBasicConfigLag": tpQosBasicConfigLag,
       "tplinkQosScheduler": tplinkQosScheduler,
       "tpQosSchedulerConfig": tpQosSchedulerConfig,
       "tpQosSchedulerWeightTable": tpQosSchedulerWeightTable,
       "tpQosSchedulerWeightEntry": tpQosSchedulerWeightEntry,
       "tpQosSchedulerTc": tpQosSchedulerTc,
       "tpQosSchedulerWeight": tpQosSchedulerWeight,
       "tplinkQos8021p": tplinkQos8021p,
       "tpQos8021pTable": tpQos8021pTable,
       "tpQos8021pEntry": tpQos8021pEntry,
       "tpQos8021pPriTag": tpQos8021pPriTag,
       "tpQos8021pPriLevel": tpQos8021pPriLevel,
       "tplinkQosDSCP": tplinkQosDSCP,
       "tpQosDSCPEnable": tpQosDSCPEnable,
       "tpQosDSCPTable": tpQosDSCPTable,
       "tpQosDSCPEntry": tpQosDSCPEntry,
       "tpQosDSCPPriTag": tpQosDSCPPriTag,
       "tpQosDSCPPriLevel": tpQosDSCPPriLevel,
       "tplinkQosNotifications": tplinkQosNotifications}
)
