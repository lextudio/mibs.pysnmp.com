# SNMP MIB module (AIPPP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AIPPP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:35:14 2024
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
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

aiPPP = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 539, 25)
)


# Types definitions



class PositiveInteger(Integer32):
    """Custom type PositiveInteger based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Aii_ObjectIdentity = ObjectIdentity
aii = _Aii_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539)
)
_AiPPPTable_Object = MibTable
aiPPPTable = _AiPPPTable_Object(
    (1, 3, 6, 1, 4, 1, 539, 25, 1)
)
if mibBuilder.loadTexts:
    aiPPPTable.setStatus("current")
_AiPPPEntry_Object = MibTableRow
aiPPPEntry = _AiPPPEntry_Object(
    (1, 3, 6, 1, 4, 1, 539, 25, 1, 1)
)
aiPPPEntry.setIndexNames(
    (0, "AIPPP-MIB", "aipppLinkNumber"),
)
if mibBuilder.loadTexts:
    aiPPPEntry.setStatus("current")
_AipppLinkNumber_Type = PositiveInteger
_AipppLinkNumber_Object = MibTableColumn
aipppLinkNumber = _AipppLinkNumber_Object(
    (1, 3, 6, 1, 4, 1, 539, 25, 1, 1, 1),
    _AipppLinkNumber_Type()
)
aipppLinkNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aipppLinkNumber.setStatus("current")


class _AipppNCPProtoOption_Type(Integer32):
    """Custom type aipppNCPProtoOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bcp", 2),
          ("ipcp", 1),
          ("ipcpbcp", 3))
    )


_AipppNCPProtoOption_Type.__name__ = "Integer32"
_AipppNCPProtoOption_Object = MibTableColumn
aipppNCPProtoOption = _AipppNCPProtoOption_Object(
    (1, 3, 6, 1, 4, 1, 539, 25, 1, 1, 2),
    _AipppNCPProtoOption_Type()
)
aipppNCPProtoOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aipppNCPProtoOption.setStatus("current")


class _AipppLocalSecurityOption_Type(Integer32):
    """Custom type aipppLocalSecurityOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("chap", 3),
          ("none", 1),
          ("pap", 2))
    )


_AipppLocalSecurityOption_Type.__name__ = "Integer32"
_AipppLocalSecurityOption_Object = MibTableColumn
aipppLocalSecurityOption = _AipppLocalSecurityOption_Object(
    (1, 3, 6, 1, 4, 1, 539, 25, 1, 1, 3),
    _AipppLocalSecurityOption_Type()
)
aipppLocalSecurityOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aipppLocalSecurityOption.setStatus("current")
_AipppIpSrcAddr_Type = IpAddress
_AipppIpSrcAddr_Object = MibTableColumn
aipppIpSrcAddr = _AipppIpSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 539, 25, 1, 1, 4),
    _AipppIpSrcAddr_Type()
)
aipppIpSrcAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aipppIpSrcAddr.setStatus("current")
_AipppIpDestAddr_Type = IpAddress
_AipppIpDestAddr_Object = MibTableColumn
aipppIpDestAddr = _AipppIpDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 539, 25, 1, 1, 5),
    _AipppIpDestAddr_Type()
)
aipppIpDestAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aipppIpDestAddr.setStatus("current")
_AipppIpSubnetMask_Type = IpAddress
_AipppIpSubnetMask_Object = MibTableColumn
aipppIpSubnetMask = _AipppIpSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 539, 25, 1, 1, 6),
    _AipppIpSubnetMask_Type()
)
aipppIpSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aipppIpSubnetMask.setStatus("current")
_AipppIpBcastAddr_Type = Integer32
_AipppIpBcastAddr_Object = MibTableColumn
aipppIpBcastAddr = _AipppIpBcastAddr_Object(
    (1, 3, 6, 1, 4, 1, 539, 25, 1, 1, 7),
    _AipppIpBcastAddr_Type()
)
aipppIpBcastAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aipppIpBcastAddr.setStatus("current")


class _AipppLocalRadiusOption_Type(Integer32):
    """Custom type aipppLocalRadiusOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2),
          ("localfallback", 3))
    )


_AipppLocalRadiusOption_Type.__name__ = "Integer32"
_AipppLocalRadiusOption_Object = MibTableColumn
aipppLocalRadiusOption = _AipppLocalRadiusOption_Object(
    (1, 3, 6, 1, 4, 1, 539, 25, 1, 1, 8),
    _AipppLocalRadiusOption_Type()
)
aipppLocalRadiusOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aipppLocalRadiusOption.setStatus("current")


class _AipppRemoteSecurityOption_Type(Integer32):
    """Custom type aipppRemoteSecurityOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("chap", 3),
          ("none", 1),
          ("pap", 2))
    )


_AipppRemoteSecurityOption_Type.__name__ = "Integer32"
_AipppRemoteSecurityOption_Object = MibTableColumn
aipppRemoteSecurityOption = _AipppRemoteSecurityOption_Object(
    (1, 3, 6, 1, 4, 1, 539, 25, 1, 1, 9),
    _AipppRemoteSecurityOption_Type()
)
aipppRemoteSecurityOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aipppRemoteSecurityOption.setStatus("current")


class _AipppMultilinkOption_Type(Integer32):
    """Custom type aipppMultilinkOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("reject", 1),
          ("request", 2))
    )


_AipppMultilinkOption_Type.__name__ = "Integer32"
_AipppMultilinkOption_Object = MibTableColumn
aipppMultilinkOption = _AipppMultilinkOption_Object(
    (1, 3, 6, 1, 4, 1, 539, 25, 1, 1, 10),
    _AipppMultilinkOption_Type()
)
aipppMultilinkOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aipppMultilinkOption.setStatus("current")


class _AipppMLGroup_Type(Integer32):
    """Custom type aipppMLGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AipppMLGroup_Type.__name__ = "Integer32"
_AipppMLGroup_Object = MibTableColumn
aipppMLGroup = _AipppMLGroup_Object(
    (1, 3, 6, 1, 4, 1, 539, 25, 1, 1, 11),
    _AipppMLGroup_Type()
)
aipppMLGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aipppMLGroup.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AIPPP-MIB",
    **{"PositiveInteger": PositiveInteger,
       "aii": aii,
       "aiPPP": aiPPP,
       "aiPPPTable": aiPPPTable,
       "aiPPPEntry": aiPPPEntry,
       "aipppLinkNumber": aipppLinkNumber,
       "aipppNCPProtoOption": aipppNCPProtoOption,
       "aipppLocalSecurityOption": aipppLocalSecurityOption,
       "aipppIpSrcAddr": aipppIpSrcAddr,
       "aipppIpDestAddr": aipppIpDestAddr,
       "aipppIpSubnetMask": aipppIpSubnetMask,
       "aipppIpBcastAddr": aipppIpBcastAddr,
       "aipppLocalRadiusOption": aipppLocalRadiusOption,
       "aipppRemoteSecurityOption": aipppRemoteSecurityOption,
       "aipppMultilinkOption": aipppMultilinkOption,
       "aipppMLGroup": aipppMLGroup}
)
