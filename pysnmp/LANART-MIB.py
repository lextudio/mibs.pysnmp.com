# SNMP MIB module (LANART-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/LANART-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:16:56 2024
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

(rptrPortOperStatus,) = mibBuilder.importSymbols(
    "SNMP-REPEATER-MIB",
    "rptrPortOperStatus")

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

_Lanart_ObjectIdentity = ObjectIdentity
lanart = _Lanart_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 712)
)
_LaMib1_ObjectIdentity = ObjectIdentity
laMib1 = _LaMib1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 712, 1)
)
_LaProducts_ObjectIdentity = ObjectIdentity
laProducts = _LaProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 712, 1, 1)
)
_LaTpHub_ObjectIdentity = ObjectIdentity
laTpHub = _LaTpHub_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 712, 1, 1, 1)
)
_LaTpHub1_ObjectIdentity = ObjectIdentity
laTpHub1 = _LaTpHub1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 712, 1, 1, 1, 1)
)
_Etm120x_ObjectIdentity = ObjectIdentity
etm120x = _Etm120x_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 712, 1, 1, 1, 1, 12)
)
_Etm160x_ObjectIdentity = ObjectIdentity
etm160x = _Etm160x_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 712, 1, 1, 1, 1, 16)
)
_Etm240x_ObjectIdentity = ObjectIdentity
etm240x = _Etm240x_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 712, 1, 1, 1, 1, 24)
)
_LaTpHub2_ObjectIdentity = ObjectIdentity
laTpHub2 = _LaTpHub2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 712, 1, 1, 1, 2)
)
_Ete120x_ObjectIdentity = ObjectIdentity
ete120x = _Ete120x_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 712, 1, 1, 1, 2, 12)
)
_Ete160x_ObjectIdentity = ObjectIdentity
ete160x = _Ete160x_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 712, 1, 1, 1, 2, 16)
)
_Ete240x_ObjectIdentity = ObjectIdentity
ete240x = _Ete240x_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 712, 1, 1, 1, 2, 24)
)
_LaTpHub3_ObjectIdentity = ObjectIdentity
laTpHub3 = _LaTpHub3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 712, 1, 1, 1, 3)
)
_BbAui_ObjectIdentity = ObjectIdentity
bbAui = _BbAui_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 712, 1, 1, 1, 3, 0)
)
_BbAuiTp_ObjectIdentity = ObjectIdentity
bbAuiTp = _BbAuiTp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 712, 1, 1, 1, 3, 1)
)
_BbAuiBnc_ObjectIdentity = ObjectIdentity
bbAuiBnc = _BbAuiBnc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 712, 1, 1, 1, 3, 2)
)
_BbAuiTpBnc_ObjectIdentity = ObjectIdentity
bbAuiTpBnc = _BbAuiTpBnc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 712, 1, 1, 1, 3, 3)
)
_BbAui10BASE_FL_ObjectIdentity = ObjectIdentity
bbAui10BASE_FL = _BbAui10BASE_FL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 712, 1, 1, 1, 3, 4)
)
_LaHubMib_ObjectIdentity = ObjectIdentity
laHubMib = _LaHubMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 712, 1, 2)
)
_LaSys_ObjectIdentity = ObjectIdentity
laSys = _LaSys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 712, 1, 2, 1)
)


class _LaSysConfig_Type(Integer32):
    """Custom type laSysConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("factory", 3),
          ("failed", 5),
          ("load", 2),
          ("ok", 4),
          ("save", 1))
    )


_LaSysConfig_Type.__name__ = "Integer32"
_LaSysConfig_Object = MibScalar
laSysConfig = _LaSysConfig_Object(
    (1, 3, 6, 1, 4, 1, 712, 1, 2, 1, 1),
    _LaSysConfig_Type()
)
laSysConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    laSysConfig.setStatus("mandatory")


class _LaJoystick_Type(Integer32):
    """Custom type laJoystick based on Integer32"""
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


_LaJoystick_Type.__name__ = "Integer32"
_LaJoystick_Object = MibScalar
laJoystick = _LaJoystick_Object(
    (1, 3, 6, 1, 4, 1, 712, 1, 2, 1, 2),
    _LaJoystick_Type()
)
laJoystick.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    laJoystick.setStatus("mandatory")


class _LaLinkAlert_Type(Integer32):
    """Custom type laLinkAlert based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("not-applicable", 3))
    )


