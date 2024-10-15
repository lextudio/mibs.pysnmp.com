# SNMP MIB module (ZYXEL-TRTCM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZYXEL-TRTCM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:22:59 2024
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

(dot1dBasePort,) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "dot1dBasePort")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

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

(esMgmt,) = mibBuilder.importSymbols(
    "ZYXEL-ES-SMI",
    "esMgmt")


# MODULE-IDENTITY

zyxelTrtcm = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 85)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZyxelTrtcmSetup_ObjectIdentity = ObjectIdentity
zyxelTrtcmSetup = _ZyxelTrtcmSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 85, 1)
)
_ZyTctcmState_Type = EnabledStatus
_ZyTctcmState_Object = MibScalar
zyTctcmState = _ZyTctcmState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 85, 1, 1),
    _ZyTctcmState_Type()
)
zyTctcmState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyTctcmState.setStatus("current")


class _ZyTrtcmMode_Type(Integer32):
    """Custom type zyTrtcmMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("colorAware", 0),
          ("colorBlind", 1))
    )


_ZyTrtcmMode_Type.__name__ = "Integer32"
_ZyTrtcmMode_Object = MibScalar
zyTrtcmMode = _ZyTrtcmMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 85, 1, 2),
    _ZyTrtcmMode_Type()
)
zyTrtcmMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyTrtcmMode.setStatus("current")
_ZyxelTrtcmPortTable_Object = MibTable
zyxelTrtcmPortTable = _ZyxelTrtcmPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 85, 1, 3)
)
if mibBuilder.loadTexts:
    zyxelTrtcmPortTable.setStatus("current")
_ZyxelTrtcmPortEntry_Object = MibTableRow
zyxelTrtcmPortEntry = _ZyxelTrtcmPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 85, 1, 3, 1)
)
zyxelTrtcmPortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    zyxelTrtcmPortEntry.setStatus("current")
_ZyTrtcmPortState_Type = EnabledStatus
_ZyTrtcmPortState_Object = MibTableColumn
zyTrtcmPortState = _ZyTrtcmPortState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 85, 1, 3, 1, 1),
    _ZyTrtcmPortState_Type()
)
zyTrtcmPortState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zyTrtcmPortState.setStatus("current")
_ZyTrtcmPortCir_Type = Integer32
_ZyTrtcmPortCir_Object = MibTableColumn
zyTrtcmPortCir = _ZyTrtcmPortCir_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 85, 1, 3, 1, 2),
    _ZyTrtcmPortCir_Type()
)
zyTrtcmPortCir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyTrtcmPortCir.setStatus("current")
_ZyTrtcmPortPir_Type = Integer32
_ZyTrtcmPortPir_Object = MibTableColumn
zyTrtcmPortPir = _ZyTrtcmPortPir_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 85, 1, 3, 1, 3),
    _ZyTrtcmPortPir_Type()
)
zyTrtcmPortPir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyTrtcmPortPir.setStatus("current")
_ZyTrtcmPortDscpProfile_Type = DisplayString
_ZyTrtcmPortDscpProfile_Object = MibTableColumn
zyTrtcmPortDscpProfile = _ZyTrtcmPortDscpProfile_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 85, 1, 3, 1, 4),
    _ZyTrtcmPortDscpProfile_Type()
)
zyTrtcmPortDscpProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyTrtcmPortDscpProfile.setStatus("current")
_ZyTrtcmMaxNumberOfDscpProfiles_Type = Integer32
_ZyTrtcmMaxNumberOfDscpProfiles_Object = MibScalar
zyTrtcmMaxNumberOfDscpProfiles = _ZyTrtcmMaxNumberOfDscpProfiles_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 85, 1, 4),
    _ZyTrtcmMaxNumberOfDscpProfiles_Type()
)
zyTrtcmMaxNumberOfDscpProfiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyTrtcmMaxNumberOfDscpProfiles.setStatus("current")
_ZyxelTrtcmDscpProfileTable_Object = MibTable
zyxelTrtcmDscpProfileTable = _ZyxelTrtcmDscpProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 85, 1, 5)
)
if mibBuilder.loadTexts:
    zyxelTrtcmDscpProfileTable.setStatus("current")
_ZyxelTrtcmDscpProfileEntry_Object = MibTableRow
zyxelTrtcmDscpProfileEntry = _ZyxelTrtcmDscpProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 85, 1, 5, 1)
)
zyxelTrtcmDscpProfileEntry.setIndexNames(
    (0, "ZYXEL-TRTCM-MIB", "zyTrtcmDscpProfileName"),
)
if mibBuilder.loadTexts:
    zyxelTrtcmDscpProfileEntry.setStatus("current")
_ZyTrtcmDscpProfileName_Type = DisplayString
_ZyTrtcmDscpProfileName_Object = MibTableColumn
zyTrtcmDscpProfileName = _ZyTrtcmDscpProfileName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 85, 1, 5, 1, 1),
    _ZyTrtcmDscpProfileName_Type()
)
zyTrtcmDscpProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyTrtcmDscpProfileName.setStatus("current")
_ZyTrtcmDscpProfileDscpGreen_Type = Integer32
_ZyTrtcmDscpProfileDscpGreen_Object = MibTableColumn
zyTrtcmDscpProfileDscpGreen = _ZyTrtcmDscpProfileDscpGreen_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 85, 1, 5, 1, 2),
    _ZyTrtcmDscpProfileDscpGreen_Type()
)
zyTrtcmDscpProfileDscpGreen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyTrtcmDscpProfileDscpGreen.setStatus("current")
_ZyTrtcmDscpProfileDscpYellow_Type = Integer32
_ZyTrtcmDscpProfileDscpYellow_Object = MibTableColumn
zyTrtcmDscpProfileDscpYellow = _ZyTrtcmDscpProfileDscpYellow_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 85, 1, 5, 1, 3),
    _ZyTrtcmDscpProfileDscpYellow_Type()
)
zyTrtcmDscpProfileDscpYellow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyTrtcmDscpProfileDscpYellow.setStatus("current")
_ZyTrtcmDscpProfileDscpRed_Type = Integer32
_ZyTrtcmDscpProfileDscpRed_Object = MibTableColumn
zyTrtcmDscpProfileDscpRed = _ZyTrtcmDscpProfileDscpRed_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 85, 1, 5, 1, 4),
    _ZyTrtcmDscpProfileDscpRed_Type()
)
zyTrtcmDscpProfileDscpRed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyTrtcmDscpProfileDscpRed.setStatus("current")
_ZyTrtcmDscpProfileRowstatus_Type = RowStatus
_ZyTrtcmDscpProfileRowstatus_Object = MibTableColumn
zyTrtcmDscpProfileRowstatus = _ZyTrtcmDscpProfileRowstatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 85, 1, 5, 1, 5),
    _ZyTrtcmDscpProfileRowstatus_Type()
)
zyTrtcmDscpProfileRowstatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zyTrtcmDscpProfileRowstatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-TRTCM-MIB",
    **{"zyxelTrtcm": zyxelTrtcm,
       "zyxelTrtcmSetup": zyxelTrtcmSetup,
       "zyTctcmState": zyTctcmState,
       "zyTrtcmMode": zyTrtcmMode,
       "zyxelTrtcmPortTable": zyxelTrtcmPortTable,
       "zyxelTrtcmPortEntry": zyxelTrtcmPortEntry,
       "zyTrtcmPortState": zyTrtcmPortState,
       "zyTrtcmPortCir": zyTrtcmPortCir,
       "zyTrtcmPortPir": zyTrtcmPortPir,
       "zyTrtcmPortDscpProfile": zyTrtcmPortDscpProfile,
       "zyTrtcmMaxNumberOfDscpProfiles": zyTrtcmMaxNumberOfDscpProfiles,
       "zyxelTrtcmDscpProfileTable": zyxelTrtcmDscpProfileTable,
       "zyxelTrtcmDscpProfileEntry": zyxelTrtcmDscpProfileEntry,
       "zyTrtcmDscpProfileName": zyTrtcmDscpProfileName,
       "zyTrtcmDscpProfileDscpGreen": zyTrtcmDscpProfileDscpGreen,
       "zyTrtcmDscpProfileDscpYellow": zyTrtcmDscpProfileDscpYellow,
       "zyTrtcmDscpProfileDscpRed": zyTrtcmDscpProfileDscpRed,
       "zyTrtcmDscpProfileRowstatus": zyTrtcmDscpProfileRowstatus}
)
