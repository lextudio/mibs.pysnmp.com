# SNMP MIB module (ASCEND-VOIP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-VOIP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:42:45 2024
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

(voipGroup,) = mibBuilder.importSymbols(
    "ASCEND-MIB",
    "voipGroup")

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


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_VoipCfgGroup_ObjectIdentity = ObjectIdentity
voipCfgGroup = _VoipCfgGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 28, 1)
)
_VoipCfgGkGroup_ObjectIdentity = ObjectIdentity
voipCfgGkGroup = _VoipCfgGkGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 28, 1, 1)
)
_VoipCfgGkTable_Object = MibTable
voipCfgGkTable = _VoipCfgGkTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 28, 1, 1, 1)
)
if mibBuilder.loadTexts:
    voipCfgGkTable.setStatus("mandatory")
_VoipCfgGkEntry_Object = MibTableRow
voipCfgGkEntry = _VoipCfgGkEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 28, 1, 1, 1, 1)
)
voipCfgGkEntry.setIndexNames(
    (0, "ASCEND-VOIP-MIB", "voipCfgGkIndex"),
)
if mibBuilder.loadTexts:
    voipCfgGkEntry.setStatus("mandatory")
_VoipCfgGkIndex_Type = Integer32
_VoipCfgGkIndex_Object = MibTableColumn
voipCfgGkIndex = _VoipCfgGkIndex_Object(
    (1, 3, 6, 1, 4, 1, 529, 28, 1, 1, 1, 1, 1),
    _VoipCfgGkIndex_Type()
)
voipCfgGkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipCfgGkIndex.setStatus("mandatory")


class _VoipCfgGkStatus_Type(Integer32):
    """Custom type voipCfgGkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-registered", 2),
          ("registered", 1))
    )


_VoipCfgGkStatus_Type.__name__ = "Integer32"
_VoipCfgGkStatus_Object = MibTableColumn
voipCfgGkStatus = _VoipCfgGkStatus_Object(
    (1, 3, 6, 1, 4, 1, 529, 28, 1, 1, 1, 1, 2),
    _VoipCfgGkStatus_Type()
)
voipCfgGkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipCfgGkStatus.setStatus("mandatory")
_VoipCfgGkIpAddress_Type = IpAddress
_VoipCfgGkIpAddress_Object = MibTableColumn
voipCfgGkIpAddress = _VoipCfgGkIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 529, 28, 1, 1, 1, 1, 3),
    _VoipCfgGkIpAddress_Type()
)
voipCfgGkIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipCfgGkIpAddress.setStatus("mandatory")
_VoipCfgGwGroup_ObjectIdentity = ObjectIdentity
voipCfgGwGroup = _VoipCfgGwGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 28, 1, 2)
)


class _VoipCfgGwVpnMode_Type(Integer32):
    """Custom type voipCfgGwVpnMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_VoipCfgGwVpnMode_Type.__name__ = "Integer32"
_VoipCfgGwVpnMode_Object = MibScalar
voipCfgGwVpnMode = _VoipCfgGwVpnMode_Object(
    (1, 3, 6, 1, 4, 1, 529, 28, 1, 2, 1),
    _VoipCfgGwVpnMode_Type()
)
voipCfgGwVpnMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipCfgGwVpnMode.setStatus("mandatory")


class _VoipCfgGwPktAudioMode_Type(Integer32):
    """Custom type voipCfgGwPktAudioMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("g711-alaw", 3),
          ("g711-ulaw", 2),
          ("g723", 4),
          ("g723-6-4kps", 6),
          ("g729", 5),
          ("other", 1))
    )


_VoipCfgGwPktAudioMode_Type.__name__ = "Integer32"
_VoipCfgGwPktAudioMode_Object = MibScalar
voipCfgGwPktAudioMode = _VoipCfgGwPktAudioMode_Object(
    (1, 3, 6, 1, 4, 1, 529, 28, 1, 2, 2),
    _VoipCfgGwPktAudioMode_Type()
)
voipCfgGwPktAudioMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voipCfgGwPktAudioMode.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-VOIP-MIB",
    **{"voipCfgGroup": voipCfgGroup,
       "voipCfgGkGroup": voipCfgGkGroup,
       "voipCfgGkTable": voipCfgGkTable,
       "voipCfgGkEntry": voipCfgGkEntry,
       "voipCfgGkIndex": voipCfgGkIndex,
       "voipCfgGkStatus": voipCfgGkStatus,
       "voipCfgGkIpAddress": voipCfgGkIpAddress,
       "voipCfgGwGroup": voipCfgGwGroup,
       "voipCfgGwVpnMode": voipCfgGwVpnMode,
       "voipCfgGwPktAudioMode": voipCfgGwPktAudioMode}
)