_LaLinkAlert_Type.__name__ = "Integer32"
_LaLinkAlert_Object = MibScalar
laLinkAlert = _LaLinkAlert_Object(
    (1, 3, 6, 1, 4, 1, 712, 1, 2, 1, 3),
    _LaLinkAlert_Type()
)
laLinkAlert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    laLinkAlert.setStatus("mandatory")
_LaTpPort_ObjectIdentity = ObjectIdentity
laTpPort = _LaTpPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 712, 1, 2, 2)
)
_LaTpPortTable_Object = MibTable
laTpPortTable = _LaTpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 712, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    laTpPortTable.setStatus("mandatory")
_LaTpPortEntry_Object = MibTableRow
laTpPortEntry = _LaTpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 712, 1, 2, 2, 1, 1)
)
laTpPortEntry.setIndexNames(
    (0, "LANART-MIB", "laTpPortGroupIndex"),
    (0, "LANART-MIB", "laTpPortIndex"),
)
if mibBuilder.loadTexts:
    laTpPortEntry.setStatus("mandatory")


class _LaTpPortGroupIndex_Type(Integer32):
    """Custom type laTpPortGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_LaTpPortGroupIndex_Type.__name__ = "Integer32"
_LaTpPortGroupIndex_Object = MibTableColumn
laTpPortGroupIndex = _LaTpPortGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 712, 1, 2, 2, 1, 1, 1),
    _LaTpPortGroupIndex_Type()
)
laTpPortGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    laTpPortGroupIndex.setStatus("mandatory")


class _LaTpPortIndex_Type(Integer32):
    """Custom type laTpPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_LaTpPortIndex_Type.__name__ = "Integer32"
_LaTpPortIndex_Object = MibTableColumn
laTpPortIndex = _LaTpPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 712, 1, 2, 2, 1, 1, 2),
    _LaTpPortIndex_Type()
)
laTpPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    laTpPortIndex.setStatus("mandatory")


class _LaTpLinkTest_Type(Integer32):
    """Custom type laTpLinkTest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("failed", 3),
          ("not-applicable", 4))
    )


_LaTpLinkTest_Type.__name__ = "Integer32"
_LaTpLinkTest_Object = MibTableColumn
laTpLinkTest = _LaTpLinkTest_Object(
    (1, 3, 6, 1, 4, 1, 712, 1, 2, 2, 1, 1, 3),
    _LaTpLinkTest_Type()
)
laTpLinkTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    laTpLinkTest.setStatus("mandatory")


class _LaTpAutoPolarity_Type(Integer32):
    """Custom type laTpAutoPolarity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("corrected", 3),
          ("disabled", 2),
          ("enabled", 1),
          ("not-applicable", 4))
    )


_LaTpAutoPolarity_Type.__name__ = "Integer32"
_LaTpAutoPolarity_Object = MibTableColumn
laTpAutoPolarity = _LaTpAutoPolarity_Object(
    (1, 3, 6, 1, 4, 1, 712, 1, 2, 2, 1, 1, 4),
    _LaTpAutoPolarity_Type()
)
laTpAutoPolarity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    laTpAutoPolarity.setStatus("mandatory")

# Managed Objects groups


# Notification objects

laPortStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 712, 0, 1)
)
laPortStatus.setObjects(
    ("SNMP-REPEATER-MIB", "rptrPortOperStatus")
)
if mibBuilder.loadTexts:
    laPortStatus.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LANART-MIB",
    **{"lanart": lanart,
       "laPortStatus": laPortStatus,
       "laMib1": laMib1,
       "laProducts": laProducts,
       "laTpHub": laTpHub,
       "laTpHub1": laTpHub1,
       "etm120x": etm120x,
       "etm160x": etm160x,
       "etm240x": etm240x,
       "laTpHub2": laTpHub2,
       "ete120x": ete120x,
       "ete160x": ete160x,
       "ete240x": ete240x,
       "laTpHub3": laTpHub3,
       "bbAui": bbAui,
       "bbAuiTp": bbAuiTp,
       "bbAuiBnc": bbAuiBnc,
       "bbAuiTpBnc": bbAuiTpBnc,
       "bbAui10BASE-FL": bbAui10BASE_FL,
       "laHubMib": laHubMib,
       "laSys": laSys,
       "laSysConfig": laSysConfig,
       "laJoystick": laJoystick,
       "laLinkAlert": laLinkAlert,
       "laTpPort": laTpPort,
       "laTpPortTable": laTpPortTable,
       "laTpPortEntry": laTpPortEntry,
       "laTpPortGroupIndex": laTpPortGroupIndex,
       "laTpPortIndex": laTpPortIndex,
       "laTpLinkTest": laTpLinkTest,
       "laTpAutoPolarity": laTpAutoPolarity}
)
