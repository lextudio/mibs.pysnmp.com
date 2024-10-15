# SNMP MIB module (TPLINK-VOICEVLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TPLINK-VOICEVLAN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:06:50 2024
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

(TPRowStatus,) = mibBuilder.importSymbols(
    "TPLINK-TC-MIB",
    "TPRowStatus")


# MODULE-IDENTITY

tplinkVoiceVlanMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 19)
)
tplinkVoiceVlanMIB.setRevisions(
        ("2012-12-13 16:30",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TplinkVoiceVlanMIBObjects_ObjectIdentity = ObjectIdentity
tplinkVoiceVlanMIBObjects = _TplinkVoiceVlanMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 19, 1)
)
_VoiceVlanGlobalConfig_ObjectIdentity = ObjectIdentity
voiceVlanGlobalConfig = _VoiceVlanGlobalConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 19, 1, 1)
)


class _VoiceVlanGlobalEnable_Type(Integer32):
    """Custom type voiceVlanGlobalEnable based on Integer32"""
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


_VoiceVlanGlobalEnable_Type.__name__ = "Integer32"
_VoiceVlanGlobalEnable_Object = MibScalar
voiceVlanGlobalEnable = _VoiceVlanGlobalEnable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 19, 1, 1, 1),
    _VoiceVlanGlobalEnable_Type()
)
voiceVlanGlobalEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceVlanGlobalEnable.setStatus("current")


class _VoiceVlanId_Type(Integer32):
    """Custom type voiceVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 4094),
    )


_VoiceVlanId_Type.__name__ = "Integer32"
_VoiceVlanId_Object = MibScalar
voiceVlanId = _VoiceVlanId_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 19, 1, 1, 2),
    _VoiceVlanId_Type()
)
voiceVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceVlanId.setStatus("current")
_VoiceVlanAgingTime_Type = Integer32
_VoiceVlanAgingTime_Object = MibScalar
voiceVlanAgingTime = _VoiceVlanAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 19, 1, 1, 3),
    _VoiceVlanAgingTime_Type()
)
voiceVlanAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceVlanAgingTime.setStatus("current")


class _VoiceVlanPriority_Type(Integer32):
    """Custom type voiceVlanPriority based on Integer32"""
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


_VoiceVlanPriority_Type.__name__ = "Integer32"
_VoiceVlanPriority_Object = MibScalar
voiceVlanPriority = _VoiceVlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 19, 1, 1, 4),
    _VoiceVlanPriority_Type()
)
voiceVlanPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceVlanPriority.setStatus("current")
_VoiceVlanPortConfig_ObjectIdentity = ObjectIdentity
voiceVlanPortConfig = _VoiceVlanPortConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 19, 1, 2)
)
_VoiceVlanPortTable_Object = MibTable
voiceVlanPortTable = _VoiceVlanPortTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 19, 1, 2, 1)
)
if mibBuilder.loadTexts:
    voiceVlanPortTable.setStatus("current")
_VoiceVlanPortEntry_Object = MibTableRow
voiceVlanPortEntry = _VoiceVlanPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 19, 1, 2, 1, 1)
)
voiceVlanPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    voiceVlanPortEntry.setStatus("current")


class _VoiceVlanPortNumber_Type(OctetString):
    """Custom type voiceVlanPortNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_VoiceVlanPortNumber_Type.__name__ = "OctetString"
_VoiceVlanPortNumber_Object = MibTableColumn
voiceVlanPortNumber = _VoiceVlanPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 19, 1, 2, 1, 1, 1),
    _VoiceVlanPortNumber_Type()
)
voiceVlanPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceVlanPortNumber.setStatus("current")


class _VoiceVlanPortMode_Type(Integer32):
    """Custom type voiceVlanPortMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("manual", 0))
    )


_VoiceVlanPortMode_Type.__name__ = "Integer32"
_VoiceVlanPortMode_Object = MibTableColumn
voiceVlanPortMode = _VoiceVlanPortMode_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 19, 1, 2, 1, 1, 2),
    _VoiceVlanPortMode_Type()
)
voiceVlanPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceVlanPortMode.setStatus("current")


class _VoiceVlanPortSecurity_Type(Integer32):
    """Custom type voiceVlanPortSecurity based on Integer32"""
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


_VoiceVlanPortSecurity_Type.__name__ = "Integer32"
_VoiceVlanPortSecurity_Object = MibTableColumn
voiceVlanPortSecurity = _VoiceVlanPortSecurity_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 19, 1, 2, 1, 1, 3),
    _VoiceVlanPortSecurity_Type()
)
voiceVlanPortSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceVlanPortSecurity.setStatus("current")


class _VoiceVlanPortStatus_Type(Integer32):
    """Custom type voiceVlanPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 0))
    )


_VoiceVlanPortStatus_Type.__name__ = "Integer32"
_VoiceVlanPortStatus_Object = MibTableColumn
voiceVlanPortStatus = _VoiceVlanPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 19, 1, 2, 1, 1, 4),
    _VoiceVlanPortStatus_Type()
)
voiceVlanPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceVlanPortStatus.setStatus("current")


class _VoiceVlanPortLag_Type(OctetString):
    """Custom type voiceVlanPortLag based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_VoiceVlanPortLag_Type.__name__ = "OctetString"
_VoiceVlanPortLag_Object = MibTableColumn
voiceVlanPortLag = _VoiceVlanPortLag_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 19, 1, 2, 1, 1, 5),
    _VoiceVlanPortLag_Type()
)
voiceVlanPortLag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceVlanPortLag.setStatus("current")
_VoiceVlanOuiConfig_ObjectIdentity = ObjectIdentity
voiceVlanOuiConfig = _VoiceVlanOuiConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 19, 1, 3)
)
_VoiceVlanOuiConfigTable_Object = MibTable
voiceVlanOuiConfigTable = _VoiceVlanOuiConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 19, 1, 3, 1)
)
if mibBuilder.loadTexts:
    voiceVlanOuiConfigTable.setStatus("current")
_VoiceVlanOuiConfigEntry_Object = MibTableRow
voiceVlanOuiConfigEntry = _VoiceVlanOuiConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 19, 1, 3, 1, 1)
)
voiceVlanOuiConfigEntry.setIndexNames(
    (0, "TPLINK-VOICEVLAN-MIB", "voiceVlanOui"),
)
if mibBuilder.loadTexts:
    voiceVlanOuiConfigEntry.setStatus("current")


class _VoiceVlanOui_Type(OctetString):
    """Custom type voiceVlanOui based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VoiceVlanOui_Type.__name__ = "OctetString"
_VoiceVlanOui_Object = MibTableColumn
voiceVlanOui = _VoiceVlanOui_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 19, 1, 3, 1, 1, 1),
    _VoiceVlanOui_Type()
)
voiceVlanOui.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    voiceVlanOui.setStatus("current")


class _VoiceVlanOuiMask_Type(OctetString):
    """Custom type voiceVlanOuiMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VoiceVlanOuiMask_Type.__name__ = "OctetString"
_VoiceVlanOuiMask_Object = MibTableColumn
voiceVlanOuiMask = _VoiceVlanOuiMask_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 19, 1, 3, 1, 1, 2),
    _VoiceVlanOuiMask_Type()
)
voiceVlanOuiMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    voiceVlanOuiMask.setStatus("current")


class _VoiceVlanDescription_Type(OctetString):
    """Custom type voiceVlanDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_VoiceVlanDescription_Type.__name__ = "OctetString"
_VoiceVlanDescription_Object = MibTableColumn
voiceVlanDescription = _VoiceVlanDescription_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 19, 1, 3, 1, 1, 3),
    _VoiceVlanDescription_Type()
)
voiceVlanDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    voiceVlanDescription.setStatus("current")
_VoiceVlanRowStatus_Type = TPRowStatus
_VoiceVlanRowStatus_Object = MibTableColumn
voiceVlanRowStatus = _VoiceVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 19, 1, 3, 1, 1, 4),
    _VoiceVlanRowStatus_Type()
)
voiceVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    voiceVlanRowStatus.setStatus("current")
_TplinkVoiceVlanMIBNotifications_ObjectIdentity = ObjectIdentity
tplinkVoiceVlanMIBNotifications = _TplinkVoiceVlanMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 19, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPLINK-VOICEVLAN-MIB",
    **{"tplinkVoiceVlanMIB": tplinkVoiceVlanMIB,
       "tplinkVoiceVlanMIBObjects": tplinkVoiceVlanMIBObjects,
       "voiceVlanGlobalConfig": voiceVlanGlobalConfig,
       "voiceVlanGlobalEnable": voiceVlanGlobalEnable,
       "voiceVlanId": voiceVlanId,
       "voiceVlanAgingTime": voiceVlanAgingTime,
       "voiceVlanPriority": voiceVlanPriority,
       "voiceVlanPortConfig": voiceVlanPortConfig,
       "voiceVlanPortTable": voiceVlanPortTable,
       "voiceVlanPortEntry": voiceVlanPortEntry,
       "voiceVlanPortNumber": voiceVlanPortNumber,
       "voiceVlanPortMode": voiceVlanPortMode,
       "voiceVlanPortSecurity": voiceVlanPortSecurity,
       "voiceVlanPortStatus": voiceVlanPortStatus,
       "voiceVlanPortLag": voiceVlanPortLag,
       "voiceVlanOuiConfig": voiceVlanOuiConfig,
       "voiceVlanOuiConfigTable": voiceVlanOuiConfigTable,
       "voiceVlanOuiConfigEntry": voiceVlanOuiConfigEntry,
       "voiceVlanOui": voiceVlanOui,
       "voiceVlanOuiMask": voiceVlanOuiMask,
       "voiceVlanDescription": voiceVlanDescription,
       "voiceVlanRowStatus": voiceVlanRowStatus,
       "tplinkVoiceVlanMIBNotifications": tplinkVoiceVlanMIBNotifications}
)
